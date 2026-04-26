# K-033 / Sub-tarea F, Fase F.1 — Apertura: CKM/PMNS desde fases del MTC `Spin(10)_1`

- **Fecha:** 2026-04-26 (sesión 62)
- **Sub-fase:** F.1 — apertura sub-tarea F del programa K-033 (mezclas CKM/PMNS).
- **Estado al inicio:** S61 cerró sub-tarea E con K-042 caveat moderado. 5/6 sub-tareas K-033 cerradas. F es la última.
- **Objetivo de sesión:** definir CKM/PMNS operacionalmente en SCG; identificar candidatos de fases en MTC; análisis preliminar de abelianidad; estimación dimensional; anticipar caveats.
- **Disciplina:** apertura conceptual disciplinada. K-005: sin postulados nuevos. Regla 4: marcar analogías. Regla 9 (preventiva): plan con criterios pivot.

---

## 1. Recapitulación: CKM y PMNS en el SM (F.1.1)

### 1.1 Origen físico de las matrices de mezcla

En el SM, los Yukawas son **matrices 3×3 complejas en el espacio de generaciones**:
- $Y_u$, $Y_d$: 3×3 matrices para up/down quarks.
- $Y_e$, $Y_\nu$: 3×3 matrices para leptones cargados/neutrinos.

Cada matriz $Y$ se diagonaliza por dos rotaciones unitarias:
$$
Y = U^L \cdot \text{diag}(y_1, y_2, y_3) \cdot (U^R)^\dagger
$$

Las matrices de mezcla físicas surgen del **desfase entre las bases de quarks/leptones**:
$$
V_{CKM} \;=\; (U_u^L)^\dagger \cdot U_d^L \;,\qquad
V_{PMNS} \;=\; (U_e^L)^\dagger \cdot U_\nu^L
$$

### 1.2 Parametrización estándar (CKM, Wolfenstein)

$V_{CKM}$ tiene 4 parámetros físicos:
- 3 ángulos: $\theta_{12} \approx 13.0°$, $\theta_{13} \approx 0.21°$, $\theta_{23} \approx 2.4°$.
- 1 fase CP: $\delta_{CP} \approx 65°$.

**Patrón Wolfenstein:** $\theta_{12} \sim \lambda$, $\theta_{23} \sim \lambda^2$, $\theta_{13} \sim \lambda^3$ con $\lambda \approx 0.225$. **Jerárquico.**

### 1.3 Parametrización estándar (PMNS)

$V_{PMNS}$ tiene 4 (Dirac) o 6 (Majorana) parámetros:
- 3 ángulos: $\theta_{12} \approx 33.5°$, $\theta_{13} \approx 8.6°$, $\theta_{23} \approx 49.0°$.
- 1 fase CP Dirac: $\delta_{CP} \approx 217°$ (preliminar).
- 0-2 fases Majorana (no medidas).

**Patrón:** **NO jerárquico** — todos los ángulos son $O(10°-50°)$. Contraste fuerte con CKM.

### 1.4 Pregunta central de sub-tarea F

> ¿Qué objeto matemático del MTC `Spin(10)_1` codifica las matrices de mezcla $V_{CKM}$ y $V_{PMNS}$ desde la estructura SCG?

**Sub-pregunta crítica:** ¿puede SCG predecir simultáneamente CKM jerárquico **y** PMNS no-jerárquico?

---

## 2. Definición operacional CKM/PMNS en SCG

### 2.1 Setup

En SCG con D-013: 1 generación SM completa = end-points $s$ (extremo $L$) y $c$ (extremo $R$) de cuerdas SCG abiertas etiquetadas. Bajo K-039: las 3 generaciones son 3 copias **postuladas** de la rep 16 (cada una en una "etiqueta de generación" $g \in \{1, 2, 3\}$).

**Yukawa SM en SCG (de K-041 + K-042):**
$$
y_f \;=\; |\mathcal{A}_{sv \to c}^{(f)}| \cdot \xi_{\text{loc}}^{(f)}
$$

donde $f$ específica generación + carga.

### 2.2 Fases ignoradas hasta ahora

En sub-tareas D + E (K-041, K-042) consideramos **solo el módulo** $|\mathcal{A}|$ y $\xi_{\text{loc}}$ — las **fases** $\arg(\mathcal{A}) = \phi_F$ se descartaron como gauge.

**En sub-tarea F estas fases vuelven a ser relevantes:**
$$
\mathcal{A}_{sv \to c}^{(f)} \;=\; |\mathcal{A}^{(f)}| \cdot e^{i \phi_F^{(f)}}
$$

con $\phi_F^{(f)}$ específica del proceso fermiónico.

### 2.3 Mapeo a CKM/PMNS

**Hipótesis tentativa:**

