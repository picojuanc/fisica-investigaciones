# R — Bosquejo arquitectónico de la Lagrangiana SCG

- **Fecha:** 2026-04-20 (sesión 12)
- **Ataca:** P-8 (dinámica temporal / acción) — la debilidad estructural más seria post-sesión 11.
- **Alcance:** **bosquejo**, no derivación completa. Mapeo del territorio; identificación de candidatos, tensiones, y próximos pasos.
- **Honestidad epistémica:** siempre que un eslabón sea ansatz, se marca. Se distingue **derivación** vs **ansatz estructural** vs **analogía**.

---

## 0. Planteamiento del problema

La teoría SCG, al cierre de sesión 11, tiene:
- un estado (cuerda gravitacional estabilizada, H-001);
- una red (Walker-Wang/Crane-Yetter 3+1D, H-003);
- un grupo gauge emergente (SU(3)×SU(2)×U(1));
- escalas derivadas (d ~ √(r_s ℓ_P));
- una predicción falsable (ecos GW).

**Lo que no tiene:** una acción *S* de la cual se deriven amplitudes, masas, constantes numéricas, ecuaciones de movimiento. Sin ella:
- No hay dinámica temporal.
- No hay cuantización rigurosa (∫ DA e^{iS/ℏ} requiere S).
- No hay predicciones cuantitativas más allá de las puramente dimensionales.
- Toda afirmación sobre "flujo del grupo gauge" o "renormalización" es heurística.

P-8 es por eso la prioridad 1 tras la sesión 11.

**El obstáculo:** la teoría SCG vive en 4 regímenes con descripciones naturales distintas. Una Lagrangiana total debería:
1. Reducirse a cada descripción en su régimen.
2. Ser internamente consistente (no dos acciones incompatibles).
3. Preservar los resultados ya derivados (D-002/H-002/D-005, D-003, D-004, K-019, K-026).

---

## 1. Los cuatro regímenes

Recordemos la imagen de tres regímenes de K-024, refinada:

| # | Régimen | Escala | Descripción natural | Invariante dominante |
|---|---|---|---|---|
| **I** | Pre-geométrico | E ≫ M_P | TQFT 4D (Crane-Yetter / Walker-Wang) | Topológico |
| **II** | Semiclásico | E ~ M_P | Plebanski autodual + Kodama-CS | Gravitacional local |
| **III** | Fase SCG (BH) | densidad ~ ρ_P | Cuerda efectiva 1D en fondo curvo | Geométrico local |
| **IV** | IR | E ≪ M_P | SM + GR semiclásica | QFT estándar |

La "madre" debe dar a cada régimen su descripción. Procedemos régimen por régimen.

---

## 2. Candidatos por régimen

### 2.1 Régimen I — UV pre-geométrico: Crane-Yetter / Walker-Wang

**Candidato principal:** state-sum de Crane-Yetter (1993) con MTC (modular tensor category) como input.

Construcción state-sum sobre triangulación de una 4-variedad *M*:

```
Z_CY[M, 𝒞] = Σ_{coloreos} [ Π_faces d_a · Π_tetrahedra {15j}_𝒞 ]
```

donde 𝒞 es la MTC, *d_a* son dimensiones cuánticas, {15j} es el símbolo 15j cuántico. Para 𝒞 = Rep(U_q(su(2))) con q = e^{iπ/k}, reproduce **gravedad 4D euclidiana con constante cosmológica** (Baez 2000) — es decir, es una discretización de BF+Λ.

**Forma Lagrangiana continua asociada** (via Plebanski):

```
S_CY[B, A] = ∫_M [ B^I ∧ F_I(A) − (Λ/2) B^I ∧ B_I ]
```

donde *B* es una 2-forma con valor en *su(2)_C* (autodual), *A* es la conexión autodual, *F(A)* su curvatura.

**Por qué es candidato:**
- La categoría 𝒞 admite el *braiding* necesario para los defectos trivalentes de SCG (K-017: SU(3)₁ es el braiding uniforme con fusión Z₃).
- Walker-Wang (2011) da la realización Hamiltoniana en lattice trivalente — exactamente la red SCG. Input a WW: UBFC; el bulk implementa Crane-Yetter.
- Crane-Yetter fue **motivada originalmente** por las variables de Ashtekar (Crane 1991).
- **Resultado conocido:** la frontera 3D de Crane-Yetter es Chern-Simons con nivel *k* (Walker-Wang 2011). Esto coincide con K-019/D-004: la teoría efectiva en 2+1D de defectos es CS.

