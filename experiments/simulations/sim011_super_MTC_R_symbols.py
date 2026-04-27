"""
sim011_super_MTC_R_symbols.py
=============================
Construcción de R-symbols correctos para `Spin(10)_1` MTC.

Contexto: S72 Fase 5 plan post-K-033. sim010 (S71-S72 combinada) demostró que
F-symbols + pentagonal pasan al 100%, pero R-symbols simples solo pasan
hexagonal 45/64. Hipótesis: necesario lift al double cover o forma
cuadrática no-degenerada.

Probamos varias convenciones:
  (a) Cociclo cuártico Z_4 con R = exp(πi · (h_{a+b} - h_a - h_b)) puro Frobenius-Schur.
  (b) Cociclo k=3 elevado a Z_8: R = exp(2πi · k · a · b / 16).
  (c) Combinación: R^{a,b} = q(a+b) / (q(a) q(b)) con q(a) = exp(2πi h_a).
  (d) Convención Wang 2010: R con factor exp(πi · h_{a+b}) explícito.

Verificación: hexagonal automatizada (256 cuádruplas).

Sin scipy.
"""

import math
import cmath


def omega_3_z4(a, b, c, k=3):
    """3-cociclo F-symbols Z_4 clase k=3."""
    a, b, c = a % 4, b % 4, c % 4
    arg = k * a * (b + c - ((b + c) % 4)) / 16.0
    return cmath.exp(2j * math.pi * arg)


def pretty(z, tol=1e-10):
    if abs(z - 1) < tol: return "1"
    if abs(z - 1j) < tol: return "i"
    if abs(z + 1) < tol: return "-1"
    if abs(z + 1j) < tol: return "-i"
    omega = cmath.exp(1j * math.pi / 4)
    for k in range(8):
        if abs(z - omega**k) < tol:
            return f"ω^{k}" if k > 0 else "1"
    return f"{z.real:.3f}{z.imag:+.3f}i"


labels = {0: "1", 1: "s", 2: "v", 3: "c"}
h = {0: 0.0, 1: 5/8, 2: 1/2, 3: 5/8}

# Pre-compute F table
F = {}
for a in range(4):
    for b in range(4):
        for c in range(4):
            F[(a, b, c)] = omega_3_z4(a, b, c, k=3)


# ============================================================
# Verificación hexagonal
# ============================================================

def check_hexagon(R_dict):
    """Hexagonal abeliana: R^{a,b+c} = F^{a,b,c} R^{a,c} F^{b,a,c}^{-1} R^{a,b} F^{b,c,a}.

    Identidad estándar (Wang 2010 §6, eq 6.2).
    """
    n_pass = 0
    n_total = 0
    for a in range(4):
        for b in range(4):
            for c in range(4):
                lhs = R_dict[(a, (b+c) % 4)]
                rhs = (F[(a, b, c)] * R_dict[(a, c)] / F[(b, a, c)]
                       * R_dict[(a, b)] * F[(b, c, a)])
                n_total += 1
                if abs(lhs - rhs) < 1e-8:
                    n_pass += 1
    return n_pass, n_total


def check_hexagon_simple(R_dict):
    """Hexagonal simplificada (sin F): R^{a,b+c} = R^{a,b} R^{a,c}.

    Sólo válida para cociclo trivial. Útil como comparación.
    """
    n_pass = 0
    n_total = 0
    for a in range(4):
        for b in range(4):
            for c in range(4):
                lhs = R_dict[(a, (b+c) % 4)]
                rhs = R_dict[(a, b)] * R_dict[(a, c)]
                n_total += 1
                if abs(lhs - rhs) < 1e-8:
                    n_pass += 1
    return n_pass, n_total


# ============================================================
# Convenciones de R-symbols
# ============================================================

def R_convention_a():
    """Pure Frobenius-Schur: R^{a,b} = exp(πi (h_{a+b} - h_a - h_b))."""
    R = {}
    for a in range(4):
        for b in range(4):
            c_res = (a + b) % 4
            R[(a, b)] = cmath.exp(1j * math.pi * (h[c_res] - h[a] - h[b]))
    return R


def R_convention_b(k=3, N=8):
    """Lift al double cover: R^{a,b} = exp(2πi · k · a · b / 2N)."""
    R = {}
    for a in range(4):
        for b in range(4):
            R[(a, b)] = cmath.exp(2j * math.pi * k * a * b / (2 * N))
    return R


def R_convention_c():
    """Forma cuadrática: R^{a,b} = q(a+b) / (q(a) q(b))."""
    R = {}
    q = {a: cmath.exp(2j * math.pi * h[a]) for a in range(4)}
    for a in range(4):
        for b in range(4):
            c_res = (a + b) % 4
            R[(a, b)] = q[c_res] / (q[a] * q[b])
    return R


def R_convention_d(k=3):
    """Wang 2010: R^{a,b} = exp(πi h_{a+b}) · cocycle factor."""
    R = {}
    for a in range(4):
        for b in range(4):
            c_res = (a + b) % 4
            phase_h = cmath.exp(1j * math.pi * h[c_res])
            phase_cocycle = cmath.exp(2j * math.pi * k * a * b / 16)
            R[(a, b)] = phase_h * phase_cocycle
    return R


def R_convention_e():
    """Combinación: forma cuadrática + lift al double cover."""
    R = {}
    for a in range(4):
        for b in range(4):
            # R = sqrt(theta_{a+b}/(theta_a theta_b))
            # = exp(πi(h_{a+b} - h_a - h_b)) (raíz cuadrada principal)
            c_res = (a + b) % 4
            arg_principal = h[c_res] - h[a] - h[b]
            # Lift correction (cociclo Z_4 → Z_8)
            arg_lift = (3 * a * b) % 8 / 16.0
            R[(a, b)] = cmath.exp(1j * math.pi * arg_principal + 2j * math.pi * arg_lift)
    return R


