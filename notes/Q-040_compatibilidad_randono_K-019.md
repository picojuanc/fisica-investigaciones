# Q-040 — Compatibilidad de Randono 2006 (β real) con K-019 (AMS 2014)

- **Fecha:** 2026-04-21 (sesión 22)
- **Pregunta abordada:** ¿la ruta Randono 2006 (parámetro de Immirzi β real) preserva la identificación K-019 "conexión autodual de Ashtekar = su(2)_L del grupo de Lorentz" (AMS 2014) sin pérdida de contenido físico?
- **Relación con K-030:** si Q-040 cierra afirmativamente, K-030 se promueve a confirmado (vía Randono). Si cierra negativamente, SCG necesita mecanismo nuevo para asimetría máxima del SM bajo β real.
- **Relación con P-11:** define la severidad final. Si afirmativa: P-11 → 🟡 baja. Si negativa: P-11 sigue 🟡 media o incluso 🟡 alta.

---

## 0. Planteamiento

Tras la sesión 21, **Q-039 con resultado negativo** estableció que ABKP 2025 no aplica en régimen I de SCG (Λ_UV ≪ Λ_c). La ruta primaria para mitigar P-11 pasó a ser **Randono 2006** (β real). Pero Randono requiere re-articular K-019, porque AMS 2014 (la base literal de K-019) usa específicamente β = −i.

**Pregunta operativa:** ¿el cambio de β = −i a β real preserva la fenomenología quiral observable (SU(2)_L máximo en el SM)?

Tres respuestas posibles:
- **(A) SÍ:** β real preserva todo. K-019 se re-articula limpiamente. K-030 se promueve.
- **(B) NO:** β real pierde asimetría máxima. K-019 se rompe. K-030 no se cierra.
- **(C) PARCIAL:** β real preserva violación P-T cualitativa pero no obviamente la asimetría máxima. K-019 se debilita. K-030 sigue candidato con reservas.

---

## 1. Qué dice la literatura

### 1.1 AMS 2014 (Alexander-Marciano-Smolin, PRD 89 065017)

Cita directa (paper abstract): *"The weak interactions emerge as the right-handed chiral half of the space-time connection, which explains the chirality of the weak interaction."*

**Construcción:** el grupo de Lorentz complexificado so(3,1)_C se descompone como su(2)_L × su(2)_R. La conexión de Ashtekar autodual (β = −i) es literalmente **una mitad** de esta descomposición. Los fermiones levógiros acoplan a su(2)_L, dextrógiros a su(2)_R. Asimetría máxima automática.

**Dependencia de β:** AMS usa β = −i explícitamente. La identificación literal "A_Ashtekar = su(2)_L" **no vale para β real**.

### 1.2 Randono 2006 (gr-qc/0504010, 0611073, 0611074)

**Construcción:** con β real, el estado Ψ_K^{(β)} = exp(i S_CS[A^{(β)}]/ℏ) donde A^{(β)} = Γ + β·K (conexión de Barbero-Immirzi real).

**Propiedades del estado:**
- Normalizable en el inner product kinemático.
- Invariante bajo grandes transformaciones gauge.
- **CPT invariant**, no CP invariant, no P invariant, no T invariant.
- Genera **4-fermión interaction violating P-T** en presencia de fermiones de Dirac minimally coupled (Perez-Rovelli 2005; Mercuri 2006).

### 1.3 Randono (hep-th/0510001) — Parity Violation and the Immirzi Parameter

**Resultado clave:** en Einstein-Cartan-Holst gravity con fermiones, β aparece EN las ecuaciones de movimiento. El término Holst (con β) induce acoplamiento asimétrico entre fermiones L y R — violación P observacional.

**Pero:** la asimetría es **modulada** por β, no máxima automáticamente. Para β = γ_Immirzi ≈ 0.2375 (Dreyer), la asimetría es **finita y moderada**, no máxima.

### 1.4 Literatura posterior (2014-2026)

- **Smolin (coautor de AMS 2014 Y de Randono-related):** no resolvió explícitamente la tensión entre β = −i (AMS 2014) y β real (Randono 2006). Ambos enfoques coexisten en su trabajo sin reconciliación cuantitativa.
- **Kaplan 2024 (PRL 132 141603):** fermiones quirales en fronteras entre fases topológicas. Mecanismo independiente de β, potencialmente reconciliador con β real.
- **Alexander et al. 2025 (ABKP):** mismo grupo que AMS 2014, trabaja con β = −i (autodual) todavía. No resuelven la tensión.

---

## 2. Análisis técnico

### 2.1 Conexión en función de β

```
A^i_a(β) = Γ^i_a + β K^i_a                                              (2.1)
```

Casos límite:
- β = 0: A = Γ (conexión de spin pura, SU(2) de la geometría 3D).
- β = ±i: A = Γ ± i K = conexión autodual/antiautodual compleja de Ashtekar 1986.
- β real finito (Barbero-Immirzi): conexión real en SU(2).
- β → ∞: A ≈ β K, escalado por β.

