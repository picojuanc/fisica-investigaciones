"""
sim006_kappa_patterns.py
=========================
Análisis de patrones en κ_f extraídos de datos SM.

Modelo S58 (E.3): cuerda abierta SCG en equilibrio dinámico tensión-Casimir.
  E(d) = T·d - ℏc·κ_f/d
  ∂E/∂d = 0 ⟹ d_LR = √(ℏc κ_f / T) = √κ_f · ℓ_P  (con T = ℏc/ℓ_P²)

Yukawa con perfil gaussiano (consistente con cuadrática):
  y_f = exp(-d_LR² / (4 ℓ_s²)) = exp(-κ_f ℓ_P² / (4 ℓ_s²))

Con ℓ_s = ℓ_P:
  κ_f = -4 ln(y_f)

Pregunta: ¿hay patrón identificable en κ_f con propiedades fermiónicas?

Tests:
  1. κ_f vs generación (¿lineal?).
  2. κ_f vs (Q, color).
  3. κ_f por familias (lepton vs quark up vs quark down).
  4. Razones κ_f / κ_g (entre generaciones distintas).
  5. κ_f como combinación entera de invariantes.

Sin scipy/matplotlib.
"""

import math


# Datos observacionales SM
# (nombre, y/y_t, Q (carga eléctrica), color (1=quark, 0=lepton), generación)
FERMIONS = [
    # gen 3
    ("top",      1.000e+00,  +2.0/3.0, 1, 3),
    ("bottom",   2.400e-02,  -1.0/3.0, 1, 3),
    ("tau",      1.000e-02,  -1.0,     0, 3),
    # gen 2
    ("charm",    7.400e-03,  +2.0/3.0, 1, 2),
    ("strange",  5.400e-04,  -1.0/3.0, 1, 2),
    ("muon",     6.100e-04,  -1.0,     0, 2),
    # gen 1
    ("down",     2.700e-05,  -1.0/3.0, 1, 1),
    ("up",       1.300e-05,  +2.0/3.0, 1, 1),
    ("electron", 2.900e-06,  -1.0,     0, 1),
]


def kappa_from_y(y, ell_s_over_ell_P=1.0):
    """κ_f = -4·(ℓ_s/ℓ_P)²·ln(y) — extraído de y_f bajo modelo dinámico gauss."""
    if y >= 1.0:
        return 0.0
    return -4.0 * (ell_s_over_ell_P ** 2) * math.log(y)


def test_kappa_table():
    """Tabla principal: κ_f por fermión + propiedades."""
    print("\n=== TEST 1: Tabla κ_f y propiedades ===")
    print(f"{'Fermión':>10}  {'y/y_t':>12}  {'κ (ℓ_s=ℓ_P)':>13}  {'d_LR/ℓ_P':>10}  {'Q':>7}  {'color':>5}  {'gen':>3}")
    data = []
    for name, y, Q, color, gen in FERMIONS:
        k = kappa_from_y(y, 1.0)
        d = math.sqrt(k)
        data.append((name, y, k, d, Q, color, gen))
        print(f"{name:>10}  {y:12.3e}  {k:13.4f}  {d:10.4f}  {Q:>+7.3f}  {color:>5d}  {gen:>3d}")
    return data


def test_by_generation(data):
    """Test 2: ¿κ_f varía con generación?"""
    print("\n=== TEST 2: κ_f por generación ===")
    print(f"{'gen':>4}  {'fermiones':>30}  {'κ rango':>20}  {'κ medio':>10}")
    by_gen = {1: [], 2: [], 3: []}
    for name, y, k, d, Q, color, gen in data:
        by_gen[gen].append((name, k))
    for gen in [3, 2, 1]:
        items = by_gen[gen]
        ks = [k for _, k in items]
        names = ", ".join(n for n, _ in items)
        if ks:
            kmin, kmax, kmean = min(ks), max(ks), sum(ks) / len(ks)
            print(f"{gen:>4}  {names:>30}  {f'[{kmin:.2f}, {kmax:.2f}]':>20}  {kmean:10.3f}")


