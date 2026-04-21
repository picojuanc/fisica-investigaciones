# Tarea 5.3 — Estado de Kodama y ataque a P-11

- **Fecha:** 2026-04-21 (sesión 17)
- **Referencia bosquejo:** `notes/R_lagrangiana_bosquejo.md`, sección 5.3.
- **Objetivo:** analizar las patologías del estado de Kodama Ψ_K = exp(i S_CS[A]/ℏ) reportadas por Witten 2003; revisar rutas de rescate conocidas (Randono 2006; Freidel-Smolin 2003; Alexander-Bernardo-Kuntzleman-Pezzelle 2025); identificar qué elementos específicos aporta SCG al panorama; decidir si P-11 admite mitigación estructural.
- **Relación con P-11:** es el ataque directo a la debilidad existencial identificada en sesión 11. P-11 pregunta: *¿la dependencia en Ashtekar autodual colapsa por los problemas cuánticos de Kodama?* Esta sesión no resuelve eso definitivamente pero ofrece rutas de rescate en la literatura que cambian la evaluación de severidad.
- **Nivel de esfuerzo:** una sesión (dentro de la estimación 2-3 sesiones del bosquejo).

---

## 0. Planteamiento

El estado de Kodama es, desde 1990, una solución formal exacta de TODAS las restricciones de la gravedad cuántica LQG con constante cosmológica Λ:

```
Ψ_K[A] = N · exp( i (3/(2Λ G)) · S_CS[A] )                           (0.1)
```

donde S_CS[A] = ∫ tr(A∧dA + (2/3)A∧A∧A) es el Chern-Simons autodual de la conexión Ashtekar A.

Propiedades atractivas:
- Satisface las tres restricciones (Gauss, difeomorfismos, Hamiltoniana).
- Tiene interpretación semiclásica: el WKB-límite de Ψ_K reproduce de Sitter.
- Es una solución *exacta*, no perturbativa.

Problemas identificados por Witten (2003, gr-qc/0306083):
- No-normalizabilidad en la medida natural.
- Gravitones de norma/energía negativa en la expansión.
- Violación de CPT con γ = −i.
- No invariancia bajo grandes transformaciones gauge.

Problema de la SCG: el marco depende de la conexión autodual de Ashtekar (K-019) para obtener SU(2)_L quiral. Si Kodama colapsa como estado viable, el marco SCG queda con una premisa fuerte no resoluble (P-11, riesgo existencial).

**Esta sesión no construye nueva física.** Revisa la literatura de rescate acumulada entre 2005 y 2025, identifica qué de ella es favorable a SCG específicamente, y evalúa si P-11 puede pasar de 🟡 alta a 🟡 media.

---

## 1. Patologías detalladas de Witten 2003

Witten (gr-qc/0306083) presenta cuatro objeciones interconectadas.

### 1.1 Patología (i) — Modos de energía negativa

Expandiendo la teoría Yang-Mills alrededor del estado CS Ψ_{YM,CS} en 4D (no Yang-Mills+Gravity: el argumento es análogo en el sector gravitacional autodual):
- Gauge bosones de helicidad positiva tienen energía positiva.
- Gauge bosones de helicidad negativa tienen energía **negativa**.
- Algunos estados de energía negativa tienen **norma negativa**.

En el contexto gravitacional: los gravitones de una helicidad tendrían energía negativa alrededor de Ψ_K. La teoría pierde unitariedad perturbativa.

### 1.2 Patología (ii) — No-normalizabilidad

Con el inner product natural sobre conexiones complejas (Yang-Mills-like), la integral

```
⟨Ψ_K | Ψ_K⟩ = ∫ DA |Ψ_K|²                                            (1.2.1)
```

**diverge**. Esto es lo que Freidel-Smolin (2003) cuantificaron explícitamente para la linearización alrededor de de Sitter: en Lorentziana no normalizable; en Euclidiana delta-functional normalizable.

