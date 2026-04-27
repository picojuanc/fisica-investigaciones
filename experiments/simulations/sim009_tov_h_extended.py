"""
sim009_tov_h_extended.py
========================
Extensión de sim003 al régimen h > 1 (tensión radial w_r < 0).

Contexto: Q-045 sesión 68. Test de la hipótesis "régimen h > 1 cierra los
17% residuales de masa ADM" (refinamiento de Q-045.A.parcial sesión 38).

Estrategia: usar el setup de sim003 con cap h_max permisivo (>1).
La ODE para y diverge formalmente en h=1 (singularidad coordinate),
pero numéricamente con paso adaptativo + cap en magnitud puede ser tratable.

Análisis físico (notes/Q-045_sesion68_ruta_b_tension_radial.md §4):
- h > 1 corresponde a cuerdas SCG preferentemente RADIALES
  (no tangenciales como sim003 sugería).
- Trace condition + DEC permiten h ∈ [-2, 4]; las energy conditions
  son satisfechas para h ∈ [0, 4] con y > 0.
- Bound de Andreasson 2008 NO aplica para ρ no-monótona (caso SCG).

ODEs (idénticas a sim003):
  dm̃/dx = 3 x² y
  dy/dx  = (1/(1-h)) [ y h'(x)
                     - y(4-h)[m̃ + x³ y(1-h)] / (2 x(x-m̃))
                     + 3 y h / x ]

Singularidad coordinate en h=1: tratada con cap en |dy/dx|.

Sin scipy. RK4 manual.
"""

import math


# ============================================================
# Perfiles h(x) extendidos
# ============================================================

def h_power(x, h0, n):
    """h(x) = h0 * x^n."""
    if x <= 0:
        return 0.0
    return h0 * x ** n


def hp_power(x, h0, n):
    """h'(x) = n * h0 * x^(n-1)."""
    if x <= 0:
        return 0.0 if n > 1 else h0
    return n * h0 * x ** (n - 1)


def h_offset(x, h_center, h_amp, n):
    """h(x) = h_center + h_amp * x^n. Permite arrancar fuera de h=0.

    Útil para evitar el cruce h=1 si h_center > 1 (todo el dominio en h>1).
    """
    if x <= 0:
        return h_center
    return h_center + h_amp * x ** n


def hp_offset(x, h_center, h_amp, n):
    """h'(x) = n * h_amp * x^(n-1)."""
    if x <= 0:
        return 0.0 if n > 1 else h_amp
    return n * h_amp * x ** (n - 1)


# ============================================================
# RHS TOV anisotrópica con cap |dy/dx|
# ============================================================

def rhs_aniso_extended(x, state, h_fn, hp_fn, h_max=3.99, dy_cap=1e10):
    """
    RHS extendida con cap en |dy/dx| para manejar singularidad h=1.

    h_fn(x), hp_fn(x): callables que dan h(x) y h'(x).
    h_max: cap superior absoluto en h (default 3.99 < 4 borde DEC).
    dy_cap: cap en |dy/dx| para regularizar cruce h=1.
    """
    m, y, Phi = state
    if y <= 0:
        return [0.0, 0.0, 0.0]

    h_raw = h_fn(x)
    hp_raw = hp_fn(x)

    # Cap absoluto en h por DEC
    h = min(max(h_raw, -1.99), h_max)
    hp = hp_raw  # No cap derivada (afectaría más)

    denom_grav = x * (x - m)
    if denom_grav <= 0:
        return [0.0, -1e30, 1e30]

    # Manejo singularidad h=1: si |1-h| muy pequeño, hacer cap suave
    aniso_denom = 1.0 - h
    if abs(aniso_denom) < 1e-3:
        # Régimen singular: cap el factor 1/(1-h) en signo correcto
        sign = 1.0 if aniso_denom > 0 else -1.0
        aniso_factor = sign * 1e3
    else:
        aniso_factor = 1.0 / aniso_denom

    grav_term = y * (4.0 - h) * (m + (x ** 3) * y * (1.0 - h)) / (2.0 * denom_grav)
    src_term = 3.0 * y * h / x

    dy = aniso_factor * (y * hp - grav_term + src_term)

    # Cap en |dy/dx| para estabilidad numérica
    if abs(dy) > dy_cap:
        dy = math.copysign(dy_cap, dy)

    dm = 3.0 * x ** 2 * y

    w_r = y * (1.0 - h) / 3.0
    dPhi = (m + 3.0 * (x ** 3) * w_r) / (2.0 * denom_grav)

    return [dm, dy, dPhi]


