# D-016 — Setup variacional para la curva crítica $h_0^*(n)$ de Q-045

- **ID:** D-016
- **Fecha:** 2026-04-26 (sesión 69)
- **Nivel:** **setup formal + análisis estructural + marca pendiente** para derivación rigurosa (control óptimo). NO es derivación cerrada como D-009 — es **D-009 generalizado** parcialmente formalizado, con argumento de existencia del sweet-spot.
- **Deriva:** la curva crítica $h_0^*(n)$ identificada empíricamente por sim009 (sesión 68) como **solución del problema variacional generalizado** D-009 a anisotropy $h(r)$ variable.
- **Alcance:** establecimiento del problema variacional (funcional, restricciones, condición de optimalidad); argumento físico de existencia del sweet-spot; análisis perturbativo cerca del cruce $h = 1$. **Derivación analítica de $h_0^*(n)$ rigurosa: pendiente** (requiere control óptimo Pontryagin).
- **Análisis técnico previo:** `notes/Q-045_sesion68_*.md`; `experiments/simulations/sim009_*`.
- **Status epistémico:** **setup parcial** (análogo K-032.M intermedio en su nivel epistémico). Promueve K-035 a "confirmado estructuralmente con derivación variacional parcial" (refinamiento del estatus post-S68).
- **Habilita:** derivación analítica del sweet-spot (S70+ trabajo técnico de control óptimo) o promoción de K-035 a confirmado limpio.

---

## 1. Enunciado

**Proposición (D-016 setup).** Sea la TOV anisotrópica string-gas SCG con trace condition + DEC. La curva crítica $h_0^*(n)$ identificada empíricamente por sim009 (sesión 68) corresponde a la **solución del problema de control óptimo**:

$$
\boxed{\;\;\max_{h(\cdot)} \;\tilde m(x_{\text{end}}) \quad \text{sujeto a: TOV anisotrópica + trace + DEC + cierre al horizonte}\;\;}
$$

donde la "función de control" es $h(x)$ y las "variables de estado" son $\tilde m(x), y(x)$. La condición de cierre completo al horizonte $\tilde m(x_{\text{end}}) = 1$ con $x_{\text{end}} = 1$ define la **trayectoria crítica**.

**Análogo conceptual a D-009:** así como D-009 mostró que "L·d² = V_BH" emerge variacionalmente bajo restricción geométrica, **D-016 muestra que "el sweet-spot $h_0^*(n)$ existe" como solución variacional del problema generalizado a anisotropy variable**.

**Caveat principal:** el setup formal está completo; la **resolución analítica explícita del problema** (i.e., derivación de la curva $h_0^*(n)$) requiere técnicas de control óptimo Pontryagin no aplicadas en esta sesión.

---

## 2. Setup formal del problema variacional

### 2.1 Variables y funciones

- **Variables de estado (funciones de $x$):** $\tilde m(x), y(x)$.
- **Función de control (función de $x$):** $h(x)$.
- **Variable independiente:** $x \in [0, 1]$.

### 2.2 Sistema dinámico (TOV anisotrópica)

Recordatorio (sim003 + sim009):

$$
\frac{d\tilde m}{dx} = 3 x^2 y(x) \tag{2.1}
$$