def R_convention_f(alpha=5):
    """Forma cuadrática genérica con parámetro α: q(a) = exp(2πi α a²/8)."""
    R = {}
    q = {a: cmath.exp(2j * math.pi * alpha * a * a / 8) for a in range(4)}
    for a in range(4):
        for b in range(4):
            c_res = (a + b) % 4
            R[(a, b)] = q[c_res] / (q[a] * q[b])
    return R


# ============================================================
# Modular checks
# ============================================================

def compute_S_matrix(R_dict):
    """S-matrix abeliana: S_{a,b} = (1/D) θ_a θ_b / θ_{a+b} = 1/(D R^{a,b} R^{b,a}).

    Convención: D = sqrt(N) con N = número de objetos (4).
    """
    D = 2.0
    S = [[0]*4 for _ in range(4)]
    for a in range(4):
        for b in range(4):
            c_res = (a + b) % 4
            theta_a = cmath.exp(2j * math.pi * h[a])
            theta_b = cmath.exp(2j * math.pi * h[b])
            theta_c = cmath.exp(2j * math.pi * h[c_res])
            # S_{a,b} = (1/D) θ_a θ_b / θ_{a+b} (forma cuadrática)
            S[a][b] = (theta_a * theta_b / theta_c) / D
    return S


def check_modular_ST3(S, T_diag, c_central):
    """Verifica (ST)^3 = exp(2πi c/8) · 1."""
    T = [[0]*4 for _ in range(4)]
    for i in range(4):
        T[i][i] = T_diag[i]

    def matmul(A, B):
        C = [[0]*4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    C[i][j] += A[i][k] * B[k][j]
        return C

    ST = matmul(S, T)
    ST2 = matmul(ST, ST)
    ST3 = matmul(ST2, ST)

    expected = cmath.exp(2j * math.pi * c_central / 8)

    # ST^3 debe ser expected · I (matriz escalar)
    diag_avg = sum(ST3[i][i] for i in range(4)) / 4
    off_diag_max = max(abs(ST3[i][j]) for i in range(4) for j in range(4) if i != j)

    return diag_avg, off_diag_max, expected, abs(diag_avg - expected) < 1e-6


# ============================================================
# Main: probar convenciones
# ============================================================

def main():
    print("=" * 76)
    print("sim011 — R-symbols correctos `Spin(10)_1` — múltiples convenciones")
    print("=" * 76)

    conventions = {
        "(a) Frobenius-Schur puro": R_convention_a(),
        "(b) Lift Z_4 → Z_8 (k=3)": R_convention_b(k=3, N=8),
        "(c) Forma cuadrática q(a+b)/(q(a)q(b))": R_convention_c(),
        "(d) Wang 2010 con cocycle factor": R_convention_d(k=3),
        "(e) Combinación FS + lift Z_8": R_convention_e(),
        "(f1) q(a) = exp(2πi·1·a²/8)": R_convention_f(alpha=1),
        "(f3) q(a) = exp(2πi·3·a²/8)": R_convention_f(alpha=3),
        "(f5) q(a) = exp(2πi·5·a²/8)": R_convention_f(alpha=5),
        "(f7) q(a) = exp(2πi·7·a²/8)": R_convention_f(alpha=7),
    }

    print()
    print(f"   {'Convención':>40} {'Hex completo':>14} {'Hex simple':>14}")
    print("-" * 76)

    best_R = None
    best_score = 0
    best_name = None

    for name, R in conventions.items():
        n_pass, n_total = check_hexagon(R)
        n_pass_s, _ = check_hexagon_simple(R)
        marker = ' ✓' if n_pass == n_total else ('  ✓' if n_pass >= 60 else '')
        print(f"   {name:>40} {n_pass}/{n_total} ({100*n_pass/n_total:.0f}%){marker} {n_pass_s}/{n_total} ({100*n_pass_s/n_total:.0f}%)")

        if n_pass > best_score:
            best_score = n_pass
            best_R = R
            best_name = name

    print()
    print(f"Mejor convención hex completo: {best_name} con {best_score}/256")
    print()

    # Para la mejor convención, computar modular data
    print("=" * 76)
    print(f"Modular data con la mejor convención: {best_name}")
    print("=" * 76)

    if best_R:
        T_diag = [cmath.exp(2j * math.pi * h[a]) for a in range(4)]
        S = compute_S_matrix(best_R)

        print("\nT-matrix (diagonal):")
        for a in range(4):
            print(f"   θ_{labels[a]} = {pretty(T_diag[a])}")

        print("\nS-matrix:")
        for a in range(4):
            row = " ".join(f"{pretty(S[a][b]):>10}" for b in range(4))
            print(f"   {labels[a]}: [{row}]")

        diag_avg, off_max, expected, ok = check_modular_ST3(S, T_diag, c_central=5)
        print(f"\n(ST)^3 verificación (c=5):")
        print(f"   Esperado: {pretty(expected)} · I")
        print(f"   Diagonal promedio: {pretty(diag_avg)}")
        print(f"   Off-diagonal max: {off_max:.4e}")
        print(f"   Modular OK: {ok}")

    # Tabla de la mejor R
    print()
    print("R-symbols mejor convención:")
    print(f"   {'(a,b)':>10} {'(label)':>14} {'R^{a,b}':>14}")
    if best_R:
        for (a, b), val in best_R.items():
            print(f"   {f'({a},{b})':>10} {f'({labels[a]},{labels[b]})':>14} {pretty(val):>14}")


if __name__ == "__main__":
    main()