# ============================================================
# Integrador RK4 con detección de cruce h=1
# ============================================================

def rk4(f, x, state, h_step, *args):
    """Un paso RK4."""
    k1 = f(x, state, *args)
    s2 = [state[i] + 0.5 * h_step * k1[i] for i in range(len(state))]
    k2 = f(x + 0.5 * h_step, s2, *args)
    s3 = [state[i] + 0.5 * h_step * k2[i] for i in range(len(state))]
    k3 = f(x + 0.5 * h_step, s3, *args)
    s4 = [state[i] + h_step * k3[i] for i in range(len(state))]
    k4 = f(x + h_step, s4, *args)
    return [state[i] + (h_step / 6.0) * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i])
            for i in range(len(state))]


def integrate_extended(y_c, h_fn, hp_fn,
                       x0=1e-5, x_max=0.99999,
                       h_init=1e-5, max_steps=2_000_000,
                       h_max_dec=3.99, dy_cap=1e10,
                       verbose_crossing=False):
    """
    Integra TOV anisotrópica con cap permisivo en h.

    Returns: (history, status, info)
    """
    m0 = y_c * x0 ** 3
    y0 = y_c * (1.0 - 2.0 * y_c * x0 ** 2)
    Phi0 = 0.0
    state = [m0, y0, Phi0]
    x = x0

    h_at_x = h_fn(x)
    w_r = state[1] * (1.0 - h_at_x) / 3.0
    w_t = state[1] * (1.0 + h_at_x / 2.0) / 3.0
    history = [(x, state[0], state[1], state[2], h_at_x, w_r, w_t)]

    h_step = h_init
    n_steps = 0
    crossing_detected = False
    x_crossing = None

    for _ in range(max_steps):
        compactness = state[0] / x if x > 0 else 0.0
        margin = x - state[0]
        if margin <= 0:
            return history, "fail_compact_1", {"steps": n_steps, "x_fail": x, "compactness": compactness}

        # Paso adaptativo, más fino cerca de h=1
        h_now = h_fn(x)
        h_step_factor = 1.0
        if 0.95 < h_now < 1.05:
            h_step_factor = 0.1  # Paso más fino cerca cruce h=1

        h_adapt = min(h_step * h_step_factor,
                      0.01 * margin)
        if x + h_adapt > x_max:
            h_adapt = x_max - x
        if h_adapt < 1e-15:
            status = "x_max" if x >= x_max * 0.9999 else "compact_1"
            return history, status, {"steps": n_steps, "x_end": x, "compactness": compactness}

        new_state = rk4(rhs_aniso_extended, x, state, h_adapt, h_fn, hp_fn, h_max_dec, dy_cap)
        new_m, new_y, new_Phi = new_state

        # Detectar cruce h=1
        new_h = h_fn(x + h_adapt)
        if (h_now < 1.0 < new_h) or (h_now > 1.0 > new_h):
            if not crossing_detected:
                crossing_detected = True
                x_crossing = x + h_adapt * (1.0 - h_now) / max(new_h - h_now, 1e-10)
                if verbose_crossing:
                    print(f"      [crossing h=1 at x≈{x_crossing:.4f}, y≈{new_y:.3e}]")

        # Detectar y inválido
        if new_y <= 0:
            frac = state[1] / max(state[1] - new_y, 1e-30)
            dm, dy, dPhi = rhs_aniso_extended(x, state, h_fn, hp_fn, h_max_dec, dy_cap)
            x_surf = x + frac * h_adapt
            m_surf = state[0] + frac * h_adapt * dm
            Phi_surf = state[2] + frac * h_adapt * dPhi
            h_surf = h_fn(x_surf)
            history.append((x_surf, m_surf, 0.0, Phi_surf, h_surf, 0.0, 0.0))
            return history, "surface", {"steps": n_steps, "x_surface": x_surf,
                                         "crossing": x_crossing}

        # Detectar y explosivo (artefacto numérico)
        if new_y > 1e15 or new_y < 0 or math.isnan(new_y) or math.isinf(new_y):
            return history, "fail_y_explosive", {"steps": n_steps, "x_end": x, "y_end": new_y,
                                                  "crossing": x_crossing}

        x = x + h_adapt
        state = new_state
        n_steps += 1

        h_at_x = h_fn(x)
        w_r = state[1] * (1.0 - h_at_x) / 3.0
        w_t = state[1] * (1.0 + h_at_x / 2.0) / 3.0
        history.append((x, state[0], state[1], state[2], h_at_x, w_r, w_t))

        # Detectar compactness ≈ 1
        if state[0] / x >= 0.999:
            return history, "compact_1", {"steps": n_steps, "x_end": x,
                                            "compactness": state[0]/x,
                                            "crossing": x_crossing}

        if x >= x_max:
            return history, "x_max", {"steps": n_steps, "x_end": x,
                                       "compactness": state[0]/x,
                                       "crossing": x_crossing}

        if compactness < 0.7 and h_adapt > h_step * 0.5:
            h_step = min(h_step * 1.1, 1e-3)

    return history, "max_steps", {"steps": n_steps, "x_end": x,
                                    "crossing": x_crossing}