$$
(V_{CKM})_{ij} \;=\; \sum_{\text{procesos}} c_{ij}(\text{proceso}) \cdot e^{i \phi_F(\text{proceso})}
$$

donde la suma es sobre todos los procesos (caminos en el lattice WW) que conectan generación $i$ del up-quark con generación $j$ del down-quark vía un Higgs (cuerda con loop-$v$ entre extremos $s$ y $c$).

**Análogamente para PMNS** con leptones.

### 2.4 ¿Es esta definición plausible?

**Pros:**
- Las fases $\phi_F$ existen en MTC (F-symbols, R-symbols).
- La estructura combinatoria de "sumas de caminos" da posibles mecanismos para mezcla.

**Cons:**
- En MTC abeliana, las fases son **discretas** (raíces de la unidad). Los ángulos físicos son **continuos**.
- No hay mecanismo natural para sumas de caminos con coeficientes $c_{ij}$ continuos.

**Veredicto preliminar:** la definición es **conceptualmente correcta** pero **cuantitativamente limitada** por abelianidad. Esto coincide con la anticipación honesta S61.

---

## 3. Catálogo de candidatos de fases (F.1.2)

### 3.1 Fases disponibles en `Spin(10)_1` MTC

| Tipo | Símbolo | Descripción | Cardinalidad |
|---|---|---|---|
| F-symbols | $F^{abc}_d$ | 3-cociclos $\omega \in H^3(\mathbb{Z}_4, U(1)) = \mathbb{Z}_4$ | 4 clases |
| R-symbols | $R^{ab}_c$ | fases de braiding | $\mathbb{Z}_4$ por canónico |
| Twists | $\theta_a = e^{2\pi i h_a}$ | spin topológico | 4 valores ($h \in \{0, 1/2, 5/8, 5/8\}$) |
| Combinaciones gauge | $F \cdot R$ cíclico | productos en loops cerrados | finita |
| S-matrix | $S_{ab}$ | $4 \times 4$ matriz unitaria | 4 parámetros independientes |

### 3.2 Fases gauge-invariantes

Recordatorio (S52): $F$ y $R$ individuales NO son físicos (gauge-dependientes). **Solo combinaciones gauge-invariantes son físicas.**

**Combinaciones canónicas:**
1. **Twists** $\theta_a$: directamente físicos ($h_a$ son fijos por la MTC).
2. **Productos $F R F^{-1} R^{-1}$ en loops cerrados:** físicos (clase de cohomología).
3. **S-matrix modular:** $S_{ab} = (1/\mathcal{D}) \sum_c (R^{ab}_c)^2 \cdot d_c$ con $\mathcal{D}$ dimensión global.
4. **T-matrix modular:** $T_{ab} = \theta_a \delta_{ab}$.

**Para `Spin(10)_1` (super-MTC fermiónica):**

S-matrix se calcula explícitamente con los datos $\{1, v, s, c\}$:
$$
S \;=\; \frac{1}{2} \begin{pmatrix} 1 & 1 & 1 & 1 \\ 1 & 1 & -1 & -1 \\ 1 & -1 & i & -i \\ 1 & -1 & -i & i \end{pmatrix}
$$

(Forma típica para $\mathbb{Z}_4$ MTC; corrección de signos super-modular omitida).

T-matrix:
$$
T \;=\; \text{diag}(1, -1, e^{5\pi i/4}, e^{5\pi i/4})
$$

### 3.3 Cuántos parámetros físicos hay disponibles

**Recuento honesto:**

- 4 twists $\theta_a$ → 3 fases independientes (hasta normalización global).
- S-matrix: matriz unitaria $4 \times 4$ sujeta a relaciones de Verlinde → ~4 parámetros físicos.
- Total fases gauge-invariantes en `Spin(10)_1` MTC abeliana: **~7 parámetros discretos** (raíces de la unidad).

**Comparación con CKM + PMNS:**
- CKM: 4 parámetros físicos (3 ángulos + 1 fase).
- PMNS: 4 parámetros (Dirac) o 6 (Majorana).
- Total: 8-10 parámetros físicos.

**Aritmética sugerente:** 7 fases discretas vs 8-10 parámetros físicos continuos.

**Pero crucial:** las fases SCG son **discretas** (raíces 4-ésimas), los parámetros físicos son **continuos**. Aritmética no implica función — la abelianidad es **insuficiente** para mapear.

---

## 4. Análisis preliminar de abelianidad (F.1.3)

### 4.1 Limitaciones esperadas

**MTC abeliana → fases puras → ángulos discretos.**

En `Spin(10)_1`:
- F-symbols: $\omega \in \{1, i, -1, -i\}$ (raíces 4-ésimas).
- R-symbols: similares.
- Ángulos generables: $\{0°, 90°, 180°, 270°\}$.

