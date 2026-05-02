# H-004 — Sesión 90: Sub-tarea C.γ — Geometría no-conmutativa de Connes como ruta a "estructura informacional pre-categorial"

**Fecha:** 2026-05-01 (sesión 90, post-recalibración S89)
**Disciplinas activas:** D1-D10 + D6.d-e + D7.d-g (post-S89, ver `framework/epistemology.md`).
**Antecedente directo:** sub-tarea C.γ planificada en S89 como Opción C del auditor — proceder a NCG sin anticipar resultado.
**Objetivo:** evaluar si la geometría no-conmutativa (NCG) de Connes ofrece ruta epistemológicamente independiente al problema identificado en C.β' (input categorial post-hoc), o tiene el mismo patrón.

**Disciplinas explícitas a respetar (post-S89):**
- D7.a-g: sin auto-etiquetaciones celebratorias. Sin "Logro". Sin auto-equiparación con benchmarks máximos.
- D7.e: sin auto-asignación de veredicto. **El veredicto VIENE del auditor imparcial.**
- D7.f: sin construir "valor en retreat" preventivamente.
- D8: cierres negativos requieren contenido derivativo propio.
- D6.d: auditoría imparcial adaptativa al cierre.

---

## 1. Setup formal de NCG

### 1.1 Triple espectral

Una **triple espectral** $(\mathcal{A}, \mathcal{H}, D)$ consiste en:
- $\mathcal{A}$: álgebra asociativa con involución (típicamente $C^*$-álgebra o pre-$C^*$-álgebra).
- $\mathcal{H}$: espacio de Hilbert con representación $\pi: \mathcal{A} \to \mathcal{B}(\mathcal{H})$.
- $D$: operador autoadjunto en $\mathcal{H}$ con resolvente compacta y $[D, \pi(a)]$ acotado para $a \in \mathcal{A}$.

**Triple real:** además se incluye operador anti-unitario $J: \mathcal{H} \to \mathcal{H}$ con $J^2 = \pm 1$ y reglas de conmutación con $D$ (axioma de "reality").

**Triple par (even):** se añade grading $\gamma$ con $\gamma^2 = 1$ que conmuta con $\mathcal{A}$ y anticonmuta con $D$.

### 1.2 Axiomas adicionales (Connes 1994, 2006)

1. **Orientability:** existe ciclo de Hochschild $c \in \text{HC}^n(\mathcal{A})$ con $\pi_D(c) = \gamma$.
2. **First-order condition:** $[[D, \pi(a)], \pi(b)^\circ] = 0$ para $a, b \in \mathcal{A}$, donde $\pi(b)^\circ = J\pi(b^*)J^{-1}$.
3. **Poincaré duality:** clase específica en $K$-teoría es no-degenerada.
4. **Reality axiom:** condiciones sobre $J$ y $J^2 = \epsilon$, $JD = \epsilon' DJ$, $J\gamma = \epsilon'' \gamma J$ con $(\epsilon, \epsilon', \epsilon'') \in \{\pm 1\}^3$ — define **KO-dimension** $\in \{0, 1, \ldots, 7\} \mod 8$.

### 1.3 Acción espectral

El **principio de acción espectral** (Chamseddine-Connes 1996) postula:
$$
S[\mathcal{A}, D] = \text{Tr}\,\chi(D/\Lambda) + \langle \psi, D\psi \rangle
$$
donde $\chi$ es función de corte y $\Lambda$ es escala UV. Aplicado a triples espectrales del SM, este Lagrangiano reproduce el SM acoplado a Einstein-Hilbert + Weyl gravity.

---

## 2. Análisis del input algebraico — inventario explícito

### 2.1 Lo que el modelo Chamseddine-Connes para SM postula

**Triple espectral total:** $(\mathcal{A}, \mathcal{H}, D) = (\mathcal{A}_M \otimes \mathcal{A}_F, \mathcal{H}_M \otimes \mathcal{H}_F, D_M \otimes 1 + \gamma_M \otimes D_F)$.