def integrate_power_ext(y_c, h0, n, **kwargs):
    """Wrapper power-law extendido."""
    h_fn = lambda x: h_power(x, h0, n)
    hp_fn = lambda x: hp_power(x, h0, n)
    return integrate_extended(y_c, h_fn, hp_fn, **kwargs)


def integrate_offset_ext(y_c, h_center, h_amp, n, **kwargs):
    """Wrapper offset (h(0) ≠ 0)."""
    h_fn = lambda x: h_offset(x, h_center, h_amp, n)
    hp_fn = lambda x: hp_offset(x, h_center, h_amp, n)
    return integrate_extended(y_c, h_fn, hp_fn, **kwargs)


def profile_summary(hist):
    """Métricas del perfil."""
    if len(hist) < 2:
        return {}
    x_end, m_end, y_end, Phi_end, h_end, wr_end, wt_end = hist[-1]
    max_compact = 0.0
    x_at_max = 0.0
    for entry in hist:
        x, m, y, Phi, h, wr, wt = entry
        c = m / x if x > 0 else 0.0
        if c > max_compact:
            max_compact = c
            x_at_max = x
    return {
        "x_end": x_end,
        "m_end": m_end,
        "y_end": y_end,
        "h_end": h_end,
        "max_compactness": max_compact,
        "x_at_max_compact": x_at_max,
        "n_points": len(hist),
    }


# ============================================================
# Test 1: extensión continua sim003 — h_0 ∈ [0.5, 3.5]
# ============================================================

def test_h0_extension(y_c=100.0):
    """Barrido de h_0 desde 0.5 hasta cerca de DEC borde (4)."""
    print("\n[Test 1] Barrido h_0 ∈ [0.5, 3.99] con n=4, y_c=100:")
    print(f"   {'h_0':>8} {'max_comp':>10} {'m̃_end':>10} {'x_end':>10} {'crossing':>10} {'status':>20}")

    h0_values = [0.5, 0.9, 0.99, 1.01, 1.1, 1.5, 2.0, 2.5, 3.0, 3.5, 3.9, 3.99]
    for h0 in h0_values:
        hist, status, info = integrate_power_ext(y_c, h0, 4)
        summary = profile_summary(hist)
        cross = info.get("crossing")
        cross_str = f"{cross:.4f}" if cross else "—"
        print(f"   {h0:>8.4f} {summary['max_compactness']:>10.4f} {summary['m_end']:>10.4f} "
              f"{summary['x_end']:>10.4f} {cross_str:>10} {status:>20}")


