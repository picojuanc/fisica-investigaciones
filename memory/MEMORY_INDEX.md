# MEMORY_INDEX — Índice de memoria a largo plazo

Este archivo es el **primer punto de lectura** al iniciar cualquier sesión. Contiene enlaces a los archivos de memoria persistente.

## Archivos clave (leer siempre al iniciar)

| Archivo | Propósito | Prioridad |
|---|---|---|
| [session_log.md](session_log.md) | Bitácora cronológica de sesiones | ALTA |
| [current_focus.md](current_focus.md) | En qué se trabaja ahora mismo | ALTA |
| [open_questions.md](open_questions.md) | Preguntas sin responder | ALTA |
| [key_insights.md](key_insights.md) | Hallazgos acumulados | MEDIA |
| [dead_ends.md](dead_ends.md) | Caminos fallidos (evitar repetir) | MEDIA |

### Snapshots consolidados

Los snapshots son documentos autocontenidos de la teoría en un estado dado. Leer el más reciente antes de sumergirse en archivos individuales.

| Snapshot | Estado capturado | Fecha |
|---|---|---|
| [`../journal/2026-04-22_snapshot_v2.1.md`](../journal/2026-04-22_snapshot_v2.1.md) | **v2.1 — Post-K-032.M: K-032 CONFIRMADO ESTRUCTURALMENTE CON CAVEAT CUANTITATIVO (nuevo nivel epistémico). Forma funcional α_gauge ∝ γ_Immirzi derivada desde Plebanski-Holst + frontera CS + `Spin(10)_1` edge modes. Λ_efectiva≈0.2 M_P² (Reuter). Bosquejo Lagrangiana 5/5 CERRADO (4 limpias + 5.5 con caveat). D-011 nueva. P-8 ✅ cerrada con caveat. Regla 9 aplicada (retreat K-032.S → K-032.M).** | 2026-04-22 (sesión 35) |
| [`../journal/2026-04-22_snapshot_v2.0.md`](../journal/2026-04-22_snapshot_v2.0.md) | v2.0 — Post-Q-043: K-030 CONFIRMADO ESTRUCTURALMENTE. UBFC específica = `Spin(10)_1` MTC. P-11 RESUELTO ESTRUCTURALMENTE. K-033 activado (SO(10)-GUT). K-034 candidato (doble derivación Q=1/3). K-017 refuerzo. D-010 nueva. Bosquejo Lagrangiana 4/5 cerradas. Sin eslabones rojos; P-11 resuelto. (histórico) | 2026-04-22 (sesión 30) |
| [`../journal/2026-04-21_snapshot_v1.9.md`](../journal/2026-04-21_snapshot_v1.9.md) | v1.9 — Post-Q-042: K-030 promovido a "confirmado con ruta identificada" (Kaplan 2024 + Wang-Wen 2018-2019 + modular WW). P-11 rebajada a 🟡 baja. K-019 tercera reinterpretación (quiralidad topológica, no gravitacional). K-026 degradada. Q-043 nueva (UBFC modular SCG con SO(10)). K-033 potencial (SO(10)-GUT). Balance Ruta A: 2 promovidos + 1 negativo + 1 parcial + 2 pendientes. (histórico) | 2026-04-21 (sesión 24) |
| [`../journal/2026-04-21_snapshot_v1.8.md`](../journal/2026-04-21_snapshot_v1.8.md) | v1.8 — Consolidación post-Ruta A. D-009 añadida; K-031 promovido. Q-039 negativo + Q-040 parcial (K-030 con reservas mayores). Q-042 nueva. OVERVIEW.md externo (histórico) | 2026-04-21 (sesión 23) |
| [`../journal/2026-04-21_snapshot_v1.7.md`](../journal/2026-04-21_snapshot_v1.7.md) | v1.7 — Bosquejo estructuralmente completo. D-007, D-008. K-029 confirmado, K-030/K-031/K-032 candidatos. P-11 rebajada 🟡 alta → 🟡 media. Ciclo II→III cerrado. Patrón α₂≈α₃≠α₁ estructural (histórico) | 2026-04-21 (sesión 19) |
| [`../journal/2026-04-20_snapshot_v1.6.md`](../journal/2026-04-20_snapshot_v1.6.md) | v1.6 — Reducción axiomática (A-003 → D-006) + K-027 + bosquejo Lagrangiana + K-007 preservado + Casimir curvo + K-028 candidato (histórico) | 2026-04-20 (sesión 15) |
| [`../journal/2026-04-19_snapshot_v1.5.md`](../journal/2026-04-19_snapshot_v1.5.md) | v1.5 — Stress-test cadena + Walker-Wang + K-025 (punto fijo) + K-026 (quiralidad) (histórico) | 2026-04-19 (sesión 11) |
| [`../journal/2026-04-18_snapshot_v1.4.md`](../journal/2026-04-18_snapshot_v1.4.md) | v1.4 — H-001 + H-002 + H-003 formalizada + stress-test + generaciones + Higgs (histórico) | 2026-04-18 (sesión 10) |
| [`../journal/2026-04-17_snapshot_v1.3.md`](../journal/2026-04-17_snapshot_v1.3.md) | v1.3 — H-001 + H-002 + grupo gauge SU(3)×SU(2)×U(1) derivado (histórico) | 2026-04-17 (fin sesión 8) |
| [`../journal/2026-04-16_snapshot_H-001_v1.2.md`](../journal/2026-04-16_snapshot_H-001_v1.2.md) | H-001 v1.2 completa: derivaciones + literatura + falsabilidad (histórico) | 2026-04-16 (fin sesión 6) |
| [`../journal/2026-04-16_snapshot_H-001_v1.1.md`](../journal/2026-04-16_snapshot_H-001_v1.1.md) | H-001 v1.1 completa, sin eslabones rojos (histórico) | 2026-04-16 (fin sesión 4) |

