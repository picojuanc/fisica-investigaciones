# Hallazgos clave

Insights genuinos que la investigación ha producido. No especulaciones — cosas que ya pasaron un filtro lógico. Cada entrada debe poder justificarse.

Formato:
```
## K-XXX — Título
- **Fecha:** YYYY-MM-DD
- **Derivado de:** [H-XXX, E-XXX, ...]
- **Enunciado:**
- **Por qué importa:**
```

---

## K-001 — Área geométrica ≠ grados de libertad físicos
- **Fecha:** 2026-04-15
- **Derivado de:** E-001, E-003.
- **Enunciado:** en una teoría gravitacional consistente, no toda superficie con área grande aloja información proporcional a su área. El principio holográfico impone que la **información física** está acotada por la frontera *físicamente alcanzable*, no por el área matemática de cualquier superficie imaginable. Corolario: intentar maximizar área geométrica (p. ej., horizontes fractales, tipo trompeta) no produce memoria infinita.
- **Por qué importa:** este insight cierra una vía ingenua y redirige la pregunta "¿cómo aumentar capacidad de información?" hacia "¿cómo generar más grados de libertad físicos?" — un cambio de marco importante.

## K-002 — La naturaleza prefiere minimizar energía total, no maximizar área
- **Fecha:** 2026-04-15
- **Derivado de:** E-002, E-003.
- **Enunciado:** a masa fija, un BH rotante tiene **menos** área que uno estático. A masa fija, un BH alargado (black string) es inestable y prefiere fragmentarse. La segunda ley de BH (ΔA ≥ 0) se cumple *cuando se añade masa/energía o se extrae momento angular*, no como un principio universal de maximización geométrica.
- **Por qué importa:** identifica qué es realmente el principio variacional relevante en gravedad — la entropía (bajo restricciones), no el área.

## K-003 — El modelo toy SCG exhibe la transición de fase cualitativa esperada
- **Fecha:** 2026-04-15
- **Derivado de:** D-001, sim001_cuerda_basica.js.
- **Enunciado:** en el modelo discreto de H-001, hay evidencia numérica de dos regímenes:
  - λ > G: configuración estable tipo cuerda (energía finita).
  - λ < G: colapso catastrófico (energía diverge).
  La frontera λ ≈ G marca una transición.
- **Por qué importa:** es la primera "evidencia" (en sentido débil) de que la competencia entre gravedad e "información" puede producir fases distintas. No prueba H-001; sí la hace no trivial.
- **Caveat:** el modelo no conserva energía ni tiene contenido físico derivado. Tratar con reserva.

## K-004 — La "presión de información" es presión cinética cuántica convencional
- **Fecha:** 2026-04-16
- **Derivado de:** análisis de P-1 (`notes/P-1_analisis.md`), E-005.
- **Enunciado:** el término repulsivo que estabiliza la cuerda en H-001 (inicialmente llamado "presión de entrelazamiento" o "presión de información") es identificable con la **presión cinética cuántica de modos confinados a escala Planck** — Heisenberg + relativista, nada exótico. La forma E ≈ ℏc/d por modo emerge directamente del principio de incertidumbre aplicado a modos sin masa.
- **Por qué importa:** elimina un postulado ad hoc. H-001 deja de requerir "nuevas entidades informacionales" y pasa a ser QM + GR en régimen Planckiano. Más modesto, más falsable.
- **Consecuencia:** A-003 reformulado como "presión de degeneración de grados de libertad gravitacionales", análoga a las presiones que estabilizan enanas blancas y estrellas de neutrones.
- **Implicación fuerte:** existe potencialmente un "cuarto nivel" de objeto estabilizado por presión de degeneración, operando a escala Planck, análogo cuantitativo de M_Chandrasekhar pero para grados de libertad gravitacionales.

## K-011 — D_espacio = 3 se deriva de p = 1 (cuerdas) + codimensión 2 (nudos)
- **Fecha:** 2026-04-16 (sesión 7)
- **Derivado de:** H-002 y E-007.
- **Enunciado:** si los objetos fundamentales son 1D (cuerdas SCG, por H-001) y el espacio macroscópico estable requiere que dichos objetos tengan topología no trivial (nudos y enlaces), entonces D = p + 2 = 3 es la **única** dimensionalidad espacial viable.
  - En D = 2: cuerdas dividen el espacio → fragmentación.
  - En D ≥ 4: todos los nudos se desatan → sin información topológica persistente → inestabilidad.
  - Solo en D = 3: nudos existen y persisten → estabilidad y codificación de información topológica.
- **Por qué importa:** conecta H-001 (por qué 1D) con el dato empírico más básico del universo (3 dimensiones espaciales). Si se sostiene, las tres dimensiones dejan de ser un parámetro libre y pasan a ser una consecuencia de la dimensionalidad Planckiana de los objetos fundamentales.
- **Advertencia:** el principio topológico (codimensión 2 para nudos) es un hecho matemático. Lo que falta es un **mecanismo físico** que vincule "topología de nudos" con "estabilidad del espacio". Sin ese mecanismo, H-002 es sugerente pero no demostrativa.

## K-010 — H-001 v1.1 predice un retraso de ecos GW la MITAD que modelos Planck-scale
- **Fecha:** 2026-04-16 (sesión 6)
- **Derivado de:** E-006, `notes/F_analisis_ringdown.md`.
- **Enunciado:** el tiempo de retraso entre ecos de ondas gravitacionales tras una fusión BH-BH, modelado como Δt ≈ 2(r_s/c)·ln(r_s/δ), da:
  - fuzzballs / stretched horizon (δ ~ ℓ_P): **Δt ≈ 2(r_s/c)·ln(r_s/ℓ_P)**
  - H-001 v1.1 (δ ~ √(r_s·ℓ_P)): **Δt ≈ (r_s/c)·ln(r_s/ℓ_P)**
  El factor ½ viene directamente del hecho de que √(r_s/ℓ_P) es la mitad de ln(r_s/ℓ_P) en el interior del logaritmo.
- **Por qué importa:** es la **primera predicción cuantitativa falsable** de H-001 v1.1 contra sus competidoras. Para un BH de 30 M_☉ la diferencia son ~26 ms. Resoluble con LIGO actual estadísticamente y con detectores 3G fusión a fusión.
- **Caveat:** la existencia misma de ecos GW es aún controvertida. Si no existen, H-001 v1.1 y fuzzballs serían indistinguibles por esta vía.
- **Consecuencia:** H-001 v1.1 deja de ser "teoría atractiva" y entra al territorio de "teoría falsable" en principio. Este es un hito metodológico.

