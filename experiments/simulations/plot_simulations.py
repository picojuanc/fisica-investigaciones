"""
plot_simulations.py
===================
Generador de gráficas SVG para sim002 (TOV radiación) y sim003 (TOV anisotrópica).
Sin dependencias externas (matplotlib no disponible). SVG manual.

Uso:
  python3 plot_simulations.py

Genera:
  sim002_atractor.svg            — y(x) numérico vs 1/(7x²) singular isothermal
  sim002_compactness.svg         — m̃/x vs x con línea 3/7
  sim003_compactness_comp.svg    — comparación isotrópico vs anisotrópico
  sim003_anisotropy_profile.svg  — h(x), w_r(x), w_t(x), y(x)
  sim003_mass_distribution.svg   — histograma masa por shell (K-035)
  sim003_h0_scan.svg             — max compactness vs h_0 para varios n
"""

import math
import os
import sys

# Hacer importables las funciones de sim003
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sim003_tov_anisotropic import integrate_power, profile_summary


# ============================================================
# Mini-librería SVG
# ============================================================

class SVGPlot:
    """Plot 2D a SVG, con soporte para escalas log/lineales."""

    def __init__(self, width=720, height=480, margin=70,
                 x_label="", y_label="", title="",
                 log_x=False, log_y=False,
                 x_range=None, y_range=None):
        self.W, self.H, self.M = width, height, margin
        self.x_label, self.y_label, self.title = x_label, y_label, title
        self.log_x, self.log_y = log_x, log_y
        self.x_range, self.y_range = x_range, y_range
        self.series = []        # lista de (xs, ys, color, label, linewidth, dash)
        self.hlines = []        # [(y, color, label, dash)]
        self.vlines = []        # [(x, color, label, dash)]
        self.annotations = []   # [(x, y, text, color)]

    def add_series(self, xs, ys, color="black", label="", linewidth=2.0, dash=None):
        self.series.append((list(xs), list(ys), color, label, linewidth, dash))

    def add_hline(self, y, color="gray", label="", dash="4,3"):
        self.hlines.append((y, color, label, dash))

    def add_vline(self, x, color="gray", label="", dash="4,3"):
        self.vlines.append((x, color, label, dash))

    def add_annotation(self, x, y, text, color="black"):
        self.annotations.append((x, y, text, color))

    # --- Helpers de escala ---

    def _autoscale(self):
        if self.x_range is None:
            xs_all = [x for s in self.series for x in s[0] if (not self.log_x) or x > 0]
            if not xs_all:
                xs_all = [0.0, 1.0]
            self.x_range = (min(xs_all), max(xs_all))
        if self.y_range is None:
            ys_all = [y for s in self.series for y in s[1] if (not self.log_y) or y > 0]
            ys_all += [y for y, *_ in self.hlines]
            if not ys_all:
                ys_all = [0.0, 1.0]
            self.y_range = (min(ys_all), max(ys_all))

    def _xpix(self, x):
        x0, x1 = self.x_range
        if self.log_x:
            x0, x1 = math.log10(max(x0, 1e-300)), math.log10(max(x1, 1e-300))
            x = math.log10(max(x, 1e-300))
        if x1 == x0:
            return self.M
        return self.M + (x - x0) / (x1 - x0) * (self.W - 2 * self.M)

    def _ypix(self, y):
        y0, y1 = self.y_range
        if self.log_y:
            y0, y1 = math.log10(max(y0, 1e-300)), math.log10(max(y1, 1e-300))
            y = math.log10(max(y, 1e-300))
        if y1 == y0:
            return self.H - self.M
        return self.H - self.M - (y - y0) / (y1 - y0) * (self.H - 2 * self.M)

    # --- Render ---

    def _render_axes(self):
        out = []
        # Marco
        out.append(
            f'<rect x="{self.M}" y="{self.M}" '
            f'width="{self.W - 2*self.M}" height="{self.H - 2*self.M}" '
            f'fill="white" stroke="black" stroke-width="1.2"/>'
        )

        # Título
        if self.title:
            out.append(
                f'<text x="{self.W/2}" y="{self.M/2 + 5}" text-anchor="middle" '
                f'font-family="Helvetica" font-size="16" font-weight="bold">{self.title}</text>'
            )
        # Eje X label
        if self.x_label:
            out.append(
                f'<text x="{self.W/2}" y="{self.H - self.M/3}" text-anchor="middle" '
                f'font-family="Helvetica" font-size="13">{self.x_label}</text>'
            )
        # Eje Y label
        if self.y_label:
            cx, cy = self.M/3, self.H/2
            out.append(
                f'<text x="{cx}" y="{cy}" text-anchor="middle" '
                f'font-family="Helvetica" font-size="13" '
                f'transform="rotate(-90 {cx} {cy})">{self.y_label}</text>'
            )

        # Ticks X
        x0, x1 = self.x_range
        if self.log_x:
            ticks = [10**k for k in range(int(math.floor(math.log10(max(x0, 1e-300)))),
                                          int(math.ceil(math.log10(max(x1, 1e-300)))) + 1)]
            ticks = [t for t in ticks if x0 <= t <= x1]
        else:
            ticks = self._linspace(x0, x1, 6)
        for tx in ticks:
            xp = self._xpix(tx)
            out.append(
                f'<line x1="{xp}" y1="{self.H - self.M}" x2="{xp}" y2="{self.H - self.M + 5}" '
                f'stroke="black" stroke-width="0.8"/>'
            )
            label = self._fmt(tx, log=self.log_x)
            out.append(
                f'<text x="{xp}" y="{self.H - self.M + 18}" text-anchor="middle" '
                f'font-family="Helvetica" font-size="10">{label}</text>'
            )

        # Ticks Y
        y0, y1 = self.y_range
        if self.log_y:
            ticks = [10**k for k in range(int(math.floor(math.log10(max(y0, 1e-300)))),
                                          int(math.ceil(math.log10(max(y1, 1e-300)))) + 1)]
            ticks = [t for t in ticks if y0 <= t <= y1]
        else:
            ticks = self._linspace(y0, y1, 6)
        for ty in ticks:
            yp = self._ypix(ty)
            out.append(
                f'<line x1="{self.M - 5}" y1="{yp}" x2="{self.M}" y2="{yp}" '
                f'stroke="black" stroke-width="0.8"/>'
            )
            label = self._fmt(ty, log=self.log_y)
            out.append(
                f'<text x="{self.M - 8}" y="{yp + 4}" text-anchor="end" '
                f'font-family="Helvetica" font-size="10">{label}</text>'
            )

        # Gridlines suaves
        for tx in ticks if not self.log_x else [10**k for k in range(int(math.floor(math.log10(max(x0,1e-300)))),
                                                                      int(math.ceil(math.log10(max(x1,1e-300))))+1)]:
            xp = self._xpix(tx)
            if self.M < xp < self.W - self.M:
                out.append(
                    f'<line x1="{xp}" y1="{self.M}" x2="{xp}" y2="{self.H - self.M}" '
                    f'stroke="#eee" stroke-width="0.5"/>'
                )
        for ty in self._linspace(y0, y1, 6) if not self.log_y else [10**k for k in range(int(math.floor(math.log10(max(y0,1e-300)))),
                                                                                          int(math.ceil(math.log10(max(y1,1e-300))))+1)]:
            yp = self._ypix(ty)
            if self.M < yp < self.H - self.M:
                out.append(
                    f'<line x1="{self.M}" y1="{yp}" x2="{self.W - self.M}" y2="{yp}" '
                    f'stroke="#eee" stroke-width="0.5"/>'
                )

        return "\n".join(out)

    def _render_series(self):
        out = []
        for xs, ys, color, label, lw, dash in self.series:
            pts = []
            for x, y in zip(xs, ys):
                if self.log_x and x <= 0:
                    continue
                if self.log_y and y <= 0:
                    continue
                pts.append((self._xpix(x), self._ypix(y)))
            if not pts:
                continue
            d = "M " + " L ".join(f"{x:.2f},{y:.2f}" for x, y in pts)
            dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
            out.append(
                f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{lw}"{dash_attr}/>'
            )
        return "\n".join(out)

    def _render_hlines(self):
        out = []
        for y, color, label, dash in self.hlines:
            yp = self._ypix(y)
            if self.M <= yp <= self.H - self.M:
                out.append(
                    f'<line x1="{self.M}" y1="{yp}" x2="{self.W - self.M}" y2="{yp}" '
                    f'stroke="{color}" stroke-width="1.5" stroke-dasharray="{dash}"/>'
                )
                if label:
                    out.append(
                        f'<text x="{self.W - self.M - 5}" y="{yp - 4}" text-anchor="end" '
                        f'font-family="Helvetica" font-size="11" fill="{color}">{label}</text>'
                    )
        return "\n".join(out)

    def _render_vlines(self):
        out = []
        for x, color, label, dash in self.vlines:
            xp = self._xpix(x)
            if self.M <= xp <= self.W - self.M:
                out.append(
                    f'<line x1="{xp}" y1="{self.M}" x2="{xp}" y2="{self.H - self.M}" '
                    f'stroke="{color}" stroke-width="1.2" stroke-dasharray="{dash}"/>'
                )
        return "\n".join(out)

    def _render_legend(self):
        out = []
        labeled = [(c, l) for _, _, c, l, *_ in self.series if l]
        if not labeled:
            return ""
        x0 = self.M + 15
        y0 = self.M + 15
        for i, (color, label) in enumerate(labeled):
            yi = y0 + i * 18
            out.append(
                f'<line x1="{x0}" y1="{yi}" x2="{x0 + 25}" y2="{yi}" '
                f'stroke="{color}" stroke-width="2.5"/>'
            )
            out.append(
                f'<text x="{x0 + 32}" y="{yi + 4}" font-family="Helvetica" font-size="11" '
                f'fill="black">{label}</text>'
            )
        return "\n".join(out)

    def _render_annotations(self):
        out = []
        for x, y, text, color in self.annotations:
            xp, yp = self._xpix(x), self._ypix(y)
            out.append(
                f'<text x="{xp}" y="{yp}" font-family="Helvetica" font-size="11" '
                f'fill="{color}">{text}</text>'
            )
        return "\n".join(out)

    @staticmethod
    def _linspace(a, b, n):
        if n < 2:
            return [a]
        return [a + (b - a) * i / (n - 1) for i in range(n)]

    @staticmethod
    def _fmt(v, log=False):
        if log and v > 0:
            e = math.log10(v)
            if abs(e - round(e)) < 1e-6:
                return f"10^{int(round(e))}"
            return f"{v:.2g}"
        if abs(v) < 1e-3 or abs(v) > 1e4:
            return f"{v:.1e}"
        return f"{v:g}"

    def render(self, filepath):
        self._autoscale()
        body = "\n".join([
            self._render_axes(),
            self._render_hlines(),
            self._render_vlines(),
            self._render_series(),
            self._render_annotations(),
            self._render_legend(),
        ])
        svg = (
            f'<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.W}" '
            f'height="{self.H}" viewBox="0 0 {self.W} {self.H}">\n'
            f'<rect width="100%" height="100%" fill="#fcfcfc"/>\n'
            f'{body}\n'
            f'</svg>\n'
        )
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(svg)


