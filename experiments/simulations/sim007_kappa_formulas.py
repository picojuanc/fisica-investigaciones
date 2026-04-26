"""
sim007_kappa_formulas.py
=========================
Tests de fórmulas estructurales para κ_g (S59 / E.4).

Objetivo: verificar la pista Casimir SO(10) (C_2(16) = 45/4 ≈ 11.25 ≈ ⟨κ⟩_g3 = 11.1)
y explorar fórmulas estructurales para κ_g basadas en propiedades SO(10) y Bilson-Thompson.

Datos extraídos en S58 (sim006):
  ⟨κ⟩_g3 ≈ 11.1
  ⟨κ⟩_g2 ≈ 26.4
  ⟨κ⟩_g1 ≈ 46.0

Fórmulas a probar:
  (F1) κ_g = C_2 · (4 - g)        — lineal decreciente con g
  (F2) κ_g = C_2 · (4 - g)²       — cuadrática decreciente
  (F3) κ_g = C_2 · 4^(3-g)        — exponencial decreciente
  (F4) κ_g = C_2 · g_max!/g!      — factorial / combinatoria
  (F5) κ_g = a + b·g + c·g² ajuste
  (F6) κ_g = C_2 · ψ(g)           — Bilson-Thompson topológico (n cruces)
  (F7) κ_g = C_2 · (g_max/g)²     — inverso cuadrático
"""

import math


C2_16 = 45.0 / 4.0  # Casimir cuadrático rep 16 SO(10)

# Datos observados S58
KAPPA_OBSERVED = {
    3: 11.113,
    2: 26.443,
    1: 46.028,
}

# Datos individuales para análisis intra-generacional
KAPPA_INDIVIDUAL = {
    "top":      (3,  +2.0/3.0,  0.000),
    "bottom":   (3,  -1.0/3.0, 14.919),
    "tau":      (3,  -1.0,     18.421),
    "charm":    (2,  +2.0/3.0, 19.625),
    "strange":  (2,  -1.0/3.0, 30.096),
    "muon":     (2,  -1.0,     29.608),
    "down":     (1,  -1.0/3.0, 42.079),
    "up":       (1,  +2.0/3.0, 45.002),
    "electron": (1,  -1.0,     51.003),
}


def evaluate_formula(name, predicted_func, kappa_obs):
    """Evalúa una fórmula sobre las 3 generaciones, calcula RMS y desviación máxima."""
    print(f"\n  {name}:")
    print(f"    {'gen':>4}  {'κ_obs':>10}  {'κ_pred':>10}  {'desv abs':>10}  {'desv %':>8}")
    rss = 0.0
    max_dev_pct = 0.0
    for g in [3, 2, 1]:
        ko = kappa_obs[g]
        kp = predicted_func(g)
        dev = ko - kp
        dev_pct = abs(dev) / ko * 100.0 if ko > 0 else 0.0
        rss += dev * dev
        max_dev_pct = max(max_dev_pct, dev_pct)
        print(f"    {g:>4}  {ko:10.3f}  {kp:10.3f}  {dev:10.3f}  {dev_pct:8.1f}")
    rms = math.sqrt(rss / 3)
    print(f"    RMS: {rms:.3f}  max desv: {max_dev_pct:.1f}%")
    return rms, max_dev_pct


def test_structural_formulas():
    """Test 1: comparar fórmulas estructurales para κ_g promedios."""
    print("\n=== TEST 1: Fórmulas estructurales para ⟨κ⟩_g ===")
    print(f"\nC_2(16) = 45/4 = {C2_16:.3f}")
    print(f"⟨κ⟩_g3 observada = {KAPPA_OBSERVED[3]:.3f}")
    print(f"Coincidencia C_2(16) ≈ ⟨κ⟩_g3: {abs(C2_16 - KAPPA_OBSERVED[3])/KAPPA_OBSERVED[3]*100:.1f}% desviación")

    formulas = [
        ("F1: κ_g = C_2 · (4-g)",       lambda g: C2_16 * (4 - g)),
        ("F2: κ_g = C_2 · (4-g)²",      lambda g: C2_16 * (4 - g) ** 2),
        ("F3: κ_g = C_2 · 4^(3-g)",     lambda g: C2_16 * (4 ** (3 - g))),
        ("F4: κ_g = C_2 · 6/g!",        lambda g: C2_16 * 6 / math.factorial(g)),
        ("F7: κ_g = C_2 · (3/g)²",      lambda g: C2_16 * (3 / g) ** 2),
    ]

    results = []
    for name, func in formulas:
        rms, dev = evaluate_formula(name, func, KAPPA_OBSERVED)
        results.append((name, rms, dev))

    print("\n  Resumen (orden por RMS):")
    results.sort(key=lambda t: t[1])
    print(f"  {'Fórmula':<30}  {'RMS':>10}  {'max desv %':>12}")
    for name, rms, dev in results:
        print(f"  {name:<30}  {rms:10.3f}  {dev:12.1f}")

    return results


