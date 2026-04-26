"""
sim008_CKM_PMNS_GST.py
=======================
Cálculo CKM/PMNS bajo modelo F+E (S63):
  V_ij ~ sqrt(Y_i * Y_j) (relación GST clásica con jerarquía Yukawa)

Aplicando K-042: y_f = exp(-κ_f / 4) con κ_f extraídos de SM.

Predicción: θ_ij ~ sqrt(m_i / m_j) (Gatto-Sartori-Tonin 1968).

Tests:
  1. Calcular ángulos CKM bajo GST aplicado a Yukawas SCG.
  2. Comparar con observado.
  3. Calcular ángulos PMNS análogamente.
  4. Identificar qué ángulos predice correctamente y cuáles no.

Sin scipy/matplotlib.
"""

import math


# Datos SM observados
# (nombre, masa en MeV (corriendo a M_Z), Q, gen, sector)
QUARKS_UP = [
    ("up",    2.2,         +2.0/3.0, 1, "u"),
    ("charm", 1275,         +2.0/3.0, 2, "u"),
    ("top",   173000,       +2.0/3.0, 3, "u"),
]
QUARKS_DOWN = [
    ("down",    4.7,        -1.0/3.0, 1, "d"),
    ("strange", 95,         -1.0/3.0, 2, "d"),
    ("bottom",  4180,       -1.0/3.0, 3, "d"),
]
LEPTONS = [
    ("electron", 0.511,     -1.0, 1, "e"),
    ("muon",     105.7,     -1.0, 2, "e"),
    ("tau",      1777,      -1.0, 3, "e"),
]
NEUTRINOS = [
    # masas neutrinos: estimaciones; ν_1 más ligero
    ("nu_1", 0.001,          0.0, 1, "nu"),
    ("nu_2", 0.009,          0.0, 2, "nu"),
    ("nu_3", 0.05,           0.0, 3, "nu"),
]


# CKM observado
CKM_OBSERVED = {
    "theta_12_deg": 13.0,    # ángulo Cabibbo
    "theta_13_deg": 0.21,
    "theta_23_deg": 2.4,
    "delta_CP_deg": 65.0,
}

# PMNS observado (mejor fit normal hierarchy)
PMNS_OBSERVED = {
    "theta_12_deg": 33.5,
    "theta_13_deg": 8.6,
    "theta_23_deg": 49.0,
    "delta_CP_deg": 217.0,
}


def gst_angle(m_lower, m_higher):
    """Ángulo GST clásico: θ ≈ sqrt(m_lower / m_higher) [rad]."""
    if m_higher <= 0:
        return 0.0
    ratio = m_lower / m_higher
    if ratio < 0:
        return 0.0
    return math.sqrt(ratio)


def predict_CKM_GST_naive():
    """Predice ángulos CKM via GST simple aplicado a masas SM."""
    print("\n=== TEST 1: Predicciones CKM via GST clásico (SCG aplica K-042) ===")
    md = QUARKS_DOWN[0][1]
    ms = QUARKS_DOWN[1][1]
    mb = QUARKS_DOWN[2][1]
    mu = QUARKS_UP[0][1]
    mc = QUARKS_UP[1][1]
    mt = QUARKS_UP[2][1]

    # Cabibbo: theta_12 ~ sqrt(md/ms)
    th12_d = math.sqrt(md / ms)
    th12_u = math.sqrt(mu / mc)
    th12_combined = abs(th12_d - th12_u)  # Different sign convention possible
    th12 = th12_d  # GST original

    # theta_23 ~ sqrt(ms/mb) o sqrt(mc/mt)
    th23_d = math.sqrt(ms / mb)
    th23_u = math.sqrt(mc / mt)
    th23 = th23_d  # Original

    # theta_13 ~ theta_12 * theta_23 (Wolfenstein generic)
    th13 = th12 * th23

    print(f"\n  Predicciones SCG via K-042 + GST clásico:")
    print(f"    θ_12 ≈ √(m_d/m_s) = √({md}/{ms}) = {math.degrees(th12_d):.3f}°")
    print(f"    θ_23 ≈ √(m_s/m_b) = √({ms}/{mb}) = {math.degrees(th23_d):.3f}°")
    print(f"    θ_13 ≈ θ_12·θ_23 = {math.degrees(th13):.3f}°")

    print(f"\n  Comparación con CKM observado:")
    print(f"  {'Ángulo':>10}  {'SCG (deg)':>12}  {'Obs (deg)':>12}  {'Ratio (obs/pred)':>16}")
    pairs = [
        ("θ_12", math.degrees(th12_d), CKM_OBSERVED["theta_12_deg"]),
        ("θ_23", math.degrees(th23_d), CKM_OBSERVED["theta_23_deg"]),
        ("θ_13", math.degrees(th13),    CKM_OBSERVED["theta_13_deg"]),
    ]
    for name, pred, obs in pairs:
        ratio = obs / pred if pred > 0 else 0.0
        print(f"  {name:>10}  {pred:12.4f}  {obs:12.4f}  {ratio:16.3f}")

    return pairs