**Estado epistémico:** 
- **Derivado parcialmente**: la equivalencia CY ↔ BF+Λ sobre triangulaciones es teorema (Baez 2000).
- **Ansatz estructural**: que la 𝒞 correcta para SCG sea la categoría modular con fusión Z₃ + braiding quiral de Ashtekar. Plausible (K-017) pero sin construcción explícita.

**Problemas conocidos:**
- CY es euclidiana. Versión Lorentziana es problemática (Barrett-Crane falló; EPRL-FK la resuelve parcialmente). P-11 se entrelaza con esto.
- Para *k* = 1 la TQFT es trivial (Z = 1). El régimen I tiene *k* pequeño pero no necesariamente 1.

### 2.2 Régimen II — Semiclásico: Plebanski autodual + Kodama

**Candidato principal:** acción de Plebanski autodual (Plebanski 1977; Krasnov 2009, 2011).

```
S_Plebanski[Σ, A, ψ] = ∫_M [ Σ^{AB} ∧ F_{AB}(A)           (1)
                           − (1/2) ψ_{ABCD} Σ^{AB} ∧ Σ^{CD}  (2)
                           − (Λ/6) Σ^{AB} ∧ Σ_{AB} ]           (3)
```

donde:
- *A* es la conexión autodual de Ashtekar, valor en *su(2)_C* (spinor izquierdo del grupo de Lorentz),
- Σ^{AB} = e^A_α ∧ e^B_β ε^{αβ...} es la 2-forma autodual construida del vierbein,
- *ψ_{ABCD}* es un tensor simétrico de Lagrange (impone la simplicidad Σ ∧ Σ ∝ ε).

El término (2) impone que Σ provenga de un vierbein real. Tras integrarlo queda la acción de Einstein-Hilbert-Palatini autodual.

El término (3) es la constante cosmológica. Via Stokes en una región con frontera, este término se reduce a **Chern-Simons autodual de nivel k = 2π/Λ**. Es decir, la frontera de la teoría de bulk es **exactamente** CS (coincide con K-019: la frontera del CY 4D es CS 3D).

**Por qué es candidato:**
- Usa la conexión autodual de Ashtekar — requerimiento de K-019 (SU(2)_L quiral).
- Reproduce GR (∴ reproduce D-002/D-003 en sus dominios).
- Contiene Λ, que acopla al nivel CS.
- La versión discretizada es precisamente la formulación state-sum asociada a CY.

**Estado epistémico:**
- **Derivación**: (2)+(3) → E-H+Λ autodual. Teorema (Plebanski 1977; Krasnov review 2009).
- **Ansatz estructural**: que *esta* sea la acción correcta en el régimen II. Es la elección mínima compatible con Ashtekar autodual, pero no derivada de primeros principios.

**Problemas conocidos (P-11 expandido):**
- Conexión compleja → condiciones de realidad (Σ^{AB} real, no A).
- Estado de Kodama Ψ_K = exp(i S_CS / ℏ) no normalizable en la medida natural (Witten 2003).
- Wick rotation al régimen euclidiano no es trivial.
- LQG mainstream abandonó esta formulación. Razón por la cual K-019 es premisa fuerte (P-11).

### 2.3 Régimen III — Fase SCG (BH interior): cuerda efectiva

**Candidato principal:** acción efectiva 2D de Nambu-Goto modificada, derivada del Lagrangiano discreto D-001 reinterpretado via K-004.

Recordemos D-001 (v1.1):
```
E = -G Σ_{i<j} m_i m_j / r_{ij}   (atracción)
    + k Σ (x_{i+1} − x_i)²          (tensión)
    + N ℏc Σ 1 / (x_{i+1} − x_i)    (degeneración cuántica, K-004)
```

En continuo, para una cuerda con 2D worldsheet parametrizada por X^μ(σ, τ) en un fondo g_{μν}:

```
S_SCG-cuerda = ∫ d²σ [ − μ √(−det h_{ab})          (Nambu-Goto)   (A)
                      + α' (∂X^μ)²                  (tensión)       (B)
                      + β / d²(σ,τ)                 (degeneración)  (C)
                      ]
```

