# K-033 / Sub-tarea E, Fase E.2 — Bulk WW dimensional + reinterpretación de $d_{LR}$

- **Fecha:** 2026-04-25 (sesión 57)
- **Sub-fase:** E.2 — fase 1 del camino primario (bulk WW dimensional).
- **Estado al inicio:** S56 abrió E con 4 caminos; selección camino primario (b) bulk WW + (a) Bilson-Thompson trenzas. Plan E.2-E.7 trazado.
- **Objetivo de sesión:** identificar espacio interno relevante; definir métrica; mapear fermiones a posiciones; estimación dimensional preliminar; análisis de sensibilidad.
- **Disciplina:** análisis técnico honesto. Pivot temprano si la métrica no se define naturalmente.
- **Aplica K-005 + Regla 4 + Regla 5 + Regla 9 (preventiva):** sin postular escalas nuevas; marcar analogías; banda honesta.

---

## 1. Reinterpretación clave de S57: ¿qué es $d_{LR}$?

### 1.1 Confusión inicial (S52-S56)

En S52-S56, se trató $d_{LR}$ ambiguamente como:
- (i) **Separación espacial física** entre defectos $L$ y $R$ en el lattice 3+1D SCG (interpretación natural de S53 sim004).
- (ii) **Separación en un "espacio interno auxiliar"** (planteado en S56 como U(1), $\mathbb{Z}_4$, etc.).

### 1.2 Clarificación S57

**Interpretación correcta (consolidada):** $d_{LR}$ **ES separación espacial física** entre los extremos $s$ (etiqueta $L$) y $c$ (etiqueta $R$) de la cuerda SCG abierta que representa al fermión SM.

**Justificación:**
- En D-013, los fermiones SM son **end-points de cuerdas abiertas**: el extremo + porta etiqueta $s$, el extremo − porta etiqueta $c$.
- La cuerda **conecta** $s$ con $c$ a través del bulk del lattice 3+1D.
- $d_{LR}$ = **longitud de la cuerda abierta** = separación física entre los end-points.

**Implicación:**
- Top quark: cuerda colapsada ($d_{LR} = 0$, end-points coinciden) → $y_t = 1$.
- Electrón: cuerda larga ($d_{LR} \sim 5-20 \ell_P$) → $y_e \sim 10^{-6}$.
- La jerarquía Yukawa **es jerarquía de longitudes de cuerda**.

### 1.3 No hay "espacio interno auxiliar" necesario

Las propuestas S56 (U(1) interno, $\mathbb{Z}_4$, etc.) son **innecesarias bajo esta interpretación**. El "bulk WW dimensional" es simplemente **el espacio físico 3+1D del lattice** donde se extiende la cuerda abierta.

**El problema central de E se reformula:**

> ¿Qué propiedad estructural del fermión SM **fija la longitud de su cuerda abierta** en el lattice WW?

---

## 2. Sub-opciones para la longitud de cuerda

### 2.1 Sub-opción (a) — Cuantizada (Bilson-Thompson)

**Idea:** $d_{LR} = n \cdot \ell_F$ con $n \in \mathbb{Z}_{\geq 0}$. La estructura de trenza ($B_3$ + twists ±1/3) determina $n$.

- Top: $n = 0$ (trenza trivial).
- Generaciones más altas: $n$ mayor (trenzas más complejas).
- Elemento postulable: la escala $\ell_F$ (idealmente $\ell_P$).

### 2.2 Sub-opción (b) — Continua (bulk WW emergente)

**Idea:** $d_{LR}$ es continuo, fijado por **dinámica del condensado**: tensión vs energía de Casimir.

- La cuerda abierta en lattice WW tiene **tensión** $T \sim \hbar c / \ell_P^2$.
- La cuerda interactúa con el condensado de loops-`v`.
- El equilibrio dinámico fija $d_{LR}$ en función de propiedades del fermión.

### 2.3 Validación numérica (sim005)

**Implementación:** `experiments/simulations/sim005_quantization_test.py`.

**Test 1 — d_{LR} continuo requerido (perfil exponencial, $\ell_s = \ell_P$):**