# ============================================================
# Loaders
# ============================================================

def load_dat(path):
    """Carga un .dat. Devuelve dict de columnas (nombres del header)."""
    cols_names = None
    rows = []
    with open(path, "r") as f:
        for line in f:
            s = line.strip()
            if not s:
                continue
            if s.startswith("#"):
                if cols_names is None and "Columns" in s:
                    parts = s.replace("# Columns:", "").strip().split()
                    cols_names = parts
                continue
            vals = [float(v) for v in s.split()]
            rows.append(vals)

    if not rows:
        return {}
    n_cols = len(rows[0])
    if cols_names is None or len(cols_names) != n_cols:
        cols_names = [f"c{i}" for i in range(n_cols)]
    return {cols_names[i]: [r[i] for r in rows] for i in range(n_cols)}


# ============================================================
# Plot 1: sim002 atractor singular isothermal
# ============================================================

def plot_sim002_atractor(d2):
    p = SVGPlot(
        width=760, height=500, margin=72,
        x_label="x = r / r_s (radial adimensional)",
        y_label="y = ρ / ρ_*  (densidad adimensional)",
        title="sim002: TOV radiación — el atractor singular isothermal",
        log_x=True, log_y=True,
        x_range=(1e-3, 1.0), y_range=(1e-1, 1e6),
    )
    xs = d2["x"]
    ys = d2["y(=rho/rho_*)"]
    p.add_series(xs, ys, color="#0e63a8", label="numérico  (y_c ≈ 10⁴)", linewidth=2.2)

    # 1/(7x²) singular isothermal
    sx = [10**(-3 + 0.02 * i) for i in range(151)]
    sy = [1.0 / (7.0 * x * x) for x in sx]
    p.add_series(sx, sy, color="#c2272d",
                 label="solución analítica  y = 1/(7x²)", linewidth=2.0, dash="6,4")

    p.render("sim002_atractor.svg")
    print("  → sim002_atractor.svg")


