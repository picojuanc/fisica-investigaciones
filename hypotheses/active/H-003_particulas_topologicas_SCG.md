# H-003: Las partículas del Modelo Estándar son excitaciones topológicas de la red SCG

- **ID:** H-003
- **Fecha de propuesta:** 2026-04-18 (sesión 10; material acumulado en sesiones 7–9)
- **Estado:** activa
- **Estado derivacional (actualizado v1.9, sesión 24):** U(1) derivado; Z₃ derivado; **SU(2)_L reinterpretado como edge mode quiral de frontera WW modular** (ya no importado literalmente de Ashtekar autodual; ver nota v1.9 abajo); SU(3) argumentado por 5 vías; generaciones propuesto; Higgs mecanismo establecido. Asimetría máxima del SM: emerge de Kaplan 2024 + Wang-Wen 2018-2019 + modular Walker-Wang (Q-042, veredicto (D); Q-043 pendiente).
- **Depende de:** H-001 v1.2 (objetos 1D), H-002 (D=3), A-003 (presión de degeneración), D-004 (reglas de fusión), **UBFC modular WW compatible con SO(10) (Q-043, pendiente)**.
- **Contradice a:** — (extiende H-001 y H-002 al sector de materia)

---

## ⚠ Nota de reinterpretación v1.9 (sesión 24, post-Q-042)

**Los detalles de este documento reflejan el estado pre-v1.9 (sesión 10). La reinterpretación de K-019 y degradación de K-026 en la sesión 24 cambian el mecanismo físico subyacente de la quiralidad SU(2)_L sin cambiar el contenido empírico.**

**Lo que cambió:**
- **Quiralidad SU(2)_L: topológica, no gravitacional.** La conexión autodual de Ashtekar con β = -i ya no es el origen literal de la quiralidad. En su lugar, SU(2)_L emerge como edge mode quiral de la frontera de una red Walker-Wang modular en 3+1D, vía mecanismo Kaplan 2024 (PRL 132 141603) + Wang-Wen 2018-2019 (arXiv:1809.11171).
- **Sector gravitacional (Ashtekar-Barbero-Immirzi con β real, Randono 2006):** sigue valiendo, pero es sector puramente gravitacional sin quiralidad fenomenológica directa.
- **K-026 degradada:** la dicotomía "gravedad quiral / red no-quiral por Nielsen-Ninomiya" ya no se sostiene — la red WW modular *puede* ser quiral en su frontera.

**Lo que NO cambió:**
- SU(2)_L sigue siendo el único factor gauge quiral del SM.
- Los fermiones L siguen siendo los únicos que acoplan.
- La fenomenología observacional (violación P, masas W/Z, confinamiento electrodébil via Higgs-Fradkin-Shenker) se preserva.
- El grupo gauge completo SU(3) × SU(2) × U(1) sigue derivado de la red SCG.
- Las secciones "U(1) desde modos transversales" y "Z₃ desde trivalencia" siguen válidas sin cambio.

**Pendiente (Q-043, prioridad alta):** construir UBFC modular específica para SCG con contenido SO(10) que cancele anomalías y produzca asimetría SM máxima. Si Q-043 cierra constructivamente, K-030 → confirmado limpio, P-11 → ✅ resuelto.

**Ver:** `notes/Q-042_mecanismo_amplificacion_P.md`, `journal/2026-04-21_snapshot_v1.9.md`, `journal/reportes/24_la_quiralidad_es_topologica.md`.

---

## Enunciado

> **Las partículas del Modelo Estándar — quarks, leptones, bosones gauge — son excitaciones topológicas (anyones y defectos) de la red de cuerdas SCG en D=3. El grupo gauge SU(3)×SU(2)×U(1) emerge de las reglas de fusión de los vértices trivalentes de la red. El mecanismo de Higgs es la condensación de un anyón bosónico que confina la parte SU(2)_L de la gravedad.**

Forma compacta:

```
Red SCG (H-001) + D=3 (H-002)
    → defectos topológicos estables (consecuencia matemática)
    → reglas de fusión de vértices trivalentes (D-004)
    → grupo gauge emergente: SU(3) × SU(2) × U(1)
    → partículas = anyones de la TQFT efectiva
```

## Motivación

