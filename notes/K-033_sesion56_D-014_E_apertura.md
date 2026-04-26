# K-033 / D-014 escrita + Sub-tarea E APERTURA: jerarquía Yukawa via geometría del lattice WW

- **Fecha:** 2026-04-25 (sesión 56)
- **Sub-fase:** D-014 (síntesis A-D escrita) + E.1 (apertura sub-tarea E).
- **Estado al inicio:** S55 cerró D con K-041 candidato caveat moderado. Plan S55: D-014 + E.1.
- **Objetivo de sesión:** (1) registrar D-014 escrita; (2) abrir sub-tarea E formalmente; (3) análisis preliminar de 4 caminos; (4) selección camino primario para S57+.
- **Disciplina:** sesión de transición. D-014 = síntesis sin contenido nuevo. E.1 = exploración.
- **Aplica K-005 + Regla 5 + Regla 9:** sin promesas prematuras. Anticipar caveats honestamente.

---

## 1. D-014 escrita: síntesis programa K-033 sub-tareas A-D

### 1.1 Documento creado

**Archivo:** `logic/derivations/D-014_programa_K-033_sintesis_A-D.md` (~340 líneas).

**Contenido:**
- Enunciado integrador A + B + C + D.
- Derivación por bloques (D-013 + K-039 + K-040 + K-041).
- Alcance/limitaciones con caveats acumulados.
- Consecuencias: hito programa, calibración 4 niveles epistémicos.
- Literatura: convergencia con Wang-Wen 2018, Witten 1985, Slansky 1981, Pendleton-Ross 1981, BHL 1990.
- Implicaciones: habilita E + F.
- Apéndices: promociones K, evolución probabilidad, calibración niveles.

### 1.2 Resultado meta de D-014

**Calibración epistémica nueva:** SCG genera **4 niveles diferenciados de candidatos K**:

| Nivel | Definición | Ejemplos |
|---|---|---|
| 1. Confirmado limpio | Predicción + verificación + sin caveats fuertes | 30 K + K-032 caveat cuantitativo |
| 2. Candidato limpio | Forma + estructura sólidas; promoción pendiente validación | K-027, K-029, K-031, K-037, K-038 |
| 3. Candidato caveat moderado | Forma + valor numérico predichos con asunciones plausibles | K-035, K-036, **K-041** |
| 4. Candidato caveat fuerte | Forma sí, valor numérico no (problema BSM compartido) | K-034, K-039, K-040 |

D-014 documenta esta jerarquía como **propiedad estructural del marco SCG**.

### 1.3 Inventario post-D-014

- **30 K confirmados** (sin cambio).
- **8 K candidatos** (K-034 a K-041).
- **14 derivaciones formales** (D-001 a D-013 + **D-014 nuevo**).
- **3 hipótesis activas** (sin cambio).

---

## 2. Sub-tarea E APERTURA — Definición del problema (E.1.1)

### 2.1 Recapitulación: lo que se necesita derivar

**Datos observacionales (jerarquía Yukawa SM):**

| Fermión | Masa (MeV) | $y$ (a $M_Z$) | $y/y_t$ |
|---|---|---|---|
| top ($t$) | 173,000 | 0.99 | 1.00 |
| bottom ($b$) | 4,180 | 0.024 | 0.024 |
| charm ($c$) | 1,275 | 0.0073 | 0.0074 |
| tau ($\tau$) | 1,777 | 0.010 | 0.010 |
| strange ($s$) | 95 | 5.4 × 10⁻⁴ | 5.4 × 10⁻⁴ |
| muon ($\mu$) | 106 | 6.1 × 10⁻⁴ | 6.1 × 10⁻⁴ |
| down ($d$) | 4.7 | 2.7 × 10⁻⁵ | 2.7 × 10⁻⁵ |
| up ($u$) | 2.2 | 1.3 × 10⁻⁵ | 1.3 × 10⁻⁵ |
| electron ($e$) | 0.511 | 2.9 × 10⁻⁶ | 2.9 × 10⁻⁶ |
| neutrinos | $\lesssim 10^{-3}$ eV | $\lesssim 10^{-13}$ | $\lesssim 10^{-13}$ |

**Rango de jerarquía:** $y_t/y_e \approx 3.4 \times 10^{5}$. Si neutrinos: $y_t/y_\nu \gtrsim 10^{13}$.

