"""
sim010_tov_h_refined.py
=======================
Refinamiento numérico de sim009 con RK45 Dormand-Prince.

Contexto: S70 plan post-K-033, opción B. sim009 (S68) demostró cierre Q-045
al ~99.88% (sweet-spot h_0=1.03, n=4). El residuo 0.12% es probablemente
artefacto del paso adaptativo cerca del cruce h=1.

Estrategia:
  - RK45 Dormand-Prince adaptativo (orden 5 con error estimación orden 4).
  - Tolerancia razonable (1e-8) — más fino sería inviable.
  - Paso refinado en banda |h-1| < 0.005.
  - Verificación cruzada con sim009 RK4.

Objetivo: cierre Q-045 al ≥ 99.99% o documentar bound numérico intrínseco.

Sin scipy. RK45 Dormand-Prince manual.
"""

import math


# ============================================================
# Perfiles h(x)
# ============================================================

def h_power(x, h0, n):
    if x <= 0:
        return 0.0
    return h0 * x ** n


def hp_power(x, h0, n):
    if x <= 0:
        return 0.0 if n > 1 else h0
    return n * h0 * x ** (n - 1)


# ============================================================
# RHS TOV anisotrópica
# ============================================================

def rhs(x, state, h_fn, hp_fn, h_max=3.99, dy_cap=1e12):
    m, y, Phi = state
    if y <= 0:
        return [0.0, 0.0, 0.0]

    h_raw = h_fn(x)
    hp = hp_fn(x)
    h = min(max(h_raw, -1.99), h_max)

    denom_grav = x * (x - m)
    if denom_grav <= 0:
        return [0.0, -1e30, 1e30]

    aniso_denom = 1.0 - h
    if abs(aniso_denom) < 1e-5:
        sign = 1.0 if aniso_denom > 0 else -1.0
        aniso_factor = sign * 1e5
    else:
        aniso_factor = 1.0 / aniso_denom

    grav_term = y * (4.0 - h) * (m + (x ** 3) * y * (1.0 - h)) / (2.0 * denom_grav)
    src_term = 3.0 * y * h / x

    dy = aniso_factor * (y * hp - grav_term + src_term)

    if abs(dy) > dy_cap:
        dy = math.copysign(dy_cap, dy)

    dm = 3.0 * x ** 2 * y

    w_r = y * (1.0 - h) / 3.0
    dPhi = (m + 3.0 * (x ** 3) * w_r) / (2.0 * denom_grav)

    return [dm, dy, dPhi]


# ============================================================
# RK45 Dormand-Prince
# ============================================================

DP_C = [0.0, 1/5, 3/10, 4/5, 8/9, 1.0, 1.0]
DP_A = [
    [],
    [1/5],
    [3/40, 9/40],
    [44/45, -56/15, 32/9],
    [19372/6561, -25360/2187, 64448/6561, -212/729],
    [9017/3168, -355/33, 46732/5247, 49/176, -5103/18656],
    [35/384, 0, 500/1113, 125/192, -2187/6784, 11/84],
]
DP_B5 = [35/384, 0, 500/1113, 125/192, -2187/6784, 11/84, 0]
DP_B4 = [5179/57600, 0, 7571/16695, 393/640, -92097/339200, 187/2100, 1/40]
DP_E = [DP_B5[i] - DP_B4[i] for i in range(7)]


def rk45_step(f, x, state, h_step, *args):
    n_state = len(state)
    k = []
    k1 = f(x, state, *args)
    k.append(k1)
    for i in range(1, 7):
        s_i = list(state)
        for j in range(i):
            for d in range(n_state):
                s_i[d] += h_step * DP_A[i][j] * k[j][d]
        ki = f(x + DP_C[i] * h_step, s_i, *args)
        k.append(ki)
    new_state = list(state)
    for d in range(n_state):
        for i in range(7):
            new_state[d] += h_step * DP_B5[i] * k[i][d]
    err_sq = 0.0
    for d in range(n_state):
        err_d = 0.0
        for i in range(7):
            err_d += DP_E[i] * k[i][d]
        err_d *= h_step
        scale = max(abs(state[d]), abs(new_state[d]), 1e-10)
        err_sq += (err_d / scale) ** 2
    err_norm = math.sqrt(err_sq / n_state)
    return new_state, err_norm