def predict_PMNS_GST_naive():
    """Predice PMNS via GST simple. Esperar problemas porque PMNS no jerárquico."""
    print("\n=== TEST 2: Predicciones PMNS via GST clásico (SCG aplica K-042) ===")
    me, mmu, mtau = LEPTONS[0][1], LEPTONS[1][1], LEPTONS[2][1]
    mn1, mn2, mn3 = NEUTRINOS[0][1], NEUTRINOS[1][1], NEUTRINOS[2][1]

    th12_e = math.sqrt(me / mmu)
    th23_e = math.sqrt(mmu / mtau)
    th13_e = th12_e * th23_e

    th12_n = math.sqrt(mn1 / mn2)
    th23_n = math.sqrt(mn2 / mn3)
    th13_n = th12_n * th23_n

    # PMNS desde sector cargado
    print(f"\n  Predicciones SCG via leptones cargados:")
    print(f"    θ_12 ≈ √(m_e/m_μ) = {math.degrees(th12_e):.3f}°")
    print(f"    θ_23 ≈ √(m_μ/m_τ) = {math.degrees(th23_e):.3f}°")
    print(f"    θ_13 ≈ {math.degrees(th13_e):.3f}°")
    print(f"\n  Predicciones SCG via neutrinos:")
    print(f"    θ_12 ≈ √(m_ν1/m_ν2) = {math.degrees(th12_n):.3f}°")
    print(f"    θ_23 ≈ √(m_ν2/m_ν3) = {math.degrees(th23_n):.3f}°")

    print(f"\n  Comparación con PMNS observado:")
    print(f"  {'Ángulo':>10}  {'SCG (deg)':>12}  {'Obs (deg)':>12}  {'Ratio':>10}")
    for name, pred, obs in [
        ("θ_12 e", math.degrees(th12_e), PMNS_OBSERVED["theta_12_deg"]),
        ("θ_12 ν", math.degrees(th12_n), PMNS_OBSERVED["theta_12_deg"]),
        ("θ_23 e", math.degrees(th23_e), PMNS_OBSERVED["theta_23_deg"]),
        ("θ_23 ν", math.degrees(th23_n), PMNS_OBSERVED["theta_23_deg"]),
    ]:
        ratio = obs / pred if pred > 0 else 0.0
        print(f"  {name:>10}  {pred:12.4f}  {obs:12.4f}  {ratio:10.3f}")


def predict_with_F_symbols_phases():
    """Test con fases discretas SCG: ángulos predichos con factor de fase."""
    print("\n=== TEST 3: Combinación con fases F-symbols `Spin(10)_1` ===")
    print("\n  Fases discretas disponibles: {0, π/2, π, 3π/2}")
    print("  Hipótesis: ángulo CP = combinación de fases (raíz 4-ésima de unidad)")
    print()
    print(f"  CKM δ_CP observado: {CKM_OBSERVED['delta_CP_deg']}°")
    print(f"  Fases SCG candidatas: 0°, 90°, 180°, 270°")
    print(f"  Distancia mínima a observado:")
    obs = CKM_OBSERVED["delta_CP_deg"]
    discrete = [0, 90, 180, 270]
    closest = min(discrete, key=lambda d: abs(d - obs))
    diff = abs(obs - closest)
    print(f"    Más cercano: {closest}°, diferencia: {diff}° (relativo: {diff/obs*100:.1f}%)")
    print()
    print(f"  PMNS δ_CP observado: {PMNS_OBSERVED['delta_CP_deg']}°")
    obs = PMNS_OBSERVED["delta_CP_deg"]
    closest = min(discrete, key=lambda d: abs(d - obs))
    diff = abs(obs - closest)
    print(f"    Más cercano: {closest}°, diferencia: {diff}° (relativo: {diff/obs*100:.1f}%)")
    print()
    print("  Conclusión: las fases discretas SCG NO coinciden con δ_CP observados.")
    print("  Caveat: requiere amplificación o estructura adicional.")


