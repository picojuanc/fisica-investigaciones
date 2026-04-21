# H-001: Fase de Cuerda Gravitacional Estabilizada (SCG)

- **ID:** H-001
- **Fecha de propuesta:** 2026-04-15
- **Origen:** derivada de una cadena de experimentos mentales sobre geometría de horizontes (E-001 → E-004)
- **Estado:** **activa** (con debilidades graves sin resolver — ver `logic/refutations/debilidades_H-001.md`)
- **Depende de:** A-001, A-002, A-003 (axiomas tentativos — ver `framework/axioms.md`)
- **Contradice a:** — (aún por chequear contra literatura)

## Enunciado

> **Existe una fase de la gravedad cuántica en la cual, cuando la densidad de energía supera un umbral crítico cercano a la escala de Planck, el colapso gravitacional NO produce un horizonte de eventos clásico, sino una configuración unidimensional extendida ("cuerda") estabilizada por el equilibrio entre tres términos de energía: gravitacional, de tensión y de "presión de entrelazamiento".**

## Forma compacta

```
E_total = E_grav + E_tensión + E_info

E_grav ≈ -G Σ_{i<j}  m_i m_j / r_ij          (tendencia a colapsar)
E_tensión ≈  k  Σ   (x_{i+1} - x_i)²          (tendencia a equiespaciar)
E_info   ≈  λ  Σ   1 / (x_{i+1} - x_i)        (penalización a densidad local)
```

Con las restricciones:
- **Radio mínimo:** r_min ~ ℓ_Planck (evita singularidad)
- **Entropía:** S ∝ L (longitud de la cuerda, **no** área)
- **Cota holográfica respetada:** dS/dL ≤ 1/ℓ_Planck

## Motivación

Surge de una cadena de preguntas:
1. ¿Puede un agujero negro tener área infinita y volumen finito (tipo trompeta de Gabriel) para maximizar entropía? → **No** (principio holográfico + estabilidad).
2. ¿Y si se "estira" el horizonte a un tubo muy largo? → Inestabilidad de Gregory–Laflamme: se fragmenta.
3. ¿Y si lo estiramos hasta escala cuántica? → La descripción geométrica deja de valer.
4. En ese límite, ¿el objeto resultante se comporta como una cuerda? → Sí, ya existe la correspondencia agujero-negro/cuerda (Horowitz–Polchinski) como pista.

**SCG generaliza:** no solo "al final" de la evaporación aparece la cuerda — sino que la cuerda es la fase estable que *reemplaza* al horizonte cuando la densidad supera el umbral.

## Consecuencias lógicas (si H-001 es correcta)

1. **No hay singularidad central** en el interior de un colapso a escala Planckiana.
2. **El horizonte de eventos es un fenómeno macroscópico emergente**, no fundamental.
3. **La entropía escala con longitud (S ∝ L)** en la fase de cuerda; recupera S ∝ A en el régimen macroscópico donde la cuerda se "pliega" cubriendo un área (conjetura a verificar).
4. **La información no se pierde en el colapso**: queda codificada en los modos de la cuerda.
5. **Existe una transición de fase gravitacional** entre "régimen BH" y "régimen cuerda" gobernada por la densidad local.

## Predicciones observables (hipotéticas, débiles por ahora)

- **Radiación de Hawking estructurada:** en lugar de espectro térmico puro, se verían modos discretos o picos correspondientes a vibraciones de la cuerda.
- **Ondas gravitacionales "filamentosas":** firmas específicas de cuerdas gravitacionales oscilantes.
- **Espectros discretos** asociados a evaporación de micro-BHs (si existen).
- **Cota superior a la densidad de información local** más restrictiva que la holográfica ordinaria.

## Experimentos mentales asociados

- [E-001: Trompeta de Gabriel gravitacional](../../experiments/thought_experiments/E-001_trompeta_gabriel_gravitacional.md)
- [E-002: Rotación y área del horizonte](../../experiments/thought_experiments/E-002_rotacion_area_horizonte.md)
- [E-003: Estiramiento del horizonte a hilo](../../experiments/thought_experiments/E-003_estiramiento_horizonte_hilo.md)
- [E-004: Hilo cuántico — ¿cuerda fundamental o emergente?](../../experiments/thought_experiments/E-004_hilo_cuantico_cuerda.md)

## Modelo computacional

- [D-001: Modelo discreto de cuerda gravitacional](../../logic/derivations/D-001_modelo_discreto_cuerda.md)
- Simulación: `experiments/simulations/sim001_cuerda_gravitacional.js`

## Problemas abiertos (serios)

Estos están desarrollados en `logic/refutations/debilidades_H-001.md`. En resumen:

1. **Definición operacional de "E_info"** — ¿qué cantidad física es? ¿cómo se mide?
2. **Escala de transición no derivada** — ¿por qué a una cierta densidad y no otra?
3. **Colapso macroscópico (estrellas) no explicado** — si la hipótesis es correcta, ¿por qué se observan agujeros negros macroscópicos y no "cuerdas estelares"?
4. **Relación con Horowitz–Polchinski** — ¿es SCG equivalente, reformulación, o extensión? ¿predice algo distinto?
5. **Número de dimensiones** — ¿por qué 1D y no otra? ¿Depende de la dimensión del espacio ambiente?
6. **Consistencia con el teorema del no-pelo** — generalmente el horizonte es caracterizado por M, J, Q. ¿SCG los preserva como hair macroscópico pero añade structure microscópica?

---