# ============================================================
# Plot 2: sim002 compactness universal
# ============================================================

def plot_sim002_compactness(d2):
    p = SVGPlot(
        width=760, height=500, margin=72,
        x_label="x = r / r_s",
        y_label="compactness  m̃(x) / x  (≡ 2Gm/(c²r))",
        title="sim002: compactness satura en 3/7 — horizonte inalcanzable",
        x_range=(0.0, 1.0), y_range=(0.0, 1.0),
    )
    xs = d2["x"]
    cs = d2["compactness(=m/x)"]
    p.add_series(xs, cs, color="#0e63a8",
                 label="numérico (radiación pura)", linewidth=2.2)

    p.add_hline(3.0/7.0, color="#c2272d", label="3/7 ≈ 0.4286 (singular isothermal)")
    p.add_hline(1.0, color="#444", label="horizonte (m̃/x = 1)", dash="2,3")
    p.render("sim002_compactness.svg")
    print("  → sim002_compactness.svg")


# ============================================================
# Plot 3: sim003 compactness comparison
# ============================================================

def plot_sim003_compactness_comparison():
    """Re-corre sim003 para varios h_0 con n=4 y compara compactness(x)."""
    p = SVGPlot(
        width=760, height=500, margin=72,
        x_label="x = r / r_s",
        y_label="compactness  m̃(x) / x",
        title="sim003: anisotropy holográfica eleva compactness (n=4)",
        x_range=(0.0, 1.0), y_range=(0.0, 1.0),
    )

    cases = [
        (0.0,  "#444444", "h₀ = 0 (isotrópico → 3/7)"),
        (0.3,  "#1f77b4", "h₀ = 0.3"),
        (0.5,  "#2ca02c", "h₀ = 0.5"),
        (0.7,  "#ff7f0e", "h₀ = 0.7"),
        (0.95, "#9467bd", "h₀ = 0.95"),
        (0.99, "#c2272d", "h₀ = 0.99 (cota ~0.83)"),
    ]
    for h0, color, label in cases:
        hist, status, info = integrate_power(100.0, h0, 4)
        xs = [e[0] for e in hist]
        cs = [e[1] / e[0] if e[0] > 0 else 0.0 for e in hist]
        p.add_series(xs, cs, color=color, label=label, linewidth=2.0)

    p.add_hline(3.0/7.0, color="#888", label="3/7 (bound isotrópico)", dash="3,3")
    p.add_hline(1.0, color="#444", label="horizonte", dash="2,3")
    p.render("sim003_compactness_comp.svg")
    print("  → sim003_compactness_comp.svg")