**Comparación con CKM observado:**
- $\theta_{12} \approx 13°$: **muy lejos** de los valores discretos.
- $\theta_{13} \approx 0.2°$: cerca de $0°$ pero no exactamente.
- $\theta_{23} \approx 2.4°$: cerca de $0°$.
- $\delta_{CP} \approx 65°$: cerca de $90°$ pero no exactamente.

**Veredicto:** la abelianidad **NO produce ángulos cuantitativos correctos** sin amplificación adicional.

### 4.2 ¿Hay mecanismo de amplificación?

**Posibles vías:**
1. **Combinación de muchas fases discretas** vía sumas — podría generar ángulos continuos efectivos.
2. **Super-MTC fermiónica $sSpin(10)_1$** con datos super-modulares adicionales.
3. **Cadena de ruptura SO(10) → SU(5) → SM** introduce fases adicionales.
4. **Mezcla con sub-tarea E** (longitudes de cuerda + fases combinadas).

**Probabilidad de éxito por vía:**
- (1) Combinaciones: ~15% — requiere mecanismo específico no derivable.
- (2) Super-MTC: ~10% — caveat técnico estándar.
- (3) Ruptura: ~10% — fases adicionales sin derivación.
- (4) Mezcla con E: ~10% — especulativo.

**Total para K-043 cuantitativo:** ~10% (similar a S61 anticipación).

### 4.3 Conclusión preliminar

**La abelianidad de `Spin(10)_1` MTC limita severamente la expresividad necesaria para CKM/PMNS cuantitativos.**

Sub-tarea F probablemente cierra con **caveat fuerte** (forma funcional sí, valores no), análogo a K-040 (jerarquía gauge no derivada).

---

## 5. Estimación dimensional preliminar (F.1.4)

### 5.1 Generación de ángulos desde fases discretas

Si los ángulos físicos se generan como **combinaciones de fases SCG**:
$$
\theta_{ij} \sim \arg\!\left(\sum_{k} A_{ij,k} e^{i \phi_k}\right)
$$
con $\phi_k \in \{0, \pi/2, \pi, 3\pi/2\}$ y $A_{ij,k}$ amplitudes reales.

**Ejemplo simple:** $\theta = \arg(A_1 + i A_2 e^{i\pi/2}) = \arg(A_1 - A_2)$. Da ángulos continuos si $A_1, A_2$ son continuos.

**Pero:** $A_{ij,k}$ deberían venir de la estructura SCG (longitudes de cuerda, $\xi_{\text{loc}}$, etc.). Esto conecta con K-042.

**Conexión potencial:** los ángulos CKM podrían depender de los $\xi_{\text{loc}}$ (sub-tarea E) Y de las fases F-symbols (sub-tarea F). Esto **podría** generar ángulos continuos no-triviales.

### 5.2 Estimación grosera

Para sector quark con $\xi_u \neq \xi_d$ (S58 K-042):
- $\theta_{ij} \sim |\xi_u - \xi_d| \cdot (\phi_{F,ij}/\pi)$.
- Con $\xi$ del orden $0.01$-$1$ y $\phi_F$ del orden $\pi/2$: $\theta \sim 0.005$-$0.5$ rad = $0.3°$-$30°$.

**Concordancia cualitativa:** $\theta_{12,CKM} \approx 13°$ cae en este rango. **Posible** dentro de orden de magnitud.

Para PMNS con $\xi_e \approx \xi_\nu$ (?): si los neutrinos están menos jerárquicos, los ángulos serían $\sim 30°-50°$ — **consistente con observación**.

**Veredicto:** estimación dimensional **compatible cualitativamente** con CKM jerárquico + PMNS no-jerárquico. **Cuantitativamente incierto.**

### 5.3 Anticipación honesta

- **Probabilidad que SCG produzca CKM jerárquico cuantitativo:** ~10-15%.
- **Probabilidad que SCG produzca PMNS no-jerárquico cuantitativo:** ~10-15%.
- **Probabilidad de cierre con caveat moderado** (forma funcional + concordancia cualitativa): ~30%.
- **Probabilidad caveat fuerte** (estructura sí, valores no): ~50%.
- **Probabilidad bloqueo:** ~10%.

---

## 6. Plan sub-tarea F (S62-S66)

### 6.1 Roadmap

| Sesión | Sub-fase | Objetivo |
|---|---|---|
| **62** | **F.1 (apertura)** | ✅ ESTA SESIÓN |
| 63 | F.2 (cálculo) | Cálculo numérico de fases F y R-symbols `Spin(10)_1`. Combinación con $\xi_{\text{loc}}$ K-042. |
| 64 | F.3 (comparación) | Comparación con CKM/PMNS observados. Análisis incertidumbres. |
| 65 | F.4 (decisión) | K-043 candidato (probablemente caveat moderado o fuerte). |
| 66 | F.5 (cierre + D-015) | Cierre formal sub-tarea F + decisión sobre D-015 (síntesis A-F). |