**Regla:** si un snapshot contradice archivos más recientes, los archivos más recientes mandan. El snapshot es una foto fija.

## Mapa del conocimiento

### Marco teórico
- `framework/axioms.md` — axiomas fundamentales
- `framework/ontology.md` — qué entidades postula la teoría
- `framework/epistemology.md` — cómo conocemos dentro del marco

### Hipótesis
- `hypotheses/active/` — en investigación
- `hypotheses/confirmed/` — consistentes con todo hasta hoy
- `hypotheses/refuted/` — descartadas

### Evidencia / razonamiento
- `experiments/thought_experiments/` — gedanken-experiments
- `experiments/simulations/` — simulaciones y cálculos
- `logic/derivations/` — derivaciones paso a paso
- `logic/consistency_checks.md` — consistencia inter-hipótesis

## Convenciones de nomenclatura
- Hipótesis: `H-001`, `H-002`, ... en `hypotheses/active/H-001_titulo_corto.md`
- Experimentos mentales: `E-001`, `E-002`, ...
- Refutaciones: `R-001`, `R-002`, ...
- Derivaciones: `D-001`, `D-002`, ...
- Axiomas: `A-001`, `A-002`, ...
- Insights: `K-001`, `K-002`, ...
- Preguntas abiertas: `Q-001` (físicas), `QM-001` (metodológicas)
- Problemas identificados en una hipótesis: `P-1`, `P-2`, ... dentro del archivo de debilidades

## Inventario actual (2026-04-22, sesión 30 — Q-043 CERRADA estructuralmente; P-11 RESUELTO)

**Sesión 25:** integración de la reinterpretación v1.9 en el cuerpo de H-003, framework/axioms.md (premisa operativa v1.9) y marcadores en memory/key_insights.md (K-019, K-026). Ningún descubrimiento técnico; consistencia documental recuperada. Sin snapshot nuevo.

**Sesión 26:** primera iteración sobre Q-043. Planteamiento formal + reducción analítica (4 condiciones → 2 efectivas: modularidad + espectro SO(10)) + criba de candidatos. **Candidato principal identificado: `Spin(10)_k` MTC** (k tentativo = 1). C1 y C2 descartados. Obstrucciones O1-O6 listadas; bloqueantes (O1, O2, O5). Roadmap sesiones 27-30 trazado. Ver `notes/Q-043_UBFC_modular_SCG.md`.