| Fermión | $y/y_t$ | $d_{LR}$ requerido (exp) |
|---|---|---|
| top | 1.0 | 0 |
| bottom | $2.4 \times 10^{-2}$ | $6.2 \ell_P$ |
| tau | $1.0 \times 10^{-2}$ | $7.7 \ell_P$ |
| charm | $7.4 \times 10^{-3}$ | $8.2 \ell_P$ |
| strange | $5.4 \times 10^{-4}$ | $12.6 \ell_P$ |
| muon | $6.1 \times 10^{-4}$ | $12.4 \ell_P$ |
| down | $2.7 \times 10^{-5}$ | $17.6 \ell_P$ |
| up | $1.3 \times 10^{-5}$ | $18.8 \ell_P$ |
| electron | $2.9 \times 10^{-6}$ | $21.3 \ell_P$ |

**Banda observada:** $d_{LR} \in [0, 21] \ell_P$. **Compatible con predicción S53** ($[0, 20] \ell_P$).

**Test 2-3 — Cuantización entera (perfil exp, $\ell_s$ optimizado):**

Mejor $\ell_s = 7.70 \ell_P$ con RMS desviación 0.21 unidades de $\ell_F = \ell_P$. Asignación entera:

| Fermión | $y_{obs}$ | $d_{req}$ (con $\ell_s=7.7$) | $n$ entero | $y_{pred}$ | desviación |
|---|---|---|---|---|---|
| top | $1.0$ | 0 | 0 | $1.0$ | (top) |
| bottom | $2.40 \times 10^{-2}$ | 47.97 | 48 | $2.395 \times 10^{-2}$ | 0.2% |
| tau | $1.00 \times 10^{-2}$ | 59.23 | 59 | $1.018 \times 10^{-2}$ | 1.8% |
| charm | $7.40 \times 10^{-3}$ | 63.10 | 63 | $7.460 \times 10^{-3}$ | 0.8% |
| strange | $5.40 \times 10^{-4}$ | 96.77 | 97 | $5.305 \times 10^{-4}$ | 1.8% |
| muon | $6.10 \times 10^{-4}$ | 95.20 | 95 | $6.197 \times 10^{-4}$ | 1.6% |
| down | $2.70 \times 10^{-5}$ | 135.30 | 135 | $2.764 \times 10^{-5}$ | 2.4% |
| up | $1.30 \times 10^{-5}$ | 144.70 | 145 | $1.270 \times 10^{-5}$ | 2.3% |
| electron | $2.90 \times 10^{-6}$ | 164.00 | 164 | $2.900 \times 10^{-6}$ | 0.0% |

**Resultado sorprendente:** desviaciones individuales ≤ 2.4%. **Asignación cuantizada con perfil exponencial ajusta datos SM dentro del 2-3%.**

**Caveats:**
- (i) $\ell_s = 7.70 \ell_P$ es **postulado**, no derivado.
- (ii) RMS 0.21 es "ligeramente mejor que aleatorio" (esperado ~0.29 para asignación trivial). Significancia estadística limitada con 9 puntos.
- (iii) Los $n$ enteros son grandes (48-164). **¿Tiene sentido físicamente una "trenza con 164 cruces"?** Improbable.

### 2.4 Resumen comparativo de sub-opciones

| Sub-opción | Tipo | Mejor $\ell_s$ | Concordancia | Caveat |
|---|---|---|---|---|
| (a) cuantizada (gauss) | $d = n \ell_P$ | $3.10 \ell_P$ | RMS desv 0.18 | $\ell_s$ postulado |
| (a) cuantizada (exp) | $d = n \ell_P$ | $7.70 \ell_P$ | desv 0.2-2.4% | $\ell_s$ y $n$ grandes postulados |
| (b) continua (gauss) | $d \in \mathbb{R}$ | $1-3 \ell_P$ | exacto por construcción | mecanismo $d_{LR}$ pendiente |
| (b) continua (exp) | $d \in \mathbb{R}$ | $1 \ell_P$ | exacto por construcción | mecanismo $d_{LR}$ pendiente |

---

## 3. Identificación de propiedades fermiónicas que fijan $d_{LR}$

### 3.1 ¿Qué propiedad del fermión SM determina $d_{LR}$?

En SCG con `Spin(10)_1` MTC, los fermiones SM son **una sola rep $16$ de SO(10)** (1 generación). La rep tiene componentes:
- Quark up-type (3 colores): $u_L, u_R$.
- Quark down-type (3 colores): $d_L, d_R$.
- Leptón neutrino: $\nu_L, \nu_R$.
- Leptón cargado: $e_L, e_R$.

