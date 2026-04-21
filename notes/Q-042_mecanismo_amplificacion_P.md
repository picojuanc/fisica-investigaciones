# Q-042 — Mecanismo SCG que amplifica la violación P de Randono hasta asimetría máxima SM

- **Fecha:** 2026-04-21 (sesión 24)
- **Pregunta abordada:** ¿qué mecanismo en SCG amplifica la violación P de Randono (β real finito) hasta la asimetría máxima observada del SM (sólo fermiones L acoplan a SU(2)_L)?
- **Relación con K-030:** si se identifica mecanismo viable, K-030 se promueve (vía Randono + mecanismo auxiliar). Si no, K-030 se degrada y P-11 se reagrava.
- **Relación con P-11:** determina severidad final. Afirmativa fuerte → 🟡 baja; afirmativa con caveat → 🟡 baja con dependencia; negativa → 🟡 media/alta.

---

## 0. Planteamiento

Tras Q-040 (sesión 22) con resultado parcial (C): Randono 2006 preserva viabilidad de Kodama con β real, pero **no preserva automáticamente la asimetría máxima del SM**. La asimetría observada es **máxima** (sólo fermiones L se acoplan a SU(2)_L; los R no se acoplan); Randono con β = γ_Immirzi ≈ 0.2375 produce asimetría **modulada y finita**, no máxima.

Q-040 identificó cuatro candidatos de mecanismo amplificador:
1. UBFC (Unitary Braided Fusion Category) con simetría L específica.
2. Condensación de anyones Higgs (K-021).
3. Kaplan 2024 (PRL 132 141603): fermiones quirales en frontera topológica.
4. Límite β → ∞ no-perturbativo.

**Esta sesión evalúa cada candidato con literatura reciente (2018-2025).** Resultado central: el candidato (3) — ampliado por Wang-Wen 2018-2019 y el framework modular Walker-Wang — provee mecanismo conceptualmente completo, independiente de β, compatible con Randono y aplicable a la red WW 3+1D de SCG. Costos: K-019 tercera reinterpretación, K-026 significativamente debilitada, Q-043 nueva (construcción UBFC específica).

---

## 1. Kaplan 2024 — Fermiones quirales en frontera topológica

### 1.1 Resultado central

**Kaplan, David B. (2024). "Chiral Gauge Theory at the Boundary between Topological Phases." PRL 132, 141603. arXiv:2312.01494.**

Demuestra que **fermiones quirales con simetría gauge exacta pueden emerger en la frontera d-dimensional de una variedad (d+1)-dimensional de volumen finito, sin mirror partners ligeros**. La construcción evade Nielsen-Ninomiya explícitamente en el marco lattice.

**Condiciones:**
- Cancelación de anomalías gauge.
- Volumen grande (localidad en la teoría de frontera).

**Companion paper:** Kaplan & Sen (2024), PRL 132 141604, arXiv:2312.04012 — ejemplo explícito lattice con Wilson fermion en (2+1)D con frontera (1+1)D mostrando edge states de Weyl sin pareja.

### 1.2 Mecanismo

El bulk (d+1)-dimensional es una **fase topológica** (SPT o con invariante de cobordismo apropiado). Los fermiones quirales emergen **ligados a la frontera** como estados de borde. La masa del bulk es Wilson-like: genera un gap en el bulk; la topología del bulk determina la estructura de frontera. La ausencia de mirror partners viene del **desbalance topológico entre las dos fases** (diferentes números de Chern, estructura de simetría, o degeneración L vs R).

### 1.3 Independencia de β

El mecanismo es **puramente topológico/lattice**. No requiere parámetro de Immirzi ni acoplamiento a gravedad. La quiralidad emerge de la discontinuidad topológica entre fases del bulk, no de la conexión gravitacional.

---

## 2. Wang-Wen 2018-2019 — SM completo en lattice 3+1D

### 2.1 Resultado central

**Wang, Juven & Wen, Xiao-Gang (2018-2019). "A Non-Perturbative Definition of the Standard Models." arXiv:1809.11171.**