**Sesión 27:** O1 + O6 confirmados. Cálculo Kac-Moody: rep 16 (λ=ω_4) integrable en `Spin(10)_1` pues (ω_4, θ)=1. Espectro MTC explicitado: 4 objetos simples {1, v(10), s(16), c(16̄)}, fusión Z_4 cíclica, c=5. Cuantización Q en 1/3 verificada por doble derivación (K-015 trivalente ↔ ruptura SU(5) algebraica); **K-034 candidato potencial** registrado (promoción diferida). UBFC candidata específicamente = `Spin(10)_1` (+ super-modular extension). Caveat: fermionic extension pendiente. K-030 NO se promueve (requiere O2+O5). Ver `notes/Q-043_sesion27_O1_O6.md`.

**Sesión 28:** O2 confirmada con caveat estructural. Tres sub-tareas: (1) Z_4 fusion compatible con lattice trivalente (10 triples admisibles mod 4); (2) Z_4 y Z₃ geométrico coprimos → capas estructurales independientes; (3) cadena de ruptura SO(10)→SU(5)→SM realiza Z₃_geom ≡ centro SU(3) via Wang-Wen. **K-017 gana interpretación más limpia** en Q-043 framework (identificación geométrica directa; ya no requiere unicidad de órdenes topológicos). Segunda "doble derivación" sugerente (tras K-015/K-034). Caveat: argumento estructural, no constructivo — estándar literatura, no específico SCG. K-030 NO se promueve (pendiente O5). Ver `notes/Q-043_sesion28_O2.md`.

**Sesión 29:** O5 confirmada con caveat estructural. Formalización del desacople sector gravitacional (Σ, A_BI, ψ, e + simplicidad, torsión, Randono, ADM) / sector topológico SM (λ_e, μ_v, ν_p + fusión, modularidad, cobordismo, condensación). Variables disjuntas; restricciones disjuntas; lagrangianas aditivas S_total = S_grav + S_top + S_int con S_int suave (QFT curvo). Chequeo Regla 9: ningún resultado previo refutado. K-017 refuerzo acumulado. **TODAS las obstrucciones bloqueantes (O1, O2, O5, O6) cerradas por primera vez.** K-030 NO se promueve (disciplina Regla 5; esperar evaluación global). P-11 🟡 baja estable. Ver `notes/Q-043_sesion29_O5.md`.

**Sesión 30:** Q-043 **CERRADA estructuralmente**. Evaluación global (sin trabajo técnico nuevo): chequeo cruzado de consistencia, evaluación de caveats agregados, decisiones de promoción. **K-030 promovido** a "confirmado estructuralmente"; **P-11 ✅ RESUELTO ESTRUCTURALMENTE**; **K-033 activado** a candidato formal (SO(10)-GUT en SCG); **K-034 promovido** a candidato formal (doble derivación Q=1/3); **K-017 refuerzo** documentado. **D-010 escrita** — síntesis formal del cierre. **Snapshot v2.0** publicado (autocontenido, cubre sesiones 0-30). **Reporte narrativo #25** publicado. Actualización documental completa (H-003, axioms.md, debilidades_H-001.md, key_insights.md, MEMORY_INDEX.md, session_log.md, open_questions.md). El fantasma existencial desde sesión 11 se disuelve **sin agregar axiomas nuevos**. Ver `notes/Q-043_sesion30_evaluacion_global.md`, `logic/derivations/D-010_Q-043_sintesis.md`, `journal/2026-04-22_snapshot_v2.0.md`, `journal/reportes/25_cierre_Q-043.md`.

**Sesión 31:** Campaña K-032 abierta (matching II→IV, última sub-tarea Lagrangiana). Formalización (K-032.S fuerte vs K-032.W débil). 4 mecanismos candidatos (M1-M4); **M3 seleccionado** (término de Holst → frontera CS → α = γ/(4π)). Compatibilidad con D-010 verificada conceptualmente. Programa 4 sesiones (32-35) delineado. Sin cálculo técnico nuevo. Ver `notes/K-032_sesion31_formalizacion.md`.

**Sesión 32:** M3 paso 1 (Plebanski-Holst + frontera CS). **Resultado positivo parcial:** k_Holst ∝ 1/(γκΛ); forma funcional α ∝ γ derivada. **P-M3.1 verificada.** Reducción a "Λ_efectiva en régimen II ~ O(0.1) M_P²". Ver `notes/K-032_sesion32_M3_Holst_frontera.md`.

