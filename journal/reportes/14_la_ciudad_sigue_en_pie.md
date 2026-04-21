# Reporte 14: La ciudad sigue en pie

**Fecha:** 2026-04-20 (sesión 14)

---

## Después del terremoto

El reporte anterior describía un logro importante: A-003, que era un axioma desde la sesión 1, se convirtió en un teorema. Un axioma menos. La teoría se volvió más modesta.

Pero cuando se mueve una piedra de los cimientos, uno teme que se caiga algo arriba. H-001 tenía predicciones concretas construidas sobre A-003 — la más importante, la escala interior de los agujeros negros, **d ~ √(r_s ℓ_P)**, que para un BH estelar daba alrededor de un femtómetro. Esa predicción es una firma observable: si alguna vez alguien mide estructura en el interior de un BH, esa es la escala que H-001 predice.

Así que la pregunta para esta sesión era simple: ¿la predicción sobrevive? ¿Si quitamos A-003, la escala interior sigue siendo √(r_s ℓ_P)? ¿O se rompe?

---

## Leyendo las viejas notas

Lo sensato era empezar volviendo a leer la derivación original. D-003, escrita en la sesión 4, donde dedujimos por primera vez la escala √(r_s ℓ_P).

Y ahí nos encontramos con algo curioso.

Releyendo paso a paso, A-003 aparecía **una sola vez**, en el segundo paso de la derivación. Decía algo como: "Por A-003 (presión de degeneración) y la cota holográfica, la densidad máxima de información a lo largo de la cuerda es un bit por longitud de Planck."

Pero ese "por A-003" era, al mirarlo con lupa, ornamental. La frase continuaba: "y la cota holográfica". Y el resto de la derivación — la entropía de Bekenstein-Hawking del agujero negro, el plegado de la cuerda dentro del volumen — **no usaba A-003 en absoluto**.

En realidad, la densidad de un bit por Planck se seguía directamente de A-001 (la escala Planck es el corte) y de la estructura de red Walker-Wang (cada sitio de la red tiene un número finito de estados, y los sitios están separados por ℓ_P). A-003 entraba como "justificación rápida" — la razón de por qué los modos saturaban a escala Planck era, en la formulación v1.1, la presión de degeneración. Pero la *conclusión* (la densidad 1 bit/ℓ_P) se podía justificar igual sin A-003, apelando directamente a la red subyacente.

**Entonces K-007 nunca dependió esencialmente de A-003.** El axioma aparecía como adorno de un argumento que funcionaba igual sin él.

---

## Rederivación en una tarde

Con esa observación, la rederivación de K-007 es casi trivial. Cuatro ingredientes, todos independientes de A-003:

1. **Bekenstein-Hawking:** la entropía de un agujero negro es un cuarto del área del horizonte (en unidades de Planck al cuadrado).
2. **Walker-Wang:** la red cuántica del espacio-tiempo tiene un bit por celda de Planck.
3. **Saturación:** la entropía de la cuerda plegada iguala la del agujero negro (para que la transición sea unitaria).
4. **Plegado geométrico:** si la cuerda de longitud L llena el volumen del BH con sección d², entonces V = L·d².

De la saturación: L = (longitud) = (entropía × longitud de Planck) = 4π N² ℓ_P = π r_s²/ℓ_P.

Del plegado: d² = V/L = (4/3) r_s ℓ_P.

Resultado: **d = √((4/3) r_s ℓ_P) ~ √(r_s ℓ_P)**. Exactamente K-007. Sin modificar.

Para un BH estelar (r_s = 30 km), esto da d ≈ 0.7 fm. Escala nuclear. Sin cambio respecto a la sesión 4.

---

## Una grieta nueva

Pero lo interesante no terminó ahí.

Ahora que tenemos D-006 (el efecto Casimir como forma derivada de A-003), podíamos hacer una verificación adicional. Sustituyendo las escalas K-007 (la L y la d que acabamos de derivar) en la fórmula del Casimir — E_Casimir = 2π ℏc L / d² — ¿qué número sale?

Sale: E_Casimir ≈ 30 Mc².

Treinta veces la masa del BH.

Esto es extraño. La energía cuántica "almacenada en el interior" de un agujero negro, según nuestro cálculo, excede la masa total observable por un factor de treinta.

¿Es una contradicción?

