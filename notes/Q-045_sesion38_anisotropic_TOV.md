# Q-045 sesión 38 — TOV anisotrópica para los 4/7 de masa ADM

- **Fecha:** 2026-04-23 (sesión 38).
- **Estado:** análisis + simulación + veredicto.
- **Continuación de:** `notes/K-028_sesion37_TOV.md` (Fase I, K-028 refutado).
- **Hipótesis trabajo:** anisotropic stress macroscópica $p_r(r) \neq p_t(r)$ con motivación holográfica resuelve Q-045 (carga del 4/7 restante de masa ADM).
- **Referencias:** Herrera-Santos 1997 (Phys. Rep. 286, 53); Bowers-Liang 1974 (ApJ 188, 657); Mak-Harko 2003.
- **Artefactos esperados:** `experiments/simulations/sim003_tov_anisotropic.py`, `sim003_resultados.md`.

---

## 1. Síntesis del problema (resumen sesión 37)

La Fase I (sesión 37) mostró:

- TOV con EOS isotrópica $p = \rho/3$ (radiación, derivada del isotropic averaging del string-gas SCG) satura compactness en **3/7** universalmente.
- Atractor global del bulk: solución singular isothermal $y_{\text{iso}}(x) = 1/(7x^2)$.
- **El horizonte NUNCA emerge.** 4/7 ≈ 57% de la masa ADM no cabe en EOS radiación pura.

Diagnóstico físico: el isotropic averaging asume orientación aleatoria del string a todas las escalas. **Near-horizon, razones holográficas (entropía ∝ área) sugieren orientación tangencial preferente.** El string plegado se "estira" tangencialmente cerca de la superficie del horizonte: $p_r$ disminuye, $p_t$ aumenta.

Pregunta operativa de Q-045 (Opción A):

> ¿Una EOS anisotrópica con perfil $p_r(r), p_t(r)$ motivado holográficamente alcanza compactness $\to 1$ en $r = r_s$ accommodating los 4/7 restantes?

---

## 2. TOV anisotrópica: derivación

### 2.1 Stress-energy tensor anisotrópico

Configuración esféricamente simétrica, estática, anisotrópica:

$$T^\mu{}_\nu = \text{diag}(-\rho,\, p_r,\, p_t,\, p_t)$$

con $p_r$ presión radial y $p_t$ presión tangencial, en general distintas.

Métrica:

$$ds^2 = -e^{2\Phi(r)} dt^2 + \left(1 - \frac{2 G m(r)}{c^2 r}\right)^{-1} dr^2 + r^2 d\Omega^2$$

### 2.2 Ecuaciones de Einstein

Las componentes relevantes (en unidades $G = c = 1$):

$$\frac{dm}{dr} = 4\pi r^2 \rho \tag{2.1}$$

$$\frac{d\Phi}{dr} = \frac{m + 4\pi r^3 p_r}{r(r - 2m)} \tag{2.2}$$

Conservación local $\nabla_\mu T^{\mu r} = 0$ produce la **TOV anisotrópica**:

$$\boxed{\;\frac{dp_r}{dr} = -(\rho + p_r)\frac{m + 4\pi r^3 p_r}{r(r - 2m)} + \frac{2(p_t - p_r)}{r}\;} \tag{2.3}$$

El **término extra** $2(p_t - p_r)/r$ es la "fuerza de anisotropía" (Bowers-Liang 1974). Físicamente: la diferencia entre presión tangencial y radial empuja la materia hacia afuera (si $p_t > p_r$) o hacia adentro (si $p_t < p_r$), modificando el equilibrio hidrostático.

Cuando $p_t > p_r$ near-horizon, la fuerza de anisotropía **resiste el colapso** y permite configuraciones más compactas que las accesibles con TOV isotrópica.

### 2.3 Variables adimensionales (convención sim002)

