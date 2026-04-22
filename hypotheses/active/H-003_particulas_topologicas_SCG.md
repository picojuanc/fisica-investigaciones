# H-003: Las partículas del Modelo Estándar son excitaciones topológicas de la red SCG

- **ID:** H-003
- **Fecha de propuesta:** 2026-04-18 (sesión 10; material acumulado en sesiones 7–9)
- **Estado:** activa
- **Estado derivacional (actualizado v2.0, sesión 30):** U(1) derivado; Z₃ derivado; **SU(2)_L como edge mode quiral de frontera WW modular** (v1.9, consolidado v2.0 via D-010); SU(3) argumentado por 5 vías + refuerzo Z₃_geom ≡ centro SU(3) (K-017 v2.0); generaciones propuesto; Higgs mecanismo establecido. **Asimetría máxima del SM: emerge de Kaplan 2024 + Wang-Wen 2018-2019 + modular Walker-Wang sobre `Spin(10)_1` (Q-043 CERRADA estructuralmente, D-010, sesión 30).**
- **Depende de:** H-001 v1.2 (objetos 1D), H-002 (D=3), A-003 (presión de degeneración), D-004 (reglas de fusión), **UBFC modular `Spin(10)_1` (Q-043 cerrada estructuralmente, D-010)**.
- **Contradice a:** — (extiende H-001 y H-002 al sector de materia)

---

## ✅ Nota de cierre v2.0 (sesión 30, post-Q-043)

**Q-043 CERRADA ESTRUCTURALMENTE (sesión 30). UBFC específica identificada: `Spin(10)_1` MTC (+ super-modular extension estándar para contenido fermiónico).**

- Las 4 obstrucciones bloqueantes (O1, O2, O5, O6) cerraron positivamente en sesiones 27-29.
- Chequeo de consistencia cruzada en sesión 30 verifica coherencia interna.
- D-010 documenta la síntesis formal.
- K-030 **promovido a "confirmado estructuralmente"**.
- P-11 (el fantasma existencial desde sesión 11) **rebajado a ✅ resuelto estructuralmente**.
- K-033 activado a candidato formal (SO(10)-GUT en SCG); K-034 promovido a candidato formal (doble derivación Q=1/3); K-017 refuerzo documentado.
- Caveats honestos: argumentos estructurales (no constructivos) en 3 de 4 piezas; estándar literatura; construcción constructiva explícita del lattice SM pendiente.
- **Snapshot v2.0** captura el estado consolidado.

**Ver:** `logic/derivations/D-010_Q-043_sintesis.md`, `notes/Q-043_sesion30_evaluacion_global.md`, `journal/2026-04-22_snapshot_v2.0.md`, `journal/reportes/25_cierre_Q-043.md`.

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

**~~Pendiente (Q-043)~~** **✅ CERRADA estructuralmente (sesión 30):** UBFC modular específica identificada como `Spin(10)_1` MTC (+ super-modular extension). K-030 promovido a "confirmado estructuralmente"; P-11 rebajado a ✅ resuelto estructuralmente. Ver D-010.

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

**Nota sobre quiralidad (K-026 — DEGRADADA v1.9, sesión 24):** el patrón cualitativo sigue siendo real (SU(2)_L quiral; SU(3), U(1)_Y no-quirales) y sigue exigiendo explicación. Lo que **ya no se sostiene** es la dicotomía originalmente propuesta — "SU(2)_L es quiral *porque* viene de la gravedad autodual (K-019), mientras que SU(3) y U(1) son no-quirales *porque* vienen de la red (Nielsen-Ninomiya)". El teorema de Nielsen-Ninomiya se aplica a fases de bulk puro; una red Walker-Wang **modular** con frontera topológica **sí puede alojar quiralidad** (Kaplan 2024, Wang-Wen 2018-2019). Interpretación v1.9: SU(3) y U(1)_Y emergen no-quiralmente del bulk WW, mientras que SU(2)_L emerge quiralmente de la estructura de defecto/frontera; pero la asignación quiral vs no-quiral no está dictada por "origen gravitacional vs origen de red" — depende de la UBFC modular específica (Q-043, pendiente).

### Niveles de confianza por eslabón (v1.9)