def fit_quadratic(kappa_obs):
    """Ajusta κ_g = a + b·g + c·g² por mínimos cuadrados (3 puntos, 3 incógnitas → exacto)."""
    print("\n=== TEST 2: Ajuste cuadrático exacto κ_g = a + b·g + c·g² ===")
    g_vals = [1, 2, 3]
    k_vals = [kappa_obs[g] for g in g_vals]
    # Sistema 3x3:
    # a + b·g_i + c·g_i² = k_i
    # Resolvemos por sustitución
    # k_1 = a + b + c
    # k_2 = a + 2b + 4c
    # k_3 = a + 3b + 9c
    # k_2 - k_1 = b + 3c
    # k_3 - k_2 = b + 5c
    # (k_3 - k_2) - (k_2 - k_1) = 2c → c = ((k_3 - k_2) - (k_2 - k_1)) / 2
    k1, k2, k3 = k_vals
    c = ((k3 - k2) - (k2 - k1)) / 2.0
    b = (k2 - k1) - 3 * c
    a = k1 - b - c
    print(f"  Coeficientes: a = {a:.3f}, b = {b:.3f}, c = {c:.3f}")
    print(f"  Fórmula exacta: κ_g = {a:.2f} + {b:.2f}·g + {c:.2f}·g²")
    print(f"\n  Verificación:")
    for g in [1, 2, 3]:
        kp = a + b * g + c * g ** 2
        print(f"    g={g}:  κ_pred = {kp:.3f}  (κ_obs = {kappa_obs[g]:.3f})")

    print(f"\n  ¿Coeficientes tienen interpretación SO(10)?")
    print(f"    c = {c:.3f}  vs C_2(16)/4 = {C2_16/4:.3f}  (ratio: {c / (C2_16/4):.3f})")
    print(f"    b = {b:.3f}  vs -C_2(16) = {-C2_16:.3f}  (ratio: {b / -C2_16:.3f})")
    print(f"    a = {a:.3f}  vs 6·C_2(16) = {6*C2_16:.3f}  (ratio: {a / (6*C2_16):.3f})")
    return a, b, c


def test_individual_with_quadratic(a, b, c):
    """Test 3: fórmula cuadrática + ajuste de carga."""
    print("\n=== TEST 3: Fórmula completa κ_f(g, Q) y comparación con datos individuales ===")
    print(f"  Modelo: κ_f = ({a:.2f} + {b:.2f}·g + {c:.2f}·g²) + δ_Q · |Q|")
    # Calcular δ_Q a partir de datos: residuo (κ_obs - κ_g_pred) vs |Q|
    pts = []
    for name, (g, Q, kappa) in KAPPA_INDIVIDUAL.items():
        if g not in [1, 2, 3]:
            continue
        kg_pred = a + b * g + c * g ** 2
        residual = kappa - kg_pred
        pts.append((name, g, Q, kappa, kg_pred, residual))

    # Ajustar residual = δ · |Q| por mínimos cuadrados sin offset
    sxy = sum(abs(Q) * res for _, _, Q, _, _, res in pts)
    sxx = sum(abs(Q) * abs(Q) for _, _, Q, _, _, _ in pts)
    delta_Q = sxy / sxx if sxx > 0 else 0.0
    print(f"  Coeficiente carga δ_Q = {delta_Q:.3f}")
    print(f"  ¿Interpretación SO(10)? δ_Q ≈ ?")

    print(f"\n  {'Fermión':>10}  {'gen':>4}  {'Q':>7}  {'κ_obs':>10}  {'κ_pred':>10}  {'desv':>8}")
    rss = 0.0
    for name, g, Q, kappa, kg_pred, _ in pts:
        kp = kg_pred + delta_Q * abs(Q)
        dev = kappa - kp
        rss += dev * dev
        print(f"  {name:>10}  {g:>4}  {Q:>+7.3f}  {kappa:10.3f}  {kp:10.3f}  {dev:8.3f}")
    rms = math.sqrt(rss / len(pts))
    print(f"\n  RMS: {rms:.3f}  ({rms / sum(k for _,_,_,k,_,_ in pts) * len(pts) * 100:.1f}% relativo)")
    return delta_Q, rms