con *h_{ab}* = ∂_a X^μ ∂_b X_μ g_{μν} inducida, *d(σ,τ)* el espaciamiento transversal efectivo, μ ~ M_P², β ~ N ℏc.

**Clave:** (C) no es un término estándar. Propuesta: *d(σ,τ)* es un escalar adicional que mide la separación promedio a cuerdas vecinas. En el bulk, puede promoverse a un campo escalar transversal φ con:

```
(C)' = N ℏc · ∫ d²σ √(h) e^{-φ}    donde  d = d_0 e^{φ/2}
```

Esto es análogo al dilatón en teoría de cuerdas. Con *φ* → ∞ (d → ∞) el término se anula; con *φ* → −∞ (d → 0) diverge.

**Por qué es candidato:**
- Reproduce D-001 en el límite discreto.
- Al variarse da las ecuaciones de equilibrio que en régimen BH seleccionan *d* ~ √(r_s ℓ_P) (K-007).
- Al acoplarse al fondo g_{μν} de Einstein, genera backreaction consistente (resolve P-5.1 potentially).

**Estado epistémico:**
- **Derivación parcial**: (A) es NG estándar; (B) recupera el límite tenso.
- **Ansatz**: (C) como función de *d*. La forma exacta no derivada de primeros principios — es la traducción continua del término discreto 1/d. La promoción a campo φ es analogía con dilatón, no derivación.

**Problemas:**
- Esta acción efectiva no es fundamental — es la descripción IR del sector BH. Debe *derivarse* de Plebanski+WW en el límite ρ → ρ_P, no postularse.
- No captura el *plegado* de D-003 directamente. El plegado emerge como solución clásica de la acción acoplada a GR, no como parte de la acción.

### 2.4 Régimen IV — IR: SM + GR semiclásica

**Candidato:** acción del Modelo Estándar + Einstein-Hilbert + Holst (Barbero-Immirzi real).

```
S_IR = S_EH + S_YM[A_U(1), A_SU(2), A_SU(3)] + S_Dirac + S_Higgs + S_Yukawa
```

Con:
- A_U(1) = campo de hipercarga (emerge de K-014: modos transversales).
- A_SU(2) = conexión electrodébil (emerge de K-019: proyección real de Ashtekar autodual).
- A_SU(3) = gluones (emerge de K-017: Z₃ + braiding).
- Fermiones: defectos topológicos puntuales (extremos de cuerdas abiertas o nudos elementales).
- Higgs: anyón condensado (K-021).

**Estado epistémico:**
- **Conocido**: la acción del SM es estándar; lo nuevo es que sus componentes emergen de los regímenes superiores.
- **Ansatz estructural**: que el flujo RG desde II a IV preserve SU(3)×SU(2)×U(1) con las representaciones correctas.

**Problema principal:** las *constantes* (g_1, g_2, g_3, v_Higgs, Yukawas) no se predicen. K-023 da solo α₂ ≈ α₃ ≈ γ/(4π) como patrón cualitativo.

---

## 3. Tensiones inter-regímenes

Cinco tensiones identificadas, ordenadas por severidad.

### T-1: k topológico vs k dinámico (severidad: alta)

**Problema.** El nivel CS *k* en Régimen I (Crane-Yetter) es entero y topológico. En Régimen II (Kodama), k = 2π/Λ. Con Λ_observed ≈ 10⁻¹²² M_P², esto daría k ~ 10¹²². Pero α^{-1} ≈ 2k / (algo) con α ~ 0.02 implica k ~ 300 (K-023). No cuadra.

**Interpretación tentativa.** El *k* medido en el régimen IV (α) no es el *k* topológico de CY. Los dos están relacionados por la renormalización de modos integrados entre II y IV. En CS 3D el nivel es técnicamente topológico y no fluye, *pero* el nivel *efectivo visto desde el bulk 4D* sí puede fluir porque la frontera tiene degrees-of-freedom bulk adjacentes que se integran.

**Honestidad.** Esto es una hipótesis de trabajo, no una derivación. Es compatible con K-024 (grupo gauge es topológico, acoplamiento es dinámico) pero necesita verificación.

**Equivale a:** Q-027 refinada.