| Eslabón | Contenido | Nivel |
|---|---|---|
| 1 | Objetos 1D | **Derivado** (D-002) |
| 2 | D=3 | **Derivado** (H-002, topología) |
| 3 | Defectos estables | **Teorema** |
| 4 | Gauge + fermiones de string-net 3D | **Demostrado** (Wen 2003 PRD; Levin-Wen 2005 PRB; Walker-Wang 2011) |
| 5 | TQFT 4D = Crane-Yetter (frontera = CS) | **Demostrado** (Crane-Yetter 1993; motivado por Ashtekar) |
| 6a | U(1)_Y | **Derivado** (D-004 Parte I) |
| 6b | Z₃ → carga en 1/3 | **Derivado** (D-004 Parte II) |
| 6c (v1.9) | SU(2)_L como edge mode quiral de frontera WW modular | **Identificado conceptualmente** (Kaplan 2024 + Wang-Wen 2018-2019 + modular WW 2208.03397); pendiente Q-043 para construcción UBFC específica |
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

### SU(2)_L — edge mode quiral de frontera Walker-Wang modular (REINTERPRETADO v1.9)

> **Historial de interpretaciones** (sesiones 9 → 22 → 24): la identificación de SU(2)_L ha recorrido tres formulaciones sucesivas, cada una más desacoplada del sector gravitacional que la anterior.
> - **(i) Sesión 9 (AMS 2014):** SU(2)_L = conexión autodual de Ashtekar (β = -i) literalmente. Identidad matemática del grupo de Lorentz. Asimetría máxima automática.
> - **(ii) Sesión 22 (Q-040, Randono 2006):** β real preserva violación P cualitativa pero no garantiza asimetría máxima automáticamente.
> - **(iii) Sesión 24 (Q-042):** **la quiralidad de SU(2)_L es topológica, no gravitacional.** Emerge de edge modes quirales en la frontera de una red Walker-Wang modular (Kaplan 2024 + Wang-Wen 2018-2019 + modular WW 2208.03397). **Independiente de β de Ashtekar.**

**Formulación v1.9 — mecanismo topológico.** Una red Walker-Wang 3+1D construida sobre una UBFC **modular** es una fase topológica *invertible* en el bulk (SPT-like). Su frontera (2+1)D hospeda una teoría quiral — edge modes sin *mirror partners* (Kaplan 2024, PRL 132 141603). Los fermiones del Modelo Estándar, que en SCG son defectos topológicos de la red (H-003), actúan localmente como fronteras: el tubo de Gauss alrededor de cada defecto es una "frontera interna" donde emergen estados de borde quirales.

La cancelación de anomalías que permite gapear el sector *mirror* sin romper la simetría on-site es el resultado de Wang-Wen 2018-2019 (arXiv:1809.11171): para Spin(N) con N ≥ 7, el grupo de cobordismo Ω⁵ admite clase invertible trivial. El caso canónico es SO(10)-GUT con 16 fermiones en la representación spinorial — exactamente la cadena de inclusiones SO(10) ⊃ SU(5) ⊃ SU(3) × SU(2)_L × U(1)_Y que ya reproduce el grupo gauge derivado en SCG (D-004).

**Sector gravitacional, sector quiral-SM: desacoplados.** El sector puramente gravitacional usa la conexión Ashtekar-Barbero-Immirzi con **β real** (Randono 2006). Este β real **resuelve** el problema de normalizabilidad de Kodama / realidad de la conexión compleja (antiguo costo forzado de la interpretación literal AMS 2014). Pero **no aporta** la asimetría máxima — no hace falta que lo haga. La asimetría máxima del SM emerge del sector topológico, no del gravitacional.

**Lo que se preserva del K-019 original:**
- SU(2)_L sigue siendo el único factor gauge quiral del SM.
- Los fermiones L siguen siendo los únicos que se acoplan.
- La fenomenología observacional (violación P, masas W/Z, confinamiento electrodébil) no cambia.
- Cada segmento de la red sigue portando holonomía SU(2) (ahora entendida como edge mode, no como proyección de conexión autodual).

**Lo que cambia:**
- SU(2)_L ya no se **importa** de la formulación de Ashtekar de GR.
- La "decisión forzada" de usar conexión autodual compleja **se levanta**. Barbero-Immirzi con β real es la formulación operativa.
- El costo técnico (Kodama no normalizable, condiciones de realidad) **se mitiga** vía Randono 2006.
- El precio conceptual (Q-043 pendiente): construcción explícita de la UBFC modular SCG con contenido SO(10) que cancele anomalías. Si Q-043 cierra constructivamente → K-030 pasa a confirmado limpio, P-11 → ✅ resuelto.

