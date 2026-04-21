# 24 — La quiralidad es topológica, no gravitacional

*Sesión 24 — 2026-04-21*

## Dónde estábamos

El reporte anterior (#23) cerró la fase de consolidación. Snapshot v1.8 publicado, OVERVIEW.md externo, repo público en GitHub, lista para feedback. Ruta A había dado un balance honestamente mixto: una promoción limpia (K-031 en sesión 20), un resultado negativo (Q-039 en sesión 21: la ruta ABKP no cerraba K-030), y un parcial ambiguo (Q-040 en sesión 22: Randono β real preservaba viabilidad pero no asimetría máxima del SM).

La pregunta natural que había quedado en el aire era **Q-042**: ¿qué mecanismo en SCG amplifica la violación P modulada de Randono hasta la asimetría máxima observada del Modelo Estándar? Un doblete de Higgs L no aparece por decreto. Y si Randono con β real no da asimetría máxima automáticamente, ¿de dónde viene la asimetría máxima?

Entre los cuatro candidatos que Q-040 había identificado, uno sobresalía: **Kaplan 2024** — *Chiral Gauge Theory at the Boundary between Topological Phases*, PRL 132 141603. El mecanismo de fermiones quirales en la frontera entre dos fases topológicas era independiente de β, del tipo de cosa que parece hecha a medida para nuestra situación. Esta sesión abordó ese camino.

## El hallazgo

Kaplan 2024 no viene solo. Tiene compañía: **Kaplan & Sen 2024** (PRL 132 141604), el caso concreto con Wilson fermion en (2+1)D y frontera (1+1)D donde los *edge states* de Weyl emergen visiblemente sin *mirror partners*. Y tiene precedente: **Wang & Wen 2018-2019** (arXiv:1809.11171), con un resultado aún más ambicioso — **el Modelo Estándar completo, desde SO(10)-GUT con 16 fermiones en la representación spinorial, puede definirse no-perturbativamente en un lattice 3+1D de bosones o qubits**. El mecanismo es cobordismo: para Spin(N) con N ≥ 7, el grupo relevante Ω⁵ admite clase invertible trivial; los estados tipo SPT del bulk garantizan que el sector *mirror* se puede gapeo mediante interacciones simétricas sin romper la simetría on-site.

Y hay una tercera pieza: **modular Walker-Wang** (Kawagoe-Gorantla-Williamson 2023, PRB 107 085134). Si la categoría unitaria de fusión trenzada que alimenta el modelo Walker-Wang 3+1D es modular, entonces el bulk es una fase *invertible* (equivalente a SPT trivial), y la frontera (2+1)D hospeda una fase *quiral*. El ejemplo canónico es el 3-fermion Walker-Wang: bulk time-reversal SPT, frontera 3F anyon theory.

Junté las piezas. **El bulk Walker-Wang 3+1D de SCG (H-003, K-026) puede ser una fase topológica invertible con UBFC modular. Los fermiones del SM, que en SCG son defectos topológicos (H-003), actúan localmente como fronteras en el bulk. En esa "frontera" — el tubo de Gauss alrededor de cada defecto — emergen estados de borde quirales, con quiralidad máxima, sin mirror partners. Esto es Kaplan 2024 aplicado a defectos. Y la estructura de cancelación de anomalías que permite gapear el mirror de un lado es Wang-Wen 2018-2019.**

El mecanismo es **independiente de β de Ashtekar**. La quiralidad no viene de la conexión gravitacional — viene de la topología de la red. El sector gravitacional, con β real (Randono), es otra cosa: ahí no hay quiralidad fenomenológica. Los dos sectores son estructuralmente desacoplados. Con β real resolvemos el problema de normalizabilidad de Kodama (sesión 17, K-030 parte A, preservado en Q-040). Con Kaplan + Wang-Wen + modular WW resolvemos la asimetría máxima SM (Q-042, esta sesión). **Dos mitigaciones concurrentes para P-11.**

## Lo que cambia

Veredicto de Q-042: **(D) Mecanismo conceptual completo, independiente de β, aplicable a SCG; requiere construcción técnica concreta (Q-043 nueva).** Primera promoción positiva de K-030 desde su introducción en sesión 17. **P-11 se rebaja de 🟡 media a 🟡 baja con caveat.** Si Q-043 cierra constructivamente, P-11 → ✅ resuelto.

Pero hay costos. Dos insights se tocan:

**K-019** — "conexión autodual de Ashtekar = su(2)_L del grupo de Lorentz, la quiralidad de la fuerza débil es gravitacional" — sufre su **tercera reinterpretación**. Originalmente (sesión 9, AMS 2014) era literal con β = -i. Luego (sesión 22, Q-040) se reinterpretó como "compatibilidad cualitativa con β real". Ahora (sesión 24) se reinterpreta como "la quiralidad es **topológica**, no gravitacional". El contenido empírico se preserva — SU(2)_L sigue siendo el único factor gauge quiral, los fermiones L siguen siendo los únicos que acoplan — pero el mecanismo físico subyacente es distinto. La conexión de Ashtekar con β real es el sector gravitacional puro; la quiralidad SM emerge de la red WW modular con frontera.

**K-026** — "el patrón quiral del SM coincide con el patrón de origen dual (gravedad = quiral, red = no-quiral por Nielsen-Ninomiya)" — se **degrada significativamente**. El problema es que, bajo modular Walker-Wang, la red **puede ser quiral** en su frontera. El argumento "Nielsen-Ninomiya impide quiralidad en lattice" aplicaba a bulk puro sin frontera. Con frontera topológica y anomalías canceladas, Nielsen-Ninomiya se evade explícitamente. La dicotomía limpia "gravedad quiral / red no-quiral" ya no se sostiene. K-026 pasa de "confirmado estructural" a "observación heurística sobre patrones sin dualidad limpia".

Esto es aplicación de la Regla 9 del protocolo: "preferir destruir un resultado propio a defenderlo por inercia". K-019 y K-026 eran piezas elegantes del marco. La elegancia cede ante la evidencia. La nueva imagen es menos simétrica — pero es más honesta, y está sostenida por literatura técnica reciente. Aplicación simultánea de K-005 ("la teoría buena es más modesta"): Kaplan, Wang-Wen y Kawagoe et al. son mecanismos establecidos; SCG los adopta sin postular nada nuevo.

## Lo que se abre

**Q-043 nueva (prioridad alta):** ¿existe una UBFC modular específica para SCG con contenido SO(10) que cancele anomalías y dé asimetría SM máxima? Las condiciones son concretas — (a) categoría trivalente (compatible con D-004 y la estructura Walker-Wang de SCG); (b) modular (para que el bulk sea invertible); (c) frontera hospede 16 Weyl spinoriales de SO(10); (d) anomalías de 't Hooft canceladas por cobordismo. Candidatos naturales existen: Drinfeld center de SU(3)×SU(2)×U(1), Witt classes generadas por Ising MTC, UBFCs derivadas de SO(10) holografía. El esfuerzo estimado es de 5-10 sesiones si se emprende técnicamente.

**K-033 candidato potencial (apertura colateral):** SCG + modular Walker-Wang + Wang-Wen = marco natural para **SO(10)-GUT no-perturbativo en lattice 3+1D**. La cadena de inclusiones SO(10) ⊃ SU(5) ⊃ SU(3) × SU(2) × U(1) coincide con el grupo gauge derivado en SCG (D-004). No se promueve K-033 aquí — es apertura, no resultado. Pero por primera vez, SCG tiene una ruta concreta hacia gran unificación. Wang-Wen proveen el marco técnico; SCG proveería la estructura geométrica subyacente. Si se emprende, es programa de 10+ sesiones.

## Balance

Tras 4 sesiones de Ruta A (20, 21, 22, 24):

- **K-031** promovido limpio (sesión 20, D-009, "enana blanca cuántica").
- **K-030** promovido a "confirmado con ruta identificada" (sesión 24, Q-042). Pendiente Q-043 para promoción limpia.
- **K-030 vía ABKP** (Q-039): negativo.
- **K-030 vía Randono solo** (Q-040): parcial.
- **K-032, K-028**: pendientes.

**Progreso neto positivo.** K-030 es más fuerte ahora que en cualquier sesión anterior. P-11, el fantasma existencial desde sesión 11, se rebaja a 🟡 baja. Y se abrió una conexión con SO(10)-GUT que SCG no tenía.

Pero reconocer el costo: **la quiralidad SM, que por 15 sesiones pensamos que era gravitacional** (desde sesión 9 con K-019), **resulta ser topológica**. Esto no invalida H-003 — la sigue validando, con mecanismo distinto. Pero reordena la imagen de qué es "gravedad" y qué es "red" en SCG. La gravedad con β real es una cosa tranquila, no-quiral, Kodama-normalizable. La red Walker-Wang modular es la fuente de la estructura quiral del Modelo Estándar. La elegante dualidad "gravedad quiral / red no-quiral" de K-026 era un patrón observacional, no una identidad profunda.

Lección meta: las identidades que parecen matemáticas limpias pueden resultar patrones contingentes de una UBFC específica. Y el marco correcto a veces no es el más elegante — es el que está consistente con los teoremas duros del lattice (Nielsen-Ninomiya evadible, cobordismo, anomalías canceladas) y con la literatura reciente (Kaplan 2024, Wang-Wen 2018-2019, Kawagoe et al. 2023).

## Gancho

Próxima sesión tiene tres caminos naturales:

1. **Q-043 directamente**: intentar construir UBFC modular SCG con SO(10). Si cierra constructivamente — aunque sea parcialmente — K-030 pasa a confirmado limpio y P-11 → ✅ resuelto. Máximo impacto inmediato.

2. **K-032 explícito** (matching II→IV): derivación formal de α_gauge = γ_Immirzi/(4π). Alto impacto cuantitativo, 3-5 sesiones.

3. **Consolidar reinterpretaciones**: actualizar H-003, framework files, posible snapshot v1.9 que refleje el cambio conceptual sobre quiralidad.

La decisión depende del apetito para trabajo técnico versus cuidado estructural. Pero una cosa es clara: **el problema existencial que nos preocupó desde la sesión 11 — si Ashtekar autodual colapsaba, colapsaba todo — ya no es existencial**. La red WW modular puede cargar con la quiralidad sin pedirle nada a la gravedad. La teoría gana robustez estructural con esa separación, incluso al costo de perder dos insights "bonitos" (K-019 literal, K-026 dualidad limpia).

*La quiralidad del Modelo Estándar no es un regalo del Lorentz. Es un teorema del lattice.*