## Refinamiento v1.1 (2026-04-16): reinterpretación de E_info

Tras atacar P-1 (ver `notes/P-1_analisis.md`), el término "presión de entrelazamiento / información" se reinterpreta como **presión cinética cuántica de los grados de libertad gravitacionales a escala Planck** — análoga a las presiones de degeneración que estabilizan enanas blancas y estrellas de neutrones.

### Reemplazo clave

```
Versión v1.0:  E_info = λ Σ 1/d           (ad hoc, "información")
Versión v1.1:  E_info ≈ N ℏc Σ 1/d        (Heisenberg + relativista)
```

donde λ = N·ℏc con N = número de modos gravitacionales por celda.

### Consecuencias del refinamiento

1. **No necesitamos un axioma nuevo exótico.** A-003 ahora es QM+GR aplicadas al régimen Planck. Menos compromiso, más anclaje.
2. **Hay análogo cuantitativo del límite de Chandrasekhar.** La cuerda gravitacional estabiliza hasta una masa crítica M ~ M_Planck. Masas mayores colapsan clásicamente a BH, pero en su interior la presión gravitacional de degeneración evita la singularidad → conecta con escenarios tipo fuzzball.
3. **Compatible con lo observado.** BHs macroscópicos siguen existiendo (el horizonte clásico se forma), pero su interior ya no es singular. Esto **resuelve parcialmente P-3**.
4. **Conexión con LQG** más transparente: los "grados de libertad gravitacionales" pueden ser espines, o modos discretos equivalentes.

### Nuevas preguntas

- Q-014: ¿qué son exactamente los grados de libertad gravitacionales? (Ver `open_questions.md`.)
- Q-015: ¿cuál es el análogo numérico de M_Chandrasekhar en este régimen?

### Problemas resueltos (total o parcial)

- **P-1 (crítico) → resuelto parcialmente.** El término E_info ya tiene anclaje físico. Queda derivar N.
- **P-3 (crítico) → camino abierto.** La formulación permite coexistencia de BH macroscópico y cuerda interior.

### Problemas que siguen

- **P-5** (por qué 1D): sin resolver aún.
- **P-7** (consistencia entrópica): por calcular.

### Experimento mental asociado

- [E-005: Analogía Chandrasekhar para la cuerda gravitacional](../../experiments/thought_experiments/E-005_analogia_chandrasekhar.md)

---

## Historial

- **2026-04-15** — Propuesta inicial (v1.0) derivada de conversación previa documentada en `notes/inbox/2026-04-15_ideas_pages_source.txt`.
- **2026-04-16** — Refinamiento v1.1: E_info reinterpretada como presión cinética cuántica de degeneración. Axioma A-003 reformulado en consecuencia. Nuevo experimento mental E-005 (analogía Chandrasekhar).
- **2026-04-16 (sesión 3)** — Derivación D-002: **D=1 no es postulado, es consecuencia**. La dimensionalidad de la fase estable se deriva del balance de exponentes entre E_deg (N^(1+1/D)) y E_grav (N²). Solo D=1 iguala exponentes para todo N. P-5 pasa a parcialmente resuelto; nuevo sub-problema P-5.1 sobre fijación fina de L*.
- **2026-04-16 (sesión 4)** — Derivación D-003: **la transición BH↔cuerda conserva entropía**. La cuerda interior se pliega con escala transversal d ~ √(r_s·ℓ_P) y satura exactamente la cota holográfica: S_cuerda = S_BH. Para BH estelar, d ~ 1 fm (nuclear). Sugiere resolución de la paradoja de información (K-008). P-7 baja a 🟡. **H-001 v1.1 ya no tiene eslabones rojos.**
- **2026-04-16 (sesión 5)** — Revisión sistemática de literatura. Comparación con fuzzballs, stretched horizon, Horowitz-Polchinski, stringy forces. H-001 v1.1 **NO es equivalente a ninguno** (escalas y ubicación de información distintas). Originalidad confirmada. P-4 parcialmente resuelto.
- **2026-04-16 (sesión 6)** — Experimento mental **E-006: ecos de ondas gravitacionales**. Primera predicción cuantitativa falsable: el retraso entre ecos en H-001 v1.1 es la **mitad** que en fuzzballs/Planck-scale models (factor ½). Diferencia numérica ~26 ms para BH de 30 M_₀. En principio distinguible con LIGO (estadística acumulada) y fácilmente con detectores 3G. **H-001 v1.1 entra en territorio falsable.**
- **2026-04-20 (sesión 13) — REDUCCIÓN AXIOMÁTICA v1.2:** **A-003 deja de ser axioma.** Se deriva como efecto Casimir de modos transversales de Polyakov con corte Planck (`logic/derivations/D-006_A-003_desde_polyakov.md`, análisis en `notes/Q-032_polyakov_y_A-003.md`). **K-027 promovido a confirmado estructuralmente.** Base axiomática de H-001: de 3 axiomas (A-001, A-002, A-003) a **2** (A-001, A-002). El término E_info de la formulación original pasa de postulado a consecuencia — efecto Casimir análogo al de placas paralelas, con *L/d²* reemplazando *L²/d*. El prefactor (N = 2π para cuerda cerrada, π/2 para abierta) es fijo por la topología worldsheet del defecto WW — ya no es parámetro libre. Nueva debilidad P-14 identificada (consistencia Polyakov 4D no-crítica). Q-036 (reverificar K-007 desde Polyakov directo) y Q-037 (prefactor exacto) abiertas.