Demuestra que el SM completo desde SO(10)-GUT con fermiones quirales en la representación spinorial 16-dim puede definirse **no-perturbativamente en lattice 3+1D** de bosones o qubits.

**Mecanismo clave:**
- El SM desde SO(10) tiene **16n fermiones quirales** libres de anomalías perturbativas locales y globales.
- La clasificación por **teorema de cobordismo**: para N ≥ 7 (donde N etiqueta Spin(N)), el grupo relevante es Ω^{D=5} = ℤ₂, y la clase invertible trivial (cobordismo 0) garantiza existencia de **frontera gapped simétrica** para el sector mirror.
- La construcción: bulk es 4+1D Spin(10) fermiónico SPT invertible trivial; boundary 3+1D hospeda el SM quiral.
- El sector mirror se **gapéa mediante interacciones simétricas** (teorema 1-2) que no rompen la simetría on-site — esto produce asimetría L-R máxima en la teoría efectiva de baja energía.

### 2.2 Grupo de simetría del bulk

La simetría de la construcción es:
```
G = (Gspacetime × Gf) / Nshared = (Spin(5) × Spin(10)) / ℤ₂^f
```
- Spin(5): rotaciones 5D del bulk.
- Spin(10): gauge interno (SM desde SO(10)-GUT).
- ℤ₂^f: fermion parity identificada.

No incluye gravedad dinámica ni parámetro de Immirzi β. Las clases de Stiefel-Whitney aparecen **solo como backgrounds no-dinámicos** (no-Immirzi).

### 2.3 Asimetría L-R máxima

Emerge **automáticamente** del gapping del sector mirror. Una frontera lleva fermiones Weyl L; la otra lleva Weyl R. Integrando el bulk + gappeando un lado, se obtiene la asimetría máxima del SM. Es **independiente de β** de Ashtekar.

---

## 3. Modular Walker-Wang — Bulk invertible, frontera quiral

### 3.1 Estructura matemática

Un modelo Walker-Wang en 3+1D construido a partir de una **UBFC modular** (p. ej., categoría Drinfeld center, Ising MTC) tiene la propiedad:
- Bulk 3+1D: fase topológica **invertible** (equivalente SPT, potencialmente trivial).
- Frontera (2+1)D: hospeda una fase **quiral** con orden topológico apropiado.

**Referencias clave:**
- Walker & Wang (2011). Arxiv:1104.2632. Construcción original.
- Kawagoe, Gorantla, Williamson et al. (2023). PRB 107 085134. Arxiv:2208.03397. "Disentangling modular Walker-Wang models via fermionic invertible boundaries" — demuestran que para modular input category el bulk es trivial/invertible y la frontera soporta la fase quiral correspondiente.
- Ejemplo concreto: 3-fermion Walker-Wang = 3D time-reversal SPT con frontera 3F anyon theory.

### 3.2 Relevancia para SCG

SCG (H-003, K-026) usa Walker-Wang 3+1D como marco para generar SU(3)×SU(2)×U(1). Si la UBFC de SCG es **modular**:
- Bulk WW 3+1D es una fase invertible/SPT.
- Frontera (o defecto interpretado como frontera efectiva) hospeda fase quiral con el contenido quiral del SM.

**Relación con Kaplan 2024 + Wang-Wen 2018-2019:** el framework modular WW es estructuralmente compatible. La construcción Wang-Wen puede verse como el caso específico con SO(10) del framework general. Kaplan 2024 provee el mecanismo general de edge states quirales en frontera de fase topológica.

---

## 4. Aplicabilidad a SCG

### 4.1 ¿Dónde está la "frontera" en SCG?

SCG macroscópicamente es 3+1D bulk sin frontera espacial evidente. Candidatos a frontera efectiva:

**(F1) Defectos topológicos como fronteras locales.** Los fermiones SM son defectos topológicos en WW (H-003). Un defecto codim-1 es localmente una frontera entre dos regiones. El tubo de Gauss alrededor de un defecto actúa como frontera efectiva donde los estados de borde quirales de Kaplan 2024 pueden emerger.

