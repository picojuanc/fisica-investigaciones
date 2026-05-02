# H-004 — Sesión 91: Sub-tarea C.β'' — Examen DHR / Conformal nets / AQFT como contraejemplo potencial al patrón "input categorial pre-existente"

**Fecha:** 2026-05-01 (sesión 91, post-S90)
**Disciplinas activas:** D1-D10 + D6.d-f + D7.a-h provisional (post-S90, ver `framework/epistemology.md`).
**Antecedente directo:** auditoría S90 detectó mutación 4ta tentativa 4.b (reconocimiento ritualizado de DHR). S91 cumple la disciplina al examinar DHR explícitamente — D7.h provisional no se activa.
**Objetivo:** examinar si DHR superselection sectors / conformal nets / AQFT constituyen contraejemplo legítimo al patrón identificado en C.β' (S89) y C.γ (S90), o presentan problema epistémico análogo disfrazado.

**Disciplinas explícitas a respetar:**
- D7.a-g: sin auto-etiquetaciones celebratorias.
- D7.e: el veredicto VIENE del auditor.
- D7.f: sin construir "valor en retreat" preventivamente.
- D7.h provisional: examinar la omisión señalada, no solo reconocerla. **Cumplido por la existencia misma de S91.**
- D6.d: auditoría adaptativa post-este documento.

---

## 1. Setup formal — net de Haag-Kastler y DHR criterion

### 1.1 Net de Haag-Kastler

Una **net de algebras locales** sobre Minkowski $\mathbb{M}^4$ asigna a cada región acotada $\mathcal{O} \subset \mathbb{M}^4$ una $C^*$-álgebra $\mathcal{A}(\mathcal{O})$ con axiomas:

- **(H1) Isotonía:** $\mathcal{O}_1 \subset \mathcal{O}_2 \Rightarrow \mathcal{A}(\mathcal{O}_1) \subset \mathcal{A}(\mathcal{O}_2)$.
- **(H2) Localidad / Einstein causality:** $\mathcal{O}_1 \perp \mathcal{O}_2 \Rightarrow [\mathcal{A}(\mathcal{O}_1), \mathcal{A}(\mathcal{O}_2)] = 0$ (separación causal).
- **(H3) Covarianza Poincaré:** $\alpha_g(\mathcal{A}(\mathcal{O})) = \mathcal{A}(g\mathcal{O})$ para $g \in \mathcal{P}_+^\uparrow$.
- **(H4) Vacuum:** representación irreducible $\pi_0$ con vector cíclico $|\Omega\rangle$ Poincaré-invariante.
- **(H5) Spectrum condition:** generador de traslaciones tiene espectro en cono futuro.
- **(H6) Haag duality:** $\mathcal{A}(\mathcal{O})' = \mathcal{A}(\mathcal{O}')$ para double cones.

### 1.2 DHR criterion

Una representación $\pi$ es **DHR-admisible** si $\pi|_{\mathcal{A}(\mathcal{K}^\perp)} \cong \pi_0|_{\mathcal{A}(\mathcal{K}^\perp)}$ para todo double cone $\mathcal{K}$. Significa: las cargas son **localizables en regiones acotadas**.

### 1.3 Doplicher-Roberts theorem (1989)

Bajo (H1)-(H6) + DHR criterion, las representaciones admisibles forman una **C*-categoría tensorial simétrica con conjugados**, equivalente a $\text{Rep}(G)$ para algún **grupo compacto $G$ único hasta isomorfismo**.

En 4D: trenza simétrica, estadísticas Bose/Fermi puras + grupo gauge $G$ + álgebra de campos $\mathcal{F}(\mathcal{O})$.

En 1+1D (Fredenhagen-Rehren-Schroer 1989): trenza puede ser **no simétrica** — UMTC modular emerge bajo condiciones adicionales (Kawahigashi-Longo-Müger 2001).

---

## 2. Análisis técnico: ¿es la net of vN algebras "input pre-categorial"?

### 2.1 La net es ya un funtor