### T-2: Conexión compleja y el problema de Kodama (severidad: alta — P-11)

**Problema.** La conexión autodual es compleja. Esto implica:
1. Estados Kodama no normalizables.
2. Wick rotation Lorentz↔Euclid no trivial.
3. LQG mainstream la descartó por Barbero-Immirzi real.

Pero K-019 requiere autodual para tener SU(2)_L quiral.

**Interpretación tentativa.** Dos rutas:
- (a) **Ruta Krasnov**: reformular Plebanski usando variables reales pero preservando quiralidad. Krasnov (2007-2011) tiene propuestas en esta línea.
- (b) **Ruta perturbativa**: aceptar Plebanski autodual solo como acción efectiva perturbativa alrededor de un fondo; no intentar cuantizarla no-perturbativamente.

**Honestidad.** No hay consenso en la literatura. P-11 sigue siendo premisa fuerte.

**Equivale a:** Q-031.

### T-3: Walker-Wang Hamiltoniano vs acción Lagrangiana (severidad: media)

**Problema.** Walker-Wang está definido como Hamiltoniano en lattice trivalente, no como acción. La conexión a Crane-Yetter es vía *path integral* state-sum, no vía un Lagrangiano local.

**Interpretación tentativa.** Para los fines de bosquejo, adoptamos la equivalencia CY ↔ WW (demostrada: Walker-Wang 2011) y la acción continua CY ↔ BF+Λ (Baez 2000). Entonces la acción candidata del Régimen I es BF+Λ, con WW como su discretización.

**Honestidad.** La equivalencia "bulk WW + frontera CS ↔ bulk CY + frontera CS" es teorema; la correspondencia con acciones continuas específicas de SCG requiere la elección de la UBFC correcta, que no está construida explícitamente.

### T-4: Matter emerge de la red, pero Plebanski la añade aparte (severidad: media)

**Problema.** En Plebanski estándar, el matter (fermiones, Higgs) se añade como término separado S_matter. En SCG, el matter ES defectos topológicos de la red (Walker-Wang). No son sectores independientes.

**Interpretación tentativa.** En el framework WW, los defectos puntuales/de-línea son excitaciones no-triviales del vacío del Hamiltoniano. En el Lagrangiano, esto correspondería a que el matter es *intrínseco* a la configuración de la conexión A — no un campo aparte. Esto es análogo al *skyrmion* como soliton del campo gauge.

**Consecuencia.** La acción madre no debería tener un S_matter separado — los fermiones del SM serían configuraciones topológicas no-triviales de A (o del vierbein Σ).

**Honestidad.** Esta imagen es la visión de Bilson-Thompson (2005) y Finkelstein. En SCG formal aún no está construida. Es programa, no teorema.

### T-5: Forma de E_info como término local (severidad: baja)

**Problema.** El término (C) de la acción de cuerda (2.3) depende de *d(σ,τ)*, el espaciamiento a cuerdas vecinas. Es no-local en el sentido de que requiere información de otras cuerdas.

**Interpretación tentativa.** Promover *d* a un campo transversal φ convierte (C) en local: β e^{−φ}/... con *φ* obedeciendo su propia ecuación. Alternativamente: reconocer que E_info es la energía cinética de modos cuánticos de la cuerda (K-004), lo cual es **exactamente** el término estándar de derivadas transversales en la acción de Polyakov:

```
S_Polyakov = (1/2) ∫ d²σ √(h) h^{ab} ∂_a X^μ ∂_b X_μ
```

En la cuantización, los modos transversales de *X* tienen energía ℏc/λ ~ ℏc/d — que es precisamente E_info por modo. **Por tanto E_info no es un término separado — ya está incluido en la acción de Polyakov, correctamente cuantizada.**

**Consecuencia.** El término (C) del sector III es espurio. La acción de cuerda correcta es Nambu-Goto/Polyakov estándar; *d* es emergente como longitud de onda característica de los modos.

**Honestidad.** Esta es una *simplificación* importante si es correcta. Haría que H-001 v1.1 sea compatible con la acción de cuerdas estándar — lo cual reabre la comparación con Horowitz-Polchinski. Volver a P-4.

**→ hallazgo candidato** (pendiente de verificación formal). Si se sostiene, es K-027.

---

## 4. Arquitectura candidata: acción madre