### 2.2 Predicción S53: $d_{LR}$ geométrico

De sim004 (S53):

| Fermión | $y/y_t$ | $d_{LR}$ gauss | $d_{LR}$ exp |
|---|---|---|---|
| $y_t$ | 1.0 | 0 | 0 |
| $y_b$, $y_\tau$ | $\sim 10^{-2}$ | $4.3 \ell_s$ | $8 \ell_s$ |
| $y_\mu$, $y_s$, $y_c$ | $\sim 10^{-3}$-$10^{-4}$ | $5-6 \ell_s$ | $11-13 \ell_s$ |
| $y_u$, $y_d$ | $\sim 10^{-5}$ | $\sim 7 \ell_s$ | $\sim 17 \ell_s$ |
| $y_e$ | $2.9 \times 10^{-6}$ | $7.4 \ell_s$ | $19 \ell_s$ |
| neutrinos | $\sim 10^{-13}$ | $\sim 16 \ell_s$ | $\sim 50 \ell_s$ |

**Banda predicha:** $d_{LR} \in [0, 20] \ell_P$ (y hasta $50 \ell_P$ para neutrinos).

### 2.3 Pregunta central de sub-tarea E

> **¿Qué estructura del lattice trivalente 3+1D SCG produce nueve valores específicos de $d_{LR}$ que reproducen la jerarquía Yukawa observada del SM?**

Sub-pregunta crítica: ¿es **emergente** la separación $d_{LR}$ desde la geometría del lattice, o es **postulable** (paramétrica)?

- **Emergente:** SCG predice cuantitativamente $d_{LR}$ desde estructura. → K-042 candidato cuantitativo. Probabilidad ~30%.
- **Postulable parcialmente:** SCG da el rango/forma pero no los valores específicos. → K-042 candidato con caveat moderado. Probabilidad ~40%.
- **Postulado:** SCG no deriva $d_{LR}$ específicos. → K-042 candidato con caveat fuerte (análogo K-040). Probabilidad ~30%.

### 2.4 Restricciones del marco SCG

**Restricciones inmovibles:**

1. **D = 4** (D-005 + K-022 + K-036 + D-012). NO extra dimensions extras.
2. **Lattice WW sobre `Spin(10)_1`** (D-010, D-013).
3. **1 generación** estructural (K-039); 3 generaciones requieren mecanismo.
4. **Caveat fuerte K-040** sobre $v_{EW}$ — no ataca jerarquía gauge en E.

Cualquier camino para E debe respetar estas restricciones.

---

## 3. Análisis preliminar de 4 caminos (E.1.2)

### 3.1 Camino (a): Bilson-Thompson trenzas

**Idea:** las 3 generaciones SM corresponden a **3 trenzas distintas en el grupo $B_3$** (trenzas de 3 cuerdas), cada una con twists ±1/3 que codifican carga eléctrica (Bilson-Thompson 2005, arXiv:hep-ph/0503213).

**Aplicación a SCG:**
- Las "ribbons" de Bilson-Thompson corresponden a las "etiquetas" de las cuerdas SCG.
- Las trenzas más complejas tienen estructura interna mayor → $d_{LR}$ efectivo mayor → Yukawa menor.
- Conexión natural con K-014 (U(1) momento angular) + K-015 (carga 1/3 trivalente).

**Fortalezas:**
- ✅ Mecanismo concreto para 3 generaciones (resuelve K-039 caveat fuerte parcialmente).
- ✅ Topológico — compatible con D-010 y D-013.
- ✅ Conexión histórica con LQG (Bilson-Thompson, Markopoulou, Smolin 2007 CQG 24 3975).

**Debilidades:**
- ⚠️ Bilson-Thompson predice **4 generaciones** (incluyendo neutrinos pesados Dirac), no 3 chirales.
- ⚠️ El conteo de 3 trenzas no-equivalentes en $B_3$ proviene de **dinámica $B_3$**, NO de espacio de fusión MTC (S47).
- ❌ Espacios de fusión $V_{27,27,27}$ en `(E_6)_1` son 1-dim (S47); no soportan estructura de 3 trenzas no-equivalentes naturalmente.

**Probabilidad cierre exitoso:** ~25%.

**Resultado más probable si camino (a):** K-042 candidato con caveat moderado/fuerte por la incompatibilidad parcial trenzas-MTC.