**Ver:** `notes/Q-042_mecanismo_amplificacion_P.md`, `journal/reportes/24_la_quiralidad_es_topologica.md`, `journal/2026-04-21_snapshot_v1.9.md`.

### SU(3) — de Z₃ + quiralidad (ARGUMENTADO)

Solo existen 2 órdenes topológicos quirales con fusión Z₃: SU(3)₁ y su conjugado temporal. La quiralidad de la red SCG (del CS gravitacional de Ashtekar) selecciona SU(3)₁ unívocamente.

A bajas energías, k_eff crece por integración de modos masivos (mecanismo QFT estándar de level-shifting, Δk = ±½ por fermión de Dirac) → SU(3) perturbativo (QCD). **Nota:** el level-shifting es un mecanismo establecido en CS general, pero su aplicación cuantitativa a la red SCG (qué modos contribuyen, con qué coeficiente) no está calculada.

Cinco argumentos convergentes: (1) unicidad matemática, (2) parsimonia (K-005), (3) level-shifting estándar, (4) confinamiento = Z₃ preservada (lattice QCD), (5) anomalías (sugerente).

### Origen geométrico unificado (v1.9)

```
Red SCG en D=3 (Walker-Wang modular sobre UBFC con contenido SO(10))
    ├── Bulk — Segmentos (edges): 2 modos transversales → U(1)_Y [no-quiral]
    ├── Bulk — Vértices trivalentes: SO(2) → Z₃ → centro de SU(3) [no-quiral]
    ├── Bulk — Vértices + matching dim.: Z₃ + valencia 3 → SU(3)₁ [no-quiral]
    └── Frontera/defectos — edge modes quirales (Kaplan 2024) → SU(2)_L [quiral]
```

Cada factor gauge tiene un origen geométrico **distinto** en la misma red. El contraste v1.9 con la versión pre-v1.9 es que **SU(2)_L ya no se deriva del sector gravitacional** (conexión Ashtekar autodual) sino de la estructura topológica de la red Walker-Wang con frontera modular. La quiralidad del SM es un teorema del lattice, no un regalo del Lorentz.

---

## Consecuencias lógicas

### C1. Cuantización de la carga en 1/3

La carga eléctrica cuantizada en tercios no es un postulado — es una consecuencia de la trivalencia de los vértices en D=3 (K-015). La cadena causal: D=3 → vértices trivalentes genéricos → Z₃ → cargas en 1/3.

### C2. Confinamiento de color

El confinamiento = preservación de la simetría Z₃ del centro de SU(3) (parámetro de orden: lazo de Polyakov ⟨L⟩ = 0). En el marco SCG, Z₃ tiene origen geométrico UV (trivalencia del vértice). Los quarks (trialidad ≠ 0) no pueden existir aislados porque la geometría del vértice impone m₁ + m₂ + m₃ ≡ 0 (mod 3). Solo estados con trialidad total 0 se propagan libremente (K-018).

### C3. Violación de paridad (reinterpretada v1.9)

La violación de paridad tiene dos capas en SCG v1.9:

**(a) Paridad discreta (K-013):** la acción de Chern-Simons cambia de signo bajo paridad (S_CS → −S_CS). Cualquier descripción efectiva CS quiral viola paridad automáticamente. Esto sigue valiendo y es independiente del mecanismo de origen.

**(b) Asimetría máxima (solo L acoplan a SU(2)):** la afirmación original — "solo los fermiones levógiros se acoplan a la conexión autodual; heredado de la estructura del grupo de Lorentz" — **se reemplaza** por el mecanismo topológico de la sección "SU(2)_L — edge mode quiral" arriba. La asimetría máxima emerge del *gap del sector mirror* en la construcción Wang-Wen 2018-2019, que es consecuencia de la cancelación de anomalías via cobordismo SO(10) (Ω⁵ clase trivial). No es una identidad del Lorentz — es un teorema del lattice 3+1D con frontera topológica.

Contenido empírico preservado; mecanismo físico distinto.

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

## Relación con la literatura (v1.9)