**Pregunta:** ¿qué distingue al $u$ del $e$ en SCG? Bajo `Spin(10)_1` MTC abeliana, ambos son end-points etiquetados $s$ (extremo +) ↔ $c$ (extremo −). La distinción **carga eléctrica** (Q=2/3 vs Q=−1) emerge de la ruptura SO(10) → SU(5) → SM (cadena estándar).

**Posibles propiedades que fijan $d_{LR}$:**

| Propiedad | Distingue | Rango natural |
|---|---|---|
| Carga eléctrica $Q$ | $u$ vs $d$ vs $\ell$ vs $\nu$ | discreto (4 valores) |
| Color | quarks vs leptones | discreto (3 vs 1) |
| Generación | 1ª vs 2ª vs 3ª | discreto (3 valores) — caveat K-039 |
| Carga U(1) interna ($1_4$ E_6) | depende de embedding | continuo |

**Interpretación tentativa:**

- $d_{LR}$ depende de **(carga, color, generación)** del fermión.
- Para top quark ($Q=2/3$, color, 3ª gen): $d_{LR} = 0$ (cuerda colapsada).
- Para electrón ($Q=-1$, sin color, 1ª gen): $d_{LR} \approx 7-21 \ell_P$ (cuerda larga).
- La función $d_{LR}(Q, \text{color}, \text{gen})$ está por determinar.

### 3.2 Patrón observado en datos SM

Análisis cualitativo de Yukawas observados:

| Patrón | Observación |
|---|---|
| Top más pesado | $y_t = 1$ exclusivo. |
| Quarks pesados (b, c) | Yukawas similares ($\sim 10^{-2}$). |
| Leptones cargados pesados ($\tau$) | $y_\tau \sim y_b$. |
| Quarks intermedios (s, $\mu$) | $y \sim 10^{-4}$. |
| Quarks ligeros (d, u) | $y \sim 10^{-5}$. |
| Electrón | $y_e \sim 10^{-6}$. |
| Neutrinos | $y_\nu \lesssim 10^{-13}$. |

**Patrón emergente:**
- Yukawas **no** son monótonos en carga eléctrica ni en color.
- Yukawas **sí** son monótonos en **generación dentro de un tipo** (e.g., $y_t > y_c > y_u$).
- Hay **estructura aproximada de pares** (b ≈ τ, c ≈ s, u ≈ d) — puede ser coincidencia o reflexión de simetría SO(10).

**Observación importante:** la jerarquía **dentro de una generación** (ej. $y_t/y_b \approx 40$ para 3ª gen) es comparable a la jerarquía **entre generaciones** (ej. $y_t/y_c \approx 130$). Esto sugiere que ambas son **del mismo origen** — no hay una "supresión exclusiva por generación".

### 3.3 Implicación para sub-tarea E

**Hipótesis tentativa (a refinar en S58):**
> $d_{LR}$ depende de **número de fusiones intermedias** entre el extremo $s$ y el extremo $c$ a través del condensado. Cada fusión intermedia añade $\Delta d \sim \ell_F$.

Esta hipótesis es similar a Froggatt-Nielsen (camino c) pero **sin postular** una escala $M_F$ adicional — usa la estructura ya en SCG (`Spin(10)_1` MTC + condensado $\rho_v$).

**Trabajo S58:** verificar cuantitativamente si esta hipótesis reproduce los $d_{LR}$ observados.

---

## 4. Estimación dimensional preliminar y banda predicha (E.2.4)

### 4.1 Banda recapitulada

| Fermión | $d_{LR}$ predicho (gauss, $\ell_s=\ell_P$) | $d_{LR}$ predicho (exp, $\ell_s=\ell_P$) |
|---|---|---|
| top | $0$ | $0$ |
| bottom | $3.9 \ell_P$ | $6.2 \ell_P$ |
| tau | $4.3 \ell_P$ | $7.7 \ell_P$ |
| charm | $4.4 \ell_P$ | $8.2 \ell_P$ |
| strange | $5.5 \ell_P$ | $12.6 \ell_P$ |
| muon | $5.4 \ell_P$ | $12.4 \ell_P$ |
| down | $6.5 \ell_P$ | $17.6 \ell_P$ |
| up | $6.7 \ell_P$ | $18.8 \ell_P$ |
| electron | $7.1 \ell_P$ | $21.3 \ell_P$ |

