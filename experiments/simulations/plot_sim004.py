"""
plot_sim004.py
==============
Genera gráficas SVG de los resultados de sim004_yukawa_overlap.py.
Reutiliza la mini-librería SVGPlot definida en plot_simulations.py.
"""

import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from plot_simulations import SVGPlot


# ============================================================
# Lectura de sim004_profile.dat (formato custom secciones)
# ============================================================

def parse_sim004_dat(path):
    """Parser custom para sim004_profile.dat con 4 secciones."""
    sections = {}
    current = None
    rows = []

    def commit():
        nonlocal rows
        if current and rows:
            sections[current] = rows
        rows = []

    with open(path, "r") as f:
        for line in f:
            s = line.strip()
            if not s:
                commit()
                continue
            if s.startswith("# SECTION"):
                commit()
                # SECTION 1: ξ_loc(d_LR/ℓ_s) ...
                # extraemos número
                num = s.split(":")[0].replace("# SECTION", "").strip()
                current = f"S{num}"
                continue
            if s.startswith("#"):
                continue
            try:
                vals = [float(x) for x in s.split()]
                rows.append(vals)
            except ValueError:
                continue
    commit()
    return sections


# ============================================================
# Plot A: ξ_loc(d_LR/ℓ_s) gaussiano vs exponencial — log y
# ============================================================

def plot_overlap_curves(sections, out_path):
    p = SVGPlot(
        width=760, height=500, margin=72,
        x_label="d_LR / ℓ_s   (separación entre defectos s y c)",
        y_label="ξ_loc   (overlap geométrico, log)",
        title="sim004: ξ_loc vs separación — origen geométrico de jerarquía Yukawa",
        log_y=True,
        x_range=(0.0, 10.5), y_range=(1e-7, 1.5),
    )

    s1 = sections.get("S1", [])  # gaussiano
    s2 = sections.get("S2", [])  # exponencial

    if s1:
        xs = [r[0] for r in s1]
        ys_num = [r[1] for r in s1]
        ys_an = [r[2] for r in s1]
        # Curva analítica gaussiana densa
        xa = [0.01 * i for i in range(1051)]
        ya = [math.exp(-x * x / 4.0) for x in xa]
        p.add_series(xa, ya, color="#0e63a8",
                     label="gaussiano  (analítico: e^(-d²/4))", linewidth=2.0)
        p.add_series(xs, ys_num, color="#0e63a8", label="", linewidth=0,
                     dash=None)
        # Marcadores numéricos como pequeños círculos: simular con segmentos cortos
        # SVGPlot no tiene marker; uso anotaciones text "•"
        for x, y in zip(xs, ys_num):
            if y > 1e-7:
                p.add_annotation(x, y, "•", color="#0e63a8")

    if s2:
        xs_e = [r[0] for r in s2]
        ys_e = [r[1] for r in s2]
        p.add_series(xs_e, ys_e, color="#c2272d",
                     label="exponencial  (numérico)", linewidth=2.2,
                     dash="6,4")
        for x, y in zip(xs_e, ys_e):
            if y > 1e-7:
                p.add_annotation(x, y, "■", color="#c2272d")

    # Líneas horizontales de referencia (Yukawas)
    p.add_hline(1e-2, color="#888", label="ξ = 10⁻² (~y_b/y_t)", dash="3,4")
    p.add_hline(1e-4, color="#888", label="ξ = 10⁻⁴ (~y_τ/y_t)", dash="3,4")
    p.add_hline(1e-6, color="#888", label="ξ = 10⁻⁶ (~y_e/y_t)", dash="3,4")

    p.render(out_path)
    print(f"  → {out_path}")


# ============================================================
# Plot B: sensibilidad a fluctuación del condensado
# ============================================================

def plot_sensitivity_fluctuation(sections, out_path):
    p = SVGPlot(
        width=720, height=480, margin=72,
        x_label="σ   (amplitud rms de fluctuación del condensado)",
        y_label="ξ_loc^(top)",
        title="sim004: sensibilidad a fluctuaciones del condensado (caso top)",
        x_range=(0.0, 1.05), y_range=(0.5, 1.1),
    )

    s3 = sections.get("S3", [])
    if s3:
        sigmas = [r[0] for r in s3]
        means = [r[1] for r in s3]
        devs = [r[2] for r in s3]
        # Curva media
        p.add_series(sigmas, means, color="#0e63a8",
                     label="ξ_loc media (5 fases)", linewidth=2.2)
        # Bandas ±desv
        upper = [m + d for m, d in zip(means, devs)]
        lower = [m - d for m, d in zip(means, devs)]
        p.add_series(sigmas, upper, color="#0e63a8",
                     label="ξ_loc ± desv", linewidth=1.0, dash="3,3")
        p.add_series(sigmas, lower, color="#0e63a8", label="",
                     linewidth=1.0, dash="3,3")
        # Markers
        for s, m in zip(sigmas, means):
            p.add_annotation(s, m, "•", color="#0e63a8")

    p.add_hline(1.0, color="#444", label="ξ = 1 (idealizado)", dash="4,3")

    p.render(out_path)
    print(f"  → {out_path}")


# ============================================================
# Plot C: jerarquía Yukawa anticipada — d_LR requerida vs y/y_t
# ============================================================

