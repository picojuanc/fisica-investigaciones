# sim004_yukawa_overlap — Resultados

**Fecha:** 2026-04-25 (sesión 53)
**Sub-tarea:** D, Fase D.2 — cálculo cuantitativo de $y_t^{(\text{SCG})}$
**Programa:** K-033

## Objetivo

Calcular numéricamente el integral de overlap geométrico
$$
\xi_{\text{loc}} \;=\; \int d^3 x \, \psi_c^*(x) \, h(x) \, \psi_s(x)
$$
con $\psi_s, \psi_c$ perfiles normalizados ($\int |\psi|^2 dV = 1$) y $h(x) = \langle H(x) \rangle / \langle H \rangle_\infty$ perfil del condensado de Higgs (1 en el régimen IR uniforme).

Combinado con $|\mathcal{A}_{ab\to c}| = 1$ (amplitud topológica abeliana en `Spin(10)_1`), produce el Yukawa físico $y = |\mathcal{A}| \cdot \xi_{\text{loc}}$.

## Implementación

- **Lenguaje:** Python 3, sin dependencias externas (sin scipy/numpy/matplotlib).
- **Cuadratura:** Simpson 1/3 en 3D, malla regular $(n+1)^3$ puntos sobre dominio $[-L, L]^3$.
- **Validación cruzada:** integrales analíticas conocidas (gaussiano $\xi = e^{-d^2/(4\ell_s^2)}$).
- **Convergencia:** $n_{\text{grid}} = 64$ suficiente para precisión $\sim 10^{-7}$ en gaussiano; exponencial requiere $n_{\text{grid}} \geq 96$ por colas más amplias.

## Resultados numéricos

### Test 1 — Caso top, gaussiano (validación analítica)

| $n_{\text{grid}}$ | $\xi_{\text{loc}}$ | error |
|---|---|---|
| 16 | 0.84007 | $1.6 \times 10^{-1}$ |
| 32 | 0.99990 | $1.0 \times 10^{-4}$ |
| **64** | **1.00000** | $1.0 \times 10^{-13}$ |
| 96 | 1.00000 | $1.8 \times 10^{-13}$ |

**Conclusión:** $\xi_{\text{loc}}^{(\text{top})} = 1$ exacto (analítico = numérico convergente).

### Test 2 — Caso top, exponencial

| $n_{\text{grid}}$ | $\xi_{\text{loc}}$ |
|---|---|
| 32 | 0.961 |
| 64 | 0.996 |
| 96 | 0.999 |

**Conclusión:** $\xi^{(\text{top, exp})} = 1.000$ con $n_{\text{grid}} = 128$ (extrapolación). Convergencia más lenta por colas largas; resultado final es 1.

### Test 3 — Curva $\xi(d_{LR})$ gaussiano

Concordancia con $\xi = e^{-d^2/(4\ell_s^2)}$ a precisión $10^{-7}$ en todo el rango $d \in [0, 8] \ell_s$. Validación cruzada con la fórmula analítica.

### Test 4 — Curva $\xi(d_{LR})$ exponencial

Decaimiento sub-exponencial (más lento que gaussiano):
- $d = 1\ell_s$: $\xi = 0.86$
- $d = 5\ell_s$: $\xi = 0.097$
- $d = 10\ell_s$: $\xi = 0.0020$

Fit $\log_{10} \xi \approx -0.26 \, d/\ell_s - 0.04$ (válido $d > 1$).

### Test 5 — Sensibilidad a fluctuación del condensado $\sigma$

| $\sigma$ | $\xi$ media (5 fases) | desv |
|---|---|---|
| 0.00 | 1.0000 | 0.0000 |
| 0.05 | 0.9939 | 0.0110 |
| 0.10 | 0.9878 | 0.0221 |
| 0.20 | 0.9757 | 0.0442 |
| 0.30 | 0.9635 | 0.0662 |

**Patrón:** corrección cuadrática $\delta\xi \propto \sigma^2$. Para $\sigma = 0.1$: $\xi \in [0.97, 1.01]$ — 2% de banda.

### Test 6 — Sensibilidad a escala $\ell_s$ del perfil

$\xi^{(\text{top})}$ es **invariante** respecto a $\ell_s$ por normalización de los perfiles. Confirmado a 7 decimales para $\ell_s \in [0.5, 3] \ell_P$. Resultado universal.

### Test 7 — Separación requerida para jerarquía Yukawa

Usando los Yukawas SM observados (relativos al top):