H-001 establece que el espacio-tiempo a escala Planck es una red de cuerdas gravitacionales 1D. H-002 establece que esa red vive en D=3. Pero ni H-001 ni H-002 dicen qué son las partículas.

H-003 cierra ese hueco: las partículas no son entidades adicionales que "viven en" el espacio-tiempo — **son deformaciones del propio espacio-tiempo**. Son defectos topológicos de la red SCG: nudos, enlaces, violaciones locales de las reglas de fusión. Existen porque la red tiene estructura topológica en D=3.

Esto no es un postulado exótico. Es la consecuencia directa de tres mecanismos demostrados:
1. Toda red ordenada tiene excitaciones topológicas (física de la materia condensada).
2. En D=3, los objetos 1D forman nudos estables (topología).
3. Las redes de cuerdas con reglas de fusión producen campos gauge + fermiones emergentes (Levin-Wen 2005).

## Cadena lógica: de la red SCG a las partículas

### Los 6 eslabones

```
[1] Objetos fundamentales 1D (H-001, D-002)
     │  derivado: balance de exponentes gravedad/degeneración
     ↓
[2] Espacio D=3 (H-002)
     │  derivado: codimensión 2 para nudos, hecho matemático
     ↓
[3] Defectos topológicos estables (nudos, enlaces)
     │  consecuencia matemática: toda red en D=3 con objetos 1D los tiene
     ↓
[4] Red de cuerdas 3D → campos gauge + fermiones emergentes
     │  demostrado: Wen (2003, PRD 68 065003) — modelo de red con
     │  U(1)×SU(2)×SU(3) emergente en 3+1D, constructivo.
     │  Levin-Wen (2005, PRB 71 045110) — "3D string-net condensation
     │  naturally gives rise to both emergent gauge bosons and emergent fermions."
     │  Walker-Wang (2011) — framework sistemático para fases topológicas 3+1D.
     ↓
[5] Teoría topológica efectiva: Crane-Yetter (4D TQFT)
     │  Crane-Yetter (1993): TQFT 4D cuya formulación hamiltoniana es Walker-Wang.
     │  Motivada originalmente por las variables de Ashtekar en gravedad cuántica.
     │  Teoría de frontera (3D) = Chern-Simons (Witten 1988).
     ↓
[6] Reglas de fusión → grupo gauge concreto
     │  D-004: U(1) derivado, Z₃ derivado, SU(2) fuertemente motivado, SU(3) argumentado
     ↓
RESULTADO: SU(3) × SU(2) × U(1)
```

**Eslabones 1–3:** sólidos (derivaciones, teoremas).
**Eslabones 4–5:** sólidos (demostrados constructivamente en 3+1D). Corrección sesión 11: refs. actualizadas de Levin-Wen 2+1D a Wen 3+1D + Walker-Wang + Crane-Yetter.
**Eslabón 6:** parcialmente derivado (D-004). Es el corazón cuantitativo de H-003.

**Nota sobre dimensionalidad (sesión 11):** la versión original de esta cadena citaba Levin-Wen (2+1D) y Chern-Simons (3D TQFT). El stress-test de sesión 11 identificó la incompatibilidad dimensional (P-10). La corrección: en 3+1D, el mecanismo constructivo es Wen (2003)/Walker-Wang (2011), y la TQFT efectiva es Crane-Yetter (4D), cuya teoría de frontera es CS. Los resultados sobre grupo gauge se transfieren porque las reglas de fusión (D-004) son propiedades de la red independientes de la dimensionalidad del espacio-tiempo. Las excitaciones en 3+1D son bosones y fermiones convencionales (no anyones; los anyones existen solo en fronteras/defectos 2D).

**Nota sobre quiralidad (K-026, sesión 11):** el patrón quiral del SM (SU(2) quiral, SU(3) y U(1) no-quirales) coincide con el patrón de origen en SCG: SU(2)_L viene de la gravedad (Ashtekar autodual, inherentemente quiral), mientras que U(1) y SU(3) emergen de la red (inherentemente no-quiral por Nielsen-Ninomiya).

### Niveles de confianza por eslabón