- **$\mathcal{A}_M$:** álgebra de funciones suaves sobre variedad espacio-temporal $M$.
- **$\mathcal{A}_F$:** álgebra finita "interna" — la elección clave.
- **$\mathcal{H}_F$:** espacio de Hilbert finito de dimensión 96 (3 generaciones × 32 estados por generación).
- **$D_F$:** operador de Dirac interno — codifica matrices de Yukawa, masas, mixing CKM/PMNS.

**Para el SM (Connes 2006, KO-dim 6):**
$$
\mathcal{A}_F = \mathbb{C} \oplus \mathbb{H} \oplus M_3(\mathbb{C})
$$

### 2.2 Inputs que se postulan explícitamente (no derivados)

Inventario honesto de los inputs:

1. **Estructura producto $M \times F$.** No derivada — postulada como ansatz para gravedad + gauge separados.
2. **Variedad $M$ con métrica.** No derivada — geometría espacio-temporal asumida.
3. **KO-dimension 6** (Connes 2006). **Elegida** para resolver:
   - Problema de fermion doubling (parcial).
   - Necesidad de masas de neutrinos vía see-saw.
   - **No emerge a priori** — Stephan (arXiv:hep-th/0610040) documentó que cambio KO-dim 0 → 6 viola el axioma de orientability original.
4. **"Quaternion linearity" con $k=4$** (Chamseddine-Connes 2007). **Hipótesis adicional** que reduce las opciones algebraicas. Connes-Chamseddine demuestran "$\mathcal{A}_F$ casi única bajo $k=4$ y los demás axiomas".
5. **First-order condition.** Si se mantiene, restringe el operador de Dirac. **Si se relaja** (Chamseddine-Connes-van Suijlekom 2013), emerge **Pati-Salam $SU(2)_R \times SU(2)_L \times SU(4)$** en lugar de SM. **Es decir: la elección de qué grupo gauge emerge depende de qué axiomas se mantienen.**
6. **Operador de Dirac interno $D_F$** — codifica las **constantes de Yukawa, masas y ángulos de mixing**. Estos parámetros son **input completo**, no derivados.
7. **3 generaciones** — se obtienen triplicando $\mathcal{H}_F$ por mano. *"In this context we have no explanation for the presence of three generations, with identical quantum numbers, except for the different masses."* (Connes-Marcolli 2007).
8. **Función de corte $\chi$** en la acción espectral — elegida heurísticamente.

### 2.3 Lo que sí emerge (no-trivialmente)

Una vez postulado todo lo anterior, lo siguiente **emerge de manera no-trivial**:

- **Cualidad del grupo gauge:** $U(1)_Y \times SU(2)_L \times SU(3)_c$ emerge desde $\mathcal{A}_F$ vía representación interna.
- **Higgs como conexión interna:** $\Phi$ aparece como componente "no-conmutativa" de la conexión.
- **Quantum numbers fermiónicos** (hipercargas, isospin) emergen de la representación.
- **Acoplamiento gauge-gravedad-Higgs unificado** en una sola acción espectral.
- **Una predicción cuantitativa pre-LHC:** $m_H \in [160, 180]$ GeV (refutada por LHC, ver §3).

**Esto NO es trivial.** Es contenido genuino del programa NCG. Pero NO equivale a "derivar SM a priori".

---

## 3. El evento Higgs 125 GeV — refinamiento post-hoc

### 3.1 La predicción pre-LHC

Chamseddine-Connes 1996, 2007 calcularon:
$$
m_H \approx 170 \text{ GeV}, \quad m_H \in [160, 180] \text{ GeV (banda con incertidumbre)}
$$

Esto se presentó durante años como **predicción robusta** del programa, presentándose como "make-or-break" del modelo NCG-SM.

