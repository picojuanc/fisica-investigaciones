# D-005: D_tiempo = 1 se sigue de la descomposición autodual + D_espacio = 3

- **ID:** D-005
- **Fecha:** 2026-04-19 (sesión 10)
- **Hipótesis asociadas:** H-002 (D_espacio = 3), H-003 (SU(2)_L de Ashtekar)
- **Depende de:** K-019 (conexión autodual = su(2)_L), D-004 Parte III, H-002
- **Resuelve:** Q-024 (¿por qué D_tiempo = 1?)

## Objetivo

Derivar que el espacio-tiempo tiene exactamente 1 dimensión temporal, completando la historia dimensional:
- D-002: objetos fundamentales son 1D (D_objeto = 1)
- H-002: espacio tiene 3 dimensiones (D_espacio = 3)
- **D-005: tiempo tiene 1 dimensión (D_tiempo = 1)**

## Resultado

> **La dimensión temporal D_tiempo = 1 se sigue de la combinación de H-002 (D_espacio = 3) con el requisito de que el álgebra de Lorentz admita una descomposición quiral (autodual/anti-autodual), como la requiere D-004 para derivar SU(2)_L.**

Cuatro argumentos convergentes, dos algebraicos (internos a la teoría) y dos físicos.

---

## Argumento A — Factorización del álgebra de Lorentz (ALGEBRAICO)

### Premisas

1. **D-004 + K-019:** la teoría SCG requiere la conexión autodual de Ashtekar, que vive en sl(2,C)_L — la mitad autodual del álgebra de Lorentz complexificada.
2. **Esto requiere** que el álgebra so(D_espacio, D_tiempo) complexificada se factorice como producto de dos álgebras simples:
   ```
   so(D_espacio, D_tiempo)_C  ≅  g_L × g_R
   ```
3. **H-002:** D_espacio = 3.

### Hecho matemático (clasificación de Dynkin)

Entre todas las álgebras so(n, C) con n ≥ 3:

| n | so(n,C) | Tipo Dynkin | ¿Factoriza? |
|---|---|---|---|
| 3 | sl(2,C) | A₁ = B₁ | No (simple) |
| **4** | **sl(2,C) × sl(2,C)** | **D₂ = A₁ + A₁** | **SÍ — ÚNICA** |
| 5 | sp(4,C) | B₂ = C₂ | No (simple) |
| 6 | sl(4,C) | D₃ = A₃ | No (simple) |
| ≥ 7 | — | B_k o D_k | No (simple) |

**so(4,C) es la ÚNICA álgebra ortogonal que se descompone como producto de álgebras simples.** Esto es un hecho de la clasificación de Dynkin: el diagrama D₂ consiste en dos vértices desconectados (A₁ + A₁), mientras que para todo n ≥ 5, D_k y B_k son diagramas conexos.

### Derivación

```
D-004/K-019: se requiere so(p, q)_C ≅ g_L × g_R
    ↓
Clasificación de Dynkin: so(n)_C factoriza ⟺ n = 4
    ↓
p + q = 4
    ↓
H-002: p = D_espacio = 3
    ↓
q = D_tiempo = 4 − 3 = 1    ∎
```

### Nivel de confianza

- La clasificación de Dynkin es un **teorema** (matemáticas puras, no depende de física).
- D_espacio = 3 es **derivado** (H-002).
- El requisito de la conexión autodual depende de K-019, que es **fuertemente motivado**.
- **Resultado: D_tiempo = 1 es FUERTEMENTE MOTIVADO.**

---

## Argumento B — Signatura del operador de Hodge (ALGEBRAICO)

### Premisas

1. La conexión autodual de Ashtekar requiere eigenvalores **imaginarios** (±i) del operador de Hodge ★ actuando sobre 2-formas.
2. Es la complexificación (eigenvalores ±i, no ±1) lo que produce la **distinción física** entre L y R — la quiralidad.

### Cálculo

El operador de Hodge actuando sobre k-formas en dimensión n con signatura (p, q) satisface:

```
★² = (-1)^{k(n-k) + q}
```

Para 2-formas (k = 2) en dimensión total 4 (n = 4):

```
★² = (-1)^{2·2 + q} = (-1)^{4 + q} = (-1)^q
```

- Si q es **par** (signaturas (4,0) o (2,2)): ★² = +1. Eigenvalores ±1 reales. La descomposición autodual/anti-autodual es **real**. Los sectores L y R son independientes o equivalentes → sin quiralidad física obligatoria.
- Si q es **impar** (signaturas (3,1) o (1,3)): ★² = −1. Eigenvalores ±i imaginarios. La descomposición **requiere complexificación**. Los sectores L y R están ligados por conjugación compleja → la quiralidad es **intrínseca e irreducible**.

### Eliminación de q = 3

q = 3 daría una signatura (1,3) con ★² = −1 ✓ (eigenvalores complejos). Sin embargo:
- q ≥ 2 produce PDEs ultrahiperbólicas → problema de Cauchy mal planteado (teorema de Asgeirsson; Tegmark 1997, CQG 14, L69).
- Las partículas se vuelven inestables (las leyes de conservación son insuficientes para prevenir decaimientos).
- q = 3 está descartado por la física.

### Resultado

```
Quiralidad intrínseca (K-019)
    → ★² = −1 en 2-formas
    → q impar
    → q = 1   (q = 3 descartado por well-posedness)
    → D_tiempo = 1    ∎
```

---

## Argumento C — Selección de signatura (3,1) (FÍSICO)

Los tres candidatos con p + q = 4 y p = 3 son:

| Signatura | q | Álgebra real | Espinores | ¿Viable? |
|---|---|---|---|---|
| (4,0) | 0 | su(2) × su(2) | Cuaterniónicos, L ≡ R | **No** — sin dinámica temporal |
| **(3,1)** | **1** | **sl(2,C) como álgebra real** | **Weyl complejos, L ↔ R por conjugación** | **SÍ** |
| (2,2) | 2 | sl(2,R) × sl(2,R) | Majorana-Weyl reales, L y R independientes | **No** — PDEs ultrahiperbólicas, L y R desacoplados |

Solo en **(3,1):**
- Los espinores de Weyl L y R son **complejos conjugados** el uno del otro.
- Un fermión L **determina** su conjugado R (y viceversa).
- La fuerza débil puede acoplarse **solo a L** sin inconsistencia algebraica.
- Esto reproduce la estructura electrodébil del SM (K-019).

En (4,0): L y R son cuaterniónicamente equivalentes → no se pueden distinguir → sin quiralidad.
En (2,2): L y R son reales e independientes (Majorana-Weyl) → la física sería radicalmente distinta del SM.

---

## Argumento D — Evolución de la red SCG (SCG-ESPECÍFICO)

La red de cuerdas SCG es una estructura **espacial** que evoluciona. La formulación hamiltoniana de GR (ADM) requiere una foliación del espacio-tiempo en hipersuperficies espaciales Σ_t parametrizadas por un tiempo t.

- **D_tiempo = 1:** la foliación Σ_t es una familia 1-paramétrica → dinámica hamiltoniana bien definida → la red SCG tiene un estado en cada instante t.
- **D_tiempo = 0:** sin evolución. Universo estático.
- **D_tiempo ≥ 2:** no existe foliación canónica por hipersuperficies "puramente espaciales" de codimensión 1 (toda hipersuperficie contiene direcciones temporales). La formulación hamiltoniana colapsa → no hay "estado de la red en el instante t" → la dinámica de la red SCG está indefinida.

---

## Síntesis: cuatro argumentos convergentes

| Argumento | Tipo | Ruta | Nivel |
|---|---|---|---|
| **A** — Dynkin (so(4) única) | Algebraico | K-019 + Dynkin + H-002 → q = 1 | Teorema + fuert. motivado |
| **B** — Hodge (★² = −1) | Algebraico | K-019 + Hodge + Tegmark → q = 1 | Teorema + fuert. motivado |
| **C** — Signatura (3,1) | Físico | Quiralidad + espinores → (3,1) única | Fuert. motivado |
| **D** — Evolución de red SCG | SCG-específico | Red necesita foliación → q = 1 | Argumentado |

Los argumentos A y B son **independientes entre sí** (Dynkin no usa Hodge, y viceversa). Ambos producen el mismo resultado.

---

## Consecuencia: la dimensionalidad completa del espacio-tiempo se explica

| Dimensionalidad | Resultado | Derivación | Nivel |
|---|---|---|---|
| D_objeto = 1 | Objetos fundamentales son cuerdas | D-002 (balance de exponentes) | Derivado |
| D_espacio = 3 | Espacio tiene 3 dimensiones | H-002 (codimensión 2 para nudos) | Derivado |
| **D_tiempo = 1** | **Tiempo tiene 1 dimensión** | **D-005 (factorización + quiralidad)** | **Fuertemente motivado** |
| **Total: 3+1** | **Espacio-tiempo es (3,1)** | Combinación de los tres | |

La cadena causal completa:

```
A-003 (presión de degeneración Planckiana)
    → D-002: D_objeto = 1 (balance de exponentes)
    → H-002: D_espacio = 1 + 2 = 3 (codimensión 2)
    → D-004/K-019: se requiere conexión autodual
    → D-005: D_espacio + D_tiempo = 4 (Dynkin) → D_tiempo = 1
```

**Todo desde QM + GR.**

---

## Nuevo insight

### K-022 — D_espacio + D_tiempo = 4 es la única dimensionalidad total con factorización quiral

La dimensionalidad total del espacio-tiempo no es un parámetro libre: p + q = 4 es la ÚNICA dimensionalidad donde el álgebra de Lorentz so(p,q) complexificada se factoriza como producto (Dynkin: D₂ = A₁ + A₁). Esta factorización es necesaria para la descomposición autodual/anti-autodual que da la quiralidad (K-019) y SU(2)_L (D-004). Combinada con D_espacio = 3 (H-002), fuerza D_tiempo = 1.

**Resultado:** la signatura completa (3,1) del espacio-tiempo se explica desde el interior de la teoría.

---

## Limitaciones

1. **Dependencia de K-019:** si SU(2)_L no viene de Ashtekar sino de otro mecanismo, el argumento A pierde su premisa principal. Sin embargo, los argumentos C (espinores) y D (evolución de red) son parcialmente independientes.

2. **El argumento B usa Tegmark** para descartar q = 3. Tegmark es un argumento de well-posedness/antrópico, no derivativo. Pero el teorema de Asgeirsson (que lo respalda) es riguroso, y Craig-Weinstein (2009) solo lo debilitan con restricciones no-locales exóticas.

3. **No explica por qué la naturaleza "elige" D_tiempo = 1** en un sentido dinámico (como D-002 explica D_objeto = 1 por minimización de energía). El argumento es de consistencia algebraica, no de selección dinámica.

4. **El argumento asume que el espacio-tiempo tiene una signatura definida.** Si la signatura es dinámica o emergente, el argumento necesita reformulación.

## Historial

- 2026-04-19 (sesión 10): derivación.