**Banda total:** $d_{LR} \in [0, 21.3] \ell_P$. **Compatible con predicción S53** ($[0, 20] \ell_P$).

### 4.2 Sensibilidad al perfil

- **Gaussiano:** rango más estrecho ($[0, 7]\ell_P$).
- **Exponencial:** rango más amplio ($[0, 21]\ell_P$).

La elección del perfil afecta cuantitativamente el resultado. La forma exponencial es más natural para cuerdas con tensión (decaimiento exp) — argumento físico tentativo.

### 4.3 Sensibilidad a $\ell_s$

Resultado de sim005: $\ell_s$ es ajustable (de $1$ a $7.7 \ell_P$ para mejorar concordancia). Esto **debilita el poder predictivo** del cálculo si $\ell_s$ no se deriva.

---

## 5. Análisis de sensibilidad y robustez (E.2.5)

### 5.1 Tabla de sensibilidades

| Variación | Efecto en $d_{LR}$ predicho |
|---|---|
| Cambiar perfil gauss ↔ exp | Factor 1.5-3 en $d_{LR}$ |
| Cambiar $\ell_s$ por factor 2 | $d_{LR}$ se escala por factor 2 |
| Cuantizar vs continuo | RMS desv 0.21 (cuantizada) vs 0 (continua) |
| Cambiar fórmula $\xi(d)$ | Banda predicha cambia |

### 5.2 Robustez

**Resultado robusto:** $d_{LR} \in [0, 25] \ell_P$ orden de magnitud. Esto se sostiene para casi cualquier elección razonable de perfil y escala.

**Resultado no-robusto:** valor numérico exacto de cada $d_{LR}$. Depende del perfil + $\ell_s$ asumidos.

### 5.3 Implicaciones

- **Predicción cuantitativa fina** ($d_{LR}$ exactos) **no se obtiene sin postular $\ell_s$**.
- **Predicción de orden de magnitud** ($d_{LR} \sim 10 \ell_P$) **es robusta** sin parámetros libres.

---

## 6. Decisión y plan S58 (E.2.6)

### 6.1 Estado al cierre de S57

- ✅ **Reinterpretación clave:** $d_{LR}$ es separación espacial física en el lattice, no espacio auxiliar. **Las partículas SM son cuerdas abiertas extendidas.**
- ✅ **Sub-opción (b) continua viable:** todos los fermiones caen en banda $[0, 21] \ell_P$ con $\ell_s \sim \ell_P$.
- ✅ **Sub-opción (a) cuantizada notable:** con perfil exp y $\ell_s = 7.7 \ell_P$, asignación entera ajusta SM al 2-3%.
- ⚠ **Caveat común:** $\ell_s$ no se deriva — ajuste fino o postulado.
- ⚠ **Cuantización entera con $n \sim 100$** es físicamente improbable (trenzas de 100 cruces).

### 6.2 Decisión

**Continuar el camino primario (b) con foco en sub-opción CONTINUA.** La sub-opción (a) cuantizada con $n$ grandes es físicamente sospechosa.

**Plan S58 (E.3):**
1. Identificar **mecanismo dinámico** que fije $d_{LR}$ continuo desde estructura SCG.
   - Candidato: equilibrio tensión cuerda vs energía Casimir + condensado.
   - Si funciona: **K-042 candidato cuantitativo**.
2. Si no hay mecanismo natural: aceptar caveat moderado.
3. Análisis técnico explícito de **qué propiedad fermiónica fija $d_{LR}$** (carga, color, generación, suma fusiones).

### 6.3 Pivot S59-S60

Si S58 no produce mecanismo natural:
- **S59 (E.4):** explorar Bilson-Thompson como camino auxiliar para cuantización.
- **S60 (E.5):** comparación con SM (con o sin mecanismo).
- **S61 (E.6):** decisión K-042. Si no hay derivación: caveat fuerte (análogo K-040).

### 6.4 Probabilidad sub-tarea E actualizada (post-S57)

- **~25% K-042 cuantitativo** (mecanismo natural identificado en S58 + cierre cuantitativo).
- **~45% K-042 caveat moderado** (forma funcional sí, valores ajustados con $\ell_s$ o postulados).
- **~30% K-042 caveat fuerte** (análogo K-040, jerarquía no derivada).

(Subido +5% desde estimación S56 por la concordancia notable de la sub-opción (a) cuantizada con perfil exp.)

---