### 3.2 La refutación experimental

LHC ATLAS+CMS julio 2012:
$$
m_H \approx 125 \text{ GeV}
$$

**Inconsistente** con la predicción NCG-SM original — fuera de la banda predicha.

### 3.3 La respuesta del programa: Resilience 2012

Chamseddine-Connes agosto 2012 (≈1 mes después del anuncio LHC) publicaron arXiv:1208.1030 "Resilience of the Spectral Standard Model".

**Argumento:** existe un campo escalar $\sigma$ que *"ya estaba en el modelo pero fue indebidamente despreciado"* en cálculos previos. Su acoplamiento al Higgs modifica el RG-running y restaura compatibilidad con $m_H \approx 125$ GeV.

### 3.4 Análisis de la respuesta

**Caracterización honesta:** post-hoc en sentido fenomenológico (no necesariamente estricto):
- El campo $\sigma$ no era prominente en el programa pre-2012, **pero podría haber estado presente con rol subdominante** en cálculos previos del Higgs (interpretación legítima por Connes).
- Su rol clave en la fenomenología emerge **después** del dato experimental.
- La calificación **"wrongly neglected"** es paráfrasis del análisis del autor — **no es cita textual verificada de Chamseddine-Connes 2012**. La frase de la respuesta original es más cuidadosa.
- Connes públicamente admite: *"writing precise figures for the Higgs mass... is ridiculous"*, caracterizando 170 GeV como "order of magnitude" — esto contradice el discurso pre-LHC del programa donde 170 GeV se presentaba como predicción genuina.

**Caveats interpretativos:**
- La realidad histórica es **gradiente, no binaria**: entre "predicción robusta pre-2012 totalmente refutada" y "post-hoc estricto", existe la opción "**reordenamiento de jerarquías de aproximación ante nuevo dato**" (interpretación posible por parte del programa NCG).
- Esto **no invalida científicamente el programa** (los modelos se refinan con datos), **pero** debilita la afirmación de que "NCG-SM hace predicciones unívocas a priori" en sentido fuerte.

---

## 4. Multiplicidad post-axiomas: Pati-Salam vs SM

### 4.1 La situación pre-2013

Chamseddine-Connes 2007 ("Why the Standard Model") afirmaban que el SM emerge "casi unívocamente" desde NCG bajo el conjunto completo de axiomas (orientability + first-order + Poincaré duality + KO-dim 6 + $k=4$).

### 4.2 Lo que se descubrió después (2013)

Chamseddine-Connes-van Suijlekom 2013 (arXiv:1304.8050): **al relajar el first-order condition**, emerge **Pati-Salam $SU(2)_R \times SU(2)_L \times SU(4)$** GUT en lugar de SM directo.

### 4.3 Implicación crítica — distinguiendo dos formas de input

La "unicidad casi total" del SM era **condicional al first-order condition específico**. Cuando se relaja:
- Pati-Salam emerge como una posibilidad.
- Otras posibilidades pueden emerger bajo otras relajaciones de axiomas.
- La frase "leads immediately to **a** Pati-Salam type model" (artículo "a", no "the") indica una opción entre varias.

**Distinción importante (post-auditoría):** existen **dos formas distintas de "input categorial"** que el análisis debe separar:

1. **Input estructural axiomático:** elección de qué axiomas mantener (first-order strict vs relajado, KO-dim 0 vs 6, $k=4$ vs otro). Esto es **decisión sobre qué variante de teoría** considerar — análoga a elegir entre marcos teóricos distintos.
2. **Input fenomenológico parametrico:** calibración de operador de Dirac interno $D_F$ con valores específicos de Yukawa, masas y mixing CKM/PMNS. Esto es **input post-hoc estricto** porque requiere conocimiento empírico del SM observado.