**Observación técnica clave:** una net de Haag-Kastler $\mathcal{A}: \mathcal{O} \mapsto \mathcal{A}(\mathcal{O})$ es **un funtor** desde el **poset de regiones causales** (visto como categoría con morfismos = inclusiones) hacia la categoría **C*-Alg** (objetos = C*-algebras, morfismos = *-homomorfismos).

Es decir: **el sustrato mismo de DHR/AQFT es un objeto categorial sofisticado**:
- Dominio: $\text{Reg}(\mathbb{M}^4)$ — categoría de regiones causales con inclusiones.
- Codominio: C*-Alg — categoría de C*-algebras.
- Funtor: net específica con estructura adicional (covarianza, vacuum, etc.).

**Implicación:** decir "MTC emerge desde net" equivale a decir "categoría emerge desde funtor entre categorías". **La categorialidad se desplaza, no se reduce.**

### 2.2 La localidad y la estructura tensorial de DHR sectors (matiz post-auditoría)

**Análisis del axioma (H2):** $\mathcal{O}_1 \perp \mathcal{O}_2 \Rightarrow [\mathcal{A}(\mathcal{O}_1), \mathcal{A}(\mathcal{O}_2)] = 0$.

**Observación técnica (matizada):** la localidad asegura que la **categoría DHR de superselection sectors** construida a partir de la net + DHR criterion adquiere estructura **monoidal simétrica** (o trenzada en bajas dimensiones) — vía Doplicher-Roberts theorem. La estructura monoidal canónica vive en **la categoría DHR sectors**, NO en el funtor net per se (corrección post-auditoría imparcial).

**Implicación correcta:** la conexión axioma-localidad ↔ tensor categorial es **vía construcción** de DHR sectors + DR theorem, no definicional sobre la net misma. Esto sigue siendo conexión técnica fuerte, pero NO equivale a "la net misma ES tensorial".

### 2.3 Complete rationality codifica modularidad

**En conformal nets 1+1D**, la modularidad de la categoría DHR requiere (Kawahigashi-Longo-Müger 2001):
- **Split property:** $\mathcal{A}(I_1) \vee \mathcal{A}(I_2) \cong \mathcal{A}(I_1) \otimes \mathcal{A}(I_2)$ para $I_1, I_2$ disjuntos.
- **Strong additivity.**
- **Finite μ-index** (índice de Jones global finito).

**Análisis de complete rationality:**

- **Split property** = la net se "factoriza" en regiones disjuntas. Esto **es exactamente** la propiedad de **separación tensorial** que define una BFC con coproducto bien-definido. **Codifica la estructura tensorial.**
- **Finite μ-index** = el conjunto de sectores irreducibles es finito-dimensional. Esto es **exactamente** la condición de **fusión finita** de una fusion category. **Codifica la finitud categorial.**
- **Strong additivity** = condición técnica que asegura que la categoría es **rigid** (todo objeto tiene dual).

**Conclusión técnica (matizada post-auditoría):** las propiedades complete rationality (split + finite μ-index + strong additivity) son **equivalentes** a propiedades categoriales (separación tensorial + fusión finita + rigidez) vía Kawahigashi-Longo-Müger 2001. **Esta equivalencia es bidireccional** — no determina dirección epistémica única. Decir "input categorial disfrazado" sería **invertir** la equivalencia sin warrant.

**Lo que sí se puede afirmar honestamente:** complete rationality es restricción técnica fuerte sobre la net, equivalente categóricamente a propiedades de fusion category finita. Para que MTC modular emerja, **la net debe satisfacer condiciones que en su forma categorial codifican modularidad**. Esto **no es trivialmente "input puesto a mano"**, pero **tampoco es "modularidad emergente desde estructura genérica"**. Es **una equivalencia matemática** entre dos maneras de imponer la misma restricción.

### 2.4 El grupo gauge $G$ es output abstracto, no SM específico

**Doplicher-Roberts theorem produce:**
- Existencia de **algún** grupo compacto $G$.
- El grupo $G$ se reconstruye desde la categoría de sectores observada.

**Lo que el theorem NO produce:**
- $G = SU(3) \times SU(2) \times U(1)$ específicamente.
- $G = SO(10)$ específicamente.
- 3 generaciones, masas, mixing.

