"""
sim012_pontryagin_verification.py
==================================
Verificación posterior de optimalidad Pontryagin para D-016.

Estrategia (más eficiente que shooting completo):
  1. Tomar la solución empírica del sweet-spot sim010: h(x) = h_0* x^n con
     h_0* = 1.028, n = 4 → m_end = 99.98%.
  2. Integrar las trayectorias de variables adjuntas λ_m, λ_y, λ_h
     HACIA ATRÁS desde las condiciones terminales:
       λ_m(1) = 1, λ_y(1) = 0, λ_h(1) = 0.
  3. Verificar que se satisface la condición de optimalidad puntualmente:
       ∂H/∂u = λ_y · y/(1-h) + λ_h ≈ 0  para todo x.
  4. Verificar que las condiciones iniciales calculadas (λ_m(0), λ_y(0), λ_h(0))
     son razonables (no divergentes, finitos).

Si pasa: la solución empírica sim010 es óptima formal → K-035 promoción.
Si no pasa: identificar dónde falla.

Usa enfoque "verificación a posteriori" en lugar de shooting Newton-Raphson.
Más simple y directo.

Sin scipy. RK45 manual.
"""

import math
import cmath


# ============================================================
# Setup desde sim010 (sweet-spot empírico)
# ============================================================

H0_STAR = 1.028  # Sweet-spot empírico (sim010)
N_EXP = 4
Y_C = 100.0


def h_func(x):
    """h(x) = h_0* x^n."""
    if x <= 0:
        return 0.0
    return H0_STAR * x ** N_EXP


def hp_func(x):
    """h'(x) = u(x) (control aplicado en sim010)."""
    if x <= 0:
        return 0.0 if N_EXP > 1 else H0_STAR
    return N_EXP * H0_STAR * x ** (N_EXP - 1)


# ============================================================
# F(m, y, h, u; x) — RHS de y
# ============================================================

def F_rhs(m, y, h, u, x, h_max=3.99, dy_cap=1e12):
    """Derivada dy/dx según TOV anisotropy."""
    h = min(max(h, -1.99), h_max)
    aniso_denom = 1.0 - h
    if abs(aniso_denom) < 1e-5:
        sign = 1.0 if aniso_denom > 0 else -1.0
        aniso_factor = sign * 1e5
    else:
        aniso_factor = 1.0 / aniso_denom

    denom_grav = x * (x - m)
    if denom_grav <= 0:
        return 0.0

    grav_term = y * (4.0 - h) * (m + (x ** 3) * y * (1.0 - h)) / (2.0 * denom_grav)
    src_term = 3.0 * y * h / x
    dy = aniso_factor * (y * u - grav_term + src_term)

    if abs(dy) > dy_cap:
        dy = math.copysign(dy_cap, dy)
    return dy


# ============================================================
# Forward integration: estados (m, y, h)
# ============================================================

def integrate_forward(y_c=Y_C, x0=1e-5, x_end=0.995, max_steps=100_000):
    """Integra (m, y) hacia adelante con h(x) ansatz fijo."""
    m = y_c * x0 ** 3
    y = y_c * (1.0 - 2.0 * y_c * x0 ** 2)
    x = x0
    h_step = 1e-5

    history = []
    history.append((x, m, y, h_func(x), hp_func(x)))

    for _ in range(max_steps):
        margin = x - m
        if margin <= 0:
            return history, "fail_compact"

        h_step_local = min(h_step, 0.01 * margin)
        if h_func(x) > 0.95 and h_func(x) < 1.05:
            h_step_local = min(h_step_local, 1e-6)
        if x > 0.99:
            h_step_local = min(h_step_local, 1e-6)
        if x + h_step_local > x_end:
            h_step_local = x_end - x

        if h_step_local < 1e-15:
            return history, "x_max"

        # RK4 simple
        h_x = h_func(x)
        u_x = hp_func(x)
        k1_m = 3 * x ** 2 * y
        k1_y = F_rhs(m, y, h_x, u_x, x)

        x_mid = x + h_step_local / 2
        h_mid = h_func(x_mid)
        u_mid = hp_func(x_mid)
        m_mid = m + h_step_local / 2 * k1_m
        y_mid = y + h_step_local / 2 * k1_y
        k2_m = 3 * x_mid ** 2 * y_mid
        k2_y = F_rhs(m_mid, y_mid, h_mid, u_mid, x_mid)

        m_mid2 = m + h_step_local / 2 * k2_m
        y_mid2 = y + h_step_local / 2 * k2_y
        k3_m = 3 * x_mid ** 2 * y_mid2
        k3_y = F_rhs(m_mid2, y_mid2, h_mid, u_mid, x_mid)

        x_new = x + h_step_local
        h_new = h_func(x_new)
        u_new = hp_func(x_new)
        m_new = m + h_step_local * k3_m
        y_new = y + h_step_local * k3_y
        k4_m = 3 * x_new ** 2 * y_new
        k4_y = F_rhs(m_new, y_new, h_new, u_new, x_new)

        m += h_step_local / 6 * (k1_m + 2 * k2_m + 2 * k3_m + k4_m)
        y += h_step_local / 6 * (k1_y + 2 * k2_y + 2 * k3_y + k4_y)
        x = x_new

        if y <= 0 or x >= x_end:
            history.append((x, m, y, h_func(x), hp_func(x)))
            return history, "complete"

        history.append((x, m, y, h_func(x), hp_func(x)))

    return history, "max_steps"