**(F2) Horizonte de BH.** En H-001, el interior del BH es una fase densa (cuerda plegada); el exterior es red diluida. El horizonte es frontera entre dos fases. Kaplan mechanism podría aplicar; implicación colateral: información emerge quiralmente del horizonte.

**(F3) Frontera temporal / cosmológica.** Big Bang como "frontera inicial" del bulk. Especulativo; no explorado aquí.

**(F4) Frontera implícita infinita.** En lattice, frontera en infinito. Si SCG se formula en espacio compacto (o con corte IR), la frontera global puede ser la sede del SM.

La opción **(F1)** es la más natural para SCG: si los fermiones son defectos topológicos en WW, el mecanismo Kaplan 2024 aplica a **cada defecto individual**. La quiralidad máxima es propiedad del defecto, no del bulk WW global. Esto es consistente con:
- H-003: fermiones = defectos.
- K-026 (refinada): la quiralidad no viene del bulk WW (que es no-quiral por Nielsen-Ninomiya en lattice sin frontera) sino de la **estructura de frontera del defecto**.

### 4.2 Compatibilidad con anomalías SM

**Condición Kaplan:** anomalías gauge canceladas. El SM tiene anomalías gauge canceladas (resultado clásico experimental + clasificación teórica). ✓

**Condición Wang-Wen:** anomalías globales (de 't Hooft) canceladas en SO(10). Se verifica por cobordismo (Ω^5 = ℤ₂; clase trivial). ✓

Entonces: **SCG cumple automáticamente las condiciones de aplicabilidad** del mecanismo.

### 4.3 Independencia de β

El mecanismo Kaplan 2024 + Wang-Wen 2018-2019 es **independiente de β** de Ashtekar:
- No requiere conexión autodual.
- No requiere Immirzi específico.
- La quiralidad es estructura lattice/topológica pura.

Compatibilidad con Randono β real (Q-040): **total**. El sector gravitacional (Ashtekar-Barbero) con β real preserva Kodama normalizable; el sector SM quiral emerge por Kaplan-Wang-Wen independientemente. **Los dos sectores son desacoplados en la cuestión de quiralidad**.

### 4.4 Consecuencia para K-019 (tercera reinterpretación)

K-019 original (sesión 9): "conexión autodual de Ashtekar = su(2)_L del Lorentz → SU(2)_L quiralidad gravitacional".

**Historial de reinterpretación:**
- (i) Sesión 9 (AMS 2014): **literal con β = -i**. Conexión autodual es literalmente su(2)_L.
- (ii) Sesión 22 (Q-040): **compatibilidad cualitativa con β real** (Randono). Violación P observacional preservada, pero asimetría máxima no automática.
- (iii) Sesión 24 (esta): **quiralidad es topológica, no gravitacional**. Viene de la estructura WW modular + Wang-Wen cobordismo + Kaplan edge states, **independiente de β**.

**K-019 se mantiene como insight**, pero con mecanismo físico distinto: "SU(2)_L emerge como edge mode quiral del defecto topológico WW, con anomalías canceladas via SO(10)". La conexión de Ashtekar (β real) es el sector **gravitacional**, no la fuente de la quiralidad SM.

### 4.5 Consecuencia para K-026 (debilitada significativamente)

K-026 original (sesión 11): "patrón quiral SM (SU(2) quiral / SU(3) U(1) no-quiral) coincide con patrón de origen dual (gravedad = quiral / red = no-quiral por Nielsen-Ninomiya)".

**Problema:** la red WW **puede ser quiral** en su frontera (modular + Wang-Wen + Kaplan). El argumento original "red no-quiral por Nielsen-Ninomiya" **no aplica** a redes con fronteras topológicas.

**Reinterpretación necesaria:** la dicotomía "gravedad quiral / red no-quiral" se rompe. La quiralidad SU(2)_L **no viene de la gravedad** sino de la estructura topológica de la red (modular UBFC + edge modes). Los factores SU(3) y U(1)_Y emergen no-quiralmente del bulk (vía trivalencia y modos transversales), consistentes con Nielsen-Ninomiya de bulk puro.

**K-026 se degrada de "confirmado estructural" a "observación heurística sin dualidad limpia".** La simetría entre "quiralidad SM" y "origen gravitacional/de red" ya no es sostenible bajo este marco.

### 4.6 Q-043 nueva

**Q-043: ¿existe UBFC modular específica para SCG con anomalías SM canceladas que produzca SU(3)×SU(2)×U(1) con contenido fermiónico SO(10)-GUT en frontera quiral?**

Esta pregunta concreta:
- Condiciones: (a) categoría de fusión trivalente (SCG); (b) modular (bulk invertible); (c) frontera hospeda 16 Weyl spinoriales de SO(10); (d) anomalías de 't Hooft canceladas por cobordismo.
- Candidatos naturales: Drinfeld center de SU(3) × SU(2) × U(1); Witt classes generadas por Ising MTC (2208.03397); UBFCs derivadas de SO(10) holografía.
- Esfuerzo estimado: 5-10 sesiones si se emprende.
- Si Q-043 se construye: K-030 pasa de "confirmado con ruta identificada" a **confirmado con construcción explícita**, y P-11 → ✅ resuelto. **Apertura mayor:** conexión SCG ↔ SO(10)-GUT (potencial K-033).

---

## 5. Evaluación de candidatos alternativos

### 5.1 Candidato 2 — Higgs / Condensación anyones (K-021)

Bais-Slingerland + Fradkin-Shenker establecen que condensación Higgs = confinamiento. K-021 (SCG): Higgs = condensación de anyón bosónico que confina SU(2)_L "gravitacional".

**¿Amplifica violación P?** **No automáticamente.** La condensación Higgs **asume** que ya existe estructura L-doublet; rompe SU(2)_L × U(1)_Y → U(1)_EM pero **presupone la estructura quiral**. El doblete de Higgs (j=½, Y=1) es **L por construcción**. Si la asimetría L-R máxima no existía previamente, Higgs no la genera; requiere el doblete ya L.

**Conclusión:** K-021 es ortogonal a Q-042. Opera sobre asimetría ya existente. No es alternativa a Kaplan 2024.

### 5.2 Candidato 1 — UBFC con simetría L específica

Es **el mismo mecanismo** que Kaplan 2024 + modular WW. Una UBFC quiral para WW es una "UBFC con simetría L" construible. No son mecanismos separados.

**Conclusión:** subsumido en 4.6 (Q-043).

### 5.3 Candidato 4 — Límite β → ∞

Especulativo. Sin literatura que lo soporte. No hay indicación de que β → ∞ genere asimetría máxima automáticamente.

**Conclusión:** descartar.

---

## 6. Veredicto sobre Q-042

### 6.1 Respuesta

**(D) MECANISMO EXISTE, independiente de β, aplicable a SCG, pero requiere construcción técnica concreta (Q-043 nueva).**

El mecanismo Kaplan 2024 + Wang-Wen 2018-2019 + modular Walker-Wang provee:
- Asimetría L-R máxima del SM ✓ (independiente de β).
- Compatibilidad con Randono β real ✓.
- Aplicabilidad a red WW 3+1D de SCG ✓.
- Anomalías gauge canceladas automáticamente ✓.
- Conexión natural con SO(10)-GUT (beneficio colateral).

**Pero:**
- Requiere construcción específica de UBFC modular SCG con contenido SO(10) (Q-043).
- Conceptualmente completo, técnicamente no cerrado.

### 6.2 Consecuencias para K-030

**K-030 se promueve de "candidato con reservas mayores" (Q-040) a "confirmado con ruta identificada, pendiente de construcción técnica (Q-043)".**

Esta es la primera promoción **positiva** de K-030 desde su introducción en sesión 17. Anteriores iteraciones (Q-039 negativo, Q-040 parcial) habían debilitado K-030. Q-042 lo fortalece significativamente al proveer mecanismo independiente de β.

**Condición de promoción a confirmado limpio:** Q-043 construida explícitamente.

### 6.3 Estado de P-11

**P-11 se rebaja de 🟡 media a 🟡 baja**, con caveat: dependencia en Q-043.

**Ruta lógica:**
- Randono β real → Kodama normalizable ✓ (sesión 17, K-030 parte A).
- Kaplan + Wang-Wen + modular WW → asimetría máxima SM independiente de β ✓ (sesión 24, Q-042).
- Los dos sectores (gravitacional via Randono; SM quiral via topología WW) son **estructuralmente separables**. β real para uno, topología para otro.

**Resultado:** P-11 deja de ser "premisa fuerte con costos identificados" y pasa a ser "premisa estructural con rutas concretas de mitigación establecidas en literatura". Riesgo bajo si Q-043 cierra.

**Si Q-043 falla:** P-11 regresa a 🟡 media.

### 6.4 Consecuencias para K-019 y K-026

- **K-019: tercera reinterpretación.** "SU(2)_L quiralidad emerge de frontera topológica WW, no de conexión gravitacional". Contenido empírico preservado; mecanismo reinterpretado.
- **K-026: degradada significativamente.** La dicotomía "gravedad quiral / red no-quiral" ya no se sostiene. K-026 pasa de "confirmado estructural" a "observación heurística sobre patrones sin dualidad limpia".

---

## 7. Re-evaluación de Ruta A

Tras 4 sesiones (20-22, 24):

| Pieza | Estado | Sesión |
|---|---|---|
| K-031 (llenado volumétrico) | ✅ PROMOVIDO | 20 |
| K-030 vía ABKP (Λ_UV) | ❌ Negativo | 21 |
| K-030 vía Randono (K-019) | ⚠️ Parcial, Q-042 nueva | 22 |
| **K-030 vía Kaplan+Wang-Wen+WW** | **✅ Promovido con Q-043 pendiente** | **24** |
| K-032 (matching II→IV) | Pendiente | — |
| K-028 (redshift riguroso) | Pendiente | — |

**Balance actualizado:** 2 promociones (K-031 limpia, K-030 con Q-043), 1 negativo (Q-039), 1 parcial (Q-040). La Ruta A **ha producido progreso neto** tras sesión 24.

**K-030 históricamente:** más fuerte que en sesión 17 por primera vez desde Q-039.

---

## 8. Apertura nueva: SO(10)-GUT como marco natural SCG

**Observación colateral:** Wang-Wen 2018-2019 usa específicamente SO(10)-GUT. El SM desde SO(10) tiene 16n fermiones quirales en representación spinorial.

**Si SCG adopta este marco:**
- SO(10) ⊃ SU(5) ⊃ SU(3) × SU(2) × U(1) — cadena gran unificación.
- El grupo gauge SCG (derivado en D-004 para SU(3)×SU(2)×U(1)) encaja en SO(10).
- La construcción Wang-Wen da ruta natural para embutir SCG en GUT.

**K-033 (CANDIDATO, potencial, no promovido en esta sesión):** *"SCG + WW modular + Wang-Wen = marco natural para SO(10)-GUT no-perturbativo en lattice 3+1D"*.

Esta es una apertura mayor. No se explora aquí (fuera del scope de Q-042). Probablemente programa de 10+ sesiones si se emprende. Abre conexión con GUT que SCG no tenía antes.

---

## 9. Honestidad epistémica

**Lo que Q-042 establece:**
- Mecanismo conceptualmente viable para asimetría máxima SM en SCG, independiente de β.
- K-030 promovido con ruta identificada.
- P-11 rebajada a 🟡 baja (pendiente Q-043).
- Apertura hacia SO(10)-GUT (K-033 potencial).

**Lo que Q-042 NO establece:**
- No construye UBFC modular específica para SCG (Q-043 queda abierta).
- No deriva cuantitativamente que asimetría sea *exactamente* máxima SM (solo que puede serlo topológicamente).
- No resuelve mirror sector específico para SCG (Wang-Wen provee el esquema, SCG necesita aplicación).
- No re-deriva α_1, α_2, α_3 (K-032 candidato sigue pendiente).

**Aplicación de K-005 ("teoría más modesta"):** Kaplan 2024 + Wang-Wen 2018-2019 + modular WW **son mecanismos ya establecidos en literatura** aplicados a SCG. SCG no "inventa" nada nuevo aquí — **adopta** un marco probado. Esto es consistente con la filosofía (más modesta, menos exótica).

**Aplicación de Regla 9 ("preferir destruir resultado propio"):** K-019 sufre tercera reinterpretación, K-026 se degrada significativamente. No se defienden por inercia. La quiralidad SM resulta ser **topológica**, no gravitacional — esto es un cambio conceptual en SCG. Aceptado honestamente.

**Aplicación de Regla 10 (K-005 "preguntar si lo viejo ya lo hace"):** la quiralidad SM puede explicarse por mecanismos lattice modernos (2018-2024). No hace falta postular nuevos principios gravitacionales. Adoptamos lo establecido.

---

## 10. Próximos pasos

### 10.1 Inmediatos (sesión 25)

- **Q-043 intentar acometer** (construcción UBFC modular SCG): si hay progreso técnico, K-030 → confirmado limpio; P-11 → ✅ resuelto.
- Alternativamente: **K-032** (matching II→IV explícito) o **K-028** (redshift riguroso P-15').

### 10.2 Medianos (sesiones 26-30)

- **Q-043 formalización** si parcial en 25.
- **K-033** exploración (SO(10) conexión) si Q-043 apunta en esa dirección.
- **Revisión K-019 + K-026** en documentos de framework (reflejar reinterpretación).

### 10.3 Largo plazo

- **Programa SO(10) SCG:** si K-033 se consolida, cambio estratégico hacia GUT lattice.
- **Masas fermiónicas via defectos WW** (Ruta B): consistente con construcción Wang-Wen.
- **Formalización completa de H-003** con nuevo mecanismo quiral.

---

## 11. Referencias

- Kaplan, D. B. (2024). *Chiral Gauge Theory at the Boundary between Topological Phases*. PRL 132, 141603. arXiv:2312.01494.
- Kaplan, D. B. & Sen, S. (2024). *Weyl Fermions on a Finite Lattice*. PRL 132, 141604. arXiv:2312.04012.
- Wang, J. & Wen, X.-G. (2018-2019). *A Solution to the 1+1D Gauged Chiral Fermion Problem*. PRD 99, 111501(R). arXiv:1807.05998.
- Wang, J. & Wen, X.-G. (2018). *A Non-Perturbative Definition of the Standard Models*. arXiv:1809.11171.
- Walker, K. & Wang, Z. (2011). *(3+1)-TQFTs and Topological Insulators*. arXiv:1104.2632.
- Kawagoe, K., Gorantla, P., Williamson, D. J. et al. (2023). *Disentangling modular Walker-Wang models via fermionic invertible boundaries*. PRB 107, 085134. arXiv:2208.03397.
- Randono, A. (2006). Tres papers: gr-qc/0504010, 0611073, 0611074.
- Alexander, Marciano, Smolin (2014). PRD 89, 065017. arXiv:1212.5246.
- Wen, X.-G. (2003). PRD 68, 065003. String-net condensation 3+1D.
- Nielsen, H. & Ninomiya, M. (1981). No-go theorem for lattice chiral fermions.

---

## 12. Firma

Q-042 parcialmente cerrada con veredicto (D): mecanismo conceptualmente viable, independiente de β, aplicable a SCG; requiere construcción técnica concreta (Q-043 nueva). K-030 se promueve por primera vez en sentido positivo desde su introducción. P-11 se rebaja a 🟡 baja con caveat Q-043. K-019 sufre tercera reinterpretación; K-026 se degrada. Apertura hacia SO(10)-GUT (K-033 potencial).

Ruta A tras sesión 24: 2 promovidos (K-031 limpio; K-030 con Q-043), 1 negativo (Q-039), 1 parcial (Q-040), 2 pendientes (K-028, K-032). Progreso neto positivo. Próxima sesión: Q-043 o K-032 o K-028.