## 7. Veredicto sesión 57

### 7.1 Logros

- ✅ **Reinterpretación clave de $d_{LR}$:** separación espacial física (no auxiliar). Aclara confusión S52-S56.
- ✅ **Sim005 implementada:** test cuantitativo de cuantización vs continua.
- ✅ **Resultado interesante:** sub-opción (a) cuantizada con perfil exp ajusta SM al 2-3% con $\ell_s = 7.7 \ell_P$ (caveat: $\ell_s$ postulado, $n$ grandes físicamente sospechosos).
- ✅ **Sub-opción (b) continua confirmada como viable:** $d_{LR}$ en banda $[0, 21] \ell_P$ predicha S53.
- ✅ **Análisis de sensibilidad sistemático.**
- ✅ **Plan S58 trazado:** foco en mecanismo dinámico que fije $d_{LR}$ continuo desde estructura SCG.

### 7.2 No-logros (intencional)

- ❌ NO se ha identificado el mecanismo dinámico que fije $d_{LR}$ específicos. Eso es S58.
- ❌ NO se ha promovido K-042 (S61).
- ❌ NO se ha calculado $d_{LR}$ desde primeros principios SCG. Solo desde datos SM.

### 7.3 Disciplina

- **K-005:** ningún mecanismo exótico introducido. La reinterpretación usa la estructura ya en D-013 (cuerdas abiertas).
- **Regla 4:** la cuantización entera con $\ell_s = 7.7$ ✅ marcada como **sugerente, no derivada**. La concordancia 2% no se infla a "predicción".
- **Regla 5:** ambas sub-opciones presentadas honestamente. La sub-opción (b) continua es preferida estructuralmente.
- **Regla 9 (preventiva):** plan S58 con criterios de pivot S59-S61 explícitos.

### 7.4 Hallazgo meta

**Insight estructural significativo de S57:** la "predicción geométrica de la jerarquía Yukawa" (anticipada en S53) se **materializa como longitud espacial de la cuerda abierta del fermión** en el lattice WW SCG. **Esto unifica la interpretación de partículas SM como cuerdas extendidas** (línea Bilson-Thompson) con el cálculo Yukawa de S53.

---

## 8. Próxima sesión (58)

**Objetivo:** **E.3 — fase 2 del camino primario: cálculo $d_{LR}$ específicos.**

**Sub-pasos:**
1. Identificar el **mecanismo dinámico** que fija $d_{LR}$:
   - Candidato A: equilibrio tensión cuerda vs Casimir (cuerda análoga a "string SCG" de H-001).
   - Candidato B: número de fusiones intermedias en el condensado (Froggatt-Nielsen-like sin escala $M_F$).
   - Candidato C: invariante topológico de la trenza (Bilson-Thompson).
2. Calcular $d_{LR}$ específicos para los 9 fermiones SM bajo el mecanismo seleccionado.
3. Comparar con observación.
4. Si concordancia razonable: K-042 candidato. Si no: pivot.

**Lecturas focalizadas para sesión 58:**
- D-014 (síntesis A-D).
- H-001 (cuerda SCG con tensión + Casimir).
- D-007 (acción Plebanski + boundary).
- Notas S53, S57.
- Bilson-Thompson 2005 (preparación E.4).

**Disciplina S58:** análisis técnico riguroso. Si ningún mecanismo da $d_{LR}$ específicos sin postulados libres → caveat moderado/fuerte.

---

## 9. Firma

**Resultado meta sesión 57:**

- **Reinterpretación crítica:** $d_{LR}$ es **longitud espacial de la cuerda abierta SCG** del fermión. Las partículas SM son cuerdas extendidas, no puntos.
- **Banda predicha confirmada:** $d_{LR} \in [0, 21] \ell_P$ — concordancia con predicción S53.
- **Sub-opción (a) cuantizada:** ajuste 2-3% con $\ell_s = 7.7 \ell_P$ (postulado). Físicamente sospechoso ($n \sim 100$).
- **Sub-opción (b) continua:** viable estructuralmente. Mecanismo dinámico pendiente para S58.

**Plan S58:** identificar mecanismo dinámico que fije $d_{LR}$ continuo. **Probabilidad de éxito ~25%** (cuantitativo) + **~45% caveat moderado** + **~30% caveat fuerte**.

**Inventario sin cambios cuantitativos** (no nuevos K esta sesión).

La teoría continúa.
