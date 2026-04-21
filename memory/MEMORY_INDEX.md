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
| [`../journal/2026-04-21_snapshot_v1.7.md`](../journal/2026-04-21_snapshot_v1.7.md) | **v1.7 — Bosquejo Lagrangiana estructuralmente completo. D-007, D-008. K-029 confirmado, K-030/K-031/K-032 candidatos. P-11 rebajada 🟡 alta → 🟡 media. Ciclo II→III cerrado. Patrón α₂≈α₃≠α₁ estructural.** | 2026-04-21 (sesión 19) |
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

## Inventario actual (2026-04-21, sesión 21)

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

### Insights candidatos (pendientes)
- **K-028 (candidato, 2026-04-20, sesión 15):** redshift gravitacional promedio del interior de un BH-SCG es ⟨f⟩ ≈ 1/(3π²). Obtenido por consistencia ADM; rigorización pendiente (P-15').
- **K-030 (candidato, 2026-04-21, sesión 17):** P-11 (Ashtekar autodual / patologías Kodama) admite mitigación estructural vía (a) ABKP 2025 (inner product holomorfico + Λ > Λ_c = 384/ℓ_P²); (b) Randono 2006 (β real, preserva CP violation). SCG añade 4 mitigantes estructurales. Severidad P-11 pasa de 🟡 alta a 🟡 media. Formalización HK-SCG pendiente.
- ~~K-031 (candidato)~~ **K-031 CONFIRMADO (sesión 20):** la acción efectiva 2D de cuerda SCG emerge por reducción dimensional de S_PA. D-009 deriva A2 (llenado volumétrico) variacionalmente. La promoción del candidato es efectiva. Ciclo Régimen II → III del bosquejo cerrado con base sólida.
- **K-032 (candidato, 2026-04-21, sesión 19):** el patrón α₂(M_P)≈α₃(M_P)≠α₁(M_P) emerge estructuralmente de "gauge de vértice (SU(2)_L, SU(3)) vs gauge de segmento (U(1)_Y)" en la red WW 3+1D. Coincidencia numérica α_3(M_P) ≈ γ_Immirzi/(4π) al 1% sugiere que γ fija el acoplamiento gauge de vértice a escala Planck. Flujo RG II→IV preserva grupo gauge (K-024) + level shifting. Primera predicción cuantitativa estructural de SCG. Promoción requiere derivar α = γ/(4π) formalmente + verificar discrepancia α_2 vs α_3 via 2-loops.

### Tensiones identificadas
- T-1: k topológico (CY) vs k dinámico (α ~ 0.02) (sesión 12, alta)
- T-2: Kodama no normalizable / conexión compleja (sesión 12, alta — = P-11 expandido)
- T-3: Walker-Wang Hamiltoniano vs acción (sesión 12, media — puentada por Baez 2000)
- T-4: matter como defectos de A vs S_matter separado (sesión 12, media — programa Bilson-Thompson)
- ~~T-5: forma de E_info~~ **RESUELTA (sesión 13, D-006 + K-027):** E_info = efecto Casimir de Polyakov transversal.
- ~~T-6~~ **CERRADA HEURÍSTICAMENTE (sesión 15):** E_Casimir plano absorbe su exceso en redshift gravitacional promedio ⟨f⟩ = 1/(3π²). K-028 candidato propuesto. Cálculo riguroso como P-15'.

### Debilidades (actualizado 2026-04-20, sesión 13)
- ~~P-10: 🔴~~ → **P-10: 🟡 parcialmente resuelto** (Wen 2003, Walker-Wang, Crane-Yetter, K-026) (sesión 11)
- P-11: 🟡 **media** (rebajada sesión 17; refinada sesión 21). Dependencia en Ashtekar autodual. K-030 candidato refinado: **Randono 2006 (β real) es la ruta primaria**; ABKP 2025 da mitigación parcial (Λ_UV en régimen I NO excede Λ_c; Q-039 negativa). Q-040 (compatibilidad K-019 ↔ β real) en **prioridad ALTA**. Destino final de K-030 depende de Q-040.
- **P-8: 🟡 arquitectura completa, 3/5 confirmadas estructuralmente + 2/5 parciales** (sesiones 12-20). Confirmadas: 5.1 (D-006), 5.2 (D-007), 5.4 (D-008 + D-009, K-031 promovido). Parciales con candidato: 5.3 (K-030), 5.5 (K-032). Piezas cuantitativas pendientes de Ruta A: Q-039 (Λ_UV → promueve K-030), matching II→IV explícito (→ promueve K-032), K-028 riguroso.
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

## Cómo actualizar este índice
Cada vez que:
- Se añade un archivo con impacto estructural → registrar aquí.
- Se mueve una hipótesis entre `active/`, `confirmed/`, `refuted/` → actualizar.
- Se cambia una convención → documentar aquí.