**Identificación con su(2)_L del grupo de Lorentz complexificado:**
- β = −i: **literal** (AMS 2014). Conexión autodual = componente izquierda de so(3,1)_C.
- β real: **no literal**. La conexión real de Barbero-Immirzi vive en su(2) de la geometría 3D; no es una sub-álgebra del Lorentz complexificado.

### 2.2 ¿Qué se preserva bajo β real?

| Propiedad | β = −i (AMS) | β real (Randono) |
|---|---|---|
| Kodama normalizable (ABKP) | No (requiere Λ > 384/ℓ_P²) | N/A — no hace falta |
| Kodama normalizable (inner product kinemático) | No | **Sí** |
| CPT invariance del estado | No | **Sí** |
| CP violation del estado | Sí (máxima) | Sí (modulada por β) |
| P, T violation | Sí (máxima) | Sí (moduladas por β) |
| Identificación A = su(2)_L literal | Sí | **No** |
| Asimetría máxima L-R en acoplamiento fermiónico | **Sí (automática)** | **No (modulada por β)** |
| Invariancia bajo grandes gauge | No (β no entero) | Sí |

**Las dos celdas críticas en negrita:** AMS 2014 da asimetría máxima automática. Randono con β real da asimetría modulada por β, no obviamente máxima.

### 2.3 La tensión

El SM tiene asimetría **máxima**: sólo fermiones L acoplan a SU(2)_L. La fracción R no acopla. Esto es lo que Q-040 pregunta si Randono reproduce.

**Bajo β = γ_Immirzi ≈ 0.2375 (valor preferido por entropía BH en LQG):**
- La violación P es finita y moderada (~β².. depende del observable).
- La asimetría L-R es parcial, no máxima.
- **No se reproduce obviamente la fenomenología observada del SM.**

**Límites:**
- β → 0: A → Γ, sin quiralidad. Fenomenología: teoría de gravedad sin asimetría L-R. No es el SM.
- β → −i: A → Γ − iK autodual. K-019 literal. Asimetría máxima. ES el SM pero β compleja.
- β → ∞: A → β K domina. Comportamiento poco claro; no hay literatura.

**Punto sensible:** para β finito real, la asimetría es finita pero NO máxima. El matching cuantitativo con el SM requiere argumento adicional.

---

## 3. ¿Cómo amplificar β real finito hasta asimetría máxima?

### 3.1 Posibilidades estructurales

1. **Defectos Walker-Wang específicos.** Los fermiones del SM en SCG son defectos topológicos de la red WW (H-003). Si la categoría de fusión UBFC tiene simetrías L específicas (y no R), los defectos heredarían asimetría máxima independientemente de β. Esto es consistente con el SM pero requiere verificación de que existe tal UBFC.

2. **Condensación de anyones (Higgs, K-021).** El mecanismo de condensación topológica que introduce el Higgs en SCG podría seleccionar la proyección L y eliminar la R. Esto es compatible con Bais-Slingerland; detalles pendientes.

3. **Kaplan 2024 (PRL 132 141603):** fermiones quirales en fronteras entre fases topológicas. Mecanismo independiente de β. Si SCG explota este mecanismo, la quiralidad emerge de la estructura del lattice, no de β. Esto **desvincula la asimetría máxima de la elección de β**.

4. **Límite β → ∞ no-perturbativo.** El acoplamiento efectivo puede fluir a "casi autodual" en un régimen específico. Argumento especulativo.

### 3.2 Evaluación

**Ninguno de los cuatro está derivado desde SCG primeros principios.** Son rutas plausibles, no mecanismos establecidos.

- (1) Es la más natural para SCG pero requiere construir la UBFC explícita con asimetría L.
- (2) Es consistente con K-021 pero no cuantificada.
- (3) Es externa (Kaplan 2024); sería una adopción, no una derivación propia.
- (4) Es especulativa.

**Conclusión provisional:** bajo β real finito, la asimetría máxima del SM requiere **mecanismo adicional**, no provisto directamente por Randono 2006.

---

## 4. Veredicto sobre Q-040

### 4.1 Respuesta

**(C) PARCIAL.** Randono 2006 preserva:
- Normalizabilidad de Kodama. ✓
- CPT invariance. ✓
- Violación P-T cualitativa. ✓
- Invariancia bajo grandes gauge. ✓

Pero NO preserva automáticamente:
- Identificación literal A = su(2)_L (AMS 2014). ✗
- Asimetría máxima del SM (sólo L acoplan a SU(2)_L). ✗ (modulada por β, no máxima)

**K-019 se debilita.** Ya no es "identidad matemática literal + asimetría máxima automática". Se reduce a "violación P observacional preservada, asimetría máxima pendiente de mecanismo adicional".

### 4.2 Consecuencia para K-030

**K-030 NO se promueve a confirmado.** Sigue candidato, con reservas adicionales. La ruta Randono NO resuelve completamente P-11 porque introduce un problema nuevo: el matching con asimetría máxima del SM.

### 4.3 Estado de P-11

P-11 sigue **🟡 media**. No se rebaja a 🟡 baja como se esperaba. Si el mecanismo adicional (sección 3) no se encuentra, P-11 podría reagravarse a 🟡 alta.