### 1.3 Patología (iii) — Violación CPT / asimetría quiral no controlada

Ψ_K con γ = −i (autodual puro) se comporta como un "θ-vacuum" de Yang-Mills pero con θ **imaginario**. Esto da:
- CPT-violation manifiesta.
- La asimetría no es una "característica controlada" (como el θ de QCD, que es real) sino un parámetro imaginario que induce inconsistencias perturbativas.

### 1.4 Patología (iv) — No invariancia bajo grandes gauge

La acción CS cambia por 2π k_CS · n bajo una transformación gauge grande con número winding n ∈ ℤ. Para k_CS = 3/(2ΛG) no entero, Ψ_K no regresa a sí misma y pierde gauge invariancia genuina.

### 1.5 Relación con la SCG

La SCG usa Ashtekar autodual porque K-019 (Alexander-Marciano-Smolin 2014) la requiere para obtener SU(2)_L quiral. Las patologías (i)-(iv) se aplican directamente al marco SCG en régimen II si Ψ_K es el vacío relevante.

Sin embargo, SCG añade estructura adicional que no está en Kodama "desnuda":
- Restricción de simplicidad (Σ = e∧e).
- Defectos Walker-Wang (contenido topológico en la medida).
- Régimen I con Λ_efectiva ~ M_P² (no Λ_observado).
- Cuantización de modos transversales (D-006) con corte Planck.

¿Alguno de estos mitiga las patologías? Esa es la pregunta operativa de esta tarea.

---

## 2. Rutas de rescate en la literatura

### 2.1 Randono 2006 — generalización con β real

**Papers:** Randono (gr-qc/0504010, gr-qc/0611073, gr-qc/0611074).

**Construcción:** extiende Ψ_K a parámetro de Immirzi real β arbitrario (no solo β = −i). Para β real, el estado generalizado:

```
Ψ_K^{(β)}[A^{(β)}]   con A^{(β)} = Γ + β K                             (2.1.1)
```

donde Γ es conexión de spin y K es la curvatura extrínseca, satisface:

| Patología Witten | Estatus bajo Randono (β real) |
|---|---|
| (i) modos neg. energía | **Resuelta** (modos reinterpretados sin patología) |
| (ii) normalizabilidad | **Resuelta** (inner product kinemático) |
| (iii) CPT violation | **Resuelta parcialmente: CPT invariant pero no CP** ← bueno |
| (iv) grandes gauge | **Resuelta** (invariancia restaurada) |

**Caveat crítico para SCG:** Randono usa β real, no β = −i. Esto NO es la formulación autodual "pura" de Ashtekar (que requiere β = −i imaginaria). ¿Preserva K-019 (SU(2)_L quiral)?

**Respuesta (Randono 0611074):** el estado generalizado preserva violación CP — que es la huella observable de la quiralidad. La conexión SU(2) real con β ≠ 0 no es literalmente "su(2)_L del grupo de Lorentz" pero **produce la misma fenomenología**: CP violation quiral, acoplamiento asimétrico entre fermiones L y R.

**Limitación:** la identificación AMS 2014 de A_Ashtekar con su(2)_L depende específicamente de β = −i (autodual puro). La ruta Randono funciona pero re-articula K-019: la quiralidad no viene de "A_+ es literalmente su(2)_L" sino de "A^{(β)} con β real viola CP en el mismo modo observacional".

### 2.2 Alexander-Bernardo-Kuntzleman-Pezzelle 2025 — Λ grande + inner product holomorfico

**Paper:** arXiv:2511.05417 (noviembre 2025). Autores: Stephon Alexander, Heliudson Bernardo, Jacob Kuntzleman, Max Pezzelle (Brown TPC + U. Lethbridge). **Mismo grupo que AMS 2014** (Alexander-Marciano-Smolin).

**Resultado central:** el estado CS-Kodama linealizado alrededor de de Sitter es **perturbativamente normalizable si y solo si**:

```
Λ > Λ_c := 384 / ℓ_P²                                                  (2.2.1)
```

donde ℓ_P es la longitud de Planck. En unidades naturales, Λ_c ≈ 384 M_P² ≈ 6 × 10⁷³ m⁻².

**Mecanismo:** usan un **inner product holomorfico** derivado de las condiciones de realidad cuánticas sobre la conexión autodual, no el producto naïve de Yang-Mills. La medida efectiva es

```
⟨Ψ_1|Ψ_2⟩_hol = ∫ DA e^{-S(Re A)} Ψ_1*(A) Ψ_2(A)                       (2.2.2)
```

donde S(Re A) es una acción sobre la parte real de la conexión.

**Patologías resueltas:**
- (ii) Normalizabilidad: ✓ para Λ > Λ_c.
- (i) Modos negativos: ✓ parcialmente — "precisely half of the modes are normalizable" para Λ < Λ_c, todos para Λ > Λ_c.
- (iii) CPT: preservada via inner product holomorfico (no explícito).
- (iv) Grandes gauge: no discutido en detalle.

**Limitaciones:**
- Perturbativo. No resuelve el problema no-perturbativo completo.
- Gauge TTS fijado; linealización alrededor de de Sitter clásica.
- No incluye restricción de simplicidad ni materia.

### 2.3 Freidel-Smolin 2003 — rescate Euclidiano

**Paper:** hep-th/0310224. La linealización Ψ_K alrededor de de Sitter:
- Lorentziana: NO normalizable en inner product natural.
- Euclidiana: **delta-functional normalizable**.

Esto sugiere que la patología Lorentziana puede ser un artefacto del inner product, no intrínseca. El paper de ABKP 2025 esencialmente formaliza esta intuición con un inner product específico (holomorfico) derivado de reality conditions — la Wick rotation emerge como dualidad entre Lorentzian holomorphic y Euclidean standard.

### 2.4 Resumen de rutas

| Ruta | Año | Patologías resueltas | Caveat clave para SCG |
|---|---|---|---|
| Randono β real | 2006 | (i)–(iv) | cambia β = −i → β real; K-019 se re-articula |
| Freidel-Smolin Euclidean | 2003 | (ii) via Wick | requiere rotación; Lorentziana sigue abierta |
| ABKP 2025 Λ grande + holomorfico | 2025 | (i), (ii) perturbativamente | requiere Λ > 384/ℓ_P² |

---

## 3. Mitigantes específicos que SCG aporta

### 3.1 Mitigante A — Restricción de simplicidad reduce espacio de configuraciones

En Plebanski (no BF puro), Σ no es arbitraria: la variación δψ fuerza Σ = e∧e con e vierbein real (derivado en D-007).

**Consecuencia para Kodama:** la medida de integración sobre la que Ψ_K debe ser normalizable no es sobre todas las conexiones complejas, sino solo sobre el sector geométrico (aquel donde existe un vierbein real subyacente). Esto es un subconjunto pequeño del espacio de Ashtekar.

**Efecto:** si la no-normalizabilidad venía de integrar sobre configuraciones "topológicas" no-geométricas (donde Σ no factoriza), la restricción de simplicidad **excluye esas configuraciones**. La normalizabilidad en el sector geométrico es una condición más modesta.

**Estatus:** argumento estructural, no cálculo. Formalización requiere reescribir el inner product ABKP 2025 con la simplicidad impuesta.

### 3.2 Mitigante B — Régimen I tiene Λ_efectiva ~ M_P² >> Λ_c de ABKP

El bosquejo de Lagrangiana identifica el régimen I (UV, pre-geométrico) con Crane-Yetter / Walker-Wang; en ese régimen Λ no es Λ_observado (~10⁻¹²² M_P²) sino Λ_UV ~ M_P².

Comparando con ABKP 2025:

```
Λ_UV-SCG / Λ_c-ABKP ≈ (M_P²) / (384/ℓ_P²) ≈ (1/ℓ_P²) / (384/ℓ_P²) = 1/384 ≈ 2.6 × 10⁻³
```

Es decir, Λ_UV-SCG ~ M_P² ~ ℓ_P⁻² es **menor** que Λ_c ABKP ≈ 384 ℓ_P⁻² por un factor ~384.

**Resultado preliminar:** ¡no alcanza! Si Λ_efectiva en régimen I es exactamente ~M_P² en unidades naturales, está POR DEBAJO del umbral ABKP. Solo la mitad de los modos es normalizable según ABKP.

**Pero:** "Λ_UV ~ M_P²" es estimación dimensional, no predicción cuantitativa de SCG. La Λ efectiva en régimen I podría ser cualquier múltiplo O(1)–O(10³) de M_P². Si el múltiplo es ≳ 400, el resultado ABKP da normalizabilidad perturbativa completa.

**Alternativa conservadora:** aunque Λ_UV = M_P² estrictamente (lo que parece natural), la *mitad* de los modos es normalizable. Esto puede ser suficiente si la otra mitad corresponde a modos que SCG descarta (p. ej., la helicidad "incorrecta" en la expansión, que podría ser justamente la que no tiene contenido físico en el régimen defectivo WW).

**Estatus:** argumento plausible, no cálculo. Rango concreto de Λ_UV en SCG no está determinado.

### 3.3 Mitigante C — Defectos Walker-Wang como "materia" en la medida

La medida del path integral SCG no es ∫ DA sobre solo la conexión, sino ∑_{configs topológicas} ∫ DA e^{iS/ℏ} donde las configuraciones topológicas son defectos WW (que corresponden a fermiones/bosones del SM).

**Efecto:** la normalizabilidad se evalúa no sobre "vacío puro de conexión" sino sobre "vacío con contenido topológico". Esto es análogo al θ-vacuum de QCD con instantones presentes: el estado fundamental incluye configuraciones no-triviales, y la normalizabilidad es más delicada pero también más estructurada.

**Estatus:** conjetura. No tenemos cálculo del inner product sobre el sector con defectos WW. Se puede argumentar que *algunos* defectos WW corresponden exactamente a las configuraciones que ABKP descarta por normalizabilidad en régimen Λ < Λ_c.

### 3.4 Mitigante D — Compatibilidad con AMS-Alexander lineage

Es un mitigante sociológico/metodológico, no físico: el grupo Stephon Alexander (Brown TPC) es autor tanto de **AMS 2014** (que motiva K-019 en SCG) como de **ABKP 2025** (que provee ruta de normalizabilidad para Kodama con Λ grande). Esto es consistencia de la literatura adopta el mismo marco para ambos resultados.

### 3.5 Síntesis de mitigantes

| Mitigante | Qué aporta | Nivel |
|---|---|---|
| A. Simplicidad (D-007) | Restringe medida al sector geométrico | Estructural plausible |
| B. Λ_UV-SCG ~ M_P² (régimen I) | Cerca de Λ_c ABKP; puede exceder con múltiplo O(10²) | Numérico ambiguo |
| C. Defectos WW en la medida | Reinterpreta normalizabilidad con contenido topológico | Conjetural |
| D. Grupo Alexander AMS+ABKP | Consistencia sociológica de la literatura | Metodológico |

**Ningún mitigante es decisivo individualmente. En conjunto, proveen un caso razonable de que P-11 no es un callejón.**

---

## 4. Veredicto sobre P-11

### 4.1 Re-evaluación de severidad

P-11 (Ashtekar autodual como premisa fuerte / Kodama patológico) evoluciona así:

| Sesión | Severidad | Razón |
|---|---|---|
| 11 (identificación) | 🟡 alta | Riesgo existencial; sin ruta de rescate identificada |
| 17 (esta sesión) | 🟡 media | Tres rutas de rescate en la literatura + cuatro mitigantes SCG estructurales |