# ============================================================
# Plot 4: sim003 perfil anisotrópico óptimo
# ============================================================

def plot_sim003_anisotropy_profile(d3):
    p = SVGPlot(
        width=760, height=500, margin=72,
        x_label="x = r / r_s",
        y_label="cantidades adimensionales (log)",
        title="sim003: perfil del caso óptimo (h₀=0.95, n=4, y_c=100)",
        log_y=True,
        x_range=(0.01, 1.0), y_range=(1e-3, 1e3),
    )
    xs = d3["x"]
    p.add_series(xs, d3["y"],   color="#0e63a8", label="y(x)  (densidad)", linewidth=2.0)
    p.add_series(xs, d3["w_r"], color="#c2272d", label="w_r(x)  (presión radial)", linewidth=1.8)
    p.add_series(xs, d3["w_t"], color="#2ca02c", label="w_t(x)  (presión tangencial)", linewidth=1.8)

    # h(x) en eje secundario "abusado": como h ∈ [0,1], lo escalamos por 100 para verlo en log
    hs_scaled = [max(h, 1e-3) for h in d3["h"]]  # evitar log(0)
    p.add_series(xs, hs_scaled, color="#9467bd",
                 label="h(x)  (anisotropy ∈ [0,1], log)", linewidth=1.6, dash="5,3")

    p.render("sim003_anisotropy_profile.svg")
    print("  → sim003_anisotropy_profile.svg")