**Sesión 33:** Λ_efectiva en régimen II. Exploración sistemática de 4 rutas: (b) **Reuter asymptotic safety λ*≈0.2 anclaje más robusto**. Convergencia [0.03, 1] M_P². **K-032.M intermedio** introducido. Hipótesis sugerente C = 4π·c = 63 a testear. Ver `notes/K-032_sesion33_Lambda_efectiva.md`.

**Sesión 34:** Edge modes `Spin(10)_1` + CS-WZW. **Retreat honesto (Regla 9)** a K-032.M. Hipótesis C = 4π·c NO se sostiene (c es densidad de estados, no multiplica coupling). Embedding canónico + RG running no cierran K-032.S al 1%. **K-032.M formalizada como veredicto final.** Ver `notes/K-032_sesion34_edge_modes.md`.

**Sesión 35:** Evaluación global tramo K-032 + consolidación. **K-032 promovido** a "confirmado estructuralmente con caveat cuantitativo" (nuevo nivel epistémico, definido en D-011). **P-8 ✅ cerrado con caveat cuantitativo**; bosquejo Lagrangiana 5/5 cerradas (4 limpias + 5.5 con caveat). **D-011 escrita** — síntesis formal K-032.M. **Snapshot v2.1** publicado. **Reporte narrativo #26** publicado. Actualización documental: key_insights.md, debilidades_H-001.md, H-003, MEMORY_INDEX.md. Disciplina K-005 + Regla 5 + Regla 9 aplicadas ejemplarmente. Ver `logic/derivations/D-011_K-032_sintesis.md`, `journal/2026-04-22_snapshot_v2.1.md`, `journal/reportes/26_matching_II_IV_K-032.md`.

### Axiomas activos (v1.2, post-sesión 13)
- A-001: corte Planck (válido)
- A-002: transición de fase gravitacional
- ~~A-003~~ → **D-006** (derivado en sesión 13: Casimir de Polyakov transversal con corte Planck)

### Hipótesis activas
- **H-001 (v1.2)** — Fase de Cuerda Gravitacional Estabilizada (SCG). Madura: derivaciones, literatura, predicción falsable.
- **H-002** — Dimensionalidad del espacio D=3 emerge de topología de cuerdas 1D (codimensión 2). (2026-04-16, sesión 7)
- **H-003** — Partículas del SM son excitaciones topológicas de la red SCG; grupo gauge SU(3)×SU(2)×U(1) emergente. (2026-04-18, sesión 10)

### Experimentos mentales registrados
- E-001: Trompeta de Gabriel gravitacional (refutado en forma naïve, detonador)
- E-002: Rotación y área del horizonte (cierra escapatoria)
- E-003: Estiramiento del horizonte a hilo (fundacional para H-001)
- E-004: Hilo cuántico — cuerda fundamental o emergente
- E-005: Analogía Chandrasekhar para la cuerda gravitacional (2026-04-16)
- E-006: Ecos de ondas gravitacionales como firma distintiva (2026-04-16, sesión 6)
- E-007: ¿Qué pasaría en un universo 4D con cuerdas 1D? (2026-04-16, sesión 7)
- **E-008: Nudos como partículas — cadena SCG → Levin-Wen → Chern-Simons** (2026-04-17, sesión 8)
- E-009: Tres generaciones (Z₃ dual) y mecanismo de Higgs (condensación de anyones) (2026-04-18, sesión 9)