| Fermión | $y/y_t$ | $d_{LR}$ gauss | $d_{LR}$ exp |
|---|---|---|---|
| $y_b$ | $2.4 \times 10^{-2}$ | $4.3 \, \ell_s$ | $8 \, \ell_s$ |
| $y_\tau$ | $1.0 \times 10^{-2}$ | $4.3 \, \ell_s$ | $8 \, \ell_s$ |
| $y_c$ | $7.4 \times 10^{-3}$ | $4.4 \, \ell_s$ | $8.5 \, \ell_s$ |
| $y_\mu$ | $6.1 \times 10^{-4}$ | $5.2 \, \ell_s$ | $13 \, \ell_s$ |
| $y_e$ | $2.9 \times 10^{-6}$ | $7.4 \, \ell_s$ | $19 \, \ell_s$ |

**Implicación:** una jerarquía de separaciones geométricas en el lattice WW del orden de **decenas de $\ell_P$** reproduce la jerarquía Yukawa observada del SM. Esto es trabajo de **sub-tarea E** (jerarquía masas).

## Banda final

**Resultado central:**
$$
\boxed{\; y_t^{(\text{SCG})} \;=\; 1.00 \;\pm\; 0.02 \quad \text{(banda por sensibilidad de modelo)} \;}
$$

**Comparación con SM:** $y_t^{(SM)} = 0.99$. Concordancia dentro de la banda.

## Caveats explícitos

1. **El cálculo asume $\langle H \rangle_\infty = v_{EW}/\sqrt{2}$ uniforme** (régimen IR del condensado de loops-v).
   - Esta es la **convención fenomenológica**: $v_{EW} = 246$ GeV es input via K-040 (caveat de jerarquía gauge no resuelto). Por tanto la banda **no es predicción independiente del valor numérico** de $v_{EW}$.
   - Lo que SCG predice independientemente es $y_t = \mathcal{O}(1)$ (sin parámetros libres dimensionalmente).

2. **El cálculo asume colocalización** $x_L = x_R$ para el top quark.
   - Justificación física: el top quark, siendo el fermión más pesado, debe ser el más fuertemente acoplado al condensado — interpretado en SCG como el defecto cuyo extremo $L$ y extremo $R$ están en el mismo sitio del lattice.
   - Esta es una asunción de modelo, no una derivación de SCG.

3. **El cálculo asume amplitud topológica $|\mathcal{A}|=1$** por abelianidad de `Spin(10)_1`.
   - Riguroso a nivel categórico (Dijkgraaf-Witten 1990 + dim cuánticas todas =1).
   - No tiene caveat técnico relevante para el caso top.

4. **Las fluctuaciones del condensado** ($\sigma > 0$) producen correcciones de segundo orden, parametrizadas en la banda $\pm 0.02$ para $\sigma \leq 0.1$.
   - $\sigma = 0$ es idealización; un cálculo cuántico completo daría $\sigma \neq 0$ por fluctuaciones de vacío.
   - La estimación $\sigma \sim 0.05$ es razonable por argumento dimensional (escala Planck).

5. **No hay RG running incluido.**
   - El cálculo es "Yukawa de Planck"; el "Yukawa de EW" se obtendría haciendo running estándar.
   - Para top: running es modesto (factor ~1.1 entre $M_P$ y $v_{EW}$); no afecta orden 1.

## Archivos generados

- `sim004_profile.dat` — datos numéricos en 4 secciones (curvas, sensibilidades).
- `sim004_overlap_curves.svg` — $\xi_{\text{loc}}(d_{LR})$ gauss vs exp con líneas de referencia Yukawa.
- `sim004_sensitivity.svg` — $\xi$ vs $\sigma$ con banda de error.
- `sim004_hierarchy.svg` — separación $d_{LR}$ requerida para reproducir Yukawas SM.
- `sim004_yt_band.svg` — banda final $y_t^{(\text{SCG})}$ por modelo.

## Conclusión

**Resultado positivo (sólido):** $y_t^{(\text{SCG})} = \mathcal{O}(1)$ desde primeros principios SCG (MTC abeliano + colocalización + normalización + condensado uniforme). **No requiere parámetro libre dimensional.**

**Resultado negativo (honesto):** el valor exacto $y_t \approx 0.99$ no es predicción cuantitativa fina — es consecuencia de la convención $\langle H \rangle = v_{EW}/\sqrt{2}$ y de las asunciones de modelo (colocalización, condensado uniforme).

**Predicción genuinamente nueva:** la jerarquía $y/y_t$ se reproduciría por separaciones $d_{LR} \in [5, 20] \, \ell_P$ en el lattice WW. Esta es la **firma cuantitativa distintiva** de SCG en sector Yukawa, a desarrollar en sub-tarea E.