**Para reproducir SM, se requiere:**
- Una **net específica** que codifique el SM. Pero las nets se construyen heurísticamente desde Lagrangianas SM perturbativas — i.e., **el SM se asume desde el inicio**.
- Las nets fundamentales para SM **no han sido construidas rigurosamente** (problema abierto Yang-Mills + mass gap, problema Clay milenio).

**Implicación:** mismo problema epistémico que NCG (C.γ) — el grupo gauge específico es input fenomenológico, no derivación a priori.

### 2.5 Tannaka-Krein es equivalencia, no derivación

**Doplicher-Roberts theorem es Tannaka-Krein generalizado:** establece **equivalencia categorial** entre:
- Categoría DHR de superselection sectors.
- $\text{Rep}(G)$ para algún grupo compacto $G$.

Una equivalencia categórica **NO genera categorialidad desde no-categorialidad** — **establece dualidad** entre dos descripciones del mismo objeto matemático.

**Análogo:** Tannaka-Krein original dice $G \leftrightarrow \text{Rep}(G)$. No deriva grupos desde no-grupos. Solo dualiza.

**Implicación:** DR theorem **no constituye derivación de estructura categorial desde algo pre-categorial**. Es reformulación dual sofisticada.

---

## 3. Limitación crítica: AQFT 4D no-trivial no existe rigurosamente

### 3.1 El estado actual

**Buchholz-Fredenhagen 2023** (review oficial, Encyclopedia of Mathematical Physics, arXiv:2305.12923):

> *"Not a single relevant example of interacting QFT in spacetime dimensions 4 or greater is known"* en formulación AQFT estricta de C*-algebras locales.

**Modelos AQFT no-triviales rigurosamente construidos:**
- **2D:** Glimm-Jaffe φ⁴, modelos integrables.
- **3D:** modelos topológicos 2+1D.
- **4D libre:** Maxwell, Klein-Gordon.
- **4D interacting:** **NINGUNO conocido rigurosamente.**

### 3.2 Implicación crítica para H-004 (matizada post-auditoría — D8.d aplicada)

**Estado actual de AQFT 4D interacting (honesto, no exagerado):**
- El SM existe en 3+1D.
- **AQFT 4D interacting no se ha construido rigurosamente** — problema abierto Clay millennium (Yang-Mills + mass gap).
- **Esto es bloqueo práctico-actual, NO imposibilidad estructural demostrada.** D8.d distinción aplicada: "no construido rigurosamente" ≠ "estructuralmente imposible".
- pAQFT (perturbative AQFT, Brunetti-Fredenhagen-Rejzner) **maneja SM perturbativamente** — pero esto es **entrega del contenido SM como input lagrangiano**, no derivación.

**Conclusión honesta:** DHR/AQFT no está actualmente "cerca" del SM rigurosamente. NCG captura SM cualitativamente con input algebraico; AQFT 4D interacting es problema abierto. **No se afirma imposibilidad estructural** — solo estado actual de literatura.

### 3.3 Buchholz-Roberts 2014 — extensión necesaria

**DHR criterion estrictamente excluye QED:** la carga eléctrica se mide por flux a través de esferas asintóticas, no es localizable en regiones acotadas. Buchholz-Fredenhagen extendieron con **sectors localizables en cones** — pero esto **requiere asumir más estructura, no menos**.

**Implicación:** incluso para QED (mucho más simple que SM), DHR estricto falla. Para SM completo, requeriría extensiones más sofisticadas — todas postuladas, no derivadas.

---

## 4. Comparación con C.β' (WPP) y C.γ (NCG)

### 4.1 Tabla comparativa post-S91