| Programa | Relación con H-003 | Status v1.9 |
|---|---|---|
| **Levin-Wen (2005)** | H-003 es una realización física del marco Levin-Wen. Diferencia: las reglas de fusión se derivan (D-004), no se postulan | Base |
| **Walker-Wang (2011)** | Framework sistemático de fases topológicas 3+1D con UBFC. Red SCG = modelo WW | Base |
| **Walker-Wang modular (Kawagoe-Gorantla-Williamson 2023, PRB 107 085134)** | Bulk 3+1D invertible/SPT con frontera (2+1)D quiral | **Ruta primaria quiralidad v1.9** |
| **Kaplan 2024 (PRL 132 141603)** | Fermiones quirales en frontera entre fases topológicas, sin mirror partners | **Mecanismo quiralidad SU(2)_L v1.9** |
| **Kaplan-Sen 2024 (PRL 132 141604)** | Weyl edge states en lattice finito con Wilson fermion; caso concreto | Ejemplo técnico v1.9 |
| **Wang-Wen 2018-2019 (arXiv:1809.11171)** | SM completo desde SO(10)-GUT no-perturbativo en lattice 3+1D via cobordismo | **Base K-033 v1.9; cancelación de anomalías** |
| **Chern-Simons/Witten (1988)** | Teoría efectiva de la red SCG en 3D; frontera de Crane-Yetter | Base |
| **Bilson-Thompson (2005)** | Los "3 ribbons" se motivan por D=3 → trivalencia. H-003 da origen físico a las trenzas | Complementario |
| **Alexander-Marciano-Smolin (2014, PRD 89 065017)** | Proponen SU(2)_gravedad = SU(2)_L (β=-i) | **Desplazado v1.9**: quiralidad es topológica, no gravitacional |
| **Randono (2006, gr-qc/0504010 + 0611073 + 0611074)** | Kodama con β real, CPT invariante | **Sector gravitacional v1.9** |
| **Bais-Slingerland (2009)** | Condensación de anyones = mecanismo de Higgs. H-003 lo aplica a la red SCG | Base K-021 |
| **Fradkin-Shenker (1979)** | Higgs = confinamiento para SU(2) fundamental. Consecuencia directa en H-003 | Base K-021 |
| **LQG (redes de espín)** | H-003 usa estructura similar (holonomías en edges, intertwiners en vértices). **v1.9:** SCG usa Barbero-Immirzi con β real como mainstream LQG; la quiralidad SM no viene de la conexión gravitacional | Actualizado v1.9 |
| **Kelvin (1867)** | Misma visión (nudos = partículas), pero sin éter: las cuerdas SON el espacio-tiempo | Complementario |
| **Finkelstein (SLq(2))** | Cuantización de cargas desde grupos cuánticos. Conexión posible pero no explorada | Pendiente |

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

## Problemas abiertos (actualizado v1.9)

### Problemas derivacionales (cómo completar lo que falta)

1. **Acción Lagrangiana de la red SCG (P-8).** Arquitectura completa (bosquejo sesión 12). 3/5 sub-tareas con derivación cerrada (D-006, D-007, D-008+D-009); 2/5 parciales con candidatos (K-030 confirmado con Q-043 pendiente, K-032 candidato). Ver snapshot v1.9 sección 6.

2. **Niveles de Chern-Simons k para cada factor gauge (Q-027).** k determina qué representaciones existen (truncación). A k=1 solo hay 3 anyones → espectro mínimo. A k grande → espectro del SM completo. El flujo k(E) no está calculado.

3. **Constantes de acoplamiento (reformulado v1.9).** Con SU(2)_L desacoplado del sector gravitacional (v1.9), el problema "G_Newton vs g_weak" deja de ser una tensión de unificación directa — son acoplamientos de sectores estructuralmente distintos. Queda abierta la predicción cuantitativa del patrón α₂ ≈ α₃ ≠ α₁ a M_P (K-032 candidato; matching II→IV explícito pendiente).

4. **Masas de fermiones.** El mecanismo de generación de masa (Yukawa) no está derivado. Los acoplamientos de Yukawa dependen de la geometría detallada de la red, que no conocemos. **v1.9:** posible apertura vía estructura SO(10)-GUT (K-033 candidato potencial, Wang-Wen 2018-2019).

5. **Ángulo de Weinberg θ_W.** Requiere la relación entre los acoplamientos g y g' de SU(2)_L y U(1)_Y. En principio derivable si se conoce la estructura de la red, pero no calculado.

6. **UBFC modular SCG específica (Q-043, NUEVA v1.9).** Construcción explícita de una categoría de fusión trenzada unitaria modular, compatible con SCG (trivalente, H-003, D-004), cuya frontera hospede 16 Weyl spinoriales de SO(10) con anomalías 't Hooft canceladas por cobordismo (clase trivial en Ω⁵). Si cierra constructivamente: K-030 → confirmado limpio, P-11 → ✅ resuelto, K-033 potencial activable.