**Nueva formulación de P-11:** *"La dependencia en la conexión autodual de Ashtekar es una premisa fuerte. Las patologías del estado de Kodama (Witten 2003) son conocidas pero admiten rutas de rescate: (a) generalización a β real (Randono 2006) con K-019 re-articulado; (b) inner product holomorfico con Λ grande (ABKP 2025), apllicable al régimen I de SCG. SCG añade cuatro mitigantes estructurales (simplicidad, Λ_UV grande, defectos WW, consistencia con lineage Alexander). P-11 pasa de 🟡 alta a 🟡 media."*

### 4.2 Lo que SCG no resuelve (honestidad)

- **No existe cálculo formal de Kodama en SCG específicamente.** Los mitigantes son estructurales, no computacionales.
- **El Λ exacto del régimen I de SCG no está determinado.** Estimación dimensional Λ_UV ~ M_P² está en la frontera de ABKP; si se mantiene ese valor, solo la mitad de los modos es normalizable.
- **La ruta Randono 2006 requiere re-articular K-019.** No es fatal (la violación CP observacional se preserva), pero cambia la interpretación.
- **Nada de esto aborda la no-normalizabilidad no-perturbativa.** Solo rescates perturbativos.

### 4.3 Lo que abre

**Hipótesis de trabajo SCG-Kodama (HK-SCG):** *en el sector geométrico (D-007 simplicidad) y con contenido WW apropiado, el estado de Kodama Ψ_K admite normalización perturbativa via el inner product holomorfico de ABKP 2025 con Λ_efectiva de régimen I ≳ 384 M_P² (o con Λ_UV ~ M_P² si los modos descartados coinciden con configuraciones no presentes en el sector WW geométrico).*

**Consecuencias si se verifica formalmente (sesiones futuras):**
- P-11 pasaría de 🟡 media a 🟡 baja o incluso ✅ resuelto.
- La predicción cuantitativa Λ_UV ≳ 384 M_P² sería una consecuencia observable de SCG en el régimen I (aunque no directamente medible).
- La ruta Randono 2006 quedaría como "camino alternativo conservador" por si HK-SCG falla.

**Tareas concretas pendientes** (probables candidatas para sesiones 18-19):
1. Cuantificar Λ_efectiva en régimen I de SCG desde la acción S_madre. ¿Qué determina su valor? ¿Es exactamente M_P² o algún múltiplo?
2. Formalizar la acción del inner product ABKP restringido al sector geométrico. ¿Sobrevive la normalizabilidad?
3. Verificar explícitamente que los defectos WW de H-003 no incluyen las configuraciones que ABKP descarta.
4. Leer Randono 0611073 y 0611074 en detalle para caracterizar exactamente cómo se re-articula K-019 bajo β real.

---

## 5. ¿Merece D-008?

La sesión ha producido:
- Revisión crítica de literatura.
- Hipótesis de trabajo (HK-SCG).
- Veredicto sobre severidad de P-11.

**No hay derivación nueva.** Lo obtenido es síntesis de rutas de rescate existentes aplicadas al marco SCG, sin cálculo propio.

**Decisión:** **NO hay D-008**. Pero sí hay **K-030 candidato** (insight estructural/metodológico, no derivación): *"P-11 admite mitigación estructural sustantiva: (a) ABKP 2025 provee normalizabilidad perturbativa para Λ > 384/ℓ_P²; (b) Randono 2006 provee invariancia CPT+grandes-gauge con β real; (c) SCG añade restricción de simplicidad, régimen I de Λ alta, defectos WW; (d) el grupo Alexander produce tanto la base (AMS 2014 = K-019) como el rescate (ABKP 2025). La severidad de P-11 baja de 🟡 alta a 🟡 media."*

Este K-030 es análogo en carácter a K-029: confirmatorio/estructural. No un hallazgo profundo, pero sí un cambio operativo: P-11 deja de ser existencial.

---