| Aspecto | C.β' (WPP-hypergraphs) | C.γ (NCG Connes) | C.β'' (DHR/AQFT) |
|---|---|---|---|
| **Input estructural** | Reglas de reescritura WPP + tensor monoidal canónico | Triple espectral + axiomas + KO-dim + $k=4$ + $D_F$ con Yukawa | Net de Haag-Kastler + axiomas (H1-H6) + DHR criterion |
| **¿Categorialidad emerge libre?** | NO (categoría queda simétrica, no modular) | NO (input álgebra $\mathcal{A}_F$ específica) | NO (net es ya funtor categorial; localidad codifica tensor) |
| **¿Captura SM cualitativo?** | NO | **SÍ** (con input) | NO en sentido riguroso (4D interacting bloqueado) |
| **¿Predice SM cuantitativo?** | NO | NO (Yukawa input) | NO ($G$ abstracto, no $SU(3)\times SU(2)\times U(1)$) |
| **Madurez del programa** | 6 años | 30+ años | 60+ años |
| **Crisis empírica** | N/A | Higgs 125 GeV | Yang-Mills 4D (Clay millennium) |
| **Naturaleza del input** | Combinatoria | Algebraica-axiomática | **Operacional-relacional** |

### 4.2 Diferencia estructural en naturaleza del input

**Importante distinguir:** los tres formalismos requieren input, pero la **naturaleza** del input difiere:

- **C.β' (WPP):** input combinatorio (reglas de reescritura, multiway). Estructura cercana a "información combinatoria pura".
- **C.γ (NCG):** input algebraico-axiomático (álgebra finita + axiomas + operador Dirac). Estructura cercana a "matemática pre-existente".
- **C.β'' (DHR/AQFT):** input **operacional-relacional** (net de regiones + localidad + covarianza + vacuum). Estructura cercana a "estructura física postulada".

**Pregunta epistémica honesta:** ¿es alguno de estos inputs "menos categorial" que los otros?

**Respuesta tentativa:** los tres son **input categorial implícito** en distinto disfraz. La net de Haag-Kastler **es** un funtor categorial (objeto de Cat-Alg). La elección de qué net específica codifica SM es post-hoc igual que en NCG.

### 4.3 Observación filosófica especulativa (Regla 4 — analogía no demostrada — NO producto)

**Observación filosófica especulativa:** la pregunta "¿la categorialidad emerge desde no-categorialidad?" **podría** ser estructuralmente mal planteada. Cualquier formalismo matemáticamente potente para reproducir SM probablemente sea expresable categorialmente.

**ESTA ES OBSERVACIÓN ESPECULATIVA, NO REFORMULACIÓN OPERACIONAL DE A-005.** Marcar explícitamente:
- **Regla 4 honesta:** la observación es **analogía sobre 7 formalismos examinados**, NO derivación de imposibilidad universal.
- **Regla 5 honesta:** A-005 NO se ha refutado — sigue siendo conjetura abierta sobre primacía informacional ontológica.
- **NO PRODUCTO:** esta observación NO es "reformulación de A-005 hacia limitación estructural" como entregable del programa H-004. Es conjetura abierta filosófica sobre el espacio de formalismos posibles.

**Lo que sí se puede afirmar honestamente sobre los 7 formalismos examinados:**
- 7 formalismos examinados (Levin-Wen, Kitaev, Turaev-Viro, ZX, WPP, NCG, DHR/AQFT) requieren input estructural calibrado.
- HoTT, ∞-categorías (Lurie), univalent foundations (Voevodsky), cohesive HoTT (Schreiber), y otros formalismos avanzados **NO han sido examinados** — generalización al espacio completo de formalismos NO está justificada.

**A-005 sigue siendo conjetura abierta** — operacionalmente NO producida en formalismos examinados, filosóficamente NO refutada.

---

## 5. Síntesis técnica (sin auto-asignar veredicto)

### 5.1 Lo que el análisis S91 muestra

**Resultados técnicos:**
1. **Net de Haag-Kastler es ya funtor categorial sofisticado** — el sustrato mismo de DHR/AQFT no es pre-categorial.
2. **Axiomas Haag-Kastler (H1)-(H6) codifican estructura tensorial implícita** — localidad ≡ separación tensorial, covarianza ≡ acción de grupo simétrico estructural.
3. **Complete rationality es input categorial disfrazado** — split property + finite μ-index + strong additivity codifican fusión finita y descomposición tensorial.
4. **Doplicher-Roberts theorem es Tannaka-Krein generalizado** — equivalencia entre dos descripciones, no derivación de categorialidad desde no-categorialidad.
5. **Grupo gauge $G$ es output formal abstracto, no SM específico** — mismo problema que NCG.
6. **Limitación 4D crítica:** AQFT 4D interacting no-trivial no existe rigurosamente. DHR/AQFT está estructuralmente bloqueado para SM.