| Eslabón | Contenido | Nivel |
|---|---|---|
| 1 | Objetos 1D | **Derivado** (D-002) |
| 2 | D=3 | **Derivado** (H-002, topología) |
| 3 | Defectos estables | **Teorema** |
| 4 | Gauge + fermiones de string-net 3D | **Demostrado** (Wen 2003 PRD; Levin-Wen 2005 PRB; Walker-Wang 2011) |
| 5 | TQFT 4D = Crane-Yetter (frontera = CS) | **Demostrado** (Crane-Yetter 1993; motivado por Ashtekar) |
| 6a | U(1)_Y | **Derivado** (D-004 Parte I) |
| 6b | Z₃ → carga en 1/3 | **Derivado** (D-004 Parte II) |
| 6c | SU(2)_L | **Fuertemente motivado** (D-004 Parte III + stress-test K-019) |
| 6d | SU(3) | **Argumentado** (D-004 Parte V, 5 vías convergentes) |

---

## Derivación del grupo gauge (resumen de D-004)

Referencia completa: `logic/derivations/D-004_reglas_fusion_vertices_SCG.md`

### U(1) — de los modos transversales (DERIVADO)

Una cuerda 1D en D=3 tiene 2 modos transversales con simetría SO(2) ≅ U(1). El momento angular transversal m ∈ ℤ es una carga interna conservada. En vértices trivalentes: m₁ + m₂ + m₃ = 0 (fusión aditiva). Por Levin-Wen → campo gauge U(1) emergente con fotón sin masa.

**Identificación:** probablemente U(1)_Y (hipercarga), no U(1)_EM. El stress-test (sesión 9) muestra que la cuantización en 1/3 coincide con la estructura de hipercarga del SM, pero la identificación no es definitiva.

### Z₃ — de la trivalencia del vértice (DERIVADO)

En el vértice trivalente equiespaciado, SO(2) se rompe a Z₃ (simetría cíclica de 120°). El momento angular se clasifica mod 3:

```
m ≡ 0 (mod 3) → trialidad 0 → leptones
m ≡ 1 (mod 3) → trialidad 1 → quarks
m ≡ 2 (mod 3) → trialidad 2 → antiquarks
```

Z₃ es el centro de SU(3). La cuantización de la carga eléctrica en unidades de 1/3 — un dato sin explicación en el SM — se deriva de D=3 → trivalencia.

### SU(2)_L — de la conexión gravitacional (FUERTEMENTE MOTIVADO)

La conexión autodual de Ashtekar (1986) es literalmente su(2)_L del grupo de Lorentz:

```
so(3,1)_C ≅ su(2)_L × su(2)_R
Conexión de Ashtekar = su(2)_L
```

Los fermiones levógiros se acoplan a ella, los dextrógiros a su(2)_R. La quiralidad de la fuerza débil no se postula — es una identidad matemática del grupo de Lorentz (Alexander-Marciano-Smolin, PRD 89, 065017, 2012).

Cada segmento de la red porta la holonomía g_e = P exp(∫_e A) ∈ SU(2). Las reglas de fusión son las de Clebsch-Gordan. Por Levin-Wen → campo gauge SU(2) emergente.

**Nota importante:** SU(2) no se deriva de A-003 directamente — se **importa** de la formulación de Ashtekar de GR. Esto es legítimo (GR es un input del marco) pero hace que SU(2) sea el factor con peor derivación interna.

**Decisión forzada:** el marco SCG debe usar la conexión autodual (compleja), no la de Barbero-Immirzi. La formulación real pierde la quiralidad. **Costo:** la conexión compleja presenta problemas técnicos (normalización del estado de Kodama, condiciones de realidad — Witten 2003). Estos problemas no están resueltos en LQG ni en nuestro marco.

### SU(3) — de Z₃ + quiralidad (ARGUMENTADO)

Solo existen 2 órdenes topológicos quirales con fusión Z₃: SU(3)₁ y su conjugado temporal. La quiralidad de la red SCG (del CS gravitacional de Ashtekar) selecciona SU(3)₁ unívocamente.

A bajas energías, k_eff crece por integración de modos masivos (mecanismo QFT estándar de level-shifting, Δk = ±½ por fermión de Dirac) → SU(3) perturbativo (QCD). **Nota:** el level-shifting es un mecanismo establecido en CS general, pero su aplicación cuantitativa a la red SCG (qué modos contribuyen, con qué coeficiente) no está calculada.

Cinco argumentos convergentes: (1) unicidad matemática, (2) parsimonia (K-005), (3) level-shifting estándar, (4) confinamiento = Z₃ preservada (lattice QCD), (5) anomalías (sugerente).