### 4.4 Q-042 nueva

**Q-042:** *¿qué mecanismo en SCG amplifica la violación P de Randono (β real finito) hasta la asimetría máxima observada del SM (sólo fermiones L acoplan a SU(2)_L)?*

Candidatos: UBFC específica, condensación de Higgs, Kaplan 2024, límite β → ∞. Esfuerzo estimado: 2-3 sesiones para evaluar cada opción.

---

## 5. Reevaluación de la Ruta A

Tras 3 sesiones de Ruta A (20, 21, 22):

| Pieza | Estado | Sesión |
|---|---|---|
| K-031 (llenado volumétrico) | ✅ PROMOVIDO | 20 |
| K-030 vía ABKP (Λ_UV) | ❌ Negativo | 21 |
| K-030 vía Randono (K-019) | ⚠️ Parcial, Q-042 nueva | 22 |
| K-032 (matching II→IV) | Pendiente | — |
| K-028 (redshift riguroso) | Pendiente | — |

**Balance:** 1 promoción clara (K-031), 1 resultado negativo (Q-039), 1 resultado parcial ambiguo (Q-040). Quedan 2 piezas.

La Ruta A está dando más refinamiento (negativo o parcial) que promociones. Esto es **honesto pero modesto en progreso**.

---

## 6. Implicaciones para la estrategia

### 6.1 Continuar Ruta A

Razones para seguir:
- K-031 promovido (una pieza clara).
- Matching II→IV (K-032) es el de mayor impacto cuantitativo si cierra.
- K-028 riguroso es técnico pero tractable (P-15').

Razones para pausar:
- 2 de 3 piezas abordadas dieron resultados no-promoción.
- Q-042 nueva abre otra sub-tarea.
- P-8 (Lagrangiana) tiene arquitectura completa pero cuantificación lenta.

### 6.2 Alternativa: Ruta B parcial

Atacar **una** pieza de Ruta B (p.ej., masas fermiónicas desde defectos WW) para ver si rinde. Si sí, cambia el énfasis. Si no, volver a Ruta A con piezas restantes.

### 6.3 Alternativa: consolidar y publicar

El marco tiene estructura significativa tras 22 sesiones. Escribir el snapshot v1.8 + documento resumido para comunidad externa podría traer feedback valioso que oriente las próximas 10 sesiones.

---

## 7. Honestidad epistémica

**Lo que Q-040 establece:**
- Randono 2006 preserva parte de la fenomenología quiral, pero no la asimetría máxima del SM.
- K-019 se debilita bajo β real (de identidad literal a compatibilidad cualitativa).
- K-030 no se cierra completamente por esta ruta.
- Q-042 es la nueva pregunta operativa.

**Lo que Q-040 NO establece:**
- No descarta definitivamente que β real + SCG reproduzca SU(2)_L máximo — sólo que no lo hace automáticamente.
- No explora cuantitativamente ninguno de los 4 mecanismos candidatos (sección 3).
- No reconcilia AMS 2014 y Randono 2006 (literatura no lo hace tampoco).

**Aplicación de K-005:** la ruta más modesta (β real) está resultando más compleja que la "más exótica" (β = −i, con patologías Kodama pero identificación literal). Esto es tensión: no hay un camino sin costo.

**Aplicación de Regla 9 del protocolo ("destruir resultado propio"):** Q-039 (sesión 21) cerró ABKP; Q-040 (sesión 22) debilita Randono. Las dos rutas de K-030 tienen ahora costos identificados. **K-030 está más débil que en la sesión 17**, no más fuerte.

Esta es la realidad. No es catástrofe (Randono sigue siendo viable fenomenológicamente), pero tampoco es la promoción limpia que esperábamos.

---

## 8. Referencias

- Alexander, Marciano, Smolin (2014). *Gravitational origin of the weak interaction's chirality*. PRD 89, 065017. arXiv:1212.5246.
- Randono (2005). *A Note on Parity Violation and the Immirzi Parameter*. arXiv:hep-th/0510001.
- Randono (2006). Generalización Kodama con β real. gr-qc/0504010, 0611073, 0611074.
- Perez, Rovelli (2005). Immirzi parameter y acoplamiento fermiónico.
- Mercuri (2006). Holst action con fermiones.
- Kaplan (2024). *Chiral Gauge Theory at the Boundary between Topological Phases*. PRL 132, 141603. arXiv:2312.01494.
- Alexander et al. (ABKP 2025). arXiv:2511.05417.
- Dreyer (2003). γ_Immirzi = 0.2375.

---

## 9. Firma

Q-040 cerrada con respuesta parcial. Randono 2006 preserva viabilidad de Kodama pero **no** preserva automáticamente la asimetría máxima del SM. K-019 se debilita bajo β real. K-030 sigue candidato; Q-042 nueva identificada.

Ruta A tras sesión 22: 1 promovido, 1 negativo, 1 parcial, 2 pendientes. Recomendación estratégica: reevaluar si continuar con K-032 (matching II→IV) o pasar a Ruta B parcial.