Síntesis tentativa de los regímenes en una sola acción.

### 4.1 Propuesta

```
S_madre = S_Plebanski-autodual[Σ, A, ψ] + S_cosmo[Σ, Λ] + S_defectos[configuraciones topológicas de A]
```

donde:

**(a) S_Plebanski-autodual:**
```
S_PA = ∫_M [ Σ^{AB} ∧ F_{AB}(A) − (1/2) ψ_{ABCD} Σ^{AB} ∧ Σ^{CD} ]
```
Da GR autodual (K-019). Este es el núcleo gravitacional y la fuente de SU(2)_L quiral.

**(b) S_cosmo:**
```
S_cosmo = -(Λ/6) ∫ Σ^{AB} ∧ Σ_{AB}
```
Acopla Λ y da, en la frontera, CS con nivel k ↦ 2π/Λ. Esta es la fuente del sector topológico de la red (U(1), Z₃, SU(3)).

**(c) S_defectos:**
No es un término aparte sino la suma sobre configuraciones no-triviales de A con topología no-trivial (nudos, enlaces). Integral sobre clases de homotopía:
```
Z[M] = Σ_{clases topológicas} ∫ DΣ DA Dψ exp(i S_PA + S_cosmo / ℏ)
```

### 4.2 Reducciones por régimen

- **Régimen I** (E ≫ M_P, región sin matter local): S_PA + S_cosmo → state-sum CY, con WW en lattice.
- **Régimen II** (gravedad semiclásica): integrar ψ → E-H-autodual + Λ.
- **Régimen III** (densidad Planckiana): las configuraciones de A que saturan la restricción de A-003 son las cuerdas SCG. La acción efectiva de cuerdas se obtiene por reducción dimensional (worldsheet 2D ⊂ 4D) de S_PA, análoga a la derivación de la acción de cuerda de Nambu-Goto desde un background.
- **Régimen IV** (IR): integrar modos UV. La fase confinante del SU(2)_L (K-021) emerge. El SM aparece con acoplamientos fijados por γ_Immirzi (K-023).

### 4.3 Estado epistémico de la arquitectura

| Componente | Nivel | Justificación |
|---|---|---|
| S_PA como forma de Plebanski | Conocido | Plebanski 1977 |
| S_cosmo como Λ autodual | Conocido | Krasnov review 2011 |
| S_defectos = sumar topologías | Ansatz | estándar en teoría gauge no-abeliana |
| Reducción I→II→III→IV | **Bosquejo** | cada paso requiere verificación |
| Constantes resultantes | Pendiente | requiere calcular flujo |

**No es una derivación. Es una arquitectura candidata.** Su mérito es que (a) es mínima — no añade más estructura que la requerida, (b) hereda todos los resultados ya obtenidos, (c) cada régimen tiene ya su formalismo desarrollado en la literatura; lo nuevo es la conexión.

---

## 5. Qué se puede calcular hoy (próximos pasos concretos)

Ordenados por viabilidad técnica inmediata.

**Estado del plan (actualizado sesión 20 — BOSQUEJO ESTRUCTURALMENTE COMPLETO, 3/5 confirmadas):**
- **5.1 ✅ COMPLETADA** (sesión 13) — D-006 (`logic/derivations/D-006_A-003_desde_polyakov.md`); K-027 promovido.
- **5.2 ✅ COMPLETADA** (sesión 16) — D-007 (`logic/derivations/D-007_ec_movimiento_plebanski.md`); K-029 añadido; Q-033 parcial.
- **5.3 ✅ PARCIAL** (sesión 17) — análisis crítico de literatura Kodama (`notes/Tarea_5.3_kodama_P-11.md`); K-030 candidato; P-11 rebajado de 🟡 alta a 🟡 media. Sin derivación propia.
- **5.4 ✅ CONFIRMADA ESTRUCTURALMENTE** (sesiones 18, 20) — D-008 + D-009. K-031 PROMOVIDO a confirmado (sesión 20). Reducción dimensional + derivación variacional de A2. K-007 recuperada por segunda vía. D-001/D-006/D-007 integrados bajo S_SCG-2D. Ciclo Régimen II→III cerrado con base sólida.
- **5.5 ✅ PARCIAL** (sesión 19) — análisis estructural del flujo RG II→IV (`notes/Tarea_5.5_flujo_RG.md`); K-032 candidato. Patrón α₂≈α₃≠α₁ derivado desde "gauge de vértice vs gauge de segmento". Coincidencia α_3(M_P)≈γ/(4π) al 1% como sugerente. Valor cuantitativo no derivado; matching explícito II→IV pendiente.