### 3.2 Camino (b): Bulk WW dimensional efectivo

**Idea:** el lattice trivalente 3+1D SCG admite una **"dimensión efectiva"** (no espacial, sino categórica o de etiqueta) en la cual los defectos $L$ y $R$ pueden separarse. La separación $d_{LR}$ vive en este espacio interno.

**Aplicación a SCG:**
- Espacio interno: $\mathbb{Z}_4$ (centro de Spin(10)) o $\mathbb{Z}_3$ (centro de E_6) o U(1) (rep $1_4$ de E_6 decomposition).
- Las generaciones distintas serían distintas "ubicaciones" en el espacio interno.
- $d_{LR}$ = distancia métrica efectiva en el espacio interno.

**Fortalezas:**
- ✅ Compatible con $D=4$ (no añade dimensiones espaciales).
- ✅ Conexión natural con la decomposición $27 = 16_1 \oplus 10_{-2} \oplus 1_4$ (K-039).
- ✅ El espacio interno U(1) (rep $1_4$) es naturalmente continuo — admite jerarquía continua de $d_{LR}$.

**Debilidades:**
- ⚠️ Requiere "métrica" en el espacio interno U(1) — postulable, no derivable.
- ⚠️ La normalización del U(1) interno respecto a $\ell_P$ es ambigua.
- ⚠️ ¿Por qué hay exactamente 3 generaciones y no más? K-039 caveat fuerte sigue presente.

**Probabilidad cierre exitoso:** ~25%.

**Resultado más probable si camino (b):** K-042 candidato con caveat moderado por la métrica postulada.

### 3.3 Camino (c): Extensión K-K-like efectiva (Froggatt-Nielsen)

**Idea:** los Yukawas del SM son suprimidos por escalas de **flavor** $M_F$ inducidas por modos altos del lattice WW (Froggatt-Nielsen 1979). Para fermión $f$:
$$
y_f \sim \left(\frac{v_{EW}}{M_F}\right)^{n_f}
$$
donde $n_f$ es el "número de flavor" y $M_F \gg v_{EW}$.

**Aplicación a SCG:**
- Modos altos del lattice WW (excitaciones de tipo $v$, $s$, $c$ con $L \cdot d^2 \neq V_{BH}$) = "scalar flavons" de Froggatt-Nielsen.
- $n_f$ corresponde al número de "fusiones intermedias" del defecto fermion antes de acoplarse al condensado.
- Para electrón: $n_e \sim 6$, $M_F \sim 10^{2-3}$ GeV → $y_e \sim (246/M_F)^6 \sim 10^{-6}$. ✓

**Fortalezas:**
- ✅ Reproduce jerarquía Yukawa cualitativamente (F-N standard).
- ✅ Compatible con MTC abeliano (modos altos como "flavon scalars").

**Debilidades:**
- ⚠️ Requiere identificar **flavon mass scale** $M_F$ desde SCG. ¿De dónde sale numéricamente?
- ❌ Equivalente a postular una nueva escala de energía (similar a heteróticas).
- ❌ Frommann-Nielsen original no predice los $n_f$ — son postulados.

**Probabilidad cierre exitoso:** ~20%.

**Resultado más probable si camino (c):** K-042 candidato con caveat fuerte (similar a K-040).

### 3.4 Camino (d): Caveat fuerte aceptado

**Idea:** la jerarquía Yukawa requiere postulado adicional (análogo K-040 para $v_{EW}$).

**Aplicación:**
- Forma funcional sí: $y = |\mathcal{A}| \cdot \xi_{\text{loc}}$ (S52, S53).
- Valor numérico de $\xi_{\text{loc}}$ para cada fermión: postulable.
- Análogo a K-040: estructura sí, valores no.

**Probabilidad de adopción si (a)-(c) fracasan:** ~30% (a S62).

**Resultado:** K-042 candidato con caveat fuerte. Sub-tarea E cierra estructuralmente con caveat análogo a B y C.

### 3.5 Tabla resumen 4 caminos