### 6.2 Camino primario

**Combinación F + E:** los ángulos CKM/PMNS emergen de la **estructura combinada** de fases F-symbols (sub-tarea F) y longitudes de cuerda $\xi_{\text{loc}}$ (sub-tarea E). 

**Justificación:** sub-tarea E da estructura cuantitativa de generaciones; sub-tarea F da fases. Mezcla = ángulos físicos continuos.

### 6.3 Criterios de pivot/aborto

- **Pivot a caveat fuerte (S65):** si las fases discretas no producen ángulos continuos correctos.
- **Aborto temprano (S64):** si ningún cálculo cualitativo da el rango correcto.
- **Cierre exitoso (S65):** K-043 candidato caveat moderado si concordancia cualitativa razonable.

### 6.4 Hard cap

**5 sesiones (S62-S66).** Si F no cierra en S66, **caveat fuerte K-043 aceptado** y D-015 escrita como síntesis honesta.

---

## 7. Veredicto sesión 62

### 7.1 Logros

- ✅ **Sub-tarea F formalmente abierta** con definición operacional clara.
- ✅ **Catálogo de fases en MTC** (F-symbols, R-symbols, twists, S-matrix, T-matrix) con cardinalidades.
- ✅ **Análisis de abelianidad:** limitación severa identificada — fases discretas vs ángulos continuos.
- ✅ **Estimación dimensional preliminar:** combinación F + E podría producir ángulos cualitativos compatibles con CKM/PMNS.
- ✅ **Plan S63-S66 trazado** con criterios pivot.
- ✅ **Probabilidad anticipada honestamente:** ~10% K-043 cuantitativo / ~30% caveat moderado / ~50% caveat fuerte / ~10% bloqueo.

### 7.2 No-logros (intencional)

- ❌ NO se ha calculado nada cuantitativo (S63).
- ❌ NO se ha promovido K-043 (S65).
- ❌ NO se ha postulado mecanismo nuevo (K-005).

### 7.3 Disciplina

- **K-005:** ningún mecanismo exótico. Solo F y R-symbols ya en MTC.
- **Regla 4:** la idea "ángulos = combinaciones de fases discretas" marcada como conjetura, no derivación.
- **Regla 5:** abelianidad severamente limitante reportada honestamente.
- **Regla 9 (preventiva):** plan S63-S66 con pivots y aborto.

### 7.4 Patrón meta

S62 sigue el patrón consolidado: apertura conceptual → catálogo → análisis estructural → estimación → caveat anticipado → plan claro. **Misma disciplina** que aperturas previas (S52, S56).

---

## 8. Próxima sesión (63)

**Objetivo:** **F.2 — cálculo numérico de fases F y R-symbols `Spin(10)_1`. Combinación con $\xi_{\text{loc}}$ K-042.**

**Sub-pasos:**
1. Computar S-matrix y T-matrix de `Spin(10)_1` MTC explícitamente.
2. Identificar las fases gauge-invariantes específicas que codifican CKM/PMNS.
3. Combinar con $\xi_{\text{loc}}^{(f)}$ extraídos S58 (K-042).
4. Cálculo numérico de elementos $V_{CKM}$ y $V_{PMNS}$.
5. Análisis de incertidumbres.

**Lecturas focalizadas:**
- D-013 (estructura `Spin(10)_1`).
- Slansky 1981 §6 (CKM en GUTs).
- Wolfenstein 1983 (parametrización CKM).
- Notas S52-S61 (cadena previa).

**Disciplina S63:** cálculo concreto. Si la abelianidad es prohibitiva → caveat fuerte directo en S64.

---

## 9. Firma

**Resultado meta sesión 62:**

- **Sub-tarea F del programa K-033 ✅ ABIERTA** con definición operacional + catálogo de fases + análisis abelianidad.
- **Insight preliminar:** la abelianidad de `Spin(10)_1` limita severamente expresividad. **Probabilidad caveat fuerte ~50%** anticipada.
- **Camino primario tentativo:** combinación F + E (fases × longitudes) podría generar ángulos continuos.
- **Plan S63-S66** trazado con hard cap y criterios pivot.

**Inventario sin cambios:** 30 K + 9 candidatos + 14 derivaciones + 7 simulaciones + 10 SVG.

**Probabilidad K-033 éxito parcial:** **60-72%** sin cambio (F era anticipada como difícil).

**Sub-tarea F es el último desafío** del programa K-033. Probabilidad caveat fuerte similar a sub-tareas B y C. Si F cierra (cualquier nivel), el programa K-033 se considera completo con D-015 como síntesis A-F.

La teoría continúa.