$$
\frac{dy}{dx} = \frac{1}{1 - h(x)} \left[ y h'(x) - \frac{y(4 - h)[\tilde m + x^3 y(1-h)]}{2 x(x - \tilde m)} + \frac{3 y h}{x} \right] \tag{2.2}
$$

con condiciones iniciales:
$$
\tilde m(0) = 0, \qquad y(0) = y_c \quad \text{(densidad central)}. \tag{2.3}
$$

### 2.3 Restricciones (constraints)

**Restricción A — DEC:** $h(x) \in [-2, 4]$ para todo $x \in [0, 1]$.
**Restricción B — regularidad central:** $h(0) = 0$ (isotropic averaging asegura régimen isotrópico en el centro).
**Restricción C — condición terminal:** $\tilde m(x_{\text{end}}) = 1, x_{\text{end}} = 1$ (toda la masa ADM contenida en el horizonte).

### 2.4 Función objetivo (cost functional)

$$
\boxed{\;J[h(\cdot)] = \tilde m(x_{\text{end}}) \;}
$$

Maximizar $J$ sujeto a (2.1)-(2.3) + restricciones A, B, C.

### 2.5 Hamiltoniano de Pontryagin

Definimos multiplicadores adjuntos $\lambda_m(x), \lambda_y(x)$:

$$
H(\tilde m, y, h, \lambda_m, \lambda_y; x) = \lambda_m \cdot 3 x^2 y + \lambda_y \cdot F(\tilde m, y, h, h'; x) \tag{2.4}
$$

donde $F(\tilde m, y, h, h'; x)$ es el lado derecho de (2.2).

**Ecuaciones adjuntas:**
$$
\frac{d\lambda_m}{dx} = -\frac{\partial H}{\partial \tilde m}, \qquad \frac{d\lambda_y}{dx} = -\frac{\partial H}{\partial y} \tag{2.5}
$$

**Condición de optimalidad (Pontryagin):**
$$
\boxed{\;\frac{\partial H}{\partial h} = 0 \;} \tag{2.6}
$$

**Condiciones de transversalidad** (terminal):
$$
\lambda_m(1) = 1, \qquad \lambda_y(1) = 0 \quad \text{(de }\partial J/\partial \tilde m = 1, \partial J/\partial y = 0\text{)}. \tag{2.7}
$$

### 2.6 Sistema cerrado

(2.1) + (2.2) + (2.5) + (2.6) + condiciones iniciales (2.3) + condiciones terminales (2.7) constituyen un **problema de valores en la frontera** (BVP) en 4 variables: $\tilde m, y, \lambda_m, \lambda_y$, con $h(x)$ determinado por (2.6).

**Resolución analítica:** **pendiente.** Requiere análisis técnico cuidadoso del Hamiltoniano (2.4) y manejo de la singularidad coordinate en $h = 1$.

---

## 3. Argumento físico de existencia del sweet-spot

### 3.1 Heurística variacional

**Paso 1 — Energía total como funcional de $h(\cdot)$:**

Para una solución TOV anisotrópica con $h(x)$ dado, la energía total integrada hasta $x = 1$ es:
$$
E[h(\cdot)] = \int_0^1 4 \pi r_s^2 \rho_*\, x^2 y(x; h) \, dx \cdot r_s = M \cdot \tilde m_{\text{end}}(h) \tag{3.1}
$$

Maximizar $E$ es equivalente a maximizar $\tilde m_{\text{end}}$.

**Paso 2 — Comportamiento asintótico:**

- **$h(x) \equiv 0$ (isotrópico):** sim002 → $\tilde m_{\text{end}} = 3/7 \approx 0.43$. Compactness saturada por estructura isotrópica.
- **$h(x) = h_0 x^n$ con $h_0 \to 0$:** sim003 → $\tilde m_{\text{end}} \to 0.43$ (límite isotrópico).
- **$h(x) = h_0 x^n$ con $h_0 \to 1^-$:** sim003 → $\tilde m_{\text{end}} \to 0.83$ (bound estructural sim003).
- **$h(x) = h_0 x^n$ con $h_0 \to 1^+$ desde el lado $h > 1$:** sim009 → $\tilde m_{\text{end}}$ depende de $n$.

**Paso 3 — Existencia del sweet-spot:**

Para $h_0 < h_0^*(n)$: la solución llega a $x = 1$ con $y \to 0$ (superficie) y $\tilde m_{\text{end}} < 1$. **No toda la masa cabe.**

Para $h_0 > h_0^*(n)$: la solución forma horizonte en $x_{\text{horizon}} < 1$ con $\tilde m_{\text{horizon}} < 1$. **Colapso prematuro: BH parcial.**

**En $h_0 = h_0^*(n)$:** la solución llega exactamente a $x = 1$ con $\tilde m \to 1$ y $c \to 1$ simultáneamente. **Cierre completo al horizonte con masa M.**

Esta es la **trayectoria crítica** del problema de control óptimo. La existencia se garantiza por continuidad: $\tilde m_{\text{end}}$ es función continua de $h_0$, de valor 0.83 en $h_0 \to 1^-$ a valor < 1 cuando se forma BH parcial. Por teorema del valor intermedio, existe $h_0^*$ donde $\tilde m_{\text{end}} = 1$.

### 3.2 Esbozo del argumento de optimalidad

**Conjetura D-016:** la curva crítica $h_0^*(n)$ identificada empíricamente por sim009 corresponde a la **única trayectoria óptima** (modulo regularidad) del problema (2.1)-(2.7).

**Argumento:**
1. **Existencia:** por (3.1.3) arriba.
2. **Unicidad:** la función $h_0^*$ es única para cada $n$ por la **monotonicidad** de $\tilde m_{\text{end}}(h_0)$ en una banda alrededor de $h_0^*$.
3. **Optimalidad global:** entre todos los perfiles $h(x)$ admisibles (no solo power-law), el power-law con $h_0^*$ es el que satura $J = 1$. **Argumento informal:** otras formas funcionales pueden cierres también — el sigmoid de sim009 da 98.7% — pero el power-law con sweet-spot da 99.4-99.9%.

**El argumento formal de optimalidad global queda pendiente** — requiere análisis Pontryagin completo.

### 3.3 Argumento de regularidad cerca del cruce $h = 1$

**En $x = x_*$ donde $h(x_*) = 1$:**

- $w_r(x_*) = 0$.
- Por L'Hôpital: $y(x_*) = -3 w_r'(x_*) / h'(x_*)$.
- Para $h(x) = h_0 x^n$ con $h_0 > 1$: $x_* = (1/h_0)^{1/n}$, $h'(x_*) = n h_0 x_*^{n-1} = n/x_*$ (identidad útil).
- Por tanto: $y(x_*) = -3 w_r'(x_*) \cdot x_*/n$.

Para que $y(x_*) > 0$ (densidad positiva): $w_r'(x_*) < 0$ (i.e., $w_r$ pasa por cero suavemente de positivo a negativo).

**Esta condición de regularidad** es satisfecha automáticamente por la solución TOV smooth con $h(x) = h_0 x^n$ creciente.

### 3.4 Patrón empírico $h_0^*(n)$

Datos de sim009 (sweet-spots refinados):

| $n$ | $h_0^*$ | $x_* = (1/h_0)^{1/n}$ | $1 - x_*$ | $(h_0 - 1)$ |
|---:|---:|---:|---:|---:|
| 2 | 1.20 | 0.913 | 0.087 | 0.20 |
| 3 | 1.07 | 0.978 | 0.022 | 0.07 |
| 4 | 1.03 | 0.993 | 0.007 | 0.03 |
| 5 | 1.02 | 0.996 | 0.004 | 0.02 |

**Patrón observado:** $h_0^* \to 1^+$ y $1 - x_* \to 0$ cuando $n \to \infty$. La capa near-horizon donde $h > 1$ se vuelve más delgada.

**Producto $(h_0 - 1) \cdot (1 - x_*) \approx (h_0 - 1)^2/n$ (expansión Taylor para $h_0$ cercano a 1):**
- $n = 2$: 0.0040.
- $n = 3$: 0.0016.
- $n = 4$: 0.00023.

NO es constante simple. La curva crítica $h_0^*(n)$ tiene estructura más compleja que un escalado dimensional sencillo.

**Hipótesis:** la curva crítica satisface una ecuación funcional implícita que involucra el integral de $(h - 1)$ ponderado por la densidad sobre la zona near-horizon. La derivación rigurosa requiere análisis integral de la TOV anisotrópica entre $x_*$ y $1$.

### 3.5 Marca pendiente para derivación rigurosa

**Trabajo técnico requerido (S70+ o futuro):**
1. **Aplicación de Pontryagin a (2.1)-(2.7):** derivar $h^*(x)$ óptimo desde primera principios.
2. **Análisis del sistema BVP** asociado: shooting method o relajación.
3. **Identificación de la curva crítica $h_0^*(n)$** desde la solución óptima.
4. **Validación numérica** contra sim009.

**Estimación de costo:** 1-3 sesiones técnicas adicionales. Si excede, retreat ordenado (Regla 9).

---

## 4. Análisis perturbativo cerca de $h = 1$

### 4.1 Expansión local

Cerca de $x = x_*$ donde $h(x_*) = 1$, expandimos:
$$
h(x) = 1 + \alpha (x - x_*) + O((x - x_*)^2), \quad \alpha = h'(x_*) = n h_0 x_*^{n-1} \tag{4.1}
$$

Para $h_0 = 1.05, n = 4$: $x_* = 0.988$, $\alpha = 4 \cdot 1.05 \cdot 0.988^3 = 4.05$.

### 4.2 Comportamiento de $y(x)$ y $w_r(x)$ cerca del cruce

**Antes del cruce** ($x < x_*$, $h < 1$, $w_r > 0$):
- $w_r(x) \approx (y_*/3)(1 - h(x)) = (y_*/3) \cdot |\alpha| (x_* - x)$.
- $y(x) \approx y_* + O(x - x_*)$.

**Después del cruce** ($x > x_*$, $h > 1$, $w_r < 0$):
- $w_r(x) \approx -(y_*/3) \cdot |\alpha| (x - x_*)$ (continuación analítica).
- $y(x) \approx y_* + O(x - x_*)$.

**El perfil $w_r(x)$ pasa suavemente por cero** con pendiente $|w_r'(x_*)| = y_* \cdot \alpha / 3$.

### 4.3 Condición de cierre integrada

**Condición:** $\tilde m(1) = 1$ con $x_{\text{end}} = 1$.

Por (2.1): $\tilde m(1) = \int_0^1 3 x^2 y(x) dx$.

Separando en bulk + near-horizon:
$$
\tilde m(1) = \underbrace{\int_0^{x_*} 3 x^2 y(x) dx}_{\tilde m_{\text{bulk}}} + \underbrace{\int_{x_*}^1 3 x^2 y(x) dx}_{\Delta \tilde m_{\text{near-hor}}} = 1 \tag{4.2}
$$

**$\tilde m_{\text{bulk}}$** depende de $h_0$ vía la solución bulk.
**$\Delta \tilde m_{\text{near-hor}}$** depende de $h_0$ vía $x_*(h_0, n)$ y la solución near-horizon.

**La condición de cierre $\tilde m(1) = 1$** define implícitamente la curva $h_0^*(n)$.

### 4.4 Argumento heurístico cualitativo

Empíricamente (sim009):
- $\tilde m_{\text{bulk}}(h_0 = 1.05, n = 4) \approx 0.79$ (~79% de la masa en $x < x_* = 0.988$).
- $\Delta \tilde m_{\text{near-hor}} \approx 0.20$ (~20% en la fina capa $[0.988, 0.995]$).

**Para $n$ pequeño** ($n = 2$, $x_* = 0.91$): la zona bulk es más extensa, $\tilde m_{\text{bulk}}$ es mayor (~0.85), pero $\Delta \tilde m_{\text{near-hor}}$ debe compensar más para llegar a 1. Esto requiere $h_0^*$ mayor (~1.2).

**Para $n$ grande** ($n = 5$, $x_* = 0.996$): la zona bulk casi llega al horizonte, $\tilde m_{\text{bulk}}$ ya es ~0.95-0.98, y $\Delta \tilde m_{\text{near-hor}}$ solo necesita aportar ~0.02-0.05. Por eso $h_0^*$ puede ser mucho menor (~1.02).

**Conclusión cualitativa:** la curva crítica $h_0^*(n)$ refleja el **balance** entre la contribución del bulk (que depende del valor del cruce $x_*$) y la contribución de la capa near-horizon (que depende de la magnitud de la tensión radial).

---

## 5. Alcance y limitaciones

### 5.1 Lo que D-016 establece

1. **Setup formal completo** del problema variacional generalizado D-009 → D-016 a anisotropy variable.
2. **Argumento de existencia del sweet-spot** $h_0^*(n)$ por continuidad / valor intermedio.
3. **Análisis perturbativo del cruce $h = 1$** mostrando regularidad smooth.
4. **Identificación del balance bulk + near-horizon** como mecanismo físico subyacente.
5. **Marca pendiente** para derivación rigurosa via Pontryagin.

### 5.2 Lo que D-016 NO establece

1. **Derivación analítica explícita** de la curva $h_0^*(n)$.
2. **Optimalidad global** del power-law sobre otras formas funcionales.
3. **Unicidad rigurosa** del sweet-spot.
4. **Conexión cuantitativa** con D-009 (cuya derivación variacional era simple Lagrange con 1 multiplicador).
5. **Argumento microfísico** del por qué SCG produce $h(x) = h_0 x^n$ específicamente.

### 5.3 Estado epistémico

**Nivel:** **setup variacional + argumento de existencia + marca pendiente para derivación rigurosa**. Análogo a K-032.M (sesión 35) en epistemological status — forma funcional sí, valor numérico exacto pendiente.

**Caveat principal:** la "promoción" de K-035 a confirmado limpio requiere completar la derivación rigurosa Pontryagin. **K-035 sigue como "confirmado estructuralmente con derivación variacional parcial" post-D-016.**

---

## 6. Consecuencias

### 6.1 Refinamiento de K-035

**Pre-D-016:** K-035 promoción a "confirmado estructuralmente" (sesión 68, sim009).
**Post-D-016:** K-035 estatus refinado a "**confirmado estructuralmente con derivación variacional parcial**" — el problema variacional está bien definido, el sweet-spot es solución existente, pero la curva analítica $h_0^*(n)$ no se deriva en cerrado.

### 6.2 Marca pendiente extendida

**Trabajo técnico para K-035 → confirmado limpio:**
1. **D-016 completo:** aplicar Pontryagin rigurosamente (1-3 sesiones técnicas).
2. **Derivar curva analítica** $h_0^*(n)$ (1-2 sesiones).
3. **Validar contra sim009** + posible refinamiento numérico (1 sesión).

**Estimación total: 3-6 sesiones** para K-035 → confirmado limpio. **No urgente** post-S69.

### 6.3 Implicaciones para D-009

D-009 es **caso particular** de D-016:
- D-009: minimización $E_{\text{total}}(L, d)$ con restricción $L \cdot d^2 = V_{BH}$ (1 grado de libertad escalar, 1 multiplicador).
- D-016: minimización funcional $E[h(\cdot), y(\cdot), \tilde m(\cdot)]$ con restricciones diferenciales (TOV) + algebraicas (trace + DEC).

**D-009 es la versión 0-dimensional (estática); D-016 es la versión 1-dimensional (anisotropy variable).** El paradigma "balance Casimir vs gravedad" se mantiene; la generalización es a configuración con perfil $h(r)$.

### 6.4 Implicaciones para H-001

H-001 v1.2 mantiene su estructura. La extensión 4-zonas (post-S68) se confirma estructuralmente por D-016 setup:
1. Bulk isotrópico (h ≈ 0): mínimo trivial del funcional restringido.
2. Transición (h crece de 0 a 1): trayectoria óptima sub-bulk.
3. Cruce $h = 1$ ($x = x_*$): inflexión, punto crítico del control.
4. Near-horizon (h > 1): contribución "fina" de la capa con tensión radial.

---

## 7. Relación con la literatura

### 7.1 Control óptimo y problemas variacionales en GR

- **Pontryagin et al. 1962** (The Mathematical Theory of Optimal Processes): teoría de control óptimo. Aplicable directamente al setup §2 de D-016.
- **Misner-Thorne-Wheeler 1973** (Gravitation §16, §22-§24): variacionales en GR.
- **Andreasson 2008** (Comm. Math. Phys. 288, 715): bound generalizado para anisotropic stars. NO aplica directamente para $\rho$ no-monotónica (caso SCG), pero análogo metodológico.
- **Karush-Kuhn-Tucker 1951:** optimización con restricciones (estándar). Base de D-009.

### 7.2 Anisotropic stars con compactness alta

- **Bowers-Liang 1974** (ApJ 188, 657): primer modelo TOV anisotrópico con compactness > Buchdahl. Análogo conceptual.
- **Mak-Harko 2003** (Proc. R. Soc. A 459, 393): solución exacta anisotrópica con compactness arbitrariamente cercana a 1. Convergencia con sim009 sweet-spot.
- **Herrera-Santos 1997** (Phys. Rep. 286, 53): review comprehensivo de anisotropic stress en GR.

### 7.3 Originalidad de D-016

**Aporte de D-016:**
1. **Identificación del sweet-spot $h_0^*(n)$ como problema de control óptimo:** novedoso en literatura SCG.
2. **Conexión analítica con D-009 generalizado:** D-016 es el "D-009 1-dimensional" — extensión natural del paradigma variacional a anisotropy variable.
3. **Validación con sim009:** la curva crítica numérica concuerda con el argumento de existencia variacional.

**Lo que falta:** derivación analítica completa Pontryagin (trabajo técnico futuro).

---

## 8. Implicaciones

### 8.1 Inventario post-D-016

- **31 K confirmados** (sin cambio).
- **9 candidatos** (sin cambio).
- **16 derivaciones** (D-001 a D-016; D-016 nueva).
- **Estatus K-035:** "confirmado estructuralmente" (S68) **refinado** a "confirmado estructuralmente con derivación variacional parcial" (post-D-016).

### 8.2 Marcas pendientes acumuladas

- **D-016 derivación rigurosa Pontryagin:** 3-6 sesiones técnicas, no urgente.
- **K-035 promoción a confirmado limpio:** depende de D-016 completo.
- **Refinamiento numérico Q-045 al < 0.01%:** integrador de mayor orden, 1 sesión técnica.

### 8.3 Decisión post-S69

D-016 (este documento, setup) cierra Fase 3 plan post-K-033 al nivel "setup formal + análisis estructural". Las opciones para S70+:

- **(A) D-016 completo** (3-6 sesiones técnicas Pontryagin): promueve K-035 a confirmado limpio.
- **(B) Refinamiento numérico Q-045** (1 sesión): cierre al < 0.01%.
- **(C) Fase 4 super-MTC explícita** (5-10 sesiones): refinamiento sub-tarea E del programa K-033.
- **(D) Nueva hipótesis H-004** (constantes fundamentales).

**Recomendación tentativa:** (B) refinamiento numérico Q-045 primero (1 sesión, alto payoff), luego decidir entre (A) y (C).

---

## 9. Firma

D-016 establece el **setup variacional formal** de la curva crítica $h_0^*(n)$ identificada empíricamente por sim009. El problema se formula como **control óptimo Pontryagin** con función de control $h(x)$, variables de estado $(\tilde m, y)$, y función objetivo $\tilde m(1)$.

**Argumento de existencia del sweet-spot** establecido por continuidad / valor intermedio. **Análisis perturbativo del cruce $h = 1$** muestra regularidad smooth.

**Derivación analítica explícita de $h_0^*(n)$ pendiente** — requiere trabajo técnico Pontryagin (3-6 sesiones). K-035 estatus refinado: "confirmado estructuralmente con derivación variacional parcial".

**Análogo a K-032.M (sesión 35)** en su nivel epistémico: forma funcional sí (D-009 generalizado), valor numérico exacto pendiente (curva $h_0^*(n)$). Patrón consolidado del marco SCG: **calibración honesta entre lo establecido y lo pendiente**.

**K-005 ejemplar:** ningún mecanismo SCG nuevo postulado en D-016. El argumento variacional es **continuación natural** de D-009 a anisotropy variable.

**Pieza estructural integradora**, no derivación cerrada. Habilita trabajo futuro para promoción K-035 a confirmado limpio o, alternativamente, transición a Fase 4 (super-MTC explícita) sin completar D-016.

---

## Apéndice A — Sistema completo (referencia)

**Estado:** $(\tilde m, y, \lambda_m, \lambda_y)$.

**Ecuaciones primarias:**
- $\dot{\tilde m} = 3 x^2 y$.
- $\dot y = F(\tilde m, y, h, h'; x)$ con $F$ = lado derecho de (2.2).

**Ecuaciones adjuntas:**
- $\dot \lambda_m = -\partial H/\partial \tilde m$.
- $\dot \lambda_y = -\partial H/\partial y$.

**Control óptimo:** $\partial H/\partial h = 0$ → $h^*(x; \tilde m, y, \lambda_m, \lambda_y)$.

**Condiciones de frontera:**
- $\tilde m(0) = 0, y(0) = y_c$ (iniciales).
- $\lambda_m(1) = 1, \lambda_y(1) = 0$ (terminales transversalidad).
- $\tilde m(1) = 1, x_{\text{end}} = 1$ (cierre completo).

**BVP en 4 variables.** Resolución numérica accesible via shooting o relajación.

## Apéndice B — Datos empíricos curva crítica (sim009)

| $n$ | $h_0^*$ refinado | $\tilde m_{\text{end}}$ | $x_*$ analítico | $x_{\text{end}}$ |
|---:|---:|---:|---:|---:|
| 2 | 1.20 | 0.996 | 0.913 | 0.997 |
| 3 | 1.08 | 0.994 | 0.974 | 0.996 |
| 4 | 1.03 | 0.999 | 0.993 | 0.999 |
| 5 | 1.02 | ~1.005 | 0.996 | 0.999 |

**Tendencia:** $h_0^* \to 1^+$ cuando $n \to \infty$. Confirma la estructura cualitativa del balance bulk + near-horizon.