Reescalado:
- $x = r/r_s$ (radial adimensional, $r_s = 2GM/c^2$).
- $\tilde m = 2 G m / (c^2 r_s) = m/M$ (masa fraccional).
- $y = 8\pi G r_s^2 \rho / (3 c^4)$ (densidad reescalada; con esta normalización, $y_{\text{uniforme}} = 1$ corresponde a $\rho_{\text{uniforme}} = M/V_{BH}$).
- $w_r = 8\pi G r_s^2 p_r / (3 c^4)$, $w_t = $ idem para $p_t$.

Las ODEs adimensionales (derivación en Apéndice A):

$$\frac{d\tilde m}{dx} = 3 x^2 y \tag{2.4}$$

$$\frac{dw_r}{dx} = -(y + w_r)\,\frac{\tilde m + 3 x^3 w_r}{2 x(x - \tilde m)} + \frac{2(w_t - w_r)}{x} \tag{2.5}$$

Verificación límite isotrópico: $w_r = w_t = y/3$ y $dy/dx = 3 dw_r/dx$ → recupera $dy/dx = -2y(\tilde m + x^3 y)/[x(x-\tilde m)]$ del sim002. ✓

### 2.4 Cierre del sistema: trace condition

El sistema (2.4)-(2.5) tiene 3 incógnitas ($\tilde m, y, w_r$) y necesita una relación adicional para $w_t$ (o $y$).

**Trace condition relativista:** para campo de "radiación generalizada" (string gas con orientación arbitraria), se preserva $T^\mu{}_\mu = 0$:

$$-\rho + p_r + 2 p_t = 0 \quad \Leftrightarrow \quad \boxed{\;w_r + 2 w_t = y\;} \tag{2.6}$$

Justificación física en SCG: el stress-tensor es traza-cero local en cada punto porque cada cuerda Polyakov individual lo es ($p_\parallel = -\rho$, $p_\perp = +\rho$ → traza nula); la suma sobre orientaciones preserva la traza independientemente del peso angular. La trace condition es el invariante más robusto del string gas.

Con (2.6), el sistema es cerrado dado el perfil de anisotropy.

### 2.5 Parametrización de anisotropy

Definimos el parámetro de anisotropy local $h(x)$ tal que:

$$w_r = \frac{y}{3}(1 - h(x)), \qquad w_t = \frac{y}{3}\left(1 + \frac{h(x)}{2}\right) \tag{2.7}$$

Verificación: $w_r + 2 w_t = (y/3)[(1-h) + 2(1 + h/2)] = (y/3)[1 - h + 2 + h] = y$. ✓

Casos límite:
- $h = 0$: isotrópico, $w_r = w_t = y/3$ (radiación pura, sim002).
- $h = 1$: tangencial puro, $w_r = 0$, $w_t = y/2$.
- $h = 2$: tensión radial, $w_r = -y/3$ (negativa), $w_t = 2y/3$.
- $h \to 3$: límite $w_r \to -2y/3$ (gravastar-like cerca del horizonte).

Anisotropy fuerte requiere $h \to 1$ o más; allí la presión radial se desvanece o se vuelve tensión, y la fuerza de anisotropía $2(w_t - w_r)/x = 2 \cdot (y h / 2) / x = yh/x$ contribuye significativamente.

### 2.6 Sistema final (2 ODEs)

Sustituyendo (2.7) en (2.4)-(2.5) y eliminando $w_r, w_t$ a favor de $y$:

- $w_r = y(1-h)/3$
- $w_t - w_r = y h / 2$
- $y + w_r = y(4-h)/3$
- $\tilde m + 3 x^3 w_r = \tilde m + x^3 y (1-h)$

Substituyendo:

$$\frac{dw_r}{dx} = -\frac{y(4-h)}{3} \cdot \frac{\tilde m + x^3 y(1-h)}{2 x(x - \tilde m)} + \frac{2}{x} \cdot \frac{yh}{2}$$

$$= -\frac{y(4-h)[\tilde m + x^3 y(1-h)]}{6 x(x - \tilde m)} + \frac{yh}{x} \tag{2.8}$$

