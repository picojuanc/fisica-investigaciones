# D-001: Modelo discreto de cuerda gravitacional

- **ID:** D-001
- **Fecha:** 2026-04-15
- **Hipótesis asociada:** H-001
- **Estado:** modelo preliminar; útil como laboratorio computacional; no es una derivación desde primeros principios.

## Objetivo

Construir un modelo mínimo, unidimensional y discreto, que permita **simular numéricamente** la dinámica propuesta por H-001 y observar si el equilibrio "gravedad / tensión / información" produce efectivamente una configuración estable tipo cuerda.

> **Advertencia importante:** este es un *modelo fenomenológico*, no una derivación rigurosa. Los tres términos de energía se postulan con formas específicas porque capturan la intuición (colapso / equiespaciado / penalización de densidad), no porque deriven de una acción fundamental. Su justificación rigurosa es un problema abierto (ver `logic/refutations/debilidades_H-001.md`).

## Construcción

### Representación
Un sistema de **n nodos** sobre la recta real. Cada nodo `i ∈ {0, ..., n-1}` tiene:
- posición `x_i ∈ ℝ`
- velocidad `v_i ∈ ℝ` (en la versión dinámica con temperatura)
- masa `m_i = 1` (unificadas por simplicidad)

### Energía total

```
E_total = E_grav + E_tensión + E_info
```

**Término gravitacional (atractivo, global):**
```
E_grav = -G Σ_{i<j}  m_i m_j / |x_i - x_j|
```
- Cada par de nodos se atrae.
- Singular cuando dos nodos coinciden — compensado por E_info.

**Término de tensión (estructura):**
```
E_tensión = k Σ_{i=0}^{n-2}  (x_{i+1} - x_i)²
```
- Análogo a una cadena elástica: penaliza alargamiento cuadráticamente.
- Favorece espaciamiento uniforme.

**Término de información (repulsión corta):**
```
E_info = λ Σ_{i=0}^{n-2}  1 / (x_{i+1} - x_i)
```
- Diverge cuando dos nodos vecinos se juntan.
- Interpretación: "penalización a concentrar información en longitud nula".

## Análisis de equilibrio (nodos vecinos, simplificación)

Para dos nodos a distancia d, las fuerzas dominantes entre ellos son:

```
F_tensión  = -2k · d       (restaura a d=0)
F_info     = +λ / d²       (repulsiva, diverge cuando d→0)
F_grav     = -G / d²       (atractiva, diverge cuando d→0)
```

La competencia entre F_info y F_grav es el corazón del modelo. Ambos divergen como 1/d² — y el signo del coeficiente *neto* determina si hay equilibrio:

- Si λ > G: hay una distancia de equilibrio d* > 0 donde F_info supera a F_grav, y F_tensión empuja al sistema hacia d* global.
- Si λ < G: el sistema colapsa (d → 0) → régimen "BH".
- Si λ = G: marginal, pero F_tensión eventualmente gobierna.

**Distancia de equilibrio estimada** (igualando F_tensión y F_info - F_grav):
```
2k · d = (λ - G) / d²
⟹ d*³ = (λ - G) / (2k)
⟹ d* = [ (λ - G) / (2k) ]^(1/3)
```

Para λ > G, d* real y positivo → **existe equilibrio estable**. Esta es la **primera predicción interna verificable** del modelo.

## Interpretación de los parámetros

| Parámetro | Interpretación en H-001 |
|---|---|
| G | Intensidad del colapso gravitacional |
| k | Rigidez de la "cuerda" (tensión efectiva) |
| λ | Coeficiente de la presión de entrelazamiento |
| d* | Espaciamiento de equilibrio. Análogo a ℓ_Planck cuando se calibre. |

## Dinámica con temperatura (extensión para `sim001_termica.js`)

Añadir ruido térmico gaussiano y disipación tipo Hawking:

```
F_total_i = F_mecánica_i + N(0, T)           (ruido)
v_i  ←  v_i · (1 - α·T)                       (disipación)
dE/dt  ∝  -T⁴                                 (emisión Stefan–Boltzmann)
```

Con estructura de ruptura y reconexión:
- Si |x_{i+1} - x_i| > d_max → la cuerda se fragmenta.
- Si dos extremos de fragmentos distintos se aproximan a distancia < d_min → se reconectan.

## Entropía en el modelo

Aproximación grosera:
```
S ≈ log(n_nodos · n_fragmentos · (1 + varianza_espacial))
```

Esto **no** es la entropía real del sistema; es una función-proxy que crece cuando:
- hay más nodos (más grados de libertad),
- hay más fragmentos (más configuraciones topológicas),
- la distribución espacial es más heterogénea.

**Su utilidad:** observar tendencias y transiciones de fase cualitativas. Para una entropía genuina se necesitaría definir el ensemble estadístico del modelo, algo aún no hecho.

## Predicciones cualitativas verificables en simulación

1. **Existencia de equilibrio** (fase "cuerda") para λ > G con d* finito.
2. **Transición cuerda → colapso** al reducir λ/G por debajo de 1.
3. **Transición cuerda → gas** al aumentar T por encima de un umbral.
4. **Histéresis** (hipótesis): ¿es la transición reversible o hay diferencia entre subir y bajar T?
5. **Escaleo de entropía con longitud**, no con área, en régimen estable.

## Límites del modelo (honestidad)

- 1D, sin considerar el espacio ambiente en que vive la cuerda.
- Gravedad implementada como potencial 1/r (apropiado en 3D, pero arbitrario en 1D).
- No hay conservación de energía (la disipación es ad hoc).
- La "información" es una palabra; no hay qubits reales.
- No hay conexión rigurosa con GR ni con teoría cuántica de campos.

**Este modelo sirve para ver si la idea es al menos consistente dinámicamente. Si falla incluso aquí, la hipótesis está en serios problemas.**

## Código de referencia

Ver: `experiments/simulations/sim001_cuerda_basica.js` (equilibrio sin temperatura)
y `experiments/simulations/sim002_cuerda_termica.js` (con temperatura, ruptura, reconexión, evaporación)

## Historial
- 2026-04-15: documentado a partir de esbozo previo.