def test_h0_extension_n2(y_c=100.0):
    """Barrido h_0 con n=2 (transición más suave)."""
    print("\n[Test 1b] Barrido h_0 ∈ [0.5, 3.99] con n=2, y_c=100:")
    print(f"   {'h_0':>8} {'max_comp':>10} {'m̃_end':>10} {'x_end':>10} {'crossing':>10} {'status':>20}")

    h0_values = [0.5, 0.9, 0.99, 1.01, 1.1, 1.5, 2.0, 2.5, 3.0, 3.5, 3.9, 3.99]
    for h0 in h0_values:
        hist, status, info = integrate_power_ext(y_c, h0, 2)
        summary = profile_summary(hist)
        cross = info.get("crossing")
        cross_str = f"{cross:.4f}" if cross else "—"
        print(f"   {h0:>8.4f} {summary['max_compactness']:>10.4f} {summary['m_end']:>10.4f} "
              f"{summary['x_end']:>10.4f} {cross_str:>10} {status:>20}")


# ============================================================
# Test 2: offset (h(0) > 1) — todo en régimen h > 1
# ============================================================

def test_offset_all_h_gt_1(y_c=100.0):
    """h(x) = h_center + h_amp x^n con h_center > 1.

    Todo el dominio en h > 1, evita singularidad cruce.
    """
    print("\n[Test 2] Offset h_center > 1 (régimen h>1 desde centro):")
    print(f"   {'h_center':>10} {'h_amp':>8} {'n':>4} {'max_comp':>10} {'m̃_end':>10} {'status':>20}")

    cases = [
        (1.5, 0.5, 4),  # h(0)=1.5, h(1)=2.0
        (1.5, 1.0, 4),  # h(0)=1.5, h(1)=2.5
        (2.0, 1.0, 4),  # h(0)=2.0, h(1)=3.0
        (2.5, 1.0, 4),  # h(0)=2.5, h(1)=3.5
        (3.0, 0.5, 4),  # h(0)=3.0, h(1)=3.5
        (3.5, 0.4, 4),  # h(0)=3.5, h(1)=3.9
        (3.9, 0.0, 4),  # h(x) ≡ 3.9 constante
    ]
    for h_center, h_amp, n in cases:
        hist, status, info = integrate_offset_ext(y_c, h_center, h_amp, n)
        summary = profile_summary(hist)
        print(f"   {h_center:>10.2f} {h_amp:>8.2f} {n:>4d} {summary['max_compactness']:>10.4f} "
              f"{summary['m_end']:>10.4f} {status:>20}")


# ============================================================
# Test 3: barrido y_c con h_0 alto
# ============================================================

def test_yc_high_h0(h0=2.0, n=4):
    """Robustez del resultado a y_c."""
    print(f"\n[Test 3] Barrido y_c con h_0={h0}, n={n}:")
    print(f"   {'y_c':>10} {'max_comp':>10} {'m̃_end':>10} {'status':>20}")

    for y_c in [10.0, 100.0, 1000.0, 10000.0]:
        hist, status, info = integrate_power_ext(y_c, h0, n)
        summary = profile_summary(hist)
        print(f"   {y_c:>10.1f} {summary['max_compactness']:>10.4f} "
              f"{summary['m_end']:>10.4f} {status:>20}")


# ============================================================
# Test 4: análisis del cruce h=1 en detalle
# ============================================================

def test_crossing_detail(y_c=100.0, h0=2.0, n=4):
    """Análisis numérico fino del cruce h=1."""
    print(f"\n[Test 4] Análisis del cruce h=1 (h_0={h0}, n={n}):")

    hist, status, info = integrate_power_ext(y_c, h0, n, verbose_crossing=True)
    summary = profile_summary(hist)

    print(f"   Status: {status}")
    print(f"   Max compactness: {summary['max_compactness']:.4f}")
    print(f"   x donde h=1 (esperado): {(1.0/h0)**(1.0/n):.4f}")
    print(f"   x_crossing detectado: {info.get('crossing', 'no detectado')}")

    # Sample del perfil
    x_targets = [0.1, 0.3, 0.5, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95]
    print(f"\n   Perfil cerca del cruce:")
    print(f"   {'x':>8} {'m̃':>10} {'y':>12} {'h':>8} {'w_r':>12} {'w_t':>12} {'m̃/x':>8}")
    for xt in x_targets:
        for entry in hist:
            if entry[0] >= xt:
                x, m, y, Phi, h, wr, wt = entry
                c = m/x if x > 0 else 0.0
                print(f"   {x:>8.4f} {m:>10.4f} {y:>12.4e} {h:>8.4f} {wr:>12.4e} {wt:>12.4e} {c:>8.4f}")
                break