### Derivaciones
- D-001: Modelo discreto de cuerda gravitacional
- D-002: Dimensionalidad crítica (D=1 derivada por balance de exponentes) (2026-04-16)
- D-003 (v1.2): Conservación entrópica por plegado de la cuerda interior, d ~ √(r_s ℓ_P) (2026-04-16; v1.2 sesión 14: clarifica que A-003 era motivacional, no esencial)
- **D-004: Reglas de fusión en vértices SCG — U(1) derivado, Z₃ derivado, SU(2) motivado** (2026-04-17, sesión 8)
- **D-005: D_tiempo = 1 — de la factorización de Dynkin (so(4) única) + H-002** (2026-04-19, sesión 10)
- **D-006: A-003 v1.1 como presión de Casimir de Polyakov transversal con corte Planck (promueve K-027; A-003 deja de ser axioma)** (2026-04-20, sesión 13)
- **D-007: Ecuaciones de movimiento de S_Plebanski-autodual + Λ → E-H + Λ autodual on-shell; A = su(2)_L; frontera CS(k=2π/κΛ) (promueve K-029; tarea 5.2 del bosquejo Lagrangiana cerrada)** (2026-04-21, sesión 16)
- **D-008: Reducción dimensional S_PA → acción efectiva 2D de cuerda SCG en fondo BH. K-007 recuperado (segunda derivación); D-001/D-003/D-006/D-007 integrados bajo S_SCG-2D. Tarea 5.4 parcial. K-031 candidato.** (2026-04-21, sesión 18)
- **D-009: Llenado volumétrico L·d²=V_BH emerge variacionalmente bajo minimización de E_Casimir + E_tens sujeta a restricción de confinamiento geométrico. Promueve K-031 a confirmado estructuralmente. D-008 deja de depender de ansatz A2.** (2026-04-21, sesión 20)
- **D-010: Síntesis formal del cierre Q-043. UBFC específica = `Spin(10)_1` MTC (+ super-modular extension estándar) + desacople sector gravitacional/topológico + cadena de ruptura SO(10) → SU(5) → SM. Promueve K-030 a "confirmado estructuralmente"; rebaja P-11 a ✅ resuelto estructuralmente; activa K-033 a candidato formal; promueve K-034 a candidato formal; documenta refuerzo K-017. Define terminología de 3 niveles de confirmación (limpio/estructural/candidato).** (2026-04-22, sesión 30)
- **D-011: Síntesis formal del cierre K-032 (tramo 31-34). Forma funcional α_gauge(M_P) ∝ γ_Immirzi derivada desde matching Plebanski-Holst (frontera CS_I) + edge modes quirales `Spin(10)_1` + Reuter asymptotic safety. Promueve K-032 a "confirmado estructuralmente con caveat cuantitativo" (nuevo nivel epistémico introducido). Cierra P-8 con caveat (5/5 sub-tareas Lagrangiana). Regla 9 aplicada: retreat K-032.S (identidad exacta al 1%) → K-032.M (forma funcional + cota). Patrón α₂ ≈ α₃ ≠ α₁ derivado (vértice vs segmento).** (2026-04-22, sesión 35)

### Simulaciones
- sim001_cuerda_basica.js (+ sim001_resultados.md)

### Bosquejos estructurales
- **`notes/R_lagrangiana_bosquejo.md`** — bosquejo arquitectónico de la Lagrangiana SCG (sesión 12): 4 regímenes, acción madre candidata (Plebanski-autodual + Λ + defectos), 5 tensiones, 5 tareas propuestas.