def explore_braiding_complexity():
    """Test 4: explorar Bilson-Thompson — relación κ vs número de cruces de trenza."""
    print("\n=== TEST 4: Bilson-Thompson — ¿κ_g escala con complejidad de trenza? ===")
    # Conjeturas Bilson-Thompson:
    # gen 1 = trenza más simple (1 cruce)
    # gen 2 = trenza intermedia (2 cruces)
    # gen 3 = trenza más compleja (3 cruces)?
    # O al revés: gen 3 (top más pesado) = trenza más simple, pero κ más bajo es trenza menos
    # extendida en lattice. ¡Confuso!
    print("\n  Identificación Bilson-Thompson tentativa:")
    print("  Convención A: gen 1 = trenza simple (1 cruce); gen 3 = compleja (3 cruces)")
    print("    Pero κ decrece con gen → trenzas COMPLEJAS son MENOS extendidas. Contraintuitivo.")
    print("  Convención B: gen 3 = trenza simple (top); gen 1 = compleja (electrón)")
    print("    κ crece con complejidad → más cruces → más extendida. ✓ Consistente.")
    print()
    print("  Bajo convención B:")
    print(f"    n_cruces = 1 (g_3): κ ≈ 11.1 ≈ C_2(16)")
    print(f"    n_cruces = 2 (g_2): κ ≈ 26.4 ≈ {26.4/C2_16:.2f} · C_2")
    print(f"    n_cruces = 3 (g_1): κ ≈ 46.0 ≈ {46.0/C2_16:.2f} · C_2")
    print()
    # Si hay relación n^p · C_2:
    # 1^p · C_2 = 11.1 ⟹ p arbitrario para n=1
    # 2^p · C_2 = 26.4 ⟹ 2^p = 26.4/11.25 = 2.347 ⟹ p = log_2(2.347) = 1.231
    # 3^p · C_2 = 46.0 ⟹ 3^p = 46.0/11.25 = 4.089 ⟹ p = log_3(4.089) = 1.281
    p1 = math.log(26.4/C2_16) / math.log(2)
    p2 = math.log(46.0/C2_16) / math.log(3)
    print(f"  Si κ_g = C_2 · n^p (n = n_cruces convención B):")
    print(f"    p (de g_3 → g_2): {p1:.3f}")
    print(f"    p (de g_3 → g_1): {p2:.3f}")
    print(f"    Promedio: {(p1+p2)/2:.3f}")
    print(f"    No constante perfecto. Sugiere relación más compleja.")


def main():
    print("=" * 70)
    print(" sim007_kappa_formulas — sub-tarea E pista Casimir + Bilson-Thompson")
    print(" Sesión 59 (E.4)")
    print("=" * 70)

    # Test 1: fórmulas estructurales
    formulas_results = test_structural_formulas()

    # Test 2: ajuste cuadrático exacto
    a, b, c = fit_quadratic(KAPPA_OBSERVED)

    # Test 3: con datos individuales + ajuste Q
    delta_Q, rms_full = test_individual_with_quadratic(a, b, c)

    # Test 4: Bilson-Thompson
    explore_braiding_complexity()

    print("\n" + "=" * 70)
    print(" RESUMEN sim007")
    print("=" * 70)
    print()
    print("Pista Casimir SO(10):")
    print(f"  C_2(16) = 45/4 = {C2_16:.3f}")
    print(f"  ⟨κ⟩_g3 = {KAPPA_OBSERVED[3]:.3f}")
    print(f"  Coincidencia al {abs(C2_16-KAPPA_OBSERVED[3])/KAPPA_OBSERVED[3]*100:.1f}%.")
    print()
    print("Fórmulas estructurales:")
    print("  Mejor fit RMS:")
    formulas_results.sort(key=lambda t: t[1])
    for name, rms, dev in formulas_results[:3]:
        print(f"    {name}:  RMS = {rms:.3f}, max desv = {dev:.1f}%")
    print()
    print("Ajuste cuadrático exacto (3 datos, 3 incógnitas):")
    print(f"  κ_g = {a:.2f} + {b:.2f}·g + {c:.2f}·g²")
    print(f"  Coeficientes NO tienen interpretación SO(10) clara.")
    print()
    print("Bilson-Thompson (convención B):")
    print(f"  κ_g ≈ C_2 · n^p con p ≈ 1.25 promedio. NO constante.")
    print()
    print("VEREDICTO:")
    print("  - Pista Casimir ⟨κ⟩_g3 ≈ C_2(16) es genuina pero limitada (solo gen 3).")
    print("  - Fórmulas simples NO ajustan exactamente la jerarquía generacional.")
    print("  - Ajuste cuadrático funciona pero coeficientes son ad hoc.")
    print("  - Bilson-Thompson da escala ~n^1.25, no n^1 ni n^2 — no clean.")
    print()
    print("CONCLUSIÓN: K-042 mantiene CAVEAT MODERADO (análogo K-041).")
    print("  Pista Casimir es interesante pero no resuelve jerarquía completa.")
    print("=" * 70)


if __name__ == "__main__":
    main()