| Camino | Idea | Probabilidad | Resultado más probable |
|---|---|---|---|
| (a) Bilson-Thompson trenzas | 3 generaciones via $B_3$ + twists ±1/3 | ~25% | K-042 caveat moderado/fuerte |
| (b) Bulk WW dimensional | $d_{LR}$ via espacio interno U(1) o $\mathbb{Z}_4$ | ~25% | K-042 caveat moderado |
| (c) K-K-like Froggatt-Nielsen | Yukawas via flavon scalars + $M_F$ | ~20% | K-042 caveat fuerte |
| (d) Caveat fuerte aceptado | Jerarquía requiere postulado | ~30% | K-042 caveat fuerte (análogo K-040) |

**Suma de probabilidades de cierre:** ~80%. **Bloqueo o reformulación:** ~20%.

---

## 4. Selección del camino primario para S57+ (E.1.3)

### 4.1 Análisis comparativo

**Criterios de selección:**

| Criterio | (a) BT | (b) bulk WW | (c) K-K | (d) caveat |
|---|---|---|---|---|
| Compatibilidad con $D=4$ | ✓ | ✓ | ✓ | ✓ |
| Compatibilidad con `Spin(10)_1` MTC | ⚠ | ✓ | ⚠ | ✓ |
| Resuelve K-039 (3 gen)? | parcial | parcial | no | no |
| Predice $d_{LR}$ cuantitativamente? | parcial | mejor | no | no |
| Sin parámetros libres adicionales | no | parcial | no | trivial |
| Conexión histórica | sólida (LQG) | natural (D-010) | postulado externo | trivial |
| Honestidad K-005 | ⚠ | ✓ | ❌ | ✓ |

**Veredicto preliminar:**
- **(b) Bulk WW dimensional** es el más prometedor estructuralmente.
- **(a) Bilson-Thompson** complementa con estructura para 3 generaciones.
- **(c) K-K-like** es el más "exótico" (postula nueva escala) — menos preferido por K-005.
- **(d) Caveat aceptado** es el plan B si (a)+(b) fracasan.

### 4.2 Decisión

**Camino primario para S57+:** **combinación (b) + (a) — bulk WW dimensional como mecanismo principal, con Bilson-Thompson trenzas como auxiliar para 3 generaciones.**

**Justificación:**

1. **Compatibilidad estructural máxima:** ambos compatibles con $D=4$, lattice WW, MTC `Spin(10)_1`/`(E_6)_1`.
2. **Sinergia:** (b) provee la métrica de $d_{LR}$; (a) provee la estructura de 3 generaciones.
3. **Honestidad K-005:** ambos usan estructura que ya está en el marco — no postulan nuevo contenido.
4. **Conexión histórica:** Bilson-Thompson + LQG (Bilson-Thompson, Markopoulou, Smolin 2007); bulk WW + Walker-Wang/Wen (D-010, K-019).

**Riesgos identificados:**

- (b) requiere métrica en espacio interno — el aspecto más sensible.
- (a) tiene incompatibilidad parcial trenzas-MTC (S47); mitigar con análisis cuidadoso.

### 4.3 Plan S57+

| Sesión | Sub-fase | Objetivo |
|---|---|---|
| 57 | E.2 (camino primario, fase 1) | Análisis técnico de "bulk WW dimensional": ¿es U(1) interno o $\mathbb{Z}_4$ centro? Métrica en este espacio. |
| 58 | E.3 (camino primario, fase 2) | Cálculo de $d_{LR}$ predichos para 3 generaciones (anticipo: distribución dimensional con escala $\sim 7 \ell_P$). |
| 59 | E.4 (Bilson-Thompson auxiliar) | ¿Las 3 trenzas $B_3$ no equivalentes corresponden a 3 generaciones? Análisis de incompatibilidad parcial (S47). |
| 60 | E.5 (comparación con SM) | Comparación cuantitativa con $y/y_t$ observado. Análisis de sensibilidad. |
| 61 | E.6 (decisión) | K-042 candidato si camino primario funciona; o pivot a camino secundario. |
| 62 | E.7 (pivot si necesario) | Camino alternativo (c) o caveat fuerte (d). |

**Hard cap sub-tarea E:** **6-7 sesiones** (S57-S62 + S63 si necesario).

### 4.4 Criterios de aborto/pivot

**Pivot a camino (c) o (d) si:**
- En S57: la "métrica en espacio interno" no se puede definir sin parámetros libres extra.
- En S58: los $d_{LR}$ calculados no caen en el rango $[5, 20] \ell_P$.
- En S59: incompatibilidad trenzas-MTC es prohibitiva.