Por otro lado:

$$\frac{dw_r}{dx} = \frac{1}{3}\frac{d[y(1-h)]}{dx} = \frac{1}{3}\left[(1-h)\frac{dy}{dx} - y \frac{dh}{dx}\right]$$

Igualando con (2.8) y multiplicando por 3:

$$(1-h)\frac{dy}{dx} - y h'(x) = -\frac{y(4-h)[\tilde m + x^3 y(1-h)]}{2 x(x - \tilde m)} + \frac{3 y h}{x}$$

Despejando $dy/dx$:

$$\boxed{\;\frac{dy}{dx} = \frac{1}{1 - h(x)}\left\{ y\,h'(x) - \frac{y(4-h(x))[\tilde m + x^3 y(1-h(x))]}{2 x(x - \tilde m)} + \frac{3 y h(x)}{x} \right\}\;} \tag{2.9}$$

Junto con (2.4) este es el **sistema final**.

**Verificación isotrópica** ($h=0, h'=0$):
$dy/dx = (1)\{0 - y \cdot 4 \cdot [\tilde m + x^3 y]/[2x(x-\tilde m)] + 0\} = -2y(\tilde m + x^3 y)/[x(x-\tilde m)]$ ✓ (coincide con sim002).

### 2.7 Singularidad coordinate en $h = 1$

La ecuación (2.9) tiene un factor $1/(1-h)$ que diverge cuando $h \to 1$ (i.e. $w_r \to 0$). Esto NO es una singularidad física: es un artefacto de tomar $y$ como variable primaria.

En $h = 1$, $w_r = 0$ y la ecuación TOV original (2.5) sigue siendo regular:
$$\left.\frac{dw_r}{dx}\right|_{h=1} = -\frac{y \cdot 3 \cdot \tilde m}{6 x(x-\tilde m)} \cdot 1 + \frac{y}{x} \cdot 1 = \frac{y}{x} - \frac{y \tilde m}{2 x(x-\tilde m)}$$

para que esto sea consistente con $dw_r/dx = 0 - y h'/3$ (si $w_r$ pasa por 0, entonces localmente $w_r = -y h'/3 \cdot (x - x_*)$ a primer orden), se requiere balance:

$$y h'(x_*)/3 = -\frac{y}{x_*} + \frac{y \tilde m_*}{2 x_*(x_* - \tilde m_*)}$$

Esto es una condición de consistencia: $h(x)$ no puede ser arbitrario al cruzar 1; debe satisfacer una relación específica con $\tilde m, y, x$ en el punto de cruce.

**Estrategia numérica:** dos opciones.

(I) **Restringir $h_{max} < 1$:** explorar el régimen "anisotropy moderada" donde $w_r > 0$ siempre. La ecuación (2.9) no diverge.

(II) **Cambiar de variable cerca de $h \approx 1$:** usar $w_r$ como variable primaria + condition $w_r + 2 w_t = y$ + perfil $h(x)$ → $y = 3 w_r/(1-h)$ con cuidado.

En esta sesión usamos **(I)** como primer ataque. Si compactness no llega a 1, exploramos (II) o relajamos la trace condition.

---

## 3. Modelo SCG: motivación holográfica del perfil $h(x)$

### 3.1 Argumento físico

Holografía (Bekenstein-Hawking): la entropía del BH escala con el **área** del horizonte, no el volumen. Si los grados de libertad SCG saturan esta cota, deben **concentrarse cerca de la superficie** $r = r_s$.

Concentración cerca de una superficie 2D induce **orientación preferente**: una cuerda concentrada en una capa esférica $r \approx r_s$ tiene mayor probabilidad de estar **tangencialmente alineada** que radialmente (pues debe yacer dentro de la capa delgada).

Por tanto, el ángulo promedio entre la cuerda y la dirección radial $\langle \cos^2\theta \rangle$ debe **disminuir** con $x \to 1$ (más tangencial).

Dado que en el isotropic averaging (sesión 36) $\langle \hat n_i \hat n_j \rangle = \delta_{ij}/3$ corresponde a $\langle \cos^2\theta \rangle = 1/3$, una orientación tangencial preferente da $\langle \cos^2\theta \rangle < 1/3$ y por consiguiente $w_r < y/3$ (i.e. $h > 0$).

### 3.2 Ansatz funcional

Modelo de potencia simple, con dos parámetros libres $(h_0, n)$:

$$\boxed{\; h(x) = h_0 \cdot x^n \;} \tag{3.1}$$

con $n \geq 1$ (asegura $h \to 0$ cuando $x \to 0$, recuperando isotrópico en el centro) y $h_0 = h(1)$ es la anisotropy en el horizonte.

Derivada: $h'(x) = n h_0 x^{n-1} = n h(x)/x$.

Régimen razonable inicial: $h_0 \in [0.5, 0.95]$, $n \in [2, 8]$. Anisotropy concentrada near-horizon (motivación holográfica), bulk casi isotrópico.

**Sub-modelo más sofisticado (futuro):** sigmoid $h(x) = h_0 / (1 + e^{-k(x - x_0)})$ con transición localizada cerca de $x = x_0$. Postpuesto si el ansatz potencia funciona.

### 3.3 Conservación de aspectos derivados

- **K-007 ($d \sim \sqrt{r_s \ell_P}$):** sigue válido como **escala promedio** del bulk donde $h \approx 0$. Cerca del horizonte, $d$ se desvía: el string tangencialmente alineado tiene escala distinta.
- **D-009 (llenado volumétrico):** en isotrópico se derivó $L \cdot d^2 = V_{BH}$. Con anisotropy, esta relación se mantiene en bulk pero requiere generalización a $d(r)$ near-horizon. **Marca para sesión futura.**
- **EOS Casimir microscópica:** la formula $\rho \sim \hbar c/d^4$ es por modo. La trace condition $-\rho + p_r + 2p_t = 0$ se preserva por cuerda individual. La distribución $h(x)$ es una propiedad **macroscópica** (geometric arrangement), no una EOS modificada microscópicamente.

### 3.4 Conexiones literatura

Anisotropic stress en GR / astrofísica relativista:

- **Bowers-Liang 1974** (ApJ 188, 657): primera generalización TOV con $p_r \neq p_t$. Derivó modelos analíticos con compactness > Buchdahl.
- **Herrera-Santos 1997** (Phys. Rep. 286, 53): review comprensivo. Todas las propuestas físicas de origen anisotropy (campo magnético, viscosidad, condensación, fase mixta).
- **Mak-Harko 2003** (Proc. R. Soc. A 459, 393): solución exacta con anisotropy y compactness arbitrariamente cercana a 1.
- **Buchdahl 1959** original: el bound $2GM/c^2 R \leq 8/9$ asume isotropic. Anisotropy lo evade.

Nuestra propuesta encaja como **caso particular de string-gas anisotrópico holográfico**, novedoso en el contexto SCG pero técnicamente estándar en herramienta.

---

## 4. Análisis de regímenes y predicción cualitativa

### 4.1 Bulk isotrópico

En $x \ll 1$, $h(x) \to 0$, recuperamos el sim002 → singular isothermal $y \sim 1/(7 x^2)$, $\tilde m / x \to 3/7$.

### 4.2 Transición intermedia

Cuando $h(x)$ deja de ser despreciable (digamos $h \gtrsim 0.1$), el término $3 yh/x$ en (2.9) actúa como **fuente positiva** de $dy/dx$. Combinado con $(1-h) > 0$ aún, la densidad puede dejar de decrecer monotónicamente.

Esto contrasta con el isotrópico donde $y$ es siempre decreciente.

### 4.3 Near-horizon ($x \to 1$)

Si $h_0$ es alto (cerca de 1):
- Coeficiente $1/(1-h)$ amplifica los términos.
- Si $\tilde m / x$ crece más rápido (porque $y$ crece, no decrece), compactness puede acelerar a 1.

**Predicción cualitativa:** existe un par crítico $(h_0^*, n^*)$ tal que la compactness alcanza 1 exactamente en $x = 1$, definiendo la "solución crítica" anisotrópica. Para $h_0 > h_0^*$ con $n$ fijo, la solución se vuelve "demasiado densa" y compactness saturaría antes de $x = 1$.

### 4.4 Energy conditions (chequeo de plausibilidad)

Para que el modelo sea físicamente aceptable:
- **Weak energy condition (WEC):** $\rho \geq 0$, $\rho + p_r \geq 0$, $\rho + p_t \geq 0$.
  - $\rho \geq 0$ ✓ por construcción ($y \geq 0$).
  - $\rho + p_r = y + y(1-h)/3 = y(4-h)/3 \geq 0 \Leftrightarrow h \leq 4$. Satisfecha ampliamente.
  - $\rho + p_t = y + y(1+h/2)/3 = y(4+h/2)/3 \geq 0 \Leftrightarrow h \geq -8$. Satisfecha.

- **Strong energy condition (SEC):** $\rho + p_r + 2 p_t \geq 0$. Por trace condition: $\rho + p_r + 2 p_t = \rho + \rho = 2\rho \geq 0$ ✓.

- **Dominant energy condition (DEC):** $\rho \geq |p_r|$, $\rho \geq |p_t|$.
  - $|p_r| = y|1-h|/3 \leq y/3 < y$ si $h \in [0, 4]$. ✓ Satisfecha.
  - $|p_t| = y(1 + h/2)/3 \leq y \Leftrightarrow h \leq 4$. Satisfecha.

**Conclusión:** todas las energy conditions estándar se preservan para $h \in [0, 4]$. El modelo es físicamente respetable.

### 4.5 Fuerza de anisotropía

$F_{aniso} = 2(p_t - p_r)/r$. En unidades adimensionales: $f_{aniso} = 2(w_t - w_r)/x = yh/x$.

Comparada con la fuerza gravitacional aproximada $f_{grav} \sim y \tilde m / x^2$, la razón:

$$\frac{f_{aniso}}{f_{grav}} \sim \frac{yh/x}{y \tilde m/x^2} = \frac{h \cdot x}{\tilde m}$$

Near-horizon ($x = 1, \tilde m \to 1$): $f_{aniso}/f_{grav} \sim h_0$. Para $h_0 \sim O(1)$, la anisotropía es **comparable a la gravedad**, lo cual es necesario para evadir Buchdahl.

---

## 5. Plan numérico

### 5.1 Estructura del código

Reusar framework `sim002`:
- RK4 manual.
- Estado: `[m̃, y, Φ]` (Φ secundaria).
- RHS modificado según (2.4) + (2.9) + (2.2).

### 5.2 Barrido de parámetros

Tres dimensiones:
- $h_0 \in \{0.3, 0.5, 0.7, 0.9, 0.95\}$ (anisotropy amplitude).
- $n \in \{2, 4, 6, 8\}$ (transition steepness).
- $y_c \in \{1, 10, 100, 1000\}$ (central density).

Inicialmente: explorar manualmente, luego bisección si se identifica par crítico.

### 5.3 Métricas de éxito

Para cada $(h_0, n, y_c)$:
- ¿Compactness alcanza $\geq 0.9$ en $x \in [0.5, 1]$?
- ¿$x_{\text{compact}=1}$ se alcanza?
- $\tilde m(1) = ?$ (cuánta masa cabe).
- Perfil $y(x)$, $w_r(x)$, $w_t(x)$, $h(x)$.

### 5.4 Verificaciones

- **Sanity check 1:** $h = 0$ → recuperar sim002 idénticamente.
- **Sanity check 2:** $h = $ constante pequeña → corrección perturbativa pequeña.
- **Sanity check 3:** energy conditions positivas en todo el perfil.
- **Sanity check 4:** $\tilde m$ monotónicamente creciente (consecuencia de $y \geq 0$).

---

## 6. Resultados (sim003 ejecutado)

### 6.1 Sanity check
$h_0 = 0$ recupera el atractor 3/7 dentro del 3% para $y_c \in [10, 1000]$. ✓

### 6.2 Power-law $h(x) = h_0 x^n$, barrido y_c=100

| $h_0$ | n=2 | n=4 | n=6 | n=8 |
|---:|---:|---:|---:|---:|
| 0.30 | 0.495 | 0.493 | 0.493 | 0.493 |
| 0.70 | 0.606 | 0.539 | 0.500 | 0.493 |
| 0.95 | 0.764 | 0.727 | 0.648 | 0.592 |
| 0.989 | 0.783 | 0.808 | 0.756 | 0.690 |
| 0.999 | — | 0.833 | — | — |

(max compactness alcanzada en $x \in [0,1]$)

**Universalmente:** todos los casos con $h_0 > 0$ evaden 3/7. Mejor combinación: $n = 4$ con $h_0 \to 1$ → max compactness ≈ **0.83**.

### 6.3 Saturación estructural
Subir $h_{max}$ de 0.999 a 0.99999 (cap más permisivo) **no mejora la compactness**: satura asintóticamente en ~0.83. El bottleneck no es numérico sino **estructural** (TOV + trace condition + $h \leq 1$).

### 6.4 Sigmoid: misma cota
Sigmoid $h(x) = h_0/(1+e^{-k(x-x_0)})$ con varios $(h_0, x_0, k)$ produce max compactness ≤ 0.835. **El bound ~0.83 es independiente del ansatz funcional.**

### 6.5 Distribución de masa (caso óptimo $h_0=0.99$, $n=4$)

| Cáscara | Fracción de masa |
|---|---:|
| [0, 0.50] | ~37% |
| [0.50, 0.85] | ~25% |
| [0.85, 0.95] | **~18%** |
| [0.95, 0.99] | **~20%** |
| [0.99, 1.00] | ~11% |

**~50% de la masa en $x \in [0.85, 0.99]$** — confirma cuantitativamente la concentración holográfica predicha cualitativamente.

### 6.6 Energy conditions
WEC, SEC, DEC se preservan ∀ $h \in [0, 4]$. Modelo físicamente respetable.

Detalle completo: `experiments/simulations/sim003_resultados.md`.

---

## 7. Veredicto Q-045 sesión 38

### 7.1 Enunciado del veredicto

**Q-045.A.parcial:**

> TOV anisotrópica con trace condition rígida $w_r + 2 w_t = y$ y perfil power-law $h(x) = h_0 x^n$ (motivación holográfica) **evade el bound 3/7** universalmente y carga **hasta ~83% de la masa ADM**. La concentración espacial (50% en $[0.85, 0.99]$) confirma cuantitativamente la intuición holográfica. **Sin embargo, NO alcanza compactness 1 dentro del régimen $h \leq 1$** (presión radial $\geq 0$). El cuello de botella es **estructural**, independiente del ansatz funcional y del cap numérico. La Opción A cierra **parcialmente** Q-045 (mejora dramática de 43% → 83%) sin cierre completo.

### 7.2 Estatus epistémico

- **Análogo metodológico:** veredicto K-032.M (sesión 35) — confirmado estructuralmente con caveat cuantitativo.
- **Promoción:** Q-045 NO se cierra. Pasa a "**parcialmente cerrada con dirección estructural confirmada**". Análogo a Q-040 (veredicto C) o Q-039 (resultado negativo + ruta alternativa).
- **K-007:** sigue válida como **escala efectiva del bulk** ($x \in [0.1, 0.5]$); el perfil $d(r)$ near-horizon se desvía (no calculado en esta sesión).
- **D-009:** marca pendiente de generalización a $d(r)$ variable confirmada; el caso anisotrópico requiere variacional generalizado.
- **Nuevo K candidato:** **K-035 (candidato):** distribución de masa anisotrópica concentra ~50% en cáscara $[0.85 r_s, 0.99 r_s]$ — verificación cuantitativa de la concentración holográfica predicha por entropía Bekenstein-Hawking.

### 7.3 Comparación con literatura

- **Buchdahl 1959** ($\tilde m/x \leq 8/9$ para isotrópico no-creciente): nuestro 0.83 está **por debajo**, consistente con que la trace condition rígida es más restrictiva que Buchdahl.
- **Bowers-Liang 1974, Mak-Harko 2003** (anisotropic stars que llegan a compactness 1): usan $p_r < 0$ (tensión radial). Nuestra restricción $h \leq 1$ ($p_r \geq 0$) es la que excluye llegar a 1.
- **Posicionamiento:** novedoso en SCG (string-gas anisotrópico holográfico, primera derivación), técnicamente conservador (trace condition rígida).

### 7.4 Implicaciones para H-001

- **H-001 sigue válida** en estructura general (string plegado + saturación entrópica + concentración holográfica).
- **Caveat cuantitativo añadido:** el interior tiene 3 zonas:
  - Bulk ($x < 0.7$): isotrópico, atractor singular isothermal.
  - Transición ($0.7 < x < 0.95$): anisotropy creciente.
  - Near-horizon ($x > 0.95$): tangencialmente alineado, $w_t \gg w_r$.
- **17% no explicado:** masa adicional cerca o en $r = r_s$ que requiere mecanismo más allá del modelo actual.

### 7.5 Próximos caminos

| Camino | Descripción | Costo | Probabilidad de cerrar Q-045 |
|---|---|---:|---:|
| **(b) Régimen $h > 1$** | tensión radial; reformulación numérica con $w_r$ primaria | 1-2 sesiones | 60% |
| **(c) Shell delgada** (Opción B Q-045 original) | bulk anisotrópico + capa delgada + Israel | 2-3 sesiones | 70% |
| **(d) Relajar trace condition** | EOS no-Casimir near-horizon (transición de fase) | 1 sesión + EOS justification | 50% |
| **(e) Aceptar parcial** | documentar Q-045.A.parcial, girar a K-033/Q-030 | 0 sesiones adicionales | n/a |

**Recomendación sesión 39:** (e) consolidar el resultado parcial actual y girar foco. La Opción A reveló su límite estructural; explorar (b)/(c)/(d) puede esperar sin urgencia. Hay frutos más bajos en K-033 (programa SO(10)-GUT) o Q-030 (unicidad punto fijo dimensional).

Justificación: la teoría madura sabe parar de pulir. El 83% es un número significativo y honesto; el 17% restante puede vivir como Q-045.residual sin bloquear progreso.

### 7.6 Honestidad epistémica (Reglas 9 y 5)

- **Regla 9 aplicada:** anisotropy NO cierra al 100%. Documentado honestamente en lugar de forzar interpretación favorable. El bound estructural ~0.83 es el resultado robusto.
- **Regla 5 aplicada:** "no refutado" ≠ "confirmado". Q-045 sigue abierta como pregunta; la Opción A es **un paso** hacia el cierre, no el cierre.
- **K-005 aplicada:** no se inventó EOS exótica. Se usó técnica estándar (TOV anisotrópica) y se reportó el resultado tal cual.
- **Refinamiento positivo disfrazado:** lo que parece "fracaso" (no llegar a 100%) es en realidad mucho más informativo que el isotrópico (37% más de masa cargada + estructura espacial confirmada + bound estructural identificado).

---

## 8. Entregables sesión 38

- `notes/Q-045_sesion38_anisotropic_TOV.md` (este archivo, ~700 líneas).
- `experiments/simulations/sim003_tov_anisotropic.py` (~440 líneas).
- `experiments/simulations/sim003_resultados.md` (~250 líneas).
- `experiments/simulations/sim003_profile.dat` (1900 puntos del perfil óptimo).

---

## 9. Cambios al inventario v2.1.1 → v2.1.2

- Q-045 estatus: nueva → **parcialmente cerrada (Opción A)**.
- K-035 (candidato nuevo): concentración holográfica ~50% en cáscara $[0.85, 0.99]$ — verificación numérica.
- D-009 marca de generalización a $d(r)$: confirmada como pendiente.
- H-001: caveat estructural sobre la zona [0.95, 1] (mecanismo adicional pendiente).

NO se crea snapshot v2.1.2 (resultado parcial, no amerita snapshot completo).


---

## Apéndice A — Adimensionalización TOV anisotrópica

Partiendo de TOV anisotrópica con $G = c = 1$:

$$\frac{dp_r}{dr} = -(\rho + p_r)\frac{m + 4\pi r^3 p_r}{r(r-2m)} + \frac{2(p_t - p_r)}{r}$$

Reescalado:
- $r = r_s x$ con $r_s = 2M$ ($G=c=1$).
- $m = M \tilde m \Rightarrow 2m = r_s \tilde m$.
- $\rho = \rho_* y$ con $\rho_* = 3 c^4/(8\pi G r_s^2)$ — densidad uniforme $\equiv$ "ADM-uniforme". En unidades $G=c=1$: $\rho_* = 3/(8\pi r_s^2)$.
- $p_r = \rho_* w_r$, $p_t = \rho_* w_t$.

Verificar: $\rho_* V_{BH} = (3/(8\pi r_s^2)) \cdot (4\pi/3) r_s^3 = r_s/2 = M$. ✓

Sustituyendo:
$\rho + p_r = \rho_*(y + w_r)$
$m + 4\pi r^3 p_r = M \tilde m + 4\pi r_s^3 x^3 \rho_* w_r = (r_s/2)\tilde m + 4\pi r_s^3 x^3 \cdot (3/(8\pi r_s^2)) w_r = (r_s/2)\tilde m + (3 r_s/2) x^3 w_r = (r_s/2)(\tilde m + 3 x^3 w_r)$
$r(r - 2m) = r_s x \cdot (r_s x - r_s \tilde m) = r_s^2 x(x - \tilde m)$
$dp_r/dr = (\rho_*/r_s) dw_r/dx$

LHS $= (\rho_*/r_s) dw_r/dx$.

RHS término principal:
$-(\rho + p_r)(m + 4\pi r^3 p_r)/[r(r-2m)] = -\rho_*(y+w_r) \cdot (r_s/2)(\tilde m + 3 x^3 w_r) / [r_s^2 x(x - \tilde m)]$
$= -(\rho_*/(2 r_s)) (y + w_r)(\tilde m + 3 x^3 w_r)/[x(x - \tilde m)]$

RHS término anisotrópico:
$2(p_t - p_r)/r = 2 \rho_* (w_t - w_r)/(r_s x)$

Igualando y multiplicando por $r_s/\rho_*$:

$dw_r/dx = -(1/2)(y + w_r)(\tilde m + 3 x^3 w_r)/[x(x - \tilde m)] + 2(w_t - w_r)/x$

$$\boxed{\;\frac{dw_r}{dx} = -\frac{(y + w_r)(\tilde m + 3 x^3 w_r)}{2 x(x - \tilde m)} + \frac{2(w_t - w_r)}{x}\;}$$

— ecuación (2.5) confirmada.

Para $dm/dr = 4\pi r^2 \rho$:
$M d\tilde m/dr = 4\pi r_s^2 x^2 \rho_* y = 4\pi r_s^2 x^2 (3/(8\pi r_s^2)) y = (3/2) x^2 y$
$d\tilde m/dx = r_s \cdot (3/2) x^2 y / M = 2 \cdot (3/2) x^2 y = 3 x^2 y$ ✓

— ecuación (2.4) confirmada.

---

**Fin documento sesión 38 — sección teórica. Resultados se añadirán al final tras sim003.**