## K-009 — H-001 v1.1 NO es equivalente a fuzzballs ni a stretched horizon
- **Fecha:** 2026-04-16 (sesión 5)
- **Derivado de:** comparación sistemática con literatura (`literature/comparacion_SCG_vs_marcos_existentes.md`).
- **Enunciado:** en la revisión de cuatro marcos que abordan preguntas similares (fuzzballs de Mathur, correspondencia Horowitz-Polchinski, stretched horizon de Susskind, stringy forces 2024), H-001 v1.1 predice una **escala interior distinta** y una **ubicación distinta** de la información:
  - H-001: cuerda plegada LLENANDO el volumen, escala d ~ √(r_s·ℓ_P).
  - Fuzzballs: capa fuzzy ~ℓ_P cerca del horizonte, interior "cap off".
  - Stretched horizon: membrana a ℓ_P, superficie pura.
  - Stringy forces: escala (r_s·α')^(1/3), profunda pero localizada.
- **Por qué importa:** confirma que H-001 v1.1 **tiene originalidad genuina**. No es una reformulación de imágenes existentes. Sus predicciones cuantitativas (d ~ √(r_s·ℓ_P) volumétrico) difieren en órdenes de magnitud de los otros marcos.
- **Ventajas de H-001 v1.1 como alternativa:** ontología más económica (solo QM + GR + holografía en 4D, sin SUSY ni compactificaciones).
- **Caveat:** esto no implica que H-001 sea correcta; solo que es **distinta y potencialmente falsable**. La comparación observacional real (LIGO/Virgo ringdown, firmas en Hawking) queda pendiente.

## K-007 — La escala interior de los BHs es la media geométrica horizonte–Planck
- **Fecha:** 2026-04-16
- **Derivado de:** D-003 (`logic/derivations/D-003_conservacion_entropia.md`).
- **Enunciado:** bajo H-001 v1.1, el interior de un BH macroscópico es una cuerda SCG plegada con escala transversal:
  ```
  d ~ √(r_s · ℓ_P)
  ```
  que es la media geométrica entre el radio de Schwarzschild y la longitud de Planck. Para un BH estelar, d ~ 1 fm (escala nuclear). Para el BH supermasivo Sgr A*, d ~ 10⁻¹³ m (sub-atómica pero mayor que Planck).
- **Por qué importa:** es una **predicción cuantitativa** específica y no-trivial. Ningún modelo clásico de BH produce esta escala. Si H-001 v1.1 es correcta, cualquier sonda interior (si la hubiera) encontraría estructura a ~fm.
- **Consecuencia:** la configuración plegada satura exactamente la cota holográfica: S_cuerda = S_BH. No viola; iguala.
- **Conexión:** similar en espíritu a los "fuzzballs" de Mathur, pero llegado desde 4D sin usar supersymmetría ni compactificaciones.

## K-008 — La cuerda plegada sugiere resolución de la paradoja de información
- **Fecha:** 2026-04-16
- **Derivado de:** D-003, razonamiento asociado.
- **Enunciado:** los estados de vibración de la cuerda plegada interior pueden codificar la información de la materia caída. La radiación de Hawking emitida desde el horizonte puede correlacionarse con estos estados vía el propio horizonte. Esto permite que la evaporación sea **unitaria** (preserva información), resolviendo la paradoja.
- **Por qué importa:** si verificable, es una predicción con firma observable — correlaciones no térmicas en la radiación de Hawking de BHs pequeños.
- **Caveat:** el mecanismo microscópico de transferencia de información está por modelar. Sólo es una imagen consistente.

## K-006 — D=1 es la única dimensionalidad donde la gravedad y la presión de degeneración Planckiana se balancean ∀ N
- **Fecha:** 2026-04-16
- **Derivado de:** D-002 (`logic/derivations/D-002_dimensionalidad_critica.md`) y su análisis en `notes/P-5_analisis.md`.
- **Enunciado:** para modos relativistas de masa M_P distribuidos en un objeto D-dimensional de tamaño L:
  - E_deg escala como N^(1+1/D) / L,
  - E_grav escala como N² / L.
  El balance marginal se da cuando los dos exponentes de N coinciden, lo cual ocurre solo en D=1. En D≥2 la gravedad vence para cualquier N > 1.
- **Por qué importa:** la dimensionalidad 1 de la cuerda **no es un postulado**, es una consecuencia forzada del régimen Planckiano. Es análogo al papel de Chandrasekhar en astrofísica, pero con modos de masa Planck en lugar de electrones.
- **Corolario elegante:** la cuerda SCG es "la enana blanca del vacío gravitacional".
- **Limitación:** D=1 queda marginal (A=0); para fijar L* finito hace falta un término subdominante. Nuevo sub-problema P-5.1.

## K-005 — La lección meta: la buena teoría es más modesta, no más exótica
- **Fecha:** 2026-04-16
- **Derivado de:** reflexión sobre la transición v1.0 → v1.1 de H-001.
- **Enunciado:** la reformulación redujo la hipótesis de "postular un principio nuevo (presión de información)" a "aplicar principios viejos (Heisenberg + GR) a un régimen nuevo (Planck)". La versión buena de la teoría es la menos ambiciosa metafísicamente y la más concreta numéricamente.
- **Por qué importa:** criterio operativo para la investigación — **antes de postular algo nuevo, pregunta si lo viejo ya lo hace**. Solo se introducen entidades nuevas si las viejas fallan explícitamente.
- **Corolario:** aplicar este criterio a los próximos problemas (P-5: por qué 1D; P-7: conservación entrópica) antes de postular más axiomas.

## K-012 — La cadena SCG → Levin-Wen → Chern-Simons → partículas topológicas es lógicamente viable
- **Fecha:** 2026-04-17 (sesión 8)
- **Derivado de:** E-008, análisis de Q-023.
- **Enunciado:** existe una cadena de 6 eslabones desde la red SCG hasta partículas con cargas cuantizadas: (1) objetos 1D (H-001/D-002), (2) D=3 (H-002), (3) nudos estables (teorema), (4) string-net → gauge + fermiones (Levin-Wen, demostrado), (5) teoría efectiva Chern-Simons (Witten, demostrado), (6) reglas de fusión → grupo gauge concreto (desconocido). Los eslabones 1-5 son sólidos. El eslabón 6 es la brecha.
- **Por qué importa:** por primera vez, la investigación tiene una **ruta concreta hacia el Modelo Estándar** que no requiere postulados nuevos — solo un cálculo: derivar las reglas de fusión de las cuerdas SCG. Si las reglas producen SU(3)×SU(2)×U(1), la teoría pasa de "sector gravitacional" a candidata ToE.
- **Caveat:** la brecha (eslabón 6) es enorme. "Existe una ruta" no es lo mismo que "la ruta llega a destino."

## K-014 — U(1) gauge emerge del momento angular transversal de cuerdas SCG
- **Fecha:** 2026-04-17 (sesión 8)
- **Derivado de:** D-004, Parte I.
- **Enunciado:** una cuerda 1D en D=3 tiene 2 modos transversales con simetría SO(2) ≅ U(1). El momento angular m ∈ ℤ es una carga interna conservada. En un vértice trivalente, m₁+m₂+m₃=0 define una regla de fusión aditiva. Por el mecanismo de Levin-Wen/Wen, esto produce un **campo gauge U(1) emergente con un fotón sin masa**.
- **Por qué importa:** es la primera derivación de un campo gauge del Modelo Estándar desde el marco SCG. Usa solo geometría (D=3 → 2 transversales) + QM (conservación de momento angular) + Levin-Wen (demostrado).

## K-015 — La cuantización de carga en 1/3 emerge de la trivalencia de vértices en D=3
- **Fecha:** 2026-04-17 (sesión 8)
- **Derivado de:** D-004, Parte II.
- **Enunciado:** en un vértice trivalente equiespaciado, los 3 segmentos rompen la simetría transversal SO(2) a Z₃ (simetría cíclica de 120°). El momento angular se clasifica modulo 3: m ≡ 0, 1, 2 (mod 3). Esto produce cargas cuantizadas en unidades de 1/3. Z₃ es además el centro de SU(3), y la clasificación por trialidad corresponde exactamente a la distinción leptones (trialidad 0) vs quarks (trialidad 1, 2).
- **Por qué importa:** la cuantización de la carga en 1/3 **no tiene explicación** dentro del Modelo Estándar — es un postulado. Que se derive de la geometría en D=3 es un resultado explicativo genuino. La cadena causal es: D=3 → vértices trivalentes → Z₃ → cargas en 1/3.

## K-016 — Dos de tres factores del grupo gauge del SM emergen de la geometría SCG
- **Fecha:** 2026-04-17 (sesión 8)
- **Derivado de:** D-004 completo.
- **Enunciado:** U(1) se deriva (modos transversales), SU(2) se motiva fuertemente (conexión gravitacional de Ashtekar), y Z₃ = centro de SU(3) se deriva (trivalencia). El grupo parcial U(1) × SU(2) × Z₃ reproduce la estructura gauge electrodébil completa más la estructura discreta del color. Lo que falta es elevar Z₃ → SU(3) completo.
- **Por qué importa:** por primera vez, la mayoría del grupo gauge del SM tiene un origen geométrico unificado: segmentos → U(1), vértices → Z₃, conexión → SU(2). Cada factor viene de un aspecto distinto de la misma red.

## K-017 — Z₃ + quiralidad gravitacional = SU(3)₁ por unicidad matemática
- **Fecha:** 2026-04-17 (sesión 8)
- **Derivado de:** Q-026, clasificación de órdenes topológicos abelianos.
- **Enunciado:** solo existen 2 órdenes topológicos quirales con fusión Z₃ (SU(3)₁ y su conjugado temporal). La quiralidad de la red SCG (del CS gravitacional/Ashtekar) selecciona SU(3)₁ unívocamente. Esto completa el grupo gauge: Z₃ (de D-004) no es "solo Z₃" — es SU(3) a nivel k=1.
- **Por qué importa:** cierra Q-026. El grupo gauge completo SU(3)×SU(2)×U(1) emerge de la geometría de la red SCG. SU(3) viene de trivalencia + quiralidad, SU(2) de la conexión gravitacional, U(1) de los modos transversales.

## K-018 — El confinamiento de color tiene origen geométrico UV
- **Fecha:** 2026-04-17 (sesión 8)
- **Derivado de:** Q-026, conexión con QCD de retículo.
- **Enunciado:** en QCD de retículo, el confinamiento equivale a la preservación de la simetría Z₃ del centro de SU(3) (parámetro de orden: lazo de Polyakov ⟨L⟩=0). En el marco SCG, esta Z₃ tiene un origen geométrico UV: la trivalencia del vértice en D=3. El confinamiento no es un misterio dinámico — es la manifestación IR de la geometría UV del espacio-tiempo.
- **Por qué importa:** da una explicación conceptual del confinamiento: los quarks (trialidad ≠ 0) no pueden existir aislados porque la geometría del vértice impone m₁+m₂+m₃ ≡ 0 (mod 3). Solo estados con trialidad total 0 se propagan libremente.

## K-020 — Las 3 generaciones podrían venir de Z₃_primal × Z₃_dual (trivalencia vista desde ambos lados)
- **Fecha:** 2026-04-18 (sesión 9)
- **Derivado de:** E-009 Parte A.
- **Enunciado:** la red SCG trivalente tiene dos Z₃ independientes: una del vértice primal (3 aristas → color/trialidad) y otra de la cara triangular del grafo dual (3 vértices del triángulo → generación). Las 3 generaciones serían los 3 modos rotacionales de la cara dual. Esto explica N_gen = N_color = 3: ambos vienen de la trivalencia (D=3).
- **Por qué importa:** si correcto, resuelve uno de los misterios más viejos del SM (por qué 3 familias) desde la misma fuente geométrica que ya explica los colores.
- **Caveat:** MUY especulativo. La conexión entre la cara del dual y los modos de generación necesita formalización. Las masas de generación no se predicen cuantitativamente.

## K-021 — El mecanismo de Higgs es condensación de anyones = confinamiento de la gravedad SU(2)_L
- **Fecha:** 2026-04-18 (sesión 9)
- **Derivado de:** E-009 Parte B, Bais-Slingerland (2009), Fradkin-Shenker (1979).
- **Enunciado:** en el marco Levin-Wen, la ruptura de simetría gauge es condensación de anyones (Bais-Slingerland, demostrado). Aplicado a SCG: un anyón (j=½, Y=1) condensa a E ~ 246 GeV, rompiendo SU(2)_L × U(1)_Y → U(1)_EM. Por Fradkin-Shenker, esta "ruptura" es indistinguible del confinamiento de SU(2). La fuerza débil es la gravedad SU(2)_L confinada.
- **Por qué importa:** el mecanismo de Higgs deja de ser un postulado ad hoc (un campo escalar que "se le ocurre" condensar) y se convierte en un fenómeno de fase de la red SCG (confinamiento gravitacional), con precedente demostrado en materia condensada.
- **Caveat:** el valor v = 246 GeV no se predice. Las masas de W/Z y los Yukawa no se derivan.

## K-019 — La conexión autodual de Ashtekar ES su(2)_L — la quiralidad de la fuerza débil es gravitacional
- **Fecha:** 2026-04-18 (sesión 9, stress-test de D-004)
- **Derivado de:** stress-test Test 2, literatura Alexander-Marciano-Smolin (2012, PRD).
- **Enunciado:** la conexión de Ashtekar original (1986) es la parte autodual de la álgebra de Lorentz: so(3,1)_C ≅ su(2)_L × su(2)_R, y A = su(2)_L. Los fermiones levógiros se acoplan a la conexión autodual, los dextrógiros a la anti-autodual (teoría de representaciones del grupo de Lorentz). Esto fue propuesto como origen de la quiralidad de la fuerza débil por Alexander, Marciano y Smolin (PRD 89, 065017, 2014).
- **Por qué importa:** la identificación SU(2)_gravedad = SU(2)_L no es una analogía — es una identidad matemática. La violación de paridad de la fuerza débil se explica porque la conexión gravitacional que elegimos (autodual) ES inherentemente quiral. Esto fortalece enormemente el eslabón SU(2) de D-004.
- **Consecuencia:** el marco SCG DEBE usar la formulación autodual (compleja) de Ashtekar. La formulación de Barbero-Immirzi (real, usada en LQG estándar) pierde la quiralidad.
- **Problemas que abre:** conexión compleja → dificultades técnicas en LQG. Separación de constantes G vs g_W bajo RG no derivada.

## K-013 — La violación de paridad puede ser una consecuencia topológica, no un postulado
- **Fecha:** 2026-04-17 (sesión 8)
- **Derivado de:** E-008, conexión Chern-Simons + quiralidad de nudos.
- **Enunciado:** la acción de Chern-Simons cambia de signo bajo paridad (S_CS → -S_CS). Si la descripción efectiva de la red SCG es Chern-Simons, la teoría viola paridad automáticamente. Los nudos quirales (como el trefoil L vs R) se distinguen por sus invariantes. Esto reproduce cualitativamente la asimetría quiral del Modelo Estándar sin postularla.
- **Por qué importa:** la violación de paridad en la fuerza débil es uno de los hechos más misteriosos de la física de partículas. Que emerja como consecuencia topológica (y no como un postulado ad hoc) sería un logro explicativo significativo.
- **Caveat:** "cualitativamente" no es "cuantitativamente". La violación MÁXIMA de paridad (solo fermiones L interactúan débilmente) requiere más que la asimetría de CS; requiere un mecanismo de selección específico.

## K-022 — D_espacio + D_tiempo = 4 es la única dimensionalidad total con factorización quiral → D_tiempo = 1
- **Fecha:** 2026-04-19 (sesión 10)
- **Derivado de:** D-005, K-019, H-002, clasificación de Dynkin.
- **Enunciado:** la dimensionalidad total del espacio-tiempo p + q = 4 es la ÚNICA donde el álgebra de Lorentz so(p,q) complexificada se factoriza como producto de dos álgebras simples (Dynkin: D₂ = A₁ + A₁). Para todo n ≥ 5, so(n,C) es simple. Esta factorización es necesaria para la descomposición autodual/anti-autodual que da la quiralidad (K-019) y SU(2)_L (D-004). Con D_espacio = 3 (H-002): D_tiempo = 4 − 3 = 1. Además, la signatura (3,1) es la única donde los espinores de Weyl L y R están ligados por conjugación compleja (en (4,0) son equivalentes; en (2,2) son reales e independientes).
- **Por qué importa:** la dimensionalidad COMPLETA del espacio-tiempo (3+1) se explica desde el interior de la teoría. La cadena es: A-003 → D-002 (D_objeto = 1) → H-002 (D_espacio = 3) → D-005 (D_tiempo = 1). Todo desde QM + GR.
- **Cuatro argumentos convergentes:** (A) factorización de Dynkin, (B) signatura del Hodge star, (C) selección de signatura por espinores, (D) evolución de la red SCG.
- **Nivel de confianza:** FUERTEMENTE MOTIVADO (limitado por la dependencia de K-019).

## K-023 — α₂(M_P) ≈ α₃(M_P) ≈ 0.02 ≈ γ_Immirzi/(4π): los acoplamientos gauge a escala Planck reflejan la geometría de la red
- **Fecha:** 2026-04-19 (sesión 10)
- **Derivado de:** análisis del RG running del SM + marco SCG.
- **Enunciado:** el running a 1 loop del SM da α₂(M_P) ≈ 0.020, α₃(M_P) ≈ 0.019, α₁(M_P) ≈ 0.030. La near-convergencia α₂ ≈ α₃ es consistente con su origen geométrico común en el marco SCG, mientras que α₁ ≠ α₂ refleja el origen diferente de U(1) (modos transversales, no gravedad). Adicionalmente, α₃(M_P) ≈ γ_Immirzi/(4π) = 0.0189 al 1%, sugiriendo que el acoplamiento gauge está fijado por el parámetro de Immirzi.
- **Por qué importa:** es la primera confrontación cuantitativa del marco SCG con datos numéricos del SM. El patrón cualitativo (α₂ ≈ α₃ ≠ α₁) se confirma. La coincidencia con γ/(4π) abre una ruta hacia predicciones cuantitativas.
- **Problema asociado (P-9):** la asunción k=1 de D-004/Q-026 parecía inconsistente con α ≈ 0.02 (k~300). **RESUELTO:** grupo gauge (topología) y nivel CS (dinámica) son independientes. Ver K-024.
- **Nivel:** OBSERVACIÓN NUMÉRICA (no derivada).

## K-024 — El grupo gauge y el nivel CS son datos independientes: SU(3) es topológico, k es dinámico
- **Fecha:** 2026-04-19 (sesión 10)
- **Derivado de:** análisis de P-9, reformulación de Q-026.
- **Enunciado:** el grupo gauge SU(3) queda fijado por la categoría de fusión del vértice trivalente (Z₃ + matching dimensional: valencia 3 → representación fundamental de dim 3 → SU(3)). El nivel CS k es fijado por la dinámica (acoplamiento, α ≈ 2π/k). Son datos independientes. En la fase pre-geométrica (E >> M_P, k≈1), el argumento de unicidad de Q-026 aplica como caso especial. En la fase semiclásica (E ~ M_P, k~300), el grupo gauge se preserva y el acoplamiento se debilita. La transición es suave (level-shifting). El grupo gauge nunca cambia bajo RG — solo el espectro de representaciones accesibles.
- **Por qué importa:** resuelve P-9. La consistencia con α~0.02 a M_P ya no requiere abandonar SU(3). Además, introduce la imagen de tres regímenes (topológico, semiclásico, perturbativo) que da estructura a toda la cadena SCG.
- **Nuevo argumento para SU(3) (matching dimensional):** la valencia del vértice (3) coincide con la dimensión de la representación fundamental de SU(3) (3). Para SU(6) haría falta valencia 6, para E₆ estructura más compleja. Argumento independiente de k.

## K-026 — El patrón quiral del SM coincide exactamente con el patrón de origen dual (gravedad vs red) en SCG
- **Fecha:** 2026-04-19 (sesión 11, análisis Walker-Wang)
- **Derivado de:** D-004, K-019, Wen (2003 PRD 68 065003), Nielsen-Ninomiya.
- **Enunciado:** en el SM, SU(2)_L es el único factor quiral (solo fermiones L se acoplan); SU(3) y U(1)_Y son no-quirales (ambas helicidades se acoplan). En el marco SCG, SU(2)_L es el único factor que viene de la gravedad (conexión autodual de Ashtekar, inherentemente quiral por la estructura del grupo de Lorentz); SU(3) y U(1)_Y emergen de la red (trivalencia y modos transversales, inherentemente no-quirales por Nielsen-Ninomiya). La correspondencia es exacta: origen gravitacional → quiral; origen de red → no-quiral. Wen (2003) demostró constructivamente que una red de espín en 3+1D produce U(1)×SU(2)×SU(3) no-quiralmente. El factor quiral (SU(2)_L) requiere un mecanismo externo a la red — que en SCG es exactamente la gravedad.
- **Por qué importa:** explica un hecho del SM que no tiene explicación interna: ¿por qué solo SU(2) viola paridad? Respuesta SCG: porque es el único factor gauge que ES gravedad. Los otros dos son emergentes de la geometría de la red, y las redes producen gauge no-quiral por Nielsen-Ninomiya. Es un resultado explicativo genuino y no circular.

## K-025 — La cadena dimensional (D_object, D_espacio, D_tiempo) es un punto fijo auto-consistente, no una cascada de derivaciones
- **Fecha:** 2026-04-19 (sesión 11, stress-test cadena completa)
- **Derivado de:** stress-test de D-002, H-002, D-005.
- **Enunciado:** D-002 asume D_ambient=3 (gravedad Newtoniana) para derivar D_object=1. H-002 usa D_object=1 para derivar D_ambient=3. D-005 usa Ashtekar (definido en 3+1D) para derivar D_tiempo=1. La terna (1, 3, 1) es una solución auto-consistente de un sistema de restricciones mutuas — un punto fijo, no una cadena causal lineal. El análisis dimensional extendido a D_ambient arbitrario muestra que es el ÚNICO punto fijo (única solución con balance marginal tanto en N como en L).
- **Por qué importa:** cambia la presentación de la cadena dimensional de "tres derivaciones en cascada" a "una condición de auto-consistencia con solución única." Esto es análogo a D=26 en cuerdas bosónicas o D=10 en supercuerdas: condiciones de consistencia, no derivaciones desde algo más primitivo. La cadena es robusta (punto fijo único) pero la calibración epistémica debe reflejarlo.

## K-032 (CANDIDATO, PENDIENTE DE CUANTIFICACIÓN) — El patrón α₂≈α₃≠α₁ a M_P emerge estructuralmente por "gauge de vértice vs gauge de segmento" en la red WW; α_gauge ≈ γ/(4π) al 1%

- **Fecha:** 2026-04-21 (sesión 19)
- **Estado:** candidato. Patrón cualitativo derivable; valor numérico aún por derivación desde primeros principios.
- **Derivado de:** Tarea 5.5 del bosquejo (`notes/Tarea_5.5_flujo_RG.md`).
- **Enunciado:** el patrón α₂(M_P) ≈ α₃(M_P) ≈ 0.02, α₁(M_P) ≈ 0.03 observado (K-023) se explica en el marco SCG por una estructura "vértice vs segmento" de la red Walker-Wang 3+1D:
  - **SU(2)_L y SU(3):** ambos viven en **vértices trivalentes**. SU(2)_L proviene de la proyección de la conexión autodual sobre el vértice (K-019); SU(3) de la trivalencia Z₃ + quiralidad (K-017). Comparten "acoplamiento de vértice" → α_2 ≈ α_3.
  - **U(1)_Y:** vive en **segmentos** de la red, como modos transversales (K-014). Acoplamiento distinto → α_1 ≠ α_2, α_3.
  - **Coincidencia numérica sugerente:** α_3(M_P) ≈ γ_Immirzi/(4π) = 0.01890 al 1%. Identifica el parámetro de Immirzi como el acoplamiento gauge de vértice a escala Planck.
  - **Flujo RG II → IV:** preservación del grupo gauge (K-024) + level shifting del nivel CS; el k_eff ≈ 2π/α ≈ 330 es semiclásico/perturbativo, consistente.
- **Por qué importa:**
  - **Primera explicación estructural** del patrón observado α₂ ≈ α₃ ≠ α₁ desde el marco SCG. La near-convergencia no es coincidencia — es consecuencia de la geometría de la red.
  - **K-026 refinado:** el patrón de acoplamientos agrupa "vértice vs segmento", mientras que el patrón quiral agrupa "gravedad vs red". Las dos distinciones son independientes en SCG.
  - **K-024 reafirmado cuantitativamente:** el nivel CS dinámico (k_eff ≈ 330) es compatible con el grupo gauge topológico.
  - **Ruta hacia predicción numérica:** si α_gauge = γ/(4π) se deriva formalmente, el 1% de discrepancia con α_3(M_P) quedaría explicado. El 7% de discrepancia de α_2 requiere 2-loops.
  - **T-1 atacada:** el flujo k_topológico (Régimen I) → k_efectivo (Régimen IV) tiene mecanismo cualitativo identificado (level shifting).
- **Caveats honestos:**
  - **Valor α ≈ 0.02 no se deriva cuantitativamente** desde primeros principios. α = γ/(4π) es hipótesis apoyada en coincidencia numérica, no teorema.
  - **Discrepancia α_2 vs α_3 (7%)** atribuible a 2-loops/thresholds; verificación explícita pendiente.
  - **Matching II → IV formal** (integración de modos) sigue por hacer. El argumento estructural es consistente pero no es cálculo cerrado.
  - **El "problema del acoplamiento gravitacional"** (G vs g_W a baja energía) sigue abierto; la propuesta es que emerge del flujo RG sin que sean "el mismo acoplamiento" en sentido QFT.
  - **α_1(M_P) = 0.030 específico no se deriva.** Solo el patrón "distinto a α_2, α_3".
- **Promoción a confirmado si:** (i) se deriva explícitamente α_gauge = γ/(4π) desde matching de S_madre al SM; (ii) se verifica que el 7% de discrepancia α_2 vs α_3 se cierra con 2-loops; (iii) se calcula el flujo level-shifting cuantitativamente.
- **Relación con literatura:** Dreyer 2003 (γ = 0.2375); Amaldi-de Boer-Furstenau 1991 (near-convergence sin SUSY); AMS 2014 (SU(2)_L gravitacional); Krasnov-Percacci 2018 (review unificación). K-023 + K-024 internos.

---

**REFINAMIENTO DE K-030 (sesión 21, Q-039):** Q-039 determinó que Λ_UV en régimen I de SCG es O(M_P²) (bajo Baez 2000: Λ(k) = 1/(4Gk), con k entero positivo → Λ(k) ≤ 0.25 M_P²), tres órdenes de magnitud por debajo de Λ_c = 384 M_P² de ABKP 2025. Consecuencia:

- **Ruta ABKP NO cierra K-030** en régimen I. Ninguna interpretación alternativa razonable (Λ como curvatura efectiva; running RG asymptotic-safety; inflación) da Λ_UV > Λ_c sin asunciones super-Planckianas especulativas.
- **Ruta Randono 2006 (β real) pasa a ser primaria.** Resuelve las 4 patologías de Witten sin requerir Λ > Λ_c. Preserva CP violation observable (quiralidad fenomenológica).
- **ABKP provee mitigación parcial:** con Λ_UV < Λ_c, solo "mitad de los modos" son normalizables según ABKP. Mejor que cero, no completa.
- **Q-040 (compatibilidad K-019 ↔ Randono β real) pasa a prioridad ALTA.** Su resolución determina el destino final de K-030 y de P-11.
- **K-030 sigue candidato**, con la caracterización más precisa: Randono primario + ABKP parcial + SCG mitigantes + K-019 re-articulado. Severidad de P-11 sigue 🟡 media.
- Análisis completo: `notes/Q-039_Lambda_UV_regimen_I.md`.

**REFINAMIENTO DE K-030 (sesión 22, Q-040):** Q-040 determinó que la ruta Randono (β real) preserva normalizabilidad + CPT + violación P-T cualitativa, pero **NO preserva automáticamente la asimetría máxima del SM** (sólo fermiones L acoplan a SU(2)_L). K-019 se debilita: pasa de "identidad matemática literal (β=-i)" a "compatibilidad cualitativa (β real)". La asimetría máxima del SM requiere **mecanismo adicional** no provisto directamente por Randono:

- Candidatos no derivados: (1) UBFC específica con simetría L; (2) condensación de anyones Higgs (K-021); (3) Kaplan 2024 fermiones quirales en frontera topológica; (4) límite β → ∞ especulativo.
- **Q-042 nueva (prioridad media):** ¿qué mecanismo SCG amplifica violación P de Randono hasta asimetría máxima del SM?
- **K-030 sigue candidato**, con reservas mayores. Ambas rutas (ABKP por Q-039, Randono por Q-040) tienen costos identificados. K-030 está **más débil** que en sesión 17, no más fuerte.
- **P-11 sigue 🟡 media** (no rebajada a 🟡 baja como se esperaba).
- Análisis completo: `notes/Q-040_compatibilidad_randono_K-019.md`.

**PROMOCIÓN DE K-030 (sesión 24, Q-042 resuelta parcialmente con veredicto (D)):**

- **K-030 pasa de "candidato con reservas mayores" a "CONFIRMADO con ruta identificada" (pendiente Q-043).** Primera promoción positiva desde su introducción en sesión 17.
- **Mecanismo identificado:** Kaplan 2024 (PRL 132 141603) + Wang-Wen 2018-2019 (arXiv:1809.11171) + modular Walker-Wang (2208.03397) proveen conjuntamente ruta conceptual completa para asimetría máxima SM:
  - Kaplan 2024: fermiones quirales sin mirror partners en frontera dD de bulk (d+1)D topológico.
  - Wang-Wen 2018-2019: SM completo desde SO(10)-GUT definible no-perturbativamente en lattice 3+1D vía cobordismo (Ω^5 = ℤ₂, clase trivial) + gap del mirror sector.
  - Modular WW: bulk 3+1D invertible/SPT; frontera (2+1)D quiral. Consistente con red SCG de H-003.
- **Aplicabilidad a SCG:** los fermiones SM como defectos topológicos (H-003) actúan localmente como fronteras. Asimetría máxima emerge estructuralmente del gap del mirror, independiente de β de Ashtekar.
- **Compatibilidad con Randono:** los sectores gravitacional (β real → Kodama normalizable) y quiral-SM (topológico → asimetría máxima) son estructuralmente desacoplados. β real no compromete la quiralidad.
- **P-11 rebajada** de 🟡 media a 🟡 **baja** con caveat: dependencia en Q-043.
- **Q-043 nueva:** ¿existe UBFC modular específica para SCG con contenido SO(10) que cancele anomalías y dé asimetría SM máxima? Decide promoción final de K-030 a "confirmado limpio".
- **Costos:** K-019 tercera reinterpretación (quiralidad es topológica, no gravitacional); K-026 significativamente debilitada (dicotomía "gravedad quiral / red no-quiral" no se sostiene bajo modular WW + Kaplan).
- **Promoción a "confirmado limpio" si:** Q-043 cierra constructivamente (UBFC modular SCG con SO(10) explícita).
- Análisis completo: `notes/Q-042_mecanismo_amplificacion_P.md`.

**REINTERPRETACIÓN DE K-019 (sesión 24, Q-042):** K-019 mantiene contenido empírico (SU(2)_L es quiral, los fermiones L acoplan) pero su **mecanismo físico** se reinterpreta por tercera vez:

- **(i) Sesión 9 — AMS 2014:** literal con β = -i. "A_Ashtekar = su(2)_L" como identidad matemática. Asimetría máxima automática.
- **(ii) Sesión 22 — Q-040 (Randono β real):** compatibilidad cualitativa. Violación P preservada observacionalmente, asimetría máxima no automática.
- **(iii) Sesión 24 — Q-042 (Kaplan + Wang-Wen + modular WW):** **la quiralidad es topológica, no gravitacional**. SU(2)_L emerge como edge mode quiral de defectos WW modulares, con anomalías canceladas via SO(10)-cobordismo. Independiente de β de Ashtekar.
- **Consecuencia:** la conexión gravitacional de Ashtekar-Barbero-Immirzi (con β real) es el sector **gravitacional puro**; la quiralidad SM no viene de ahí. Los dos sectores son estructuralmente desacoplados.
- **Contenido empírico preservado:** SU(2)_L sigue siendo el único factor gauge quiral; los fermiones L siguen siendo los únicos que acoplan. No cambia la fenomenología.

**DEGRADACIÓN DE K-026 (sesión 24, Q-042):** K-026 pasa de "confirmado estructural" a **"observación heurística sin dualidad limpia"**:

- **Problema:** la red WW **puede ser quiral** en su frontera (modular WW + Kaplan + Wang-Wen). El argumento original "red no-quiral por Nielsen-Ninomiya" aplicaba a bulk puro sin frontera; no aplica a WW con frontera topológica.
- **Qué sigue valiendo:** el patrón observado (SU(2) quiral, SU(3) y U(1) no-quirales) es real y requiere explicación. El patrón **origen** (SU(2) viene de Ashtekar, SU(3)/U(1) de red) sigue siendo una observación.
- **Qué NO sigue valiendo:** la dicotomía "gravedad = único origen quiral, red = inherentemente no-quiral" ya no es teorema aplicable a SCG. La red WW con frontera topológica **es** una fuente potencial de quiralidad.
- **Nueva interpretación:** SU(3) y U(1)_Y pueden emerger no-quiralmente del bulk WW (modos transversales + trivalencia), mientras SU(2)_L emerge quiralmente de la estructura de defecto/frontera. Pero la asignación "quiral vs no-quiral" NO es dictada por "origen gravitacional vs de red" — depende de la UBFC específica (Q-043).
- Análisis: `notes/Q-042_mecanismo_amplificacion_P.md`.

## K-033 (CANDIDATO POTENCIAL, NO PROMOVIDO) — SCG + modular Walker-Wang + Wang-Wen = marco natural para SO(10)-GUT no-perturbativo en 3+1D

- **Fecha:** 2026-04-21 (sesión 24)
- **Estado:** candidato potencial. Apertura colateral identificada, no explorada técnicamente.
- **Enunciado:** la combinación de (i) red SCG Walker-Wang en 3+1D (H-003, K-026), (ii) construcción Wang-Wen 2018-2019 de SM completo desde 16 Weyl spinoriales de SO(10), y (iii) estructura modular WW con frontera quiral (2208.03397), provee un marco natural para definir SO(10)-GUT no-perturbativamente en lattice 3+1D dentro de SCG. La cadena de inclusiones SO(10) ⊃ SU(5) ⊃ SU(3) × SU(2) × U(1) coincide con el grupo gauge derivado en SCG (D-004).
- **Por qué importa:**
  - Conexión con gran unificación no disponible previamente en SCG.
  - SCG + Wang-Wen = definición no-perturbativa de SM completo en lattice.
  - Posible apertura para masas fermiónicas, Yukawas, generaciones desde estructura SO(10).
- **Condiciones para promoción:**
  - Q-043 resuelta: UBFC modular SCG con SO(10) contenido construida.
  - Verificación de que las reglas de fusión de D-004 son compatibles con embebimiento SO(10).
  - Programa técnico de 10+ sesiones.
- **Caveats honestos:**
  - No es derivación — es identificación de compatibilidad estructural.
  - Elecciones específicas de UBFC pueden forzar grupos distintos a SO(10).
  - Wang-Wen trata SO(10) con fermiones quirales libres; SCG tiene estructura geométrica adicional.
- **Relación con literatura:** Wang-Wen 2018-2019 (marco técnico); Georgi-Glashow 1974 (SO(10)-GUT original); Langacker (review GUT).

## K-031 — La acción efectiva 2D de cuerda SCG emerge por reducción dimensional de S_PA e integra D-001/D-003/D-006/D-007 [PROMOVIDO A CONFIRMADO SESIÓN 20]

- **Fecha:** 2026-04-21 (sesión 18)
- **Estado:** candidato. Derivación estructural con dos ansatz físicos marcados (A1 worldsheet 2D, A2 llenado volumétrico). Promoción a confirmado requiere derivar A2 desde variación.
- **Derivado de:** D-008 (`logic/derivations/D-008_reduccion_a_cuerda_SCG.md`) y análisis completo en `notes/Tarea_5.4_reduccion_a_cuerda.md`.
- **Enunciado:** partiendo de S_PA + S_cosmo (D-007) evaluada en fondo Schwarzschild con ansatz A1 (worldsheet 2D) + A2 (llenado volumétrico L·d²~V_BH) + A3 (saturación entrópica S_cuerda = S_BH, derivada de D-007 + frontera), la reducción dimensional transversal produce:
  ```
  S_SCG-2D = −μ(d) ∫dτdσ√(−h) + E_Casimir[L,d]·∫dτ + S_backreaction + topológicos
  ```
  con μ(d) ~ M_P²(ℓ_P/d)² y E_Casimir = 2π ℏc·L/d² (= D-006 directamente). En el punto de equilibrio (combinación A2 + A3), se recupera d ∼ √(r_s ℓ_P), L ~ r_s²/ℓ_P (= K-007 de D-003 v1.2). El modelo fenomenológico D-001 emerge como límite IR discretizado.
- **Por qué importa:**
  - **Cierra estructuralmente el ciclo Régimen II → Régimen III del bosquejo.** El sector BH deja de ser ansatz separado y pasa a ser consecuencia de S_madre reducida.
  - **Doble derivación de K-007**: la escala d ∼ √(r_s ℓ_P) se obtiene ahora desde (a) holografía pura (D-003 v1.2) y (b) reducción dimensional de S_PA (D-008). Ambas concordantes.
  - **D-006 (Casimir) emerge naturalmente** como cuantización de modos transversales de la worldsheet — ya no es "resultado separado" sino ingrediente natural de la acción reducida.
  - **D-001 justificado a posteriori**: los tres términos fenomenológicos (grav, tensión, info) corresponden respectivamente a backreaction del fondo, expansión NG, Casimir transversal.
  - **Balance energético coherente con masa ADM** via K-028 candidato (⟨f⟩ = 1/(3π²)): E_Casimir plano = 3π² Mc² absorbido por redshift.
  - **P-8 (Lagrangiana) refinada**: 2/5 sub-tareas completadas (D-006, D-007), 2/5 parciales con candidatos (K-030, K-031), 1/5 pendiente (flujo RG).
- **Caveats honestos:**
  - A2 (llenado volumétrico) es **ansatz**, no derivación. Q-041 nueva: ¿cómo emerge L·d²~V_BH desde variación?
  - Factores O(1) no cerrados (convenciones de cuerda cerrada vs abierta, corte UV, geometría del plegado).
  - S_backreaction está bosquejada, no calculada explícitamente. Requiere teoría de cuerdas en fondo curvo (Callan-Thorn 1986).
  - Dinámica de formación (Q-017, P-7.1) sigue abierta.
  - K-028 sigue candidato; rigorización pendiente (P-15').
- **PROMOCIÓN (sesión 20):** K-031 pasa de candidato a confirmado estructuralmente. D-009 (`logic/derivations/D-009_llenado_volumetrico_variacional.md`) deriva el ansatz A2 (llenado volumétrico) como mínimo variacional de E_total bajo restricción de confinamiento geométrico. La condición (i) de las condiciones de promoción queda satisfecha. La cuerda SCG plegada es el análogo cuántico-gravitacional de una enana blanca (Casimir vs horizonte). Residuales: alternativas topológicas al plegado cilíndrico + factor de empaquetamiento O(1) + μ(d)~1/d² asumido.
- **Relación con literatura:** Polchinski 1998 (reducción Nambu-Goto); Callan-Thorn 1986 (cuerdas en fondos curvos); Mathur fuzzballs (imagen análoga, derivación distinta desde SUSY); Chandrasekhar 1931/1935 (balance presión-gravedad en enanas blancas, análogo directo al argumento D-009). Cada pieza individual es estándar; novedad es la aplicación integradora al marco SCG.

## K-030 (CANDIDATO, REFINADO SESIÓN 21 — RANDONO PRIMARIO, ABKP PARCIAL) — P-11 mitigado vía Randono 2006 como ruta primaria + ABKP 2025 parcial

- **Fecha:** 2026-04-21 (sesión 17)
- **Estado:** candidato. Obtenido por síntesis crítica de literatura; formalización SCG-específica pendiente.
- **Derivado de:** Tarea 5.3 del bosquejo (`notes/Tarea_5.3_kodama_P-11.md`).
- **Enunciado:** las cuatro patologías de Kodama identificadas por Witten 2003 (modos de energía negativa; no-normalizabilidad; CPT violation; no invariancia bajo grandes gauge) admiten rutas de rescate en la literatura. Para el marco SCG específicamente:
  - **Ruta A (Alexander-Bernardo-Kuntzleman-Pezzelle 2025, arXiv:2511.05417):** con inner product holomorfico derivado de reality conditions y Λ > Λ_c = 384/ℓ_P², Ψ_K es perturbativamente normalizable. Mismo grupo que AMS 2014 (K-019).
  - **Ruta B (Randono 2006, gr-qc/0504010 + 0611073 + 0611074):** con Immirzi β real, Ψ_K^{(β)} es CPT-invariant, CP-no-invariant (preserva violación de paridad), invariante bajo grandes gauge, y normalizable. Requiere re-articular K-019 (la quiralidad no es literalmente "A = su(2)_L" sino "CP violation observacional preservada").
  - SCG añade cuatro mitigantes estructurales: (i) restricción de simplicidad de D-007 (reduce medida al sector geométrico); (ii) régimen I con Λ_efectiva ~ M_P² (cerca de Λ_c ABKP); (iii) defectos Walker-Wang en la medida (reinterpreta normalizabilidad con contenido topológico); (iv) consistencia del lineage: grupo Alexander produce tanto AMS 2014 como ABKP 2025.
- **Consecuencia operativa:** P-11 pasa de 🟡 alta (riesgo existencial) a 🟡 media (riesgo manejable con dos rutas alternativas).
- **Por qué importa:**
  - Elimina el miedo existencial sobre Ashtekar autodual que motivó P-11 desde sesión 11.
  - El régimen I del bosquejo (sesión 12) deja de ser ansatz aislado y se conecta activamente con el programa de rescate de Kodama: si Λ_UV ≳ 384 M_P², Kodama normalizable.
  - La compatibilidad sociológica (mismo grupo Alexander detrás de K-019 y de la ruta de rescate) refuerza la coherencia interna del marco.
  - Abre tareas concretas para sesiones futuras: cuantificar Λ_UV en régimen I; formalizar HK-SCG; clarificar compatibilidad K-019 ↔ β real.
- **Caveats honestos:**
  - **Ningún cálculo es específico de SCG.** Los mitigantes son estructurales; formalización computational requeriría 2-3 sesiones adicionales.
  - Λ_UV = M_P² estrictamente está justo POR DEBAJO del umbral ABKP (Λ_c = 384 M_P²) → solo la mitad de los modos es normalizable. Si Λ_UV ≳ 400 M_P², normalización completa. El valor exacto no está derivado.
  - La ruta Randono requiere re-articular K-019. No es fatal (CP violation observacional se preserva) pero cambia la interpretación.
  - Ninguna ruta aborda el problema no-perturbativo global.
- **Promoción a confirmado** si: (i) Λ_UV en régimen I de SCG se cuantifica >Λ_c vía cálculo de S_madre; o (ii) se demuestra que los modos descartados por ABKP a Λ < Λ_c coinciden con configuraciones excluidas por los defectos WW de SCG.

## K-028 (CANDIDATO, PENDIENTE DE RIGORIZACIÓN) — El redshift gravitacional promedio del interior de un BH-SCG es ⟨f⟩ ≈ 1/(3π²)
- **Fecha:** 2026-04-20 (sesión 15)
- **Estado:** candidato. Obtenido por consistencia (no por cálculo formal QFT+GR).
- **Derivado de:** Q-037+Q-038 (`notes/Q-037-038_casimir_fondo_curvo.md`).
- **Enunciado:** el redshift gravitacional promedio de los modos cuánticos internos de un BH-SCG, medido desde el infinito, es ⟨f⟩ = 1/(3π²) ≈ 0.034. Este factor se determina por consistencia entre el Casimir local de los modos transversales de Polyakov (plano: 3π² Mc²) y la masa ADM observable del BH (Mc²).
- **Comparación con redshift volumétrico naïve:** ⟨f⟩_vol = 3π/16 ≈ 0.59 para distribución uniforme en V_BH. La discrepancia (factor ~17) refleja que la cuerda está efectivamente concentrada cerca del horizonte por holografía (S ∝ A, no V).
- **Por qué importa:**
  - Resuelve la tensión T-6 a nivel de orden-de-magnitud. Permite que D-006 (Casimir plano) y GR (masa ADM) coexistan consistentemente.
  - Cuantifica cómo la holografía "comprime" la cuerda cerca del horizonte.
  - Posible firma observacional en el espectro modulado de Hawking.
- **Caveats honestos:**
  - No derivado rigurosamente — el cálculo formal en QFT en fondo Schwarzschild interior queda pendiente (P-15').
  - El factor exacto podría ajustarse (1/(4π²), 1/π², etc.) al hacer el cálculo riguroso; el orden de magnitud ~1/30 es robusto.
  - Depende de la elección de vacío cuántico (Boulware vs Unruh vs Hartle-Hawking).

## K-027 — A-003 es la presión de Casimir de los modos transversales de Polyakov con corte Planck — no un axioma independiente
- **Fecha:** 2026-04-20 (sesión 13, resolución de Q-032 / tarea 5.1)
- **Estado:** CONFIRMADO ESTRUCTURALMENTE. Forma funcional derivada rigurosamente; coeficiente O(1) depende de convención.
- **Derivado de:** D-006 (`logic/derivations/D-006_A-003_desde_polyakov.md`) y análisis completo en `notes/Q-032_polyakov_y_A-003.md`.
- **Enunciado:** la cuantización canónica estándar de la acción de Polyakov para cuerda cerrada, restringida al sector transversal (2 modos en D=4) y con corte UV físico en longitud de onda λ ≥ d (*d* = espaciamiento Walker-Wang, ≥ ℓ_P), produce una energía del vacío E_vac = 2π ℏc L/d² — exactamente la forma funcional del término E_info de A-003 v1.1 con la identificación N ↔ 2π.
- **Por qué importa:**
  - A-003 deja de ser axioma; se convierte en proposición derivada (D-006).
  - Se elimina un postulado sin pérdida explicativa — aplicación directa de K-005 ("la buena teoría es más modesta").
  - La "presión de degeneración gravitacional" se identifica como presión de Casimir confinada — fenómeno conocido y bien caracterizado.
  - Los axiomas activos de SCG se reducen a dos (A-001, A-002).
  - Reabre comparación cuantitativa con Horowitz-Polchinski y teoría de cuerdas estándar (P-4).
- **Caveats honestos:**
  - El coeficiente numérico (2π para cuerda cerrada; π/2 para abierta) depende de la topología worldsheet del defecto WW; es O(1) pero no "libre" ni "entero".
  - La derivación asume Polyakov como acción efectiva IR del defecto WW — consistencia cuántica (P-14) pendiente.
  - K-007 (d ~ √(r_s ℓ_P)) necesita reverificación directa desde Polyakov sin usar A-003 como intermedio (Q-036).
- **Relación con literatura:** análogo directo del efecto Casimir (1948) en 1+1D. Cada pieza individual es estándar (Polchinski 1998); novedad es la aplicación al contexto SCG/WW y la consecuente reducción axiomática.

## K-029 — El núcleo gravitacional de S_madre (Plebanski-autodual + Λ) reduce on-shell a E-H + Λ con A = su(2)_L, y su frontera es CS(k=2π/κΛ)

- **Fecha:** 2026-04-21 (sesión 16, tarea 5.2 del bosquejo)
- **Estado:** CONFIRMADO ESTRUCTURALMENTE (clásico). Nivel: insight confirmatorio de consistencia, no hallazgo conceptual profundo.
- **Derivado de:** D-007 (`logic/derivations/D-007_ec_movimiento_plebanski.md`) y análisis en `notes/Tarea_5.2_ec_movimiento_plebanski.md`. Resultados clásicos: Plebanski 1977; Capovilla-Dell-Jacobson 1991; Baez 2000; Krasnov 2009-2011; Alexander-Marciano-Smolin 2014.
- **Enunciado:** variando el núcleo gravitacional S_PA + S_cosmo del bosquejo (sesión 12):
  - δψ → restricción de simplicidad Σ = e ∧ e (sector geométrico).
  - δΣ → F(A) = ψ Σ + (Λ/3) Σ → ec. de Einstein autoduales con Λ; ψ on-shell = tensor de Weyl autodual; R = 4Λ.
  - δA → d_A Σ = 0 → A = ω_+ (conexión de spin autodual = **Ashtekar = su(2)_L**, confirma K-019).
  On-shell: S_núcleo ≡ (1/2κ) ∫ (R − 2Λ)√(−g) d⁴x + términos topológicos. Frontera (Baez 2000): Chern-Simons autodual con k = 2π/(κΛ).
- **Por qué importa:**
  - **Primera pieza concreta del programa Lagrangiana SCG.** Confirma que el núcleo de S_madre es consistente con GR + Λ.
  - **Reconfirma K-019 desde primeros principios clásicos.** La conexión autodual es literalmente su(2)_L del grupo de Lorentz — ni analogía ni importación; identidad derivada.
  - Cierra Tarea 5.2 del bosquejo. Debilidad P-8 se refina: "núcleo gravitacional derivado, quedan 3 sub-tareas (5.3 Kodama, 5.4 reducción a cuerda, 5.5 flujo RG)".
  - Respuesta parcial a Q-033 (frontera = CS(k=2π/κΛ)): argumento estructural via Baez 2000; correcciones por ψ sub-dominantes pero no computadas.
  - Consistente con el ansatz de sesión 12: núcleo Plebanski-autodual cuantiza a Crane-Yetter (bulk) / Walker-Wang (lattice), con frontera CS.
- **Caveats honestos:**
  - El resultado clásico (Plebanski = GR autodual) es **teorema conocido desde 1977**. La originalidad reside en la *aplicación al contexto SCG*, no en el cálculo en sí.
  - No resuelve tensiones T-1 (k topológico vs k dinámico), T-2/P-11 (condiciones de realidad para A compleja), T-3 (WW Hamiltoniano vs Lagrangiana), T-4 (matter de red vs S_matter).
  - No predice ninguna constante del SM.
  - La cuantización (incluyendo el análogo Kodama y su no-normalizabilidad Witten 2003) no se aborda aquí; queda para tarea 5.3.
- **Relación con literatura:** estrictamente aplicación de Plebanski 1977 (teorema original), Baez 2000 (reducción bulk-boundary), Krasnov 2009-2011 (revisión moderna), AMS 2014 (identificación A=su(2)_L). Ningún paso es novedoso individualmente.

---

(Las debilidades de H-001 están en `logic/refutations/debilidades_H-001.md`, no aquí. Aquí va lo que sí aprendimos, con honestidad.)