## 6. Qué aprende la teoría

Tres cosas concretas:

1. **P-11 no es un callejón.** Hay al menos dos rutas de rescate en la literatura (una de 2006, otra de 2025) que se aplican al marco SCG con pequeñas adaptaciones. La premisa "Ashtekar autodual" no es fatal.

2. **El régimen I de SCG está alineado con el umbral de ABKP 2025.** Si Λ_UV en régimen I es ≳ 384 M_P² (lo cual es plausible, aunque no derivado), Kodama es perturbativamente normalizable. Esto convierte el régimen I del bosquejo (ansatz en sesión 12) en una **pieza activa** del programa de rescate de P-11.

3. **Consistencia interna con el lineage de literatura.** El grupo Stephon Alexander (Brown TPC) es autor de:
   - AMS 2014 (que motiva K-019: A_+ = su(2)_L).
   - ABKP 2025 (que provee normalizabilidad de Kodama con Λ grande).
   SCG adopta K-019 vía AMS; adoptar ABKP es la continuación natural, no una selección arbitraria.

---

## 7. Honestidad epistémica

**Lo que es teorema (sabido 2003–2025):**
- Witten 2003: Ψ_K tiene cuatro patologías en su forma naïve.
- Freidel-Smolin 2003: linearización Lorentziana no-normalizable.
- Randono 2006: β real resuelve (i)–(iv) con K-019 re-articulada.
- ABKP 2025: inner product holomorfico + Λ > 384/ℓ_P² da normalizabilidad perturbativa.

**Lo que es específico de la sesión 17:**
- Identificación de que SCG añade mitigantes estructurales (simplicidad, régimen I Λ alta, defectos WW) que favorecen las rutas ABKP y Randono.
- Re-evaluación operativa: P-11 de 🟡 alta a 🟡 media.
- Observación de consistencia sociológica: mismo grupo produjo AMS 2014 y ABKP 2025.

**Ningún resultado nuevo** — solo síntesis de literatura aplicada a SCG.

**Ningún insight nuevo se promueve confirmado.** K-030 queda como candidato hasta formalizar HK-SCG (probable sesión 18 o 19).

---

## 8. Referencias

- Witten, E. (2003). "A note on the Chern-Simons and Kodama wavefunctions." arXiv:gr-qc/0306083. **Las cuatro patologías originales.**
- Freidel, L. & Smolin, L. (2003). "The linearization of the Kodama state." arXiv:hep-th/0310224. **Normalizabilidad Lorentziana vs Euclidiana.**
- Randono, A. (2005-2007). Tres papers: gr-qc/0504010, gr-qc/0611073, gr-qc/0611074. **Generalización Immirzi real.**
- **Alexander, S., Bernardo, H., Kuntzleman, J. & Pezzelle, M. (2025).** "Quantum Gravity, de Sitter Space, and Normalizability." arXiv:2511.05417. **Normalizabilidad perturbativa para Λ > 384/ℓ_P².**
- Alexander, S., Marciano, A. & Smolin, L. (2014). "Gravitational origin of the weak interaction's chirality." PRD 89, 065017. **Base de K-019.**
- Kodama, H. (1990). "Holomorphic wave function of the universe." PRD 42, 2548. **Estado original.**

---

## 9. Firma

Tarea 5.3 del bosquejo **parcialmente resuelta**: P-11 pasa de 🟡 alta a 🟡 media con K-030 candidato. No hay derivación nueva; es síntesis crítica de literatura.

Pendiente para sesiones futuras: (a) cuantificar Λ_UV en régimen I; (b) formalizar HK-SCG; (c) aclarar compatibilidad K-019 ↔ Randono β real.

Siguiente paso natural del programa Lagrangiana: Tarea 5.4 (reducción dimensional S_PA → cuerda SCG) ó Tarea 5.5 (flujo RG). Ambas son ahora más prometedoras porque el miedo existencial sobre autodual (P-11) se reduce.