**Caveat fuerte (camino d) si:**
- Hasta S62: ningún camino produce predicción cuantitativa.

---

## 5. Veredicto sesión 56

### 5.1 Logros

- ✅ **D-014 escrita** como síntesis formal del programa K-033 sub-tareas A-D.
- ✅ **Sub-tarea E formalmente abierta** con definición clara del problema cuantitativo.
- ✅ **4 caminos para E analizados** sistemáticamente con probabilidades estimadas.
- ✅ **Camino primario seleccionado:** combinación (b) bulk WW dimensional + (a) Bilson-Thompson trenzas.
- ✅ **Plan S57-S62/63 trazado** con criterios de aborto/pivot.
- ✅ **Inventario derivaciones:** **14** (D-001 a D-014).
- ✅ **Calibración 4 niveles epistémicos SCG** documentada formalmente en D-014.

### 5.2 No-logros (intencional)

- ❌ NO se promueve K-042 (eso es S61 si procede).
- ❌ NO se calcula nada cuantitativo nuevo (S57+).
- ❌ NO se inventa mecanismo exótico (K-005 + Regla 9 preventiva).

### 5.3 Disciplina

- **K-005:** los 4 caminos analizados usan estructura ya en el marco. (c) y (d) marcados como "menos preferidos por K-005".
- **Regla 5:** probabilidades estimadas honestamente. ~30% caveat fuerte aceptado.
- **Regla 9 (preventiva):** plan con criterios de pivot explícitos antes de comprometerse.
- **D-014 disciplinada:** síntesis sin contenido nuevo. K-005 + Regla 5.

### 5.4 Patrón consolidado

D-014 + apertura E sigue el patrón maduro de SCG: cierre de bloque → síntesis formal → apertura siguiente con análisis honesto. Misma disciplina que en sub-tareas A, B, C, D.

---

## 6. Próxima sesión (57)

**Objetivo:** **E.2 — fase 1 del camino primario (bulk WW dimensional).**

**Sub-pasos:**
1. Identificar el "espacio interno" relevante: ¿U(1) (rep $1_4$ de E_6 decomposition)? ¿$\mathbb{Z}_4$ (centro Spin(10))? ¿Otro?
2. Definir la métrica en este espacio: ¿escala fundamental $\ell_F$? ¿es $\ell_P$ por holografía?
3. Identificar la "ubicación" de los defectos $L$ y $R$ en el espacio interno para fermiones SM.
4. Estimación dimensional preliminar: ¿caen los $d_{LR}$ en $[0, 20] \ell_F$?

**Lecturas focalizadas para sesión 57:**
- D-014 (síntesis, base de partida).
- Walker-Wang 2011 (bulk + frontera).
- Wen 2003 (string-net 3+1D + emergencia SM).
- Bilson-Thompson 2005, Bilson-Thompson-Markopoulou-Smolin 2007 (preparación E.4).
- D-013 (estructura `Spin(10)_1`).

**Disciplina S57:** análisis técnico, no compromiso con valores numéricos finales. Si la métrica del espacio interno no se define naturalmente → pivot temprano (S58).

---

## 7. Firma

**Resultado meta sesión 56:**

- **D-014 escrita** — síntesis formal del programa K-033 sub-tareas A-D. **14 derivaciones** en el marco SCG.
- **Calibración epistémica nueva:** 4 niveles de candidatos K (limpio / candidato / caveat moderado / caveat fuerte).
- **Sub-tarea E formalmente abierta** con definición clara del problema, 4 caminos analizados, camino primario seleccionado.
- **Plan S57-S62/63** trazado con criterios de pivot.
- **Probabilidad sub-tarea E:** ~30% K-042 cuantitativo, ~40% caveat moderado, ~30% caveat fuerte. **Hard cap 6-7 sesiones.**

**Inventario post-S56:** 30 K confirmados + 8 candidatos + **14 derivaciones** + 3 hipótesis activas + 4 simulaciones + 10 SVG.

**Probabilidad K-033 éxito parcial:** **55-70% sin cambio significativo** (D-014 es síntesis, no nuevo contenido).

**Sub-tarea E es el siguiente desafío crítico del programa K-033:** la jerarquía Yukawa $y_e/y_t \sim 10^{-6}$ requiere mecanismo geométrico no trivial. Honestidad anticipada: ~30% probabilidad de caveat fuerte.

La teoría continúa.
