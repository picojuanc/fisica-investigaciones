# Investigación de una Teoría del Todo alternativa

Bitácora pública de una investigación en curso sobre física teórica fundamental, desarrollada por **Juan Pico** ([@picojuanc](https://github.com/picojuanc)) en colaboración con Claude (Anthropic) como asistente de razonamiento.

No es un paper. No es un tratado cerrado. Es el registro vivo de un programa exploratorio — con sus avances, sus resultados negativos, sus candidatos pendientes y sus callejones sin salida. Se publica con la expectativa de que exponer el proceso abiertamente es más útil que exponer solo conclusiones.

## De qué trata

El marco central — provisional — se llama **SCG (Stabilized Gravitational String)**. Parte de la gravedad cuántica en formulación autodual de Ashtekar, cuantizada sobre una red tipo Walker-Wang en 3+1D, y propone que de ahí emerge:

- La dimensionalidad del espacio-tiempo: un punto fijo auto-consistente (1 objeto, 3 espacio, 1 tiempo).
- El grupo gauge del Modelo Estándar: SU(3) × SU(2) × U(1), con la carga cuantizada en 1/3 y la violación de paridad sólo en SU(2) como consecuencias geométricas.
- El interior no-singular de los agujeros negros: una cuerda gravitacional plegada con escala d ~ √(r_s · ℓ_P).
- Una predicción falsable: ecos de ondas gravitacionales con un retraso específico (≈ ½ del predicho por fuzzballs).

Todo desde solo dos axiomas activos (corte Planck y transición de fase gravitacional).

## Estado al día de hoy

- **21 sesiones documentadas** (desde 2026-04-15).
- **9 derivaciones** formales (D-001 a D-009).
- **29 insights confirmados** (K-001 a K-027, K-029, K-031) + 3 candidatos pendientes de cuantificación (K-028, K-030, K-032).
- **3 hipótesis activas** (H-001, H-002, H-003).
- **Bosquejo de Lagrangiana** estructuralmente completo: 3/5 sub-tareas confirmadas + 2/5 parciales.
- **Sin eslabones rojos** en la cadena lógica.

El estado consolidado más reciente está en [`journal/2026-04-21_snapshot_v1.7.md`](journal/2026-04-21_snapshot_v1.7.md) — documento autocontenido, cubre sesiones 0–19.

## Cómo navegar

| Carpeta | Qué hay |
|---|---|
| [`CLAUDE.md`](CLAUDE.md) | Protocolo, rol y reglas de auto-mejoramiento de la investigación. |
| [`memory/`](memory/) | Memoria a largo plazo. Empezar por `MEMORY_INDEX.md`. |
| [`framework/`](framework/) | Axiomas y ontología del marco. |
| [`hypotheses/active/`](hypotheses/active/) | Las tres hipótesis vivas (H-001, H-002, H-003). |
| [`logic/derivations/`](logic/derivations/) | Derivaciones formales D-001 a D-009. |
| [`logic/refutations/`](logic/refutations/) | Debilidades identificadas con honestidad. |
| [`experiments/thought_experiments/`](experiments/thought_experiments/) | Experimentos mentales E-001 a E-009. |
| [`experiments/simulations/`](experiments/simulations/) | Código de simulaciones numéricas. |
| [`notes/`](notes/) | Análisis específicos por pregunta (Q-XXX) o tarea. |
| [`journal/`](journal/) | Snapshots consolidados + reportes narrativos por sesión. |
| [`literature/`](literature/) | Referencias y comparación con marcos existentes. |

## Punto de entrada recomendado

Si tienes 5 minutos: [`journal/reportes/01_el_punto_de_partida.md`](journal/reportes/01_el_punto_de_partida.md).

Si tienes 30 minutos: [`journal/2026-04-21_snapshot_v1.7.md`](journal/2026-04-21_snapshot_v1.7.md).

Si quieres seguir la historia completa: los 21 reportes narrativos en [`journal/reportes/`](journal/reportes/), en orden.

## Honestidad epistémica

Varios de los resultados principales son **candidatos**, no confirmados. El marco tiene premisas fuertes (la conexión autodual de Ashtekar es una de ellas). Ninguna constante numérica del Modelo Estándar se predice cuantitativamente aún. Hay tensiones abiertas (flujo RG entre regímenes, consistencia cuántica de Polyakov 4D, etc.).

La investigación distingue explícitamente entre: lo que se **deriva**, lo que se **argumenta**, lo que se **propone** y lo que queda **pendiente**. Cada documento marca el nivel de confianza de sus afirmaciones.

## Sobre la colaboración con IA

Las sesiones se desarrollaron usando Claude (Anthropic) como asistente. El rol de la IA es ayudar a estructurar derivaciones, revisar la literatura, y mantener coherencia interna. Las decisiones estratégicas, los saltos imaginativos y las direcciones de investigación los elige el humano. El diseño metodológico (protocolos, reglas de auto-mejoramiento, estructura de memoria) está descrito en `CLAUDE.md`.

## Contacto

Juan Pico — picojuanc@gmail.com — [@picojuanc](https://github.com/picojuanc)

## Licencia

Por definir. Provisionalmente: todo el contenido se publica con la expectativa de que pueda ser leído, citado y discutido libremente; la reutilización sustancial requiere permiso mientras se clarifica la licencia.