# ============================================================
# Plot 5: sim003 distribución de masa por shell (K-035)
# ============================================================

def plot_sim003_mass_distribution(d3):
    """Histograma de masa por cáscara."""
    shells = [(0.00, 0.10), (0.10, 0.30), (0.30, 0.50), (0.50, 0.70),
              (0.70, 0.85), (0.85, 0.95), (0.95, 0.99), (0.99, 1.00)]
    xs = d3["x"]
    ms = d3["m_tilde"]
    m_total = max(ms)

    fracs = []
    for x_lo, x_hi in shells:
        m_lo = next((m for x, m in zip(xs, ms) if x >= x_lo), 0.0)
        m_hi = next((m for x, m in zip(xs, ms) if x >= x_hi), m_total)
        delta = m_hi - m_lo
        fracs.append(delta / m_total if m_total > 0 else 0.0)

    # Render manual de barras
    W, H, M = 760, 500, 80
    bars = []
    n = len(shells)
    bar_w = (W - 2*M) / n * 0.8
    gap = (W - 2*M) / n * 0.2

    out = []
    out.append(f'<?xml version="1.0" encoding="UTF-8"?>')
    out.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
    out.append(f'<rect width="100%" height="100%" fill="#fcfcfc"/>')
    out.append(f'<rect x="{M}" y="{M}" width="{W-2*M}" height="{H-2*M}" fill="white" stroke="black"/>')
    out.append(f'<text x="{W/2}" y="{M/2+5}" text-anchor="middle" font-family="Helvetica" '
               f'font-size="16" font-weight="bold">'
               f'sim003: distribución de masa por cáscara — K-035 (concentración holográfica)</text>')
    out.append(f'<text x="{W/2}" y="{H - 18}" text-anchor="middle" font-family="Helvetica" '
               f'font-size="13">cáscara radial  [x_lo, x_hi]  con  x = r/r_s</text>')
    cx, cy = M/3, H/2
    out.append(f'<text x="{cx}" y="{cy}" text-anchor="middle" font-family="Helvetica" '
               f'font-size="13" transform="rotate(-90 {cx} {cy})">fracción de masa total cargada</text>')

    # Eje Y ticks (0%, 5%, 10%, 15%, 20%, 25%)
    for f in [0.0, 0.05, 0.10, 0.15, 0.20, 0.25]:
        yp = (H - M) - f / 0.25 * (H - 2*M)
        out.append(f'<line x1="{M-5}" y1="{yp}" x2="{M}" y2="{yp}" stroke="black"/>')
        out.append(f'<text x="{M-8}" y="{yp+4}" text-anchor="end" font-family="Helvetica" '
                   f'font-size="10">{int(f*100)}%</text>')
        out.append(f'<line x1="{M}" y1="{yp}" x2="{W-M}" y2="{yp}" stroke="#eee" stroke-width="0.5"/>')

    for i, ((x_lo, x_hi), frac) in enumerate(zip(shells, fracs)):
        # Color highlighting K-035 cáscara [0.85, 0.99]
        is_holo = (x_lo >= 0.85 and x_hi <= 0.99)
        color = "#c2272d" if is_holo else "#0e63a8"
        x_bar = M + i * ((W - 2*M) / n) + gap/2
        h_bar = (frac / 0.25) * (H - 2*M)
        y_bar = (H - M) - h_bar
        out.append(f'<rect x="{x_bar}" y="{y_bar}" width="{bar_w}" height="{h_bar}" '
                   f'fill="{color}" stroke="black" stroke-width="0.8"/>')
        # Label de la cáscara
        x_center = x_bar + bar_w / 2
        out.append(f'<text x="{x_center}" y="{H-M+18}" text-anchor="middle" '
                   f'font-family="Helvetica" font-size="9">[{x_lo:.2f},{x_hi:.2f}]</text>')
        # Valor en porcentaje sobre la barra
        out.append(f'<text x="{x_center}" y="{y_bar-5}" text-anchor="middle" '
                   f'font-family="Helvetica" font-size="10" font-weight="bold">{frac*100:.1f}%</text>')

    # Anotación K-035
    holo_total = sum(f for (lo, hi), f in zip(shells, fracs) if lo >= 0.85 and hi <= 0.99)
    out.append(f'<text x="{M+12}" y="{M+18}" font-family="Helvetica" font-size="11" '
               f'fill="#c2272d" font-weight="bold">'
               f'K-035: cáscara [0.85, 0.99] concentra {holo_total*100:.1f}% de la masa</text>')
    out.append(f'<text x="{M+12}" y="{M+34}" font-family="Helvetica" font-size="10" '
               f'fill="#666">'
               f'(verificación cuantitativa de holografía Bekenstein-Hawking)</text>')
    out.append('</svg>')

    with open("sim003_mass_distribution.svg", "w") as f:
        f.write("\n".join(out))
    print("  → sim003_mass_distribution.svg")