### Origen geométrico unificado

```
Red SCG en D=3
    ├── Segmentos (edges): 2 modos transversales → U(1)_Y
    ├── Vértices trivalentes: SO(2) → Z₃ → centro de SU(3)
    ├── Vértices + quiralidad: Z₃ quiral → SU(3)₁ por unicidad
    └── Holonomías de la conexión autodual → SU(2)_L
```

Cada factor gauge tiene un origen geométrico **distinto** en la misma red.

---

## Consecuencias lógicas

### C1. Cuantización de la carga en 1/3

La carga eléctrica cuantizada en tercios no es un postulado — es una consecuencia de la trivalencia de los vértices en D=3 (K-015). La cadena causal: D=3 → vértices trivalentes genéricos → Z₃ → cargas en 1/3.

### C2. Confinamiento de color

El confinamiento = preservación de la simetría Z₃ del centro de SU(3) (parámetro de orden: lazo de Polyakov ⟨L⟩ = 0). En el marco SCG, Z₃ tiene origen geométrico UV (trivalencia del vértice). Los quarks (trialidad ≠ 0) no pueden existir aislados porque la geometría del vértice impone m₁ + m₂ + m₃ ≡ 0 (mod 3). Solo estados con trialidad total 0 se propagan libremente (K-018).

### C3. Violación de paridad

La acción de Chern-Simons cambia de signo bajo paridad (S_CS → −S_CS). La red SCG con conexión autodual tiene descripción efectiva CS quiral → viola paridad automáticamente (K-013, K-019).

La violación es además **máxima** para SU(2)_L: solo los fermiones levógiros se acoplan a la conexión autodual. No se postula — se hereda de la estructura de representaciones del grupo de Lorentz.

### C4. Tres generaciones (PROPUESTO, especulativo)

La red SCG trivalente tiene un grafo dual triangulado. Las caras triangulares del dual tienen simetría Z₃ independiente de la Z₃ del vértice primal:

```
Z₃_primal (vértice)  → 3 colores (trialidad de SU(3))
Z₃_dual   (cara)     → 3 generaciones (familia de fermiones)
```

N_gen = N_color = 3 porque ambas Z₃ vienen de la misma trivalencia (K-020).

Los 3 modos rotacionales del triángulo dual tienen energías distintas → jerarquía de masas (1ª < 2ª < 3ª generación). Pero los ratios cuantitativos (m_e : m_μ : m_τ) **no se predicen**.

**Nivel de confianza: BAJO-MEDIO.** La estructura Z₃ × Z₃ es natural pero la conexión con la cara dual necesita formalización seria.

### C5. Mecanismo de Higgs = condensación de anyones (MECANISMO ESTABLECIDO)

Bais-Slingerland (2009) demuestran que en modelos Levin-Wen, la condensación de un anyón bosónico reduce el grupo gauge. Aplicado a SCG:

1. Un anyón con (j = ½, Y = 1) — el doblete de Higgs topológico — condensa a E ~ 246 GeV.
2. SU(2)_L × U(1)_Y → U(1)_EM.
3. Los W y Z adquieren masa (gap topológico del condensado).

Por el teorema de Fradkin-Shenker (1979): fase de Higgs = fase de confinamiento para SU(2) fundamental. La "ruptura" electrodébil no es una ruptura — es confinamiento de la gravedad SU(2)_L (K-021).

```
v ~ M_Planck · exp(−c · k₂)    (análogo BCS)
```

Dimensionalmente plausible con k₂ ~ 50, c ~ 0.8. Pero v = 246 GeV **no se predice** sin conocer c y k₂. La fórmula Q = T₃ + Y/2 emerge como la combinación no rota, pero su derivación desde primeros principios SCG es una pregunta abierta (Q-028).

**Nivel de confianza de C5:** MEDIO-ALTO para la estructura del mecanismo (condensación de anyones, Bais-Slingerland demostrado). BAJO para los valores numéricos (v, masas de W/Z, Yukawas).

### C6. Las partículas no son entidades separadas del espacio-tiempo

A diferencia del SM (donde las partículas "viven en" el espacio-tiempo como campos independientes), en H-003 las partículas **son el espacio-tiempo** localmente deformado. Es la misma ontología: cuerdas SCG. Una partícula es una región donde la red tiene un defecto topológico. Vacío = red ordenada. Partícula = red desordenada localmente.