**Síntesis (post-sesión 20):** 3/5 con derivaciones cerradas/confirmadas estructuralmente (D-006, D-007, D-008+D-009) + 2/5 parciales con candidatos (K-030, K-032). Ruta A en progreso. Próximas piezas de promoción: K-030 (vía Q-039, Λ_UV) y K-032 (vía matching II→IV explícito).

### 5.1 Verificar reducción de NG con modos transversales cuantizados (T-5)

**Objetivo.** Mostrar que la energía cinética cuántica de los modos transversales de la cuerda (Polyakov) reproduce la presión de degeneración A-003 sin necesidad de un término (C) adicional.

**Método.** Cuantizar la cuerda abierta/cerrada en Polyakov con corte UV en λ ≥ ℓ_P; calcular ⟨T_{++}⟩ en vacío; verificar que da ~ N ℏc / d por modo.

**Si se sostiene:** K-027 y simplificación de 2.3. Un término menos que postular.

**Si falla:** el término (C) es real y no reducible a Polyakov — entonces A-003 es más que Heisenberg estándar.

**Esfuerzo estimado:** factible una sesión. Puramente analítico.

### 5.2 Escribir explícitamente S_PA + S_cosmo y derivar ecuaciones de movimiento

**Objetivo.** Variar S_madre respecto a Σ, A, ψ y obtener (a) Σ^{AB} = e^A∧e^B (de ψ), (b) F^{AB} = Λ Σ^{AB}/3 (de Σ), (c) d_A Σ = 0 (de A — torsion-free autodual).

**Método.** Cálculo variacional estándar. Resultado esperado: ecuaciones de Einstein con Λ + definición del vierbein.

**Mérito.** Confirma que el núcleo gravitacional es consistente. Necesario como punto de partida para añadir materia.

**Esfuerzo.** Una sesión.

### 5.3 Computar el estado semiclásico (análogo de Kodama) y ver si la patología es curable

**Objetivo.** Escribir Ψ_K = exp(i S_CS[A]/ℏ) y analizar por qué no es normalizable (Witten 2003). Ver si con la estructura SCG adicional (Σ simple, defectos) hay una versión normalizable.

**Método.** Literatura (Krasnov 2005+, Freidel; Witten 2003). Trabajo técnico de LQG.

**Mérito.** Ataca directamente P-11.

**Esfuerzo.** Probablemente 2-3 sesiones. Requiere lectura cuidadosa de literatura LQG.

### 5.4 Verificar que la reducción dimensional da la acción SCG de cuerda

**Objetivo.** Partir de S_PA en un fondo BH y mostrar que las soluciones con simetría axial + densidad saturada reducen a una acción 2D con el contenido de D-001.

**Método.** Ansatz con métrica de BH + Σ simple. Integrar sobre coordenadas transversales. Comparar con acción efectiva.

**Mérito.** Cerraría el ciclo Régimen II → Régimen III desde primeros principios.

**Esfuerzo.** 2-3 sesiones. Técnicamente complejo.

### 5.5 Derivar el flujo de acoplamientos desde II a IV

**Objetivo.** Integrar modos entre M_P y Λ_EW, verificar que el acoplamiento efectivo viene correcto y explicar α₂ ≈ α₃ (K-023) estructuralmente.

**Método.** RG estándar + matching entre regímenes. Novedad: el matching no es con una UV completion arbitraria sino con Plebanski-autodual + Λ.

**Mérito.** Primera predicción cuantitativa de constantes del SM desde SCG.

**Esfuerzo.** 3-5 sesiones. Requiere cálculos de loops.

---

## 6. Debilidades honestas del bosquejo