def integrate_rk45(y_c, h_fn, hp_fn,
                   x0=1e-6, x_max=0.99999,
                   tol=1e-8, h_init=1e-4, h_min=1e-12, h_max_step=1e-2,
                   max_steps=500_000,
                   h_max_dec=3.99,
                   crossing_window=0.005, crossing_step=1e-6):
    """Integrador adaptativo RK45 con manejo del cruce h=1."""
    m0 = y_c * x0 ** 3
    y0 = y_c * (1.0 - 2.0 * y_c * x0 ** 2)
    state = [m0, y0, 0.0]
    x = x0

    h_at_x = h_fn(x)
    history = [(x, state[0], state[1], state[2], h_at_x,
                state[1]*(1-h_at_x)/3, state[1]*(1+h_at_x/2)/3)]

    h_step = h_init
    n_steps = 0
    n_rejected = 0

    for _ in range(max_steps):
        compactness = state[0] / x if x > 0 else 0.0
        margin = x - state[0]
        if margin <= 0:
            return history, "fail_compact_1", {"steps": n_steps,
                                                "compactness": compactness,
                                                "n_rejected": n_rejected}

        h_now = h_fn(x)
        h_step_max = h_max_step
        if abs(h_now - 1.0) < crossing_window:
            h_step_max = min(h_step_max, crossing_step)
        if x > 0.99:
            h_step_max = min(h_step_max, 1e-5)

        h_adapt = min(h_step, h_step_max, 0.01 * margin)
        if x + h_adapt > x_max:
            h_adapt = x_max - x

        if h_adapt < h_min:
            status = "x_max" if x >= x_max * 0.9999 else "compact_1"
            return history, status, {"steps": n_steps, "x_end": x,
                                       "compactness": compactness,
                                       "n_rejected": n_rejected}

        new_state, err_norm = rk45_step(rhs, x, state, h_adapt, h_fn, hp_fn, h_max_dec)

        if err_norm > tol and h_adapt > h_min * 10:
            h_step = max(h_step * 0.5, h_min)
            n_rejected += 1
            continue

        if new_state[1] <= 0:
            frac = state[1] / max(state[1] - new_state[1], 1e-30)
            x_surf = x + frac * h_adapt
            m_surf = state[0] + frac * h_adapt * 3 * x ** 2 * state[1]
            history.append((x_surf, m_surf, 0.0, state[2], h_fn(x_surf), 0.0, 0.0))
            return history, "surface", {"steps": n_steps, "x_surface": x_surf,
                                          "n_rejected": n_rejected}

        if new_state[1] > 1e18 or math.isnan(new_state[1]) or math.isinf(new_state[1]):
            return history, "fail_y_explosive", {"steps": n_steps, "x_end": x,
                                                   "n_rejected": n_rejected}

        x = x + h_adapt
        state = new_state
        n_steps += 1

        h_at_x = h_fn(x)
        history.append((x, state[0], state[1], state[2], h_at_x,
                        state[1]*(1-h_at_x)/3, state[1]*(1+h_at_x/2)/3))

        if state[0] / x >= 0.9999:
            return history, "compact_1", {"steps": n_steps, "x_end": x,
                                            "compactness": state[0]/x,
                                            "n_rejected": n_rejected}

        if x >= x_max:
            return history, "x_max", {"steps": n_steps, "x_end": x,
                                        "compactness": state[0]/x,
                                        "n_rejected": n_rejected}

        if err_norm < tol * 0.1 and h_step < h_max_step:
            h_step = min(h_step * 1.2, h_max_step)

    return history, "max_steps", {"steps": n_steps, "n_rejected": n_rejected}