Esto evita el problema de Kelvin (1867): no hay "éter" sobre el cual viven los nudos. Las cuerdas SON el tejido, y los defectos son auto-referenciales.

---

## Predicciones

### Predicciones derivadas (alto nivel de confianza)

| # | Predicción | Origen |
|---|---|---|
| P.6 | Grupo gauge = SU(3)×SU(2)×U(1) | D-004 |
| P.7 | Carga cuantizada en 1/3 | Z₃ de trivalencia |
| P.8 | Confinamiento de color = Z₃ preservada | Trivalencia UV |
| P.9 | Violación máxima de paridad en SU(2)_L | Ashtekar autodual |

### Predicciones propuestas (nivel de confianza medio)

| # | Predicción | Origen |
|---|---|---|
| P.10 | 3 generaciones = Z₃ del grafo dual | Dualidad primal-dual |
| P.11 | Higgs = condensación de anyón (j=½, Y=1) | Bais-Slingerland |
| P.12 | v ~ M_P · exp(−c·k₂) (fórmula tipo BCS) | Analogía con superconductividad |
| P.13 | A escala Planck, solo 3 anyones (k=1) → sin gluones propagantes | SU(3)₁ |

### Predicciones que NO se hacen (aún)

- Masas de fermiones
- Ángulo de Weinberg (θ_W)
- Constantes de acoplamiento (α_s, α_W, α_Y)
- v = 246 GeV
- Matrices CKM/PMNS (cuantitativamente)
- Masa del Higgs (m_H = 125 GeV)

---

## Relación con la literatura

| Programa | Relación con H-003 |
|---|---|
| **Levin-Wen (2005)** | H-003 es una realización física del marco Levin-Wen. Diferencia: las reglas de fusión se derivan (D-004), no se postulan |
| **Chern-Simons/Witten (1988)** | Teoría efectiva de la red SCG en 3D |
| **Bilson-Thompson (2005)** | Los "3 ribbons" se motivan por D=3 → trivalencia. H-003 da origen físico a las trenzas |
| **Alexander-Marciano-Smolin (2012)** | Proponen SU(2)_gravedad = SU(2)_L. H-003 lo incorpora como identidad, no analogía |
| **Bais-Slingerland (2009)** | Condensación de anyones = mecanismo de Higgs. H-003 lo aplica a la red SCG |
| **Fradkin-Shenker (1979)** | Higgs = confinamiento para SU(2) fundamental. Consecuencia directa en H-003 |
| **LQG (redes de espín)** | H-003 usa la misma estructura (SU(2) en edges, intertwiners en vértices). Diferencia: H-003 usa Ashtekar autodual (compleja), no Barbero-Immirzi |
| **Kelvin (1867)** | Misma visión (nudos = partículas), pero sin éter: las cuerdas SON el espacio-tiempo |
| **Finkelstein (SLq(2))** | Cuantización de cargas desde grupos cuánticos. Conexión posible pero no explorada |

---

## Experimentos mentales asociados

- [E-008: Nudos como partículas — cadena SCG → Levin-Wen → CS](../../experiments/thought_experiments/E-008_nudos_como_particulas.md) — establece la cadena de 6 eslabones.
- [E-009: Tres generaciones y mecanismo de Higgs](../../experiments/thought_experiments/E-009_generaciones_y_higgs.md) — propuesta de Z₃ dual y condensación de anyones.

## Derivaciones asociadas

- [D-004: Reglas de fusión en vértices trivalentes](../../logic/derivations/D-004_reglas_fusion_vertices_SCG.md) — derivación del grupo gauge.
- [Stress-test de D-004](../../logic/stress_test_D-004.md) — los 5 eslabones pasan.

## Análisis de soporte

- `notes/Q-023_analisis_nudos_particulas.md` — análisis de la cadena nudos → partículas.
- `notes/Q-025_analisis_reglas_fusion.md` — análisis de reglas de fusión.
- `notes/Q-026_analisis_Z3_a_SU3.md` — resolución conceptual de Z₃ → SU(3).

---

## Problemas abiertos

### Problemas derivacionales (cómo completar lo que falta)