def test_by_charge_class(data):
    """Test 3: κ_f por clase de carga."""
    print("\n=== TEST 3: κ_f por clase (up-quark, down-quark, lepton) ===")
    classes = {
        "up-quarks (Q=+2/3)": [(n, k, gen) for n, _, k, _, Q, c, gen in data if abs(Q - 2.0/3.0) < 0.01],
        "down-quarks (Q=-1/3)": [(n, k, gen) for n, _, k, _, Q, c, gen in data if abs(Q + 1.0/3.0) < 0.01],
        "leptones (Q=-1)": [(n, k, gen) for n, _, k, _, Q, c, gen in data if abs(Q + 1.0) < 0.01],
    }
    for cls, items in classes.items():
        print(f"\n  {cls}:")
        items.sort(key=lambda t: t[2])  # ordenar por gen
        for name, k, gen in items:
            print(f"    gen {gen}: {name:>10}  κ = {k:.3f}")


def test_ratios(data):
    """Test 4: razones κ_f / κ_g entre fermiones."""
    print("\n=== TEST 4: Razones κ entre generaciones (misma carga) ===")
    classes = {
        "up-quarks": [(n, k, gen) for n, _, k, _, Q, c, gen in data if abs(Q - 2.0/3.0) < 0.01],
        "down-quarks": [(n, k, gen) for n, _, k, _, Q, c, gen in data if abs(Q + 1.0/3.0) < 0.01],
        "leptones": [(n, k, gen) for n, _, k, _, Q, c, gen in data if abs(Q + 1.0) < 0.01],
    }
    for cls, items in classes.items():
        items.sort(key=lambda t: t[2])
        print(f"\n  {cls}:")
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                ni, ki, gi = items[i]
                nj, kj, gj = items[j]
                if ki > 0:
                    ratio = kj / ki
                    print(f"    κ({nj}, gen{gj}) / κ({ni}, gen{gi}) = {kj:.2f}/{ki:.2f} = {ratio:.3f}")


def test_lineal_fit(data):
    """Test 5: ¿κ_f tiene ajuste lineal en alguna variable simple?"""
    print("\n=== TEST 5: Ajuste lineal κ_f ≈ A + B · gen + C · |Q| ===")
    # Modelo: κ_f = A + B · gen + C · |Q| (lineal)
    # Resolver mínimos cuadrados manualmente
    pts = [(k, gen, abs(Q)) for n, _, k, _, Q, c, gen in data if k > 0]
    n = len(pts)
    # Variables: x = (1, gen, |Q|), y = κ
    # Construir sistema normal
    sx = [0.0, 0.0, 0.0]  # sum(1), sum(gen), sum(|Q|)
    sy = 0.0
    sxy = [0.0, 0.0, 0.0]
    sxx = [[0.0] * 3 for _ in range(3)]
    for (k, gen, Q) in pts:
        x = [1.0, float(gen), Q]
        for i in range(3):
            sx[i] += x[i]
            sxy[i] += x[i] * k
            for j in range(3):
                sxx[i][j] += x[i] * x[j]
        sy += k
    # Resolver sxx · β = sxy via eliminación gaussiana
    M = [row[:] + [sxy[i]] for i, row in enumerate(sxx)]
    # Gaussian elimination 3x3
    for i in range(3):
        # pivot
        max_row = i
        for r in range(i + 1, 3):
            if abs(M[r][i]) > abs(M[max_row][i]):
                max_row = r
        M[i], M[max_row] = M[max_row], M[i]
        for r in range(i + 1, 3):
            factor = M[r][i] / M[i][i]
            for c in range(4):
                M[r][c] -= factor * M[i][c]
    # back substitution
    beta = [0.0, 0.0, 0.0]
    for i in [2, 1, 0]:
        s = M[i][3]
        for j in range(i + 1, 3):
            s -= M[i][j] * beta[j]
        beta[i] = s / M[i][i]
    A, B, C = beta
    print(f"  Ajuste: κ_f ≈ {A:.3f} + {B:.3f} · gen + {C:.3f} · |Q|")
    # Calcular residuos
    rss = 0.0
    print(f"  {'Fermión':>10}  {'κ_obs':>10}  {'κ_pred':>10}  {'residuo':>10}")
    for n, _, k, _, Q, c, gen in data:
        if k <= 0:
            continue
        kp = A + B * gen + C * abs(Q)
        r = k - kp
        rss += r * r
        print(f"  {n:>10}  {k:10.3f}  {kp:10.3f}  {r:10.3f}")
    rms = math.sqrt(rss / max(1, len(pts)))
    # Compute relative RMS
    mean_k = sum(k for _, _, k, _, _, _, _ in data if k > 0) / max(1, sum(1 for _, _, k, _, _, _, _ in data if k > 0))
    rel_rms = rms / mean_k if mean_k > 0 else 0.0
    print(f"  RMS residual: {rms:.3f}  (RMS relativo: {rel_rms*100:.1f}%)")
    return A, B, C, rms