# ============================================================
# Backward integration: variables adjuntas (λ_m, λ_y, λ_h)
# ============================================================

def adjoint_rhs(m, y, h, u, lam_m, lam_y, lam_h, x):
    """Calcula -∂H/∂(m, y, h) para integrar λ hacia atrás.

    H = λ_m · 3x²y + λ_y · F(m, y, h, u; x) + λ_h · u
    """
    h_eff = min(max(h, -1.99), 3.99)
    aniso_denom = 1.0 - h_eff
    if abs(aniso_denom) < 1e-5:
        sign = 1.0 if aniso_denom > 0 else -1.0
        aniso_factor = sign * 1e5
    else:
        aniso_factor = 1.0 / aniso_denom

    denom_grav = x * (x - m)
    if denom_grav <= 0:
        return 0, 0, 0

    A = m + x ** 3 * y * (1.0 - h_eff)

    # ∂F/∂m: usando D-016 §A.1
    # F = aniso_factor [y·u - y(4-h)A/(2x(x-m)) + 3yh/x]
    # ∂A/∂m = 1
    # ∂[A/(x-m)]/∂m = (x-m + A)/(x-m)^2 = (x + x^3 y(1-h))/(x-m)^2
    dF_dm = -aniso_factor * y * (4 - h_eff) * (x + x ** 3 * y * (1 - h_eff)) / (2 * x * (x - m) ** 2)

    # ∂F/∂y:
    # ∂[yu]/∂y = u
    # ∂[y(4-h)A/(2x(x-m))]/∂y = (4-h)/(2x(x-m)) · [A + y · x^3(1-h)] = (4-h)/(2x(x-m)) · [m + 2 x^3 y (1-h)]
    # ∂[3yh/x]/∂y = 3h/x
    dF_dy = aniso_factor * (u - (4 - h_eff) * (m + 2 * x ** 3 * y * (1 - h_eff)) / (2 * x * (x - m)) + 3 * h_eff / x)

    # ∂F/∂h: combinación de derivadas
    # Termo de aniso_factor: ∂[1/(1-h)]/∂h = 1/(1-h)^2
    # Otros: -∂A/∂h = x^3 y, ∂(4-h)/∂h = -1, ∂(3yh/x)/∂h = 3y/x
    F_value = aniso_factor * (y * u - y * (4 - h_eff) * A / (2 * x * (x - m)) + 3 * y * h_eff / x)
    inner_dh = (-(-y) * (4 - h_eff) * A / (2 * x * (x - m))  # de ∂(4-h)/∂h = -1, signo: -y·(-1)·A/...
                - y * (4 - h_eff) * (-x ** 3 * y) / (2 * x * (x - m))  # de ∂A/∂h = -x³y
                + 3 * y / x)
    dF_dh = F_value / (1 - h_eff) + aniso_factor * inner_dh

    # -∂H/∂m = -lam_m · 0 - lam_y · ∂F/∂m
    dlam_m = -lam_y * dF_dm

    # -∂H/∂y = -lam_m · 3x² - lam_y · ∂F/∂y
    dlam_y = -lam_m * 3 * x ** 2 - lam_y * dF_dy

    # -∂H/∂h = -lam_y · ∂F/∂h
    dlam_h = -lam_y * dF_dh

    return -dlam_m, -dlam_y, -dlam_h  # negativo porque integramos hacia atrás (substitución dx → -dx)


def integrate_backward(history_forward):
    """Integra λ's hacia atrás con condiciones terminales λ_m(1) = 1, λ_y(1) = 0, λ_h(1) = 0."""
    # Ordenar de mayor a menor x
    rev = list(reversed(history_forward))

    # Condiciones terminales
    lam_m, lam_y, lam_h = 1.0, 0.0, 0.0
    history_lam = []

    for i in range(len(rev) - 1):
        x_curr, m_curr, y_curr, h_curr, u_curr = rev[i]
        x_prev, m_prev, y_prev, h_prev, u_prev = rev[i + 1]

        history_lam.append((x_curr, lam_m, lam_y, lam_h))

        dx = x_prev - x_curr  # negativo (hacia atrás)

        # Euler hacia atrás (simple, podría refinarse con RK4)
        dlam_m_dx, dlam_y_dx, dlam_h_dx = adjoint_rhs(
            m_curr, y_curr, h_curr, u_curr, lam_m, lam_y, lam_h, x_curr
        )
        lam_m += dx * (-dlam_m_dx)  # signo: dλ/dx = derivada hacia adelante; aquí integramos hacia atrás
        lam_y += dx * (-dlam_y_dx)
        lam_h += dx * (-dlam_h_dx)

        # Cap para evitar blow-up
        if abs(lam_m) > 1e10 or abs(lam_y) > 1e10 or abs(lam_h) > 1e10:
            history_lam.append((x_prev, lam_m, lam_y, lam_h))
            return history_lam, "blow_up"

    history_lam.append((rev[-1][0], lam_m, lam_y, lam_h))
    return history_lam, "complete"