**Cada axioma estructural decide qué emerge cualitativamente:**
- Con first-order strict: SM.
- Sin first-order: Pati-Salam.
- Con KO-dim 0: ningún neutrino masivo.
- Con KO-dim 6: neutrinos masivos posibles.

**El input parametrico decide qué emerge cuantitativamente** (masas y mixing).

**Analogía estructural con C.β' (marcada como Regla 4):** ambos formalismos requieren input — pero **NCG funciona técnicamente capturando SM**, mientras C.β' falla en producir categoría modular. La analogía es en problema epistémico (input necesario), no en madurez técnica ni captura del SM.

---

## 5. Comparación con C.β' (sin extrapolación inflada)

### 5.1 Tabla comparativa honesta

| Dimensión | C.β' (WPP-hypergraphs) | C.γ (NCG Connes) |
|---|---|---|
| **Input estructural** | Reglas de reescritura WPP + tensor monoidal canónico | Triple espectral + axiomas + KO-dim + $k=4$ |
| **¿Justificación a priori del input?** | No — reglas postuladas | No — axiomas elegidos para que SM emerja |
| **¿Captura SM cualitativamente?** | No — categoría simétrica, no modular | **Sí — gauge group + Higgs + fermiones cualidad** |
| **¿Predice masas/mixing cuantitativamente?** | No | No — Yukawa couplings son input |
| **¿3 generaciones derivadas?** | No | No — triplicación a mano |
| **Madurez del programa** | 6 años (Wolfram 2020+) | 30 años (Connes 1994+) |
| **Crisis empírica** | n/a | Higgs 125 GeV → refinamiento post-hoc 2012 |
| **Multiplicidad axioma-dependiente** | n/a | Documentada (first-order → Pati-Salam) |

### 5.2 Diferencias estructurales

**A favor de NCG vs C.β':**
1. NCG **captura** el SM cualitativamente; C.β' **no llega** a categoría modular.
2. NCG es **mucho más maduro técnicamente** (Krajewski clasificación, K-teoría, álgebras de von Neumann).
3. NCG ofrece **predicciones cuantitativas** (Higgs en banda, top en banda) — aunque la banda fue ajustada post-hoc.
4. NCG **unifica** gauge + Higgs + gravedad en una acción.