def plot_hierarchy_required(out_path):
    """Para cada Yukawa observado y/y_t, calcular d_LR/ℓ_s requerida (analítico)."""
    fermions = [
        # (etiqueta, y/y_t observado SM)
        ("y_t", 1.0),
        ("y_b/y_t", 2.4e-2),
        ("y_τ/y_t", 1.0e-2),
        ("y_c/y_t", 7.4e-3),
        ("y_s/y_t", 5.4e-4),
        ("y_μ/y_t", 6.1e-4),
        ("y_u/y_t", 1.3e-5),
        ("y_d/y_t", 2.7e-5),
        ("y_e/y_t", 2.9e-6),
    ]
    # Gaussiano: d = 2 √(-ln(ratio))
    # Exponencial 3D: aproximación numérica  d ≈ a + b·log10(ratio) (lineal en log10)
    # De los datos sim004:  d=10 → ξ=2e-3 ⟹ log10=-2.7  ⟹ slope ≈ -3.7 ℓ_s/decade
    # Mejor: usar fit lineal sobre puntos sim004 exponencial:
    # (0, 0.996), (1, 0.857), (3, 0.348), (5, 0.0965), (10, 2e-3)
    # log10: (0,0), (1,-0.067), (3,-0.458), (5,-1.016), (10,-2.696)
    # slope ~ -0.27 per ℓ_s ⟹ ratio decade ~ 3.7 ℓ_s/decade
    # Fit completo (manual):  log10(ξ_exp) ≈ -0.26 · d - 0.04 (d en ℓ_s, d > 1)
    p = SVGPlot(
        width=820, height=520, margin=80,
        x_label="d_LR / ℓ_s   (separación geométrica L-R requerida)",
        y_label="y / y_t   (Yukawa relativo, SM observado)",
        title="sim004: separación d_LR requerida para reproducir jerarquía Yukawa",
        log_y=True,
        x_range=(0.0, 22.0), y_range=(1e-6, 2.0),
    )

    # Curva continua gaussiana
    xs_g = [0.05 * i for i in range(0, 161)]
    ys_g = [math.exp(-x * x / 4.0) for x in xs_g]
    p.add_series(xs_g, ys_g, color="#0e63a8",
                 label="gaussiano: y/y_t = e^(-d²/4)", linewidth=2.2)

    # Curva exponencial 3D (fit aproximado)
    xs_e = [0.1 * i for i in range(0, 221)]
    # Mejor fit a sim004:  log10(ξ) = -0.26 d (lineal log)
    ys_e = [10 ** (-0.26 * x) for x in xs_e]
    p.add_series(xs_e, ys_e, color="#c2272d",
                 label="exponencial: y/y_t ≈ 10^(-0.26 d)",
                 linewidth=2.0, dash="6,4")

    # Marcadores de fermiones
    for (name, ratio) in fermions:
        # d_g (analítico)
        if ratio < 1.0:
            d_g = 2.0 * math.sqrt(-math.log(ratio))
            d_e = -math.log10(ratio) / 0.26
            p.add_annotation(d_g, ratio, f"  {name}", color="#0e63a8")
            if d_e <= 22:
                p.add_annotation(d_e, ratio, f"  {name}", color="#c2272d")

    p.render(out_path)
    print(f"  → {out_path}")


# ============================================================
# Plot D: y_t banda — banda final de S53
# ============================================================

def plot_yt_band(sections, out_path):
    """Visualización de la banda y_t = 1.0 ± δ por sensibilidad de modelo."""
    p = SVGPlot(
        width=720, height=460, margin=72,
        x_label="parámetro de modelo (forma de perfil, σ del condensado)",
        y_label="y_t^(SCG)",
        title="sim004: banda y_t^(SCG) por sensibilidad de modelo  vs y_t^(SM)",
        x_range=(0.0, 6.0), y_range=(0.85, 1.10),
    )

    # Cada parámetro: (etiqueta, (y_min, y_max), x posición)
    params = [
        # (label, mid, lo, hi, x)
        ("gaussiano (analítico)", 1.000, 1.000, 1.000, 1.0),
        ("exponencial (numérico)", 0.999, 0.998, 1.000, 2.0),
        ("σ_condensado=0.05", 0.994, 0.983, 1.005, 3.0),
        ("σ_condensado=0.10", 0.988, 0.966, 1.010, 4.0),
        ("σ_condensado=0.20", 0.976, 0.932, 1.020, 5.0),
    ]

    # Render como segmentos verticales
    xs_mid = [pp[4] for pp in params]
    ys_mid = [pp[1] for pp in params]
    p.add_series(xs_mid, ys_mid, color="#0e63a8",
                 label="y_t^(SCG) media", linewidth=0)
    for label, mid, lo, hi, x in params:
        p.add_annotation(x, mid, "●", color="#0e63a8")
        # Barra de error como dos puntos extremos
        p.add_annotation(x, hi, "—", color="#0e63a8")
        p.add_annotation(x, lo, "—", color="#0e63a8")
        p.add_annotation(x - 0.4, 0.86, label, color="#444")

    p.add_hline(1.0, color="#888", label="y_t = 1 (predicción central SCG)",
                dash="4,3")
    p.add_hline(0.99, color="#c2272d", label="y_t^(SM) = 0.99",
                dash="3,4")

    p.render(out_path)
    print(f"  → {out_path}")


# ============================================================
# MAIN
# ============================================================

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    dat_path = os.path.join(here, "sim004_profile.dat")
    if not os.path.exists(dat_path):
        print(f"ERROR: no encuentro {dat_path}. Ejecutar sim004 primero.")
        return

    sections = parse_sim004_dat(dat_path)
    print(f"Secciones encontradas: {list(sections.keys())}")

    print("\nGenerando gráficas SVG...")
    os.chdir(here)
    plot_overlap_curves(sections, "sim004_overlap_curves.svg")
    plot_sensitivity_fluctuation(sections, "sim004_sensitivity.svg")
    plot_hierarchy_required("sim004_hierarchy.svg")
    plot_yt_band(sections, "sim004_yt_band.svg")
    print("\nDone.")


if __name__ == "__main__":
    main()