# ============================================================
# Verificación condición de optimalidad
# ============================================================

def check_optimality(history_lam, history_forward):
    """Verifica que ∂H/∂u = λ_y · y/(1-h) + λ_h ≈ 0 para todo x."""
    # Mapear x a (lam_m, lam_y, lam_h)
    lam_dict = {x: (lm, ly, lh) for x, lm, ly, lh in history_lam}

    print(f"\n   {'x':>8} {'h':>8} {'y':>10} {'λ_m':>12} {'λ_y':>12} {'λ_h':>12} {'∂H/∂u':>12}")
    n_check = 0
    n_pass = 0
    max_violation = 0
    for entry in history_forward:
        x, m, y, h, u = entry
        if x not in lam_dict:
            continue
        lm, ly, lh = lam_dict[x]
        # ∂H/∂u = λ_y · y/(1-h) + λ_h
        if abs(1 - h) < 1e-5:
            opt = float('inf')
        else:
            opt = ly * y / (1 - h) + lh
        n_check += 1
        if abs(opt) < 0.1 * (abs(lm) + abs(ly) + abs(lh) + 1):
            n_pass += 1
        max_violation = max(max_violation, abs(opt))

        # Mostrar muestreo
        if x in [0.1, 0.3, 0.5, 0.7, 0.9, 0.95, 0.99] or (n_check % 1000 == 0):
            try:
                print(f"   {x:>8.4f} {h:>8.4f} {y:>10.3e} {lm:>12.3e} {ly:>12.3e} {lh:>12.3e} {opt:>12.3e}")
            except:
                pass

    print(f"\n   Pasaron condición optimalidad: {n_pass}/{n_check}")
    print(f"   Violación máxima: {max_violation:.4e}")

    return n_pass, n_check, max_violation


# ============================================================
# Main
# ============================================================

def main():
    print("=" * 76)
    print("sim012 — Verificación posterior optimalidad Pontryagin (D-016)")
    print("=" * 76)
    print()
    print(f"Solución empírica sim010: h(x) = {H0_STAR} · x^{N_EXP}, y_c = {Y_C}")
    print()

    # Forward integration
    print("[1] Forward integration (estado m, y con h fijo):")
    hist_fwd, status_fwd = integrate_forward()
    if hist_fwd:
        last = hist_fwd[-1]
        print(f"   x_end = {last[0]:.4f}, m_end = {last[1]:.4f}, y_end = {last[2]:.4f}")
        print(f"   Status: {status_fwd}, n_points = {len(hist_fwd)}")

    # Backward integration de λ's
    print()
    print("[2] Backward integration (variables adjuntas λ_m, λ_y, λ_h):")
    hist_lam, status_lam = integrate_backward(hist_fwd)
    if hist_lam:
        # Λ's en x = 0 (último de la integración hacia atrás)
        first = hist_lam[-1]
        print(f"   En x ≈ 0: λ_m = {first[1]:.4e}, λ_y = {first[2]:.4e}, λ_h = {first[3]:.4e}")
        print(f"   Status: {status_lam}")

    # Verificación condición optimalidad
    print()
    print("[3] Verificación condición de optimalidad ∂H/∂u = λ_y · y/(1-h) + λ_h ≈ 0:")
    n_pass, n_check, max_viol = check_optimality(hist_lam, hist_fwd)

    print()
    print("=" * 76)
    print("VEREDICTO sim012")
    print("=" * 76)
    if n_pass / max(n_check, 1) > 0.8:
        print("  ✓ CONDICIÓN DE OPTIMALIDAD APROXIMADAMENTE SATISFECHA")
        print("  → solución empírica sim010 es CONSISTENTE con BVP Pontryagin")
        print("  → K-035 promoción a confirmado limpio JUSTIFICADA")
    else:
        print("  ⚠ CONDICIÓN DE OPTIMALIDAD NO SATISFECHA SUFICIENTEMENTE")
        print("  → solución empírica sim010 puede no ser óptima, o BVP incompleto")
        print(f"  → violación máxima {max_viol:.4e} sugiere refinamiento necesario")


if __name__ == "__main__":
    main()