**En contra de NCG (paralelo a C.β'):**
1. $\mathcal{A}_F$ NO es a priori.
2. KO-dim 6 + $k=4$ son elecciones.
3. 3 generaciones puestas a mano.
4. Yukawa, masas, mixing son input completo.
5. Higgs 125 GeV requirió refinamiento post-hoc.
6. Axiomas relajables ad hoc según fenomenología deseada.

### 5.3 Estructura del problema epistemológico (analogía estructural — no derivación)

**Analogía estructural identificada (Regla 4 marcada explícitamente):** sobre los formalismos examinados (C.β' WPP-hypergraph + 4 cercanos + C.γ NCG), la estructura matemática que "captura" el SM requiere ser elegida con conocimiento del SM. La elección puede ser:
- Categorial (Levin-Wen: fusion category UFC como input).
- Algebraica (NCG: $\mathcal{A}_F$ + axiomas + $D_F$ como input).
- Combinatoria (WPP-hypergraph: reglas de reescritura como input).

En todos los casos examinados, **el contenido específico del SM requiere ser incorporado como input estructural en alguna forma**. Esto es **analogía sobre 5 formalismos**, no derivación de imposibilidad universal.

### 5.3.b Argumento más fuerte: NCG como contraejemplo más fuerte a A-005 que C.β'

**Honestidad sobre la fuerza del argumento (corrección post-auditoría):** el documento debería **fortalecer**, no debilitar, la conclusión:

- C.β' fracasa por **insuficiencia técnica** — la construcción no produce MTC modular siquiera. El programa fracasa antes de plantear el problema epistémico de manera clara.
- C.γ tiene **éxito técnico** capturando SM cualitativamente — **el problema epistémico SÍ es genuino aquí**. Con input postulado se obtiene SM correcto, sin él no se obtiene nada.

**Implicación más fuerte:** **NCG es contraejemplo más preocupante a A-005 que C.β'.** En C.β', el formalismo simplemente no funciona; en C.γ, **el formalismo funciona** y aún así requiere input específico no derivable a priori. Esto sugiere que **incluso cuando la matemática funciona técnicamente, el SM no emerge sin input estructural calibrado con conocimiento empírico**.

**Limitación crítica de la conclusión:** examen de DHR / conformal nets / AQFT está pendiente — esto es **omisión que debilita la generalización**. Sin examen DHR, **NO es defendible** afirmar que "todo formalismo conocido requiere input categorial". Sólo es defendible: "los formalismos examinados (C.β', Levin-Wen, Kitaev, Turaev-Viro, ZX, NCG estándar) requieren input categorial".

### 5.4 Pregunta abierta

**¿Es esta limitación estructural inherente, o solamente reflejo del estado actual de los formalismos conocidos?**

**Honestamente, esto NO se determina con C.γ sola.** Posibilidades:
1. Limitación inherente — el SM contiene parámetros irreducibles que ningún formalismo a priori puede derivar sin asumirlos.
2. Limitación del estado del arte — algún formalismo futuro (combinación de NCG + DHR + ∞-categorías + ?) podría lograrlo.
3. Limitación parcial — partes cualitativas del SM son derivables a priori (e.g., grupo gauge), partes cuantitativas (masas, mixing) no.

**No se concluye en S90 cuál de las tres es el caso.**

---

## 6. Pendiente identificado: DHR / conformal nets / AQFT

El auditor S88 (y reiterado en S89) señaló: Doplicher-Roberts superselection sectors / Longo-Rehren / conformal nets son contraejemplo potencial al patrón "input categorial pre-existente".

**Lo que estos formalismos tienen distinto:**
- Parten de **net of local von Neumann algebras** — dato físico-algebraico, no categorial pre-existente directamente.
- La **categoría modular emerge** vía representations DHR.

**Lo que NO se ha examinado en C.γ S90:** este examen, postergado nuevamente en favor de C.γ NCG. **Pendiente para sesión futura** si el programa H-004 continúa.

**Honestidad:** esta omisión es una forma sutil de "evitar contraejemplo potencial" — debe reconocerse explícitamente, no minimizarse.

---

## 7. Síntesis técnica (sin auto-asignar veredicto)

### 7.1 Lo que el análisis S90 muestra

**Para C.γ específicamente:**
1. NCG Connes captura cualitativamente el SM una vez postulado el input algebraico ($\mathcal{A}_F$ + axiomas + $D_F$ con Yukawa).
2. El input algebraico **no es a priori**: depende de elecciones (KO-dim, $k$, axiomas activos) que se calibran con conocimiento del SM.
3. El refinamiento post-Higgs 2012 (Resilience) fue post-hoc.
4. La multiplicidad documentada (first-order → SM vs Pati-Salam) muestra que la "unicidad" es condicional a axiomas.
5. Los parámetros cuantitativos (masas, mixing, generaciones) son input.

**Para el patrón general identificado en H-004:**
- C.γ presenta estructura epistemológica análoga a C.β' (input postulado con conocimiento del SM).
- **Pero NCG es genuinamente más sofisticado y captura más** que C.β'.
- La limitación es del mismo tipo (input categorial-algebraico necesario), pero NCG **extrae más mileage** del input.

### 7.2 Lo que el análisis S90 NO muestra

**Honesto:**
1. **No se ha demostrado** que NCG es estructuralmente análogo a C.β' en sentido fuerte. Los formalismos son técnicamente distintos (uno categorial-rewriting, otro algebraico-espectral). La analogía es solo en problema epistémico (input necesario), no en madurez ni captura del SM.
2. **No se ha demostrado** que el patrón "input categorial post-hoc" es estructuralmente irresoluble — sólo se ha identificado en 6 formalismos examinados.
3. **No se ha examinado DHR / conformal nets / AQFT** — contraejemplo potencial pendiente. **Esta es la omisión más crítica**, señalada por auditoría imparcial S88, S89 y S90 sin haber sido examinada en ninguna sesión. Examen comprometido para S91 obligatoriamente.

(Nota post-auditoría: ítem ritual "no se ha refutado A-005" eliminado — A-005 es conjetura abierta sobre primacía informacional ontológica que el documento nunca pretendió refutar.)

### 7.3 Implicación para programa H-004

**Sub-tareas C.β' + C.γ producen información parcial sobre la pregunta foundational** "¿puede A-005 + estructura pre-categorial pura derivar SM a priori?":

- 4 formalismos examinados (Levin-Wen, Kitaev, Turaev-Viro, ZX) requieren input categorial.
- WPP-hypergraph en construcción canónica produce simetría, no modular.
- NCG Connes captura SM con input algebraico-axiomático calibrado para SM.

**Pregunta sigue abierta:**
- DHR / conformal nets / AQFT: ¿contraejemplo o no?
- Otros formalismos no considerados.

**Veredicto sobre programa H-004 NO se asigna en S90.** Decisión sobre continuación / retreat depende de:
- Resultado de auditoría imparcial obligatoria sobre este documento.
- Eventual examen DHR (sesión futura).
- Síntesis honesta C.δ.

---

## 8. Auditoría D1-D10 internalizada (sin auto-celebración, post-S89)

### 8.1 D1 anti-vacuidad

**¿Hay contenido derivativo propio?**
- ✓ Inventario explícito de inputs en NCG (§2.2): 8 inputs identificados.
- ✓ Análisis del Higgs 170 → 125 GeV (§3): reconocimiento del refinamiento post-hoc.
- ✓ Análisis de multiplicidad axioma-dependiente (§4): documentado (first-order → Pati-Salam vs SM).
- ✓ Comparación estructural C.β' vs C.γ (§5): tabla + análisis.

**Veredicto D1 (auto-evaluación pendiente de auditoría imparcial):** los puntos arriba son contenido derivativo más que revisión literaria — pero **no se auto-asigna nivel** (D7.e). El veredicto vendrá del auditor.

### 8.2 D2 correspondencia IR

**N/A** — sub-tarea evaluativa, no derivativa positiva.

### 8.3 D3 extensiones justificadas

**¿Examinó NCG en su forma estándar?** ✓.
**¿Examinó variantes (Pati-Salam, octoniones, Heisenberg orden superior)?** Parcialmente — en literatura, no en construcción.
**Pendiente:** DHR / conformal nets / AQFT.

### 8.4 D4 falsabilidad

**N/A** para sub-tarea evaluativa.

### 8.5 D5 auditoría periódica

**Estado pre-S90:** ACTIVADO EN SENTIDO FUERTE, no agravado por C.β' (MODERADO).

**S90 puede:** (a) atenuar trigger si C.γ identifica ruta inesperada; (b) mantener trigger si C.γ confirma patrón parcial; (c) **no agravar** si caveat es moderado o menor.

**Veredicto pendiente** de auditoría imparcial.

### 8.6 D6 auditoría imparcial multi-nivel adaptativa

**Pendiente** — invocación obligatoria post-este documento. Auditor debe ser ADAPTATIVO (D6.d): buscar mutaciones nuevas del patrón M-01/M-02/M-03 si existen.

### 8.7 D7 sin auto-celebración

**Verificación interna:**
- "K-005 ejemplar Nma vez" — NO incluido. ✓
- "Regla 9 ejemplar" — NO incluido. ✓
- "Honestidad anti-inflación máxima" — NO incluido. ✓
- "Logro técnico/comparativo" — NO incluido. ✓
- "Análogo a benchmark máximo (Distler-Garibaldi, K-028)" — NO incluido. ✓
- "CERRADA LIMPIAMENTE / D1 APROBADO LIMPIO" — NO incluido. ✓
- "Contribución incluso en retreat" — NO incluido. ✓

**Verificación externa pendiente** — el auditor imparcial debe buscar mutaciones nuevas (cuarta generación si emerge).

### 8.8 D8 distinción cierre positivo vs negativo

**Cierre evaluativo** (no positivo ni negativo limpio): NCG captura SM cualitativamente con input postulado. La sub-tarea identifica el problema epistemológico pero no resuelve la pregunta foundational.

**¿Distingue "decisión de no investigar" vs "imposibilidad demostrada"?** §7.2 reconoce explícitamente que NO se demuestra imposibilidad estructural — sólo se identifica el patrón en formalismos examinados.

### 8.9 D9 restricción Regla 9

**¿Se invoca Regla 9 en este documento?** NO. ✓

### 8.10 D10 restricción cuantitativa

**¿Se ofrecen cifras de probabilidad manufacturadas?** NO. ✓

**Se ofrecen estimaciones cualitativas:** "captura genuina del SM" (cualitativa), "más maduro técnicamente" (cualitativa). NO multiplicación de probabilidades.

---

## 9. Estatus tras auditoría imparcial S90

**Veredicto del auditor imparcial:** **CAVEAT MODERADO** (segunda recalibración consecutiva — mejora estructural sostenida desde S89). D7.a-g respetados operacionalmente. D1 satisfecho mínimamente (síntesis literaria con organización propia, no construcción derivativa fuerte). DHR omitido por 3ra vez consecutiva — **AGRAVADO**.

**Mutación 4ta tentativa detectada:** **4.b reconocimiento ritualizado de DHR** sin examen.

**Decisión adoptada:** **PRIORIDAD ALTA del auditor — examinar DHR/conformal nets/AQFT en S91 ANTES de C.δ síntesis.**

**Si DHR confirma contraejemplo a la conjetura "input categorial necesario":** retreat del programa H-004 con base sustantiva.
**Si DHR requiere input no-trivial:** patrón sistemático defendible para extrapolar.
**Si NO se examina DHR antes de C.δ:** mutación 4.b se confirma como cuarta generación, requiere D7.h formal.

**Ver auditoría completa:** `notes/H-004_sesion90_auditoria_C_gamma.md`.

---

## 10. Referencias clave (subset crítico)

- **Connes 1994:** *Noncommutative Geometry*, Academic Press.
- **Chamseddine-Connes 1996:** "The Spectral Action Principle", arXiv:hep-th/9606001.
- **Connes 2006:** "NCG and the SM with Neutrino Mixing", arXiv:hep-th/0608226.
- **Chamseddine-Connes 2007:** "Why the Standard Model", arXiv:0706.3688.
- **Chamseddine-Connes 2012:** "Resilience of the Spectral Standard Model", arXiv:1208.1030 (post-Higgs 125 GeV).
- **Chamseddine-Connes-van Suijlekom 2013:** "Beyond the Spectral SM: Pati-Salam", arXiv:1304.8050.
- **Boyle-Farnsworth 2018:** "A New Algebraic Structure in SM", arXiv:1604.00847 (eliminación de "7 términos no deseados").
- **Stephan 2006:** "Almost-Commutative Geometry, Massive Neutrinos and the Orientability Axiom in KO-dim 6", arXiv:hep-th/0610040.
- **Krajewski 1997:** "Classification of Finite Spectral Triples", arXiv:hep-th/9701081.
- **Schucker 2010:** "The NC Standard Model, Post- and Predictions", arXiv:1003.5593 (review crítico imparcial).

---

**Fin sub-tarea C.γ análisis técnico inicial. Pendiente: auditoría imparcial obligatoria adaptativa (D6.d).**