def integrate_rk45_power(y_c, h0, n, **kwargs):
    h_fn = lambda x: h_power(x, h0, n)
    hp_fn = lambda x: hp_power(x, h0, n)
    return integrate_rk45(y_c, h_fn, hp_fn, **kwargs)


def profile_summary(hist):
    if len(hist) < 2:
        return {}
    x_end, m_end, y_end, Phi_end, h_end, wr_end, wt_end = hist[-1]
    return {
        "x_end": x_end,
        "m_end": m_end,
        "y_end": y_end,
        "h_end": h_end,
        "n_points": len(hist),
    }


# ============================================================
# Tests simplificados
# ============================================================

def test_compare_rk4_rk45():
    """Comparación clave: RK4 vs RK45 en sweet-spot."""
    print("[Test 1] RK4 (sim009) vs RK45 (sim010) en sweet-spot h_0=1.03, n=4:")
    print()

    # sim009 RK4
    import sys
    sys.path.insert(0, '.')
    from sim009_tov_h_extended import integrate_power_ext, profile_summary as ps9
    hist4, _, _ = integrate_power_ext(100.0, 1.03, 4)
    s4 = ps9(hist4)
    print(f"  sim009 RK4 manual:  m_end = {s4['m_end']:.6f}, x_end = {s4['x_end']:.6f}")

    # sim010 RK45 con tol 1e-7
    hist45a, _, infoa = integrate_rk45_power(100.0, 1.03, 4, tol=1e-7)
    sa = profile_summary(hist45a)
    print(f"  sim010 RK45 tol=1e-7: m_end = {sa['m_end']:.6f}, x_end = {sa['x_end']:.6f}, steps = {infoa['steps']}, rej = {infoa['n_rejected']}")

    # sim010 RK45 con tol 1e-9
    hist45b, _, infob = integrate_rk45_power(100.0, 1.03, 4, tol=1e-9, max_steps=100_000)
    sb = profile_summary(hist45b)
    print(f"  sim010 RK45 tol=1e-9: m_end = {sb['m_end']:.6f}, x_end = {sb['x_end']:.6f}, steps = {infob['steps']}, rej = {infob['n_rejected']}")


def test_sweep_h0():
    """Barrido de h_0 con RK45 fino."""
    print("\n[Test 2] Barrido fino h_0 (n=4, RK45 tol=1e-8):")
    print(f"   {'h_0':>10} {'m_end':>12} {'x_end':>12} {'compactness':>12} {'steps':>8}")

    for h0 in [1.020, 1.025, 1.028, 1.030, 1.032, 1.035, 1.040, 1.050]:
        hist, status, info = integrate_rk45_power(100.0, h0, 4, tol=1e-8, max_steps=50_000)
        s = profile_summary(hist)
        c = s['m_end']/s['x_end'] if s['x_end'] > 0 else 0.0
        marker = ' ✓' if s['m_end'] >= 0.9999 else ''
        print(f"   {h0:>10.4f} {s['m_end']:>12.6f} {s['x_end']:>12.6f} {c:>12.6f} {info['steps']:>8d} {marker}")


def test_robustness_yc():
    """Robustez vs y_c con sweet-spot."""
    print("\n[Test 3] Robustez vs y_c (h_0=1.03, n=4, tol=1e-8):")
    print(f"   {'y_c':>10} {'m_end':>12} {'x_end':>12}")

    for yc in [10.0, 100.0, 1000.0]:
        hist, status, info = integrate_rk45_power(yc, 1.03, 4, tol=1e-8, max_steps=50_000)
        s = profile_summary(hist)
        print(f"   {yc:>10.1f} {s['m_end']:>12.6f} {s['x_end']:>12.6f}")


def main():
    print("=" * 76)
    print("sim010 — TOV anisotrópica RK45 Dormand-Prince refinado")
    print("=" * 76)
    print()

    test_compare_rk4_rk45()
    test_sweep_h0()
    test_robustness_yc()

    print("\n" + "=" * 76)
    print("ANÁLISIS sim010")
    print("=" * 76)


if __name__ == "__main__":
    main()