1. **No es una derivación** — es un mapa de territorio. Cada reducción entre regímenes es hipótesis.
2. **P-11 no resuelto.** La conexión autodual sigue siendo premisa fuerte.
3. **T-1 (k topológico vs k dinámico)** no tiene resolución clara. La idea de que el nivel efectivo fluye es compatible pero no derivada.
4. **T-4 (matter de la red)** es programa a la Bilson-Thompson, no teorema.
5. **Ninguna constante numérica se predice todavía.** La arquitectura no resuelve eso, sólo lo organiza.
6. **La relación con EPRL-FK (modelos spinfoam Lorentzianos)** no se ha explorado. EPRL-FK es la ruta mainstream para Plebanski; SCG podría ser un caso especial con UBFC específica.

### Lo que el bosquejo sí hace
1. Identifica candidatos concretos con literatura respaldante en cada régimen.
2. Marca explícitamente tensiones — cinco identificadas, una (T-5) con resolución candidata.
3. Da un plan de 5 cálculos concretos, ordenados por viabilidad.
4. Hace honor al principio K-005: no añade estructura nueva más allá de lo que los marcos existentes ya tienen; solo los conecta.

---

## 7. Síntesis

**La Lagrangiana "madre" candidata** es Plebanski autodual + término cosmológico (= BF+Λ autodual) con los defectos del SM emergiendo como configuraciones topológicas no-triviales de la conexión.

**Esto NO es una derivación** — es la elección mínima compatible con los resultados ya obtenidos (K-019, K-024, K-026, Walker-Wang/CY) y con la literatura de gravedad cuántica (Plebanski, Krasnov, Baez, Freidel).

**Cinco tensiones** identificadas, una (T-5) con posible resolución que eliminaría el término E_info separado y simplificaría la sección SCG. Verificación pendiente.

**Cinco cálculos concretos propuestos** para sesiones futuras; la tarea 5.1 (T-5) es la más inmediata y menos ambiciosa.

**El bosquejo NO resuelve P-8.** Lo estructura. Resolver P-8 completamente requerirá al menos completar los cálculos 5.1–5.5.

---

## 8. Nuevas preguntas abiertas

- **Q-032:** ¿La presión de degeneración A-003 es reducible a energía cinética cuántica de modos transversales de la cuerda en Polyakov? (T-5; → tarea 5.1)
- **Q-033:** ¿La frontera del bulk 4D Plebanski-autodual es exactamente CS con nivel k = 2π/Λ, incluyendo corrections por ψ?
- **Q-034:** ¿El flujo RG entre Régimen II y Régimen IV preserva k como topológico o lo modifica efectivamente? (T-1)
- **Q-035:** ¿Los defectos topológicos de A en SCG (solitones del conexión) reproducen el contenido fermiónico del SM? (T-4, programa Bilson-Thompson)

---

## 9. Nuevo insight candidato

**K-027 (candidato):** Si T-5 se verifica, la "presión de degeneración gravitacional" A-003 no es un término adicional de la Lagrangiana — es la manifestación de los modos cuánticos transversales de la cuerda de Polyakov con corte UV en ℓ_P.

**Nivel:** conjeturado (pendiente de cálculo 5.1).

**Si se confirma:** simplificaría H-001 (un término menos) y reabriría la comparación cuantitativa con teoría de cuerdas estándar (Horowitz-Polchinski, P-4).

---

## 10. Referencias clave

- Plebanski, J. (1977). "On the separation of Einstein substructures." J. Math. Phys. 18, 2511.
- Crane, L. & Yetter, D. (1993). "A categorical construction of 4D topological quantum field theories."
- Baez, J. (2000). "An introduction to spin foam models of BF theory and quantum gravity." Lect. Notes Phys. 543, 25–93.
- Walker, K. & Wang, Z. (2011). "(3+1)-TQFTs and topological insulators." Front. Phys. 7, 150.
- Krasnov, K. (2009-2011). Review articles on Plebanski formulation and alternatives.
- Witten, E. (2003). "A note on the Chern-Simons and Kodama wavefunctions." hep-th/0306083.
- Alexander, Marciano, Smolin (2014). "Gravitational origin of the weak interaction's chirality." PRD 89, 065017.
- Freidel, L. & Livine, E. (2006). "Effective 3d quantum gravity and non-commutative QFT."
- Bilson-Thompson, S. (2005). "A topological model of composite preons." hep-ph/0503213.

---

**Archivo asociado:** este documento complementa la cadena H-001/H-002/H-003. La Lagrangiana propuesta no es parte de una hipótesis — es el andamiaje dinámico que toda la teoría necesita.