### Problemas conceptuales (qué no entendemos bien)

7. **Z₃ dual → generaciones.** La conexión entre la cara del grafo dual y los modos de generación necesita formalización. ¿La Z₃ dual se conserva realmente como número cuántico? ¿Cómo se acopla a los otros sectores?

8. **Red SCG densa (BH) vs red SCG diluida (vacío).** H-001 describe el interior de un BH como red densa. H-003 describe el vacío como red ordenada. ¿Cómo se conectan las dos fases? ¿Hay una transición de fase?

9. **Fermiones emergentes vs fundamentales.** En Levin-Wen, los fermiones emergen como compuestos de excitaciones topológicas (diones = carga + flujo). ¿Son los fermiones del SM compuestos en este sentido?

10. **Espectro bosónico.** Los bosones gauge (γ, W±, Z, gluones) deben emerger como excitaciones colectivas de la red. El mecanismo para el fotón (sin masa, U(1)_EM) vs W/Z (masivos, SU(2)_L confinado) requiere la condensación de anyones. ¿Es consistente con todos los datos del SM? **v1.9:** el confinamiento de SU(2)_L = Higgs (K-021) sigue operativo, pero la SU(2)_L confinada es ahora la emergente del edge mode de frontera WW, no la gravitacional de Ashtekar.

11. **D_tiempo = 1.** ~~H-002 explica D_espacio = 3 pero no D_tiempo = 1. H-003 hereda este problema.~~ **RESUELTO (D-005, sesión 10, K-022):** so(4,C) única factorización de Dynkin + signatura fijada por espinores de Weyl + H-002. **Nota v1.9:** uno de los cuatro argumentos convergentes de D-005 era K-019 literal (que se debilita). Los otros tres (Dynkin, Hodge, espinores) siguen válidos. El resultado se preserva como "auto-consistente" (punto fijo K-025).

---

## Lo que H-003 logra y lo que no

### Logra (por primera vez, desde QM + GR solamente) — v1.9

- Deriva por qué el grupo gauge tiene 3 factores (3 aspectos geométricos distintos de la red)
- Deriva por qué la carga se cuantiza en 1/3 (trivalencia → Z₃)
- Explica el confinamiento como geometría UV (K-018)
- Explica la violación de paridad como **fenómeno topológico de frontera** (v1.9, Kaplan + Wang-Wen + modular WW), no como identidad del grupo de Lorentz
- Identifica un mecanismo de Higgs (condensación de anyones, demostrado en materia condensada)
- Propone una explicación para N_gen = 3 = N_color (Z₃ × Z₃ de la dualidad)
- **v1.9:** desacopla sector gravitacional (Barbero-Immirzi β real, Randono) de sector quiral-SM (topología WW modular), mitigando P-11 (Kodama) sin renunciar a la asimetría máxima

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
- **2026-04-19 (sesión 11):** K-026 propuesta — dicotomía "gravedad quiral / red no-quiral".
- **2026-04-21 (sesión 22, Q-040):** K-019 segunda reinterpretación — Randono β real, violación P cualitativa pero asimetría máxima no automática.
- **2026-04-21 (sesión 24, Q-042):** **K-019 tercera reinterpretación — quiralidad topológica vía Kaplan 2024 + Wang-Wen 2018-2019 + modular WW; independiente de β de Ashtekar. K-026 degradada (dicotomía no se sostiene). Q-043 nueva: construcción UBFC modular SCG con SO(10).**
- **2026-04-21 (sesión 25, saneamiento documental):** cuerpo de H-003 integrado con reinterpretación v1.9 (ya no solo nota al tope).
- **2026-04-21/22 (sesiones 26-29, ataque técnico Q-043):** O1 (k=1 integrable), O6 (Y cuantizada doble derivación), O2 (trivalencia+Z₃ coprimos), O5 (desacople grav/top) — 4 obstrucciones bloqueantes cerradas.
- **2026-04-22 (sesión 30, Q-043 CERRADA):** UBFC específica `Spin(10)_1` identificada; D-010 síntesis; K-030 confirmado estructuralmente; P-11 resuelto estructuralmente; K-033 activado; K-034 candidato; K-017 refuerzo. Snapshot v2.0.