# ============================================================
# Test 5: comparación con sim003 (h_max ≤ 1)
# ============================================================

def test_compare_with_sim003():
    """Verificar consistencia con sim003 en régimen común h ≤ 1."""
    print("\n[Test 5] Verificación contra sim003 (h ≤ 1):")
    print(f"   {'h_0':>8} {'n':>4} {'sim003 max_comp':>16} {'sim009 max_comp':>16} {'diff':>10}")

    expected_sim003 = {
        (0.30, 2): 0.495,
        (0.50, 2): 0.524,
        (0.70, 2): 0.606,
        (0.95, 2): 0.764,
        (0.95, 4): 0.727,
        (0.99, 4): 0.808,
    }
    for (h0, n), exp in expected_sim003.items():
        hist, status, info = integrate_power_ext(100.0, h0, n)
        summary = profile_summary(hist)
        c = summary['max_compactness']
        diff = abs(c - exp)
        print(f"   {h0:>8.2f} {n:>4d} {exp:>16.4f} {c:>16.4f} {diff:>10.4f}")


# ============================================================
# Test 6: predicción cuantitativa del análisis técnico
# ============================================================

def test_predicted_compactness():
    """Verificar predicción §5.5 del análisis: h_0 ∈ (1, 4] → c ∈ [0.85, ~1]."""
    print("\n[Test 6] Predicción cuantitativa: compactness vs h_0:")
    print(f"   {'h_0 range':>15} {'h_0 sample':>10} {'max_comp':>10} {'cierra Q-045?':>16}")

    samples = {
        "h_0 ∈ (1, 2]": [1.1, 1.5, 2.0],
        "h_0 ∈ (2, 3]": [2.5, 3.0],
        "h_0 ∈ (3, 4]": [3.5, 3.9, 3.99],
    }
    for rng, vals in samples.items():
        for h0 in vals:
            hist, status, info = integrate_power_ext(100.0, h0, 4)
            summary = profile_summary(hist)
            c = summary['max_compactness']
            cierra = "✓ ≥0.99" if c >= 0.99 else ("parcial ≥0.90" if c >= 0.90 else "no")
            print(f"   {rng:>15} {h0:>10.2f} {c:>10.4f} {cierra:>16}")


# ============================================================
# Main
# ============================================================

def main():
    print("=" * 76)
    print("sim009 — TOV anisotrópica EXTENDIDA al régimen h > 1")
    print("=" * 76)

    # Test 5 primero: verificar consistencia con sim003
    test_compare_with_sim003()

    # Test 1: barrido principal h_0 hasta DEC borde
    print("\n" + "-" * 76)
    test_h0_extension()

    # Test 1b: idem con n=2
    print("\n" + "-" * 76)
    test_h0_extension_n2()

    # Test 2: offset
    print("\n" + "-" * 76)
    test_offset_all_h_gt_1()

    # Test 3: robustez y_c
    print("\n" + "-" * 76)
    test_yc_high_h0(h0=2.0, n=4)

    # Test 4: cruce h=1 detallado
    print("\n" + "-" * 76)
    test_crossing_detail(h0=2.0, n=4)

    # Test 6: predicción cuantitativa
    print("\n" + "-" * 76)
    test_predicted_compactness()

    # Resumen
    print("\n" + "=" * 76)
    print("RESUMEN sim009")
    print("=" * 76)
    print("  Verificar:")
    print("  • Test 5: consistencia con sim003 en h ≤ 1.")
    print("  • Test 1: tendencia compactness vs h_0 cuando h_0 > 1.")
    print("  • Test 2: comportamiento del offset (todo dominio en h > 1).")
    print("  • Test 4: tratamiento numérico del cruce h=1.")
    print("  • Test 6: ¿predicción del análisis técnico se cumple?")
    print()
    print("  Veredicto Q-045.b dependerá de Test 1 + Test 2 + Test 6.")


if __name__ == "__main__":
    main()