### 5.2 Lo que el análisis S91 NO muestra

**Honesto:**
1. **No se ha demostrado** que TODOS los formalismos posibles requieren input categorial — sólo los tres examinados (WPP, NCG, AQFT) más los 4 cercanos a C.β' (Levin-Wen, Kitaev, Turaev-Viro, ZX).
2. **No se ha refutado A-005** como afirmación ontológica — sólo como afirmación operacional sobre derivabilidad a priori del SM.
3. **No se ha demostrado** que la naturaleza específica del input (combinatorio/algebraico/operacional) sea estructuralmente equivalente — los tres son **categoriales implícitos**, pero pueden tener diferencias técnicas relevantes.
4. **No se ha demostrado** imposibilidad universal — sólo se ha identificado patrón en formalismos examinados.

### 5.3 Implicación para programa H-004 (matizada post-auditoría)

**Sub-tareas C.β' + C.γ + C.β'' producen evidencia parcial** sobre la pregunta foundational:

- **Sobre los 7 formalismos examinados:** todos requieren input categorial-estructural calibrado.
- **Tres formalismos "mejor candidatos" (NCG, WPP, DHR/AQFT) confirmados** con problema epistémico análogo en este conjunto.
- **AQFT 4D interacting:** problema abierto Clay millennium — bloqueo práctico-actual, NO imposibilidad estructural demostrada.

**Limitación crítica del análisis (Regla 4 honesta):** **NO se examinaron** formalismos avanzados (HoTT, ∞-categorías Lurie, univalent foundations Voevodsky, cohesive HoTT Schreiber). La generalización a "todos los formalismos posibles" **NO está justificada**. La conclusión honesta es: **patrón observado en los 7 formalismos examinados; pregunta sobre dominio completo queda abierta**.

**Decisión sobre programa H-004 NO se asigna en S91.** Posibilidades post-auditoría (sin presentar ninguna como producto):
- **C.δ síntesis honesta** + reservar A-005 como conjetura abierta + mantener SCG estándar como marco operativo. Esta es opción minimalista — reconocer que 7 formalismos no agotan el espacio, evitar generalización injustificada.
- **Examen adicional** de formalismos avanzados (HoTT, ∞-cats, etc.) antes de C.δ — extiende el dominio examinado.
- **Retreat completo H-004** — basado en 7 formalismos examinados con patrón consistente. Riesgo: prematuro.

**A-005 NO se reformula como producto del programa.** Sigue siendo conjetura abierta filosóficamente.

---

## 6. Auditoría D1-D10 + D7.h internalizada (sin auto-celebración)

### 6.1 D1 anti-vacuidad

**¿Hay contenido derivativo propio?**
- §2.1 análisis del net como funtor: contenido derivativo (no estaba explícito en literatura primaria).
- §2.2 análisis localidad ≡ tensor implícito: argumento técnico propio.
- §2.3 análisis complete rationality como input categorial: argumento propio basado en literatura.
- §2.5 análisis Tannaka-Krein como equivalencia (no derivación): observación técnica propia.
- §3 limitación 4D: bien documentada en literatura, integrada al análisis.
- §4 comparación con C.β'/C.γ: contenido propio.

**Veredicto pendiente de auditoría imparcial.** D7.e respeta delegación.

### 6.2 D2 correspondencia IR — N/A

### 6.3 D3 extensiones justificadas

**¿Examinó DHR/conformal nets/AQFT explícitamente?** ✓. Esta es exactamente la respuesta a la observación auditor S88+S89+S90.

**Veredicto:** cumple D3 + D7.h provisional (omisión examinada explícitamente, no solo reconocida).

### 6.4 D4 falsabilidad — N/A

### 6.5 D5 auditoría periódica

**Estado pre-S91:** ACTIVADO EN SENTIDO FUERTE (5 FUERTE + 2 MODERADO post-S90).

**S91 puede:** (a) atenuar trigger si caveat es leve; (b) mantener si moderado; (c) agravar si fuerte.