# ============================================================
# Plot 6: sim003 escaneo h_0 vs max compactness
# ============================================================

def plot_sim003_h0_scan():
    """Re-corre sim003 sobre (h_0, n) y plotea max compactness vs h_0."""
    p = SVGPlot(
        width=760, height=500, margin=72,
        x_label="h₀  (anisotropy en el horizonte)",
        y_label="max compactness alcanzada",
        title="sim003: escaneo h₀ vs max compactness — cota estructural ~0.83",
        x_range=(0.0, 1.0), y_range=(0.4, 1.0),
    )

    h0_grid = [0.0, 0.1, 0.2, 0.3, 0.5, 0.7, 0.85, 0.95, 0.99, 0.999]
    colors = {2: "#0e63a8", 4: "#2ca02c", 6: "#ff7f0e", 8: "#9467bd"}

    for n in (2, 4, 6, 8):
        ys = []
        for h0 in h0_grid:
            hist, status, info = integrate_power(100.0, h0, n, h_max=0.999)
            s = profile_summary(hist)
            ys.append(s["max_compactness"])
        p.add_series(h0_grid, ys, color=colors[n], label=f"n = {n}", linewidth=2.0)

    p.add_hline(3.0/7.0, color="#888", label="3/7 (isotrópico)", dash="3,3")
    p.add_hline(0.83, color="#c2272d", label="cota estructural ~0.83", dash="5,3")
    p.add_hline(1.0, color="#444", label="horizonte", dash="2,3")
    p.render("sim003_h0_scan.svg")
    print("  → sim003_h0_scan.svg")


# ============================================================
# Main
# ============================================================

def main():
    print("=" * 60)
    print("Generando gráficas SVG para sim002 y sim003")
    print("=" * 60)

    d2 = load_dat("sim002_profile.dat")
    d3 = load_dat("sim003_profile.dat")

    print("\n[sim002 plots]")
    plot_sim002_atractor(d2)
    plot_sim002_compactness(d2)

    print("\n[sim003 plots]")
    plot_sim003_compactness_comparison()
    plot_sim003_anisotropy_profile(d3)
    plot_sim003_mass_distribution(d3)
    plot_sim003_h0_scan()

    print("\n" + "=" * 60)
    print("Gráficas generadas en experiments/simulations/")


if __name__ == "__main__":
    main()