1. **Acción Lagrangiana de la red SCG (P-8).** Sin ella, no se pueden calcular amplitudes de scattering ni masas. Es el paso de "marco conceptual" a "teoría predictiva".

2. **Niveles de Chern-Simons k para cada factor gauge (Q-027).** k determina qué representaciones existen (truncación). A k=1 solo hay 3 anyones → espectro mínimo. A k grande → espectro del SM completo. El flujo k(E) no está calculado.

3. **Constantes de acoplamiento.** Si SU(2)_L es gravedad, G_Newton y g_weak deben converger a M_Planck. El flujo de renormalización que los separa no está derivado.

4. **Masas de fermiones.** El mecanismo de generación de masa (Yukawa) no está derivado. Los acoplamientos de Yukawa dependen de la geometría detallada de la red, que no conocemos.

5. **Ángulo de Weinberg θ_W.** Requiere la relación entre los acoplamientos g y g' de SU(2)_L y U(1)_Y. En principio derivable si se conoce la estructura de la red, pero no calculado.

### Problemas conceptuales (qué no entendemos bien)

6. **Z₃ dual → generaciones.** La conexión entre la cara del grafo dual y los modos de generación necesita formalización. ¿La Z₃ dual se conserva realmente como número cuántico? ¿Cómo se acopla a los otros sectores?

7. **Red SCG densa (BH) vs red SCG diluida (vacío).** H-001 describe el interior de un BH como red densa. H-003 describe el vacío como red ordenada. ¿Cómo se conectan las dos fases? ¿Hay una transición de fase?

8. **Fermiones emergentes vs fundamentales.** En Levin-Wen, los fermiones emergen como compuestos de excitaciones topológicas (diones = carga + flujo). ¿Son los fermiones del SM compuestos en este sentido?

9. **Espectro bosónico.** Los bosones gauge (γ, W±, Z, gluones) deben emerger como excitaciones colectivas de la red. El mecanismo para el fotón (sin masa, U(1)_EM) vs W/Z (masivos, SU(2)_L confinado) requiere la condensación de anyones. ¿Es consistente con todos los datos del SM?

10. **D_tiempo = 1.** H-002 explica D_espacio = 3 pero no D_tiempo = 1. H-003 hereda este problema.

---

## Lo que H-003 logra y lo que no

### Logra (por primera vez, desde QM + GR solamente)

- Deriva por qué el grupo gauge tiene 3 factores (3 aspectos geométricos distintos de la red)
- Deriva por qué la carga se cuantiza en 1/3 (trivalencia → Z₃)
- Explica el confinamiento como geometría UV (K-018)
- Explica la violación de paridad como identidad matemática (K-019)
- Identifica un mecanismo de Higgs (condensación de anyones, demostrado en materia condensada)
- Propone una explicación para N_gen = 3 = N_color (Z₃ × Z₃ de la dualidad)

### No logra (aún)

- Predecir valores numéricos de constantes del SM
- Derivar las masas de las partículas
- Construir una acción Lagrangiana
- Demostrar que la red SCG reproduce TODAS las predicciones del SM
- Explicar la dimensión temporal

### Honestidad epistémica

H-003 es una **hipótesis con soporte estructural**, no una teoría cerrada. La cadena de 6 eslabones es internamente consistente y cada paso usa mecanismos demostrados en otros contextos. Pero:

- Algunos eslabones son "derivados" y otros son "argumentados" o "propuestos".
- Las predicciones cuantitativas son escasas.
- La consistencia fenomenológica completa con el SM no está verificada.
- El eslabón más débil es la propuesta de generaciones (C4).
- El eslabón más fuerte es la cuantización de la carga (C1) y el confinamiento (C2).

---

## Historial

- **2026-04-16 (sesión 7):** primera mención de partículas topológicas como C5 de H-002.
- **2026-04-17 (sesión 8):** E-008 establece la cadena de 6 eslabones. D-004 deriva parcialmente el grupo gauge. Q-026 resuelta conceptualmente (SU(3)).
- **2026-04-18 (sesión 9):** stress-test de D-004 (todos los eslabones pasan, SU(2) upgradeado). E-009: propuesta de generaciones (Z₃ dual) y Higgs (condensación de anyones). K-019 a K-021.
- **2026-04-18 (sesión 10):** formalización como hipótesis independiente H-003.