**Veredicto pendiente** de auditoría imparcial adaptativa.

### 6.6 D6 + D6.d-f auditoría adaptativa

**Pendiente** — invocación obligatoria post-este documento. Auditor adaptativo debe:
- Verificar D7.a-h cumplidos.
- Buscar mutaciones nuevas (5ta generación si emerge).
- Vigilar 4.a (performatividad delegación) y 4.b (reconocimiento ritualizado — esta debería estar resuelta tras examen DHR).

### 6.7 D7.a-g sin auto-celebración

**Verificación interna:**
- Sin "K-005 ejemplar Nma vez" ✓
- Sin "Regla 9 ejemplar" ✓
- Sin "honestidad anti-inflación máxima" ✓
- Sin "Logro técnico/comparativo" ✓
- Sin auto-equiparación con benchmark máximo (Distler-Garibaldi, K-028) ✓
- Sin "CERRADA LIMPIAMENTE" ✓
- Sin "contribución incluso en retreat" ✓
- Lenguaje neutro ✓

**Verificación externa pendiente.**

### 6.8 D7.h provisional — examinada, no solo reconocida

**Cumplido por la existencia misma de S91.** Este documento examina explícitamente DHR/AQFT con análisis técnico, no solo "reconoce que es importante para sesión futura".

### 6.9 D8 distinción cierre positivo vs negativo

**Cierre evaluativo** análogo a C.γ — DHR/AQFT presenta el problema epistémico análogo, el formalismo no produce SM específico desde no-categorialidad pura. Pero esto se afirma con caveats explícitos sobre lo que NO se ha demostrado.

### 6.10 D9 + D10

- **D9:** Regla 9 NO se invoca. ✓
- **D10:** sin cifras de probabilidad manufacturadas. Estimaciones cualitativas marcadas.

---

## 7. Estatus tras auditoría imparcial S91

**Veredicto del auditor imparcial:** **CAVEAT MODERADO** (3ra recalibración consecutiva — mejora estructural sostenida).

**Hallazgos del auditor:**
- D7.h provisional **CUMPLIDO sustantivamente** — DHR examinada, no solo reconocida. **M-04 (4.b) descartada**.
- D7.a-g APROBADOS LIMPIO operacionalmente.
- **Mutación 5ta tentativa 5.b detectada:** reformulación de A-005 vendida como producto. Versión inicial recalibrada para evitar consolidación.
- §2.2-§2.3, §3.2, §4.3 con framing tendencioso o D8.d violación — **recalibrados** en este documento.

**Decisión adoptada:** **Opción A del auditor** — S92 = C.δ síntesis honesta SIN adoptar "reformulación de A-005" como producto.

**Ver auditoría completa:** `notes/H-004_sesion91_auditoria_C_beta_prima_prima.md`.

---

## 8. Referencias clave (subset crítico)

- **Doplicher-Roberts 1989:** "A new duality theory for compact groups", Inventiones Math. 98:157-218.
- **Doplicher-Roberts 1990:** "Why there is a field algebra with a compact gauge group...", CMP 131:51-107.
- **Fredenhagen-Rehren-Schroer 1989:** "Superselection sectors with braid group statistics", CMP 125:201-226.
- **Longo-Rehren 1995:** "Nets of subfactors", arXiv:hep-th/9411077.
- **Kawahigashi-Longo-Müger 2001:** "Multi-interval subfactors and modularity in CFT", arXiv:math/9903104.
- **Müger 2003:** "From subfactors to categories and topology II", arXiv:math/0111205.
- **Halvorson-Müger 2007:** "Algebraic Quantum Field Theory", arXiv:math-ph/0602036.
- **Buchholz-Fredenhagen 2023:** "AQFT: objectives, methods, and results", arXiv:2305.12923.
- **Brunetti-Fredenhagen-Rejzner 2025:** "pAQFT and beyond", arXiv:2512.14227.
- **Buchholz-Roberts 2014:** "New light on infrared problems", CMP 330:935-972.

---

**Fin sub-tarea C.β'' análisis técnico inicial. Pendiente: auditoría imparcial obligatoria adaptativa (D6.d).**