### Insights confirmados
- K-001: área geométrica ≠ grados de libertad físicos
- K-002: naturaleza minimiza energía, no maximiza área
- K-003: modelo toy SCG exhibe transición de fase cualitativa
- K-004: "presión de información" = presión cinética cuántica convencional (2026-04-16)
- K-005: lección meta — teoría buena es más modesta, no más exótica (2026-04-16)
- K-006: D=1 emerge como única dimensión con balance E_deg ↔ E_grav ∀ N (2026-04-16, sesión 3)
- K-007: escala interior del BH es la media geométrica d ~ √(r_s·ℓ_P) (2026-04-16, sesión 4)
- K-008: la cuerda plegada sugiere resolución de la paradoja de información (2026-04-16, sesión 4)
- K-009: H-001 v1.1 NO es equivalente a fuzzballs ni stretched horizon — originalidad confirmada (2026-04-16, sesión 5)
- K-010: H-001 v1.1 predice retraso de ecos GW la MITAD que modelos Planck-scale — predicción falsable (2026-04-16, sesión 6)
- K-011: D_espacio = 3 se deriva de p=1 + codimensión 2 (nudos) (2026-04-16, sesión 7)
- K-012: cadena SCG → Levin-Wen → Chern-Simons → partículas topológicas es lógicamente viable (2026-04-17, sesión 8)
- K-013: violación de paridad emerge automáticamente de Chern-Simons (2026-04-17, sesión 8)
- **K-014: U(1) gauge emerge del momento angular transversal de las cuerdas SCG** (2026-04-17, sesión 8)
- **K-015: cuantización de carga en 1/3 emerge de trivalencia Z₃ de vértices en D=3** (2026-04-17, sesión 8)
- K-016: 2 de 3 factores del grupo gauge del SM (U(1), SU(2)) + centro Z₃ de SU(3) emergen de la geometría SCG (2026-04-17, sesión 8)
- **K-017: Z₃ + quiralidad gravitacional = SU(3)₁ por unicidad → grupo gauge COMPLETO SU(3)×SU(2)×U(1)** (2026-04-17, sesión 8)
- K-018: confinamiento de color = manifestación IR de la trivalencia UV del vértice SCG (2026-04-17, sesión 8)
- K-019: Ashtekar autodual = su(2)_L del grupo de Lorentz — quiralidad de la fuerza débil es gravitacional (2026-04-18, sesión 9)
- **K-020: 3 generaciones = Z₃ del grafo dual (Z₃_primal×Z₃_dual) — N_gen=N_color=3 por trivalencia** (2026-04-18, sesión 9, especulativo)
- **K-021: Higgs = condensación de anyones = confinamiento de gravedad SU(2)_L (Bais-Slingerland + Fradkin-Shenker)** (2026-04-18, sesión 9)
- **K-022: D_espacio + D_tiempo = 4 es la ÚNICA dimensionalidad con factorización quiral (Dynkin) → D_tiempo = 1** (2026-04-19, sesión 10)
- K-023: α₂(M_P) ≈ α₃(M_P) ≈ γ_Immirzi/(4π) — near-convergence consistente con origen geométrico común, coincidencia numérica con Immirzi al 1% (2026-04-19, sesión 10, observación)
- ~~P-9: k=1 vs k~300~~ **RESUELTO** (K-024: grupo gauge y nivel CS son independientes) (2026-04-19, sesión 10)
- **K-024: grupo gauge (topología) y nivel CS (dinámica) son independientes → SU(3) sobrevive a cualquier k** (2026-04-19, sesión 10)
- **K-025: la cadena dimensional (D_object, D_espacio, D_tiempo) es punto fijo auto-consistente, no cascada de derivaciones** (2026-04-19, sesión 11)
- **K-026: el patrón quiral del SM (SU(2) quiral, U(1)/SU(3) no-quirales) coincide con el origen dual en SCG (gravedad=quiral, red=no-quiral)** (2026-04-19, sesión 11)

- **K-027: A-003 = efecto Casimir de modos transversales de Polyakov con corte Planck → axioma removido, D-006 deriva la forma** (2026-04-20, sesión 13, promovido de candidato a confirmado estructuralmente)
- **K-029: núcleo gravitacional de S_madre (Plebanski-autodual + Λ) on-shell ≡ E-H + Λ autodual; A = su(2)_L; frontera CS(k=2π/κΛ) — reconfirma K-019 desde primeros principios clásicos** (2026-04-21, sesión 16, confirmatorio/estructural vía D-007)
- **K-030 (CONFIRMADO ESTRUCTURALMENTE sesión 30): SCG + Walker-Wang modular sobre `Spin(10)_1` + ruptura Wang-Wen + sector gravitacional desacoplado con Randono β real cierra estructuralmente P-11. UBFC específica y espectro identificados.** (sesión 17 candidato → sesión 24 con ruta → sesión 30 confirmado estructuralmente via D-010)
- **K-031: reducción S_PA → S_SCG-2D por reducción dimensional; D-008 + D-009 (variacional)** (2026-04-21, sesión 18+20)