def predict_F_E_combination():
    """Modelo combinación F+E: V_ij ~ sqrt(Y_i Y_j) · e^(iφ) con φ discreto."""
    print("\n=== TEST 4: Combinación F+E (Yukawas K-042 + fases discretas) ===")
    print("\n  Modelo: V_ij = sqrt(Y_i Y_j) / N · e^(iφ_ij)")
    print("  Y_f = exp(-κ_f / 4) con κ_f extraídos de SM")
    print()

    # Yukawas relativos (a y_t)
    ratios_u = {
        "u":  math.exp(-45.00 / 4.0),
        "c":  math.exp(-19.63 / 4.0),
        "t":  math.exp(-0.000 / 4.0),
    }
    ratios_d = {
        "d":  math.exp(-42.08 / 4.0),
        "s":  math.exp(-30.10 / 4.0),
        "b":  math.exp(-14.92 / 4.0),
    }

    print("  y/y_t calculados desde κ_f (K-042):")
    print(f"    y_u/y_t = {ratios_u['u']:.3e}, y_c/y_t = {ratios_u['c']:.3e}, y_t/y_t = {ratios_u['t']:.3f}")
    print(f"    y_d/y_t = {ratios_d['d']:.3e}, y_s/y_t = {ratios_d['s']:.3e}, y_b/y_t = {ratios_d['b']:.3e}")

    # Calcular elementos V_ij sin normalizar
    print("\n  Matriz |V_ij| ~ sqrt(y_i y_j) (sin normalizar, sin fase):")
    V = {}
    for ui, yu in ratios_u.items():
        for dj, yd in ratios_d.items():
            V[(ui, dj)] = math.sqrt(yu * yd)
            print(f"    |V_{ui}{dj}| ~ sqrt({yu:.2e} * {yd:.2e}) = {math.sqrt(yu*yd):.3e}")

    # Identificar ángulos
    print("\n  Ángulos efectivos (con normalización heurística):")
    # θ_12 from |V_us| / |V_ud| ratio
    th12 = V[("u", "s")] / V[("u", "d")]
    print(f"    θ_12 ~ |V_us|/|V_ud| = {th12:.3f} (en rad: {math.degrees(math.atan(th12)):.2f}°)")
    # Factor exacto: θ_12 ~ sqrt(y_s/y_d) por GST corregido
    th12_alt = math.sqrt(ratios_d["s"] / ratios_d["d"])
    print(f"    Alternativo θ_12 ~ √(y_s/y_d) = {th12_alt:.3f}")


def main():
    print("=" * 70)
    print(" sim008_CKM_PMNS_GST — sub-tarea F (S63)")
    print(" Modelo F+E: GST + fases discretas SCG")
    print("=" * 70)

    pairs_ckm = predict_CKM_GST_naive()
    predict_PMNS_GST_naive()
    predict_with_F_symbols_phases()
    predict_F_E_combination()

    print("\n" + "=" * 70)
    print(" RESUMEN sim008")
    print("=" * 70)
    print()
    print("CKM via GST aplicado a masas SM (SCG K-042):")
    for name, pred, obs in pairs_ckm:
        ratio = obs/pred if pred > 0 else 0.0
        match = "✓" if 0.5 <= ratio <= 2.0 else ("⚠" if 0.2 <= ratio <= 5.0 else "✗")
        print(f"  {name}: SCG = {pred:.3f}°, Obs = {obs:.3f}°, ratio = {ratio:.2f} {match}")
    print()
    print("CKM δ_CP: fases discretas SCG (0°, 90°, 180°, 270°) NO coinciden con 65° observado.")
    print()
    print("PMNS: GST naive predice θ_12 ~ 4° (vs 33° observado) — discrepancia mayor.")
    print("PMNS no-jerárquico requiere mecanismo distinto al de CKM.")
    print()
    print("VEREDICTO PRELIMINAR (S63):")
    print("  - θ_12_CKM (Cabibbo): SCG predice ~13° (GST), coincide con observado.")
    print("  - θ_23_CKM, θ_13_CKM: SCG off por factor 3-9.")
    print("  - δ_CP_CKM: fases discretas no coinciden.")
    print("  - PMNS: GST simple incompatible (no jerárquico).")
    print()
    print("⟹ K-043 candidato CAVEAT FUERTE.")
    print("  Predicción cualitativa (Cabibbo correcto) + valores específicos no derivados.")
    print("=" * 70)


if __name__ == "__main__":
    main()