def test_inverse_gen(data):
    """Test 6: ¿κ_f ≈ -ln(y) escala como 1/gen?"""
    print("\n=== TEST 6: ¿κ_f decrece como gen creciente? ===")
    by_gen = {1: [], 2: [], 3: []}
    for n, _, k, _, _, _, gen in data:
        if k > 0:
            by_gen[gen].append(k)
    for gen in [1, 2, 3]:
        if by_gen[gen]:
            mean = sum(by_gen[gen]) / len(by_gen[gen])
            print(f"  gen {gen}: ⟨κ⟩ = {mean:.3f}")
    # Razones
    if by_gen[1] and by_gen[2] and by_gen[3]:
        m1 = sum(by_gen[1]) / len(by_gen[1])
        m2 = sum(by_gen[2]) / len(by_gen[2])
        m3 = sum(by_gen[3]) / len(by_gen[3])
        print(f"  ⟨κ⟩_g1 / ⟨κ⟩_g2 = {m1/m2:.3f}")
        print(f"  ⟨κ⟩_g2 / ⟨κ⟩_g3 = {m2/m3:.3f}")
        print(f"  ⟨κ⟩_g1 / ⟨κ⟩_g3 = {m1/m3:.3f}")


def main():
    print("=" * 70)
    print(" sim006_kappa_patterns — análisis κ_f desde modelo dinámico SCG")
    print(" Sesión 58 (E.3)")
    print("=" * 70)

    data = test_kappa_table()
    test_by_generation(data)
    test_by_charge_class(data)
    test_ratios(data)
    A, B, C, rms = test_lineal_fit(data)
    test_inverse_gen(data)

    print("\n" + "=" * 70)
    print(" RESUMEN sim006")
    print("=" * 70)
    print()
    print("Test 1: κ_f extraídos de SM por modelo dinámico:")
    print("  rango: 0 (top) a ~51 (electrón).")
    print()
    print("Test 2: tendencia generacional:")
    print("  gen 3: κ ~ 0-18  (top más liviano en κ).")
    print("  gen 2: κ ~ 19-30")
    print("  gen 1: κ ~ 42-51 (electrón más pesado en κ).")
    print()
    print("Test 5: ajuste lineal κ ≈ {:.2f} + {:.2f}·gen + {:.2f}·|Q|".format(A, B, C))
    print("  RMS residual: {:.3f} (relativo ~{:.0f}% del valor medio).".format(rms, rms/30*100))
    print()
    print("VEREDICTO:")
    print("  - κ_f tiene tendencia generacional clara (decreciente con gen).")
    print("  - Variación intra-generacional (entre fermiones) más sutil.")
    print("  - NO hay derivación cuantitativa desde primeros principios SCG.")
    print("  - Forma funcional d_LR = √κ_f · ℓ_P es derivada (mecanismo dinámico).")
    print("  - Valores específicos κ_f requieren postulado o teoría más profunda.")
    print()
    print("⟹ K-042 CANDIDATO CON CAVEAT MODERADO (forma sí, valores no exclusivos).")
    print("  Análogo a K-041 — predicción estructural verificada al orden de mag.")
    print("=" * 70)


if __name__ == "__main__":
    main()