### Insights candidatos (pendientes v2.0)
- **K-028 (candidato, 2026-04-20, sesión 15):** redshift gravitacional promedio del interior de un BH-SCG es ⟨f⟩ ≈ 1/(3π²). Obtenido por consistencia ADM; rigorización pendiente (P-15').
- ~~K-032 (candidato, 2026-04-21, sesión 19)~~ **PROMOVIDO a "CONFIRMADO ESTRUCTURALMENTE CON CAVEAT CUANTITATIVO" (sesión 35, D-011).** Ver sección `### Insights confirmados` al final. Resumen: forma funcional α_gauge ∝ γ_Immirzi derivada estructuralmente desde Plebanski-Holst + frontera CS + `Spin(10)_1` edge modes. Valor numérico en rango [0.005, 0.1] consistente con α_SM; identidad α_3 ≈ γ/(4π) al 1% sugerente pero no derivada. Regla 9 aplicada.
- **K-033 (CANDIDATO FORMAL — ACTIVADO sesión 30):** SCG + `Spin(10)_1` modular Walker-Wang + Wang-Wen 2018-2019 = marco natural para SO(10)-GUT no-perturbativo en lattice 3+1D. Base técnica del cierre de P-11. Programa asociado abierto: masas fermiónicas, Yukawas, CKM/PMNS. 10+ sesiones si se emprende.
- **K-034 (CANDIDATO FORMAL — PROMOVIDO sesión 30):** la cuantización Q en 1/3 tiene doble derivación en SCG: (a) K-015 desde trivalencia Z₃ geométrica; (b) ruptura algebraica SO(10) → SU(5) → SM. Convergencia estructural; corroboración cruzada. Promoción a confirmado requiere demostrar equivalencia rigurosamente.

### Tensiones identificadas
- T-1: k topológico (CY) vs k dinámico (α ~ 0.02) (sesión 12, alta)
- T-2: Kodama no normalizable / conexión compleja (sesión 12, alta — = P-11 expandido)
- T-3: Walker-Wang Hamiltoniano vs acción (sesión 12, media — puentada por Baez 2000)
- T-4: matter como defectos de A vs S_matter separado (sesión 12, media — programa Bilson-Thompson)
- ~~T-5: forma de E_info~~ **RESUELTA (sesión 13, D-006 + K-027):** E_info = efecto Casimir de Polyakov transversal.
- ~~T-6~~ **CERRADA HEURÍSTICAMENTE (sesión 15):** E_Casimir plano absorbe su exceso en redshift gravitacional promedio ⟨f⟩ = 1/(3π²). K-028 candidato propuesto. Cálculo riguroso como P-15'.

### Debilidades (actualizado 2026-04-22, sesión 30)
- ~~P-10: 🔴~~ → **P-10: 🟡 parcialmente resuelto** (Wen 2003, Walker-Wang, Crane-Yetter, K-026) (sesión 11)
- ~~P-11: 🟡 baja~~ → **P-11: ✅ RESUELTO ESTRUCTURALMENTE (sesión 30, D-010).** Q-043 cerrada estructuralmente; UBFC específica `Spin(10)_1` identificada; sector gravitacional (Randono β real) y sector topológico (Walker-Wang sobre `Spin(10)_1`) desacoplables. Las 4 patologías de Witten 2003 mitigadas. Reserva de "resuelto limpio puro" para futura construcción constructiva explícita del lattice SM.
- **P-8: ✅ CERRADO CON CAVEAT CUANTITATIVO (sesión 35, D-011). Arquitectura completa, 5/5 sub-tareas cerradas** (4 limpias + 5.5 con caveat). Confirmadas: 5.1 (D-006), 5.2 (D-007), 5.3 cerrada via D-010 sesión 30 (K-030 confirmado estructuralmente), 5.4 (D-008 + D-009, K-031), **5.5 cerrada con caveat cuantitativo via D-011 sesión 35 (K-032 confirmado estructuralmente con caveat cuantitativo).** Residual: refinamiento cuantitativo K-032.M → K-032.S (opcional, 3-5 sesiones técnicas adicionales).
- **P-14 🟡 (sesión 13):** consistencia cuántica de Polyakov 4D no-crítica como teoría efectiva WW. Plausible pero sin demostración formal.
- **P-15' 🟡 baja (sesión 14 → rebajada 15):** cálculo riguroso de redshift interior BH; T-6 cerrada heurísticamente vía K-028 candidato.
- ✅ **P-1 resuelto mayor (sesión 13):** A-003 derivado como Casimir de Polyakov (D-006). K-027 confirmado.
- P-3: camino abierto (horizonte macro + cuerda interior)
- P-5: parcialmente resuelto (D=1 derivada); sub-problema P-5.1 abierto
- P-7: parcialmente resuelto (plegado + holografía saturada); sub-problemas P-7.1, P-7.2 abiertos
- **P-4 REABRE CUANTITATIVAMENTE (sesión 13):** cuerda SCG = Polyakov en IR del defecto WW. Comparación directa con Horowitz-Polchinski ahora tractable.
- **SIN ESLABONES ROJOS.**

### Stress-tests realizados
- `logic/stress_test_D-004.md` — D-004 pasa (sesión 9)
- **`logic/stress_test_cadena_completa.md`** — cadena completa: 1 rojo (P-10), 3 naranjas, resto verde (sesión 11)

### Preguntas abiertas
- Q-014: ¿qué son los grados de libertad gravitacionales? (subsumida en Q-025)
- Q-015: análogo de M_Chandrasekhar
- Q-016: término subdominante para L*
- Q-017: dinámica de formación de cuerda plegada
- Q-018: relación con fuzzballs (parcialmente cerrada)
- Q-019: correlación cuerda ↔ Hawking
- Q-025: reglas de fusión — **PARCIALMENTE RESUELTA** (D-004)
- Q-026: Z₃ → SU(3) — **RESUELTA CONCEPTUALMENTE**
- Q-027: niveles CS k
- Q-028: ¿Higgs = fase de red SCG?
- ~~Q-029~~ **RESUELTA: sí, D-004 se transfiere a 3+1D** (Wen 2003 constructivo; Walker-Wang framework; K-026 quiralidad)
- **Q-030: ¿punto fijo dimensional (1,3,1) es único formalmente?** (sesión 11)
- **Q-031: ¿existe conexión gravitacional quiral sin problemas de la autodual?** (sesión 11)
- ~~Q-032~~ **RESUELTA (sesión 13, D-006):** SÍ. A-003 = Casimir de Polyakov transversal con corte Planck. K-027 confirmado.
- **Q-033: ¿frontera de Plebanski+Λ es CS con k=2π/Λ, incluyendo correcciones de ψ?** — **PARCIALMENTE RESUELTA (sesión 16, D-007):** SÍ para el término dominante (Baez 2000 aplicado a nuestro núcleo); correcciones por ψ argumentadas sub-dominantes pero no computadas.
- **Q-034: ¿el flujo RG entre II y IV preserva k como topológico o lo modifica?** (sesión 12)
- **Q-035: ¿defectos de A en la red SCG reproducen el contenido fermiónico del SM?** (sesión 12)
- ~~Q-036~~ **RESUELTA (sesión 14):** SÍ, K-007 se preserva. D-003 no dependía esencialmente de A-003. Ver `notes/Q-036_K-007_sin_A-003.md`.
- **Q-037: prefactor Casimir en topología worldsheet** — **PARCIALMENTE RESUELTA (sesión 15):** para H-001 (bucle cerrado) = 2π, confirmado. Pendiente para H-003.
- **Q-038: Casimir en fondo curvo** — **CERRADA HEURÍSTICAMENTE (sesión 15):** ⟨f⟩_redshift = 1/(3π²) por consistencia ADM. K-028 candidato. Rigorización pendiente (P-15').
- **Q-039: Λ_UV régimen I** — **PARCIALMENTE RESUELTA con resultado NEGATIVO (sesión 21):** Λ_UV ≪ Λ_c ABKP. Ruta ABKP no cierra K-030 completamente.
- **Q-040: compatibilidad Randono β real ↔ K-019** — **PARCIALMENTE RESUELTA con veredicto (C) (sesión 22):** preserva viabilidad pero NO asimetría máxima SM. K-019 debilitado.
- **Q-041: llenado volumétrico variacional** — **PARCIALMENTE RESUELTA (sesión 20, D-009):** A2 deriva bajo KKT. K-031 promovido.
- **Q-042: mecanismo amplificación P** — **PARCIALMENTE RESUELTA con veredicto (D) (sesión 24):** Kaplan 2024 + Wang-Wen 2018-2019 + modular WW. K-030 promovido a "confirmado con ruta identificada"; P-11 rebajada a 🟡 baja. K-019 tercera reinterpretación; K-026 degradada. Ver `notes/Q-042_mecanismo_amplificacion_P.md`.
- **Q-043 nueva (sesión 24, prioridad alta):** ¿UBFC modular específica para SCG con contenido SO(10) que cancele anomalías y dé asimetría SM máxima? Decide promoción final de K-030 a confirmado limpio.

## Cómo actualizar este índice
Cada vez que:
- Se añade un archivo con impacto estructural → registrar aquí.
- Se mueve una hipótesis entre `active/`, `confirmed/`, `refuted/` → actualizar.
- Se cambia una convención → documentar aquí.