Probablemente no. Hay al menos tres razones por las que este cálculo ingenuo puede dar un número mayor que Mc² sin violar nada físico:

**Primera:** la masa de un agujero negro medida desde fuera (la "masa ADM") ya incluye todas las correcciones gravitacionales. La energía "local" en el interior puede ser muy distinta de la masa observable.

**Segunda:** cerca del horizonte, el redshift gravitacional es enorme. Una energía local grande se ve muy reducida desde el infinito. Este efecto no lo incluye el cálculo de Polyakov en fondo plano.

**Tercera:** la cuerda interior no es libre; está confinada por su propia gravedad. La energía cinética cuántica (Casimir) debe balancearse con la energía potencial gravitacional. El balance completo puede dar una energía neta mucho menor.

Todas estas correcciones **requieren hacer el cálculo en una métrica curva**, no en el espacio plano de Polyakov estándar. Y eso no lo hemos hecho.

Así que declaramos una **tensión nueva**, T-6: el cálculo plano del Casimir excede Mc²; necesita fondo curvo. **Esto no invalida K-007** — K-007 es un resultado puramente geométrico-entrópico, no depende del cálculo energético. Pero sí abre una nueva pregunta para sesiones futuras: **Q-038**, cuál es el Casimir de Polyakov en un fondo de Schwarzschild interior.

---

## Lo que esta sesión enseña

Dos lecciones, una metodológica y una técnica.

**Metodológica:** cuando uno promueve un axioma a teorema, conviene regresar a todas las derivaciones que lo invocaban y revisar si la promoción cambia algo. En nuestro caso no cambió: el axioma no estaba "haciendo trabajo real" en la derivación. Esto **valida la reducción axiomática** — no perdimos nada al simplificar.

Pero podría haber sido al revés. Podríamos haber encontrado que K-007 sí dependía de A-003 de una manera sutil, y que al cambiar a D-006 el resultado se modificaba. En ese caso habríamos tenido que replantear. La sesión sirvió como due diligence.

**Técnica:** el cálculo del Casimir en fondo plano revela que el balance energético interior del BH requiere más cuidado del que le hemos dado hasta ahora. Hemos estado trabajando con escalas y con saturación holográfica, pero no con un cálculo energético consistente en métrica curva. La tensión T-6 es un recordatorio de que hay trabajo técnico pendiente — no en el dominio geométrico (que está bien) sino en el dinámico.

---

## Balance de la sesión

| Lo que se preserva | Lo que se cuestiona | Lo que queda |
|---|---|---|
| K-007 (d ~ √(r_s ℓ_P)) | Balance E_Casimir / Mc² (T-6) | Q-038 (Casimir en fondo curvo) |
| D-003 (rederivado limpio) | | |
| Predicciones ecos GW (E-006) | | |
| S_cuerda = S_BH saturada | | |

Tras la sesión: 27 insights (sin cambio), 6 derivaciones (D-003 clarificada a v1.2, sin nueva). Una tensión nueva (T-6), una pregunta nueva (Q-038). La teoría **no perdió predicciones**. La reducción axiomática de la sesión 13 pasó esta verificación.

---

## Lo que viene

Tres caminos naturales:

1. **Hacer un snapshot v1.6.** Los cambios de sesiones 12, 13, 14 son estructurales (bosquejo de Lagrangiana; A-003 → D-006; K-007 rederivada) y merecen consolidación. La documentación actual está dispersa.

2. **Atacar T-6 directamente** resolviendo Q-038: calcular el Casimir de Polyakov en un fondo de Schwarzschild interior. Esto también contestaría Q-037 (el prefactor exacto). Trabajo técnico de teoría de campos en espacio curvo.

3. **Seguir con el bosquejo de la Lagrangiana** — tarea 5.2, derivar las ecuaciones de movimiento de S_Plebanski + Λ. Cálculo variacional estándar.

En cualquiera de los tres casos, la teoría queda en mejor forma después de la sesión 14 que antes. K-007 sobrevivió a la prueba. La ciudad sigue en pie.

---

*La investigación tiene 27 insights, 3 hipótesis activas, 6 derivaciones (D-003 actualizada a v1.2), y — importante — **ninguna predicción perdida** en la reducción axiomática. T-6 nueva pero acotada, Q-038 abierta. Sin eslabones rojos.*
