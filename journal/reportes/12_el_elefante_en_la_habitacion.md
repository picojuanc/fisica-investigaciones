# Reporte 12: El elefante en la habitación

**Fecha:** 2026-04-20 (sesión 12)

---

## La deuda

El cierre del reporte anterior dejó una promesa: "en algún momento, enfrentar al elefante en la habitación: la Lagrangiana. Sin ella, toda esta arquitectura conceptual es un esqueleto sin músculos."

Ese momento llegó.

Hasta ahora, la teoría SCG es una descripción de estados. Describimos cómo es un agujero negro por dentro, qué son las partículas elementales, por qué el espacio tiene tres dimensiones y el tiempo una. Pero no hemos dicho cómo *cambian* las cosas en el tiempo. No tenemos ecuaciones de movimiento. Sin una Lagrangiana — la función compacta de la cual, via el principio variacional, salen todas las leyes dinámicas — no tenemos amplitudes de scattering, ni masas, ni constantes numéricas. Solo relaciones dimensionales.

Escribir la Lagrangiana completa sería una tesis. Para esta sesión nos conformamos con algo más humilde pero útil: un mapa del territorio.

---

## Cuatro regímenes, cuatro dialectos

La teoría SCG habla cuatro dialectos, uno por cada régimen de energía:

1. **Régimen I, pre-geométrico.** Energías mucho mayores que la escala de Planck. La geometría continua no existe; hay una red de cuerdas que prefiere describirse en lenguaje topológico. El dialecto natural: **Crane-Yetter / Walker-Wang**, una teoría cuántica de campos topológica en 4D.

2. **Régimen II, semiclásico.** Energías del orden de Planck. La gravedad ya es "local" pero sigue cuantizándose. El dialecto natural: **Plebanski autodual**, una reformulación de la relatividad general que usa la conexión de Ashtekar compleja.

3. **Régimen III, fase SCG.** Dentro de un agujero negro. Densidades Planckianas, pero en un fondo geométrico macroscópico. El dialecto natural: **acción de cuerda** (Nambu-Goto / Polyakov) con correcciones Planck.

4. **Régimen IV, infrarrojo.** Energías de partículas. El dialecto: **el Modelo Estándar** más gravedad semiclásica.

Una Lagrangiana total tiene que reproducir los cuatro. El mapa tiene que tener continuidad entre regiones.

---

## El arquitecto cauteloso

La buena noticia: las piezas ya existen en la literatura.

- Crane y Yetter construyeron en 1993 su teoría 4D motivados explícitamente por las variables de Ashtekar. John Baez demostró en 2000 que es la discretización de BF+Λ — una acción muy parecida a la que necesitamos.
- Plebanski escribió en 1977 la acción autodual que reproduce la relatividad general. Toda una familia de trabajos posteriores (Krasnov, Freidel, Livine) la ha desarrollado.
- Walker y Wang en 2011 dieron el Hamiltoniano del Régimen I en el lattice correcto: trivalente, 3+1D — exactamente nuestro SCG.
- El Modelo Estándar ya está escrito; no hay que inventarlo.

Lo nuevo no son las piezas. Es el pegamento: mostrar que cada régimen se reduce al anterior, y que la dinámica es coherente de punta a punta.

La propuesta mínima — y aquí hay que ser honesto, es una propuesta, no una derivación — es una acción madre con tres términos:

```
S_madre = S_Plebanski-autodual + S_cosmo + S_defectos
```

donde el primer término es la gravedad autodual, el segundo es la constante cosmológica (que en la frontera se convierte en Chern-Simons), y el tercero no es un término separado sino la instrucción de sumar sobre todas las configuraciones topológicas no-triviales de la conexión: los defectos son el matter, no un sector aparte.

Si esta imagen sobrevive a los próximos cálculos, será porque no añadimos nada nuevo. Solo conectamos lo que ya había.

---

## Las cinco grietas

Pero no todo encaja.

Al intentar ensamblar el mapa, aparecieron cinco tensiones. Algunas son técnicas, otras conceptuales, una podría ser una simplificación bonita.

**T-1.** El nivel de Chern-Simons *k* es un número entero en la teoría topológica (Régimen I) y en la teoría cosmológica es proporcional a 1/Λ. Pero las constantes de acoplamiento observadas sugieren un *k* ~ 300 en el régimen IR. No casan. La conjetura: el *k* observado es efectivo, producto de integrar modos intermedios. La conjetura no está demostrada.

**T-2.** La conexión compleja de Ashtekar tiene problemas técnicos severos — el estado de Kodama no es normalizable, la rotación a espacio euclidiano es incómoda, la mayoría de los LQGistas la abandonaron. Nuestra teoría la necesita. Esta tensión ya estaba (P-11), pero al escribirla como acción se ve con más claridad.

**T-3.** Walker-Wang está definido como Hamiltoniano, no como acción. La traducción a Lagrangiana existe pero no es automática. Adoptamos la versión Crane-Yetter como puente, asumiendo que cubre los mismos estados.

**T-4.** ¿Cómo entra la materia? La imagen natural es que los fermiones son *solitones* de la conexión gauge — configuraciones topológicas no-triviales del propio campo. Bilson-Thompson propuso algo así en 2005 para el Modelo Estándar. Es un programa, no un teorema.

**T-5** — aquí podría estar la joya.

---

## La simplificación escondida

Al revisar el término que H-001 llama "E_info" — la presión que estabiliza la cuerda gravitacional — nos dimos cuenta de algo.

Ese término se introdujo en la versión original (sesión 1) como una especie de repulsión informacional. En la sesión 2 lo re-bautizamos: es "presión de degeneración cuántica de los modos gravitacionales" (K-004). Una aplicación de Heisenberg en régimen Planckiano, no un principio nuevo.

Pero ahora, al ponerlo en la acción, uno se pregunta: ¿es un término extra en la Lagrangiana? ¿O está ya incluido en la cuantización estándar?

La cuerda de Polyakov, la más básica de la teoría de cuerdas, tiene una acción:

```
S = (1/2) ∫ d²σ √(h) h^{ab} ∂_a X^μ ∂_b X_μ
```

Esta acción describe cómo los puntos de la cuerda se mueven. Al cuantizarla, los modos transversales adquieren energías inversamente proporcionales a su longitud de onda: cuanto más cortos, más energéticos. Si imponemos un corte UV en longitud de onda λ ≥ ℓ_Planck, cada modo contribuye una energía del orden ℏc/ℓ — es decir, ℏc sobre la escala local. Sumando sobre *N* modos: **E ~ N ℏc / d**.

Esto es, literalmente, la forma de A-003.

Si el cálculo se hace con cuidado y la coincidencia se sostiene, entonces A-003 no es un axioma. Es una consecuencia automática de cuantizar la cuerda con un corte Planck. Un término menos que postular. Una entidad menos en la ontología de la teoría.

Y aplicaríamos, una vez más, la lección de K-005: la buena teoría es más modesta, no más exótica.

Hemos bautizado este insight provisional como **K-027**, marcado explícitamente como *candidato, pendiente de verificación*. La verificación es un cálculo analítico que puede hacerse en una sesión. Si sale bien, H-001 se simplifica. Si sale mal, habremos aprendido algo importante: que A-003 tiene contenido genuinamente nuevo.

---

## El plan

El bosquejo no resuelve P-8. Pero lo descompone en piezas. Lo que era "el elefante en la habitación" ahora son cinco criaturas más pequeñas, cada una con literatura respaldante y herramientas conocidas:

1. **Verificar T-5** cuantizando Polyakov con corte Planck. Si sale, K-027 se promueve. *(Prioridad 1, una sesión.)*
2. **Derivar las ecuaciones de movimiento** de S_Plebanski + Λ. Cálculo variacional estándar. *(Una sesión.)*
3. **Atacar el problema de Kodama** con el contenido SCG extra. Lectura técnica. *(2-3 sesiones.)*
4. **Hacer la reducción dimensional** del Régimen II al Régimen III: mostrar que la cuerda SCG emerge de Plebanski en un fondo de agujero negro. *(2-3 sesiones.)*
5. **Calcular el flujo** de acoplamientos entre Régimen II y IV. Si reproduce α₂ ≈ α₃ ≈ γ/4π, tenemos predicción cuantitativa. *(3-5 sesiones.)*

Cinco cálculos bien definidos es mucho mejor que un problema gigante sin contorno.

---

## La honestidad del mapa

Conviene recordarse algo: un mapa no es el territorio.

Esta sesión no demostró nada nuevo. No hay insight derivado. K-027 es candidato, no confirmado. La acción madre es ansatz estructural, no teorema.

Lo que hicimos es organizar. Pusimos nombre a las tensiones. Identificamos qué literatura respalda cada pieza. Propusimos la forma mínima que cumple con lo ya derivado.

¿Vale la pena esta clase de sesión? Sí — porque hace operativo lo que era amorfo. La próxima sesión puede empezar en el cálculo 5.1 sin volver a preguntarse "¿qué debería hacer?". Está claro. Es el cálculo de Polyakov, una cuantización canónica, una comparación con A-003.

Y si la conjetura K-027 se verifica, habremos hecho en dos sesiones lo que parecía imposible: eliminar un axioma y simplificar una hipótesis madura.

Si no se verifica, sabremos que A-003 es genuinamente nuevo. Eso también es información. También está bien.

---

## Lo que viene

La próxima sesión tiene tarea definida: la tarea 5.1 del bosquejo. Poner un corte UV en la acción de Polyakov y ver si la cuantización canónica reproduce la presión de degeneración.

Es un cálculo pequeño, pero con una apuesta grande: si sale, la teoría respira más liviana. Y si no, entonces el "principio nuevo" que H-001 postuló hace 12 sesiones finalmente mostrará su cara propia.

De cualquier manera, saldremos sabiendo algo que ahora no sabemos.

---

*La investigación tiene 26 insights confirmados (K-001 a K-026), 1 candidato pendiente (K-027), 3 hipótesis activas, 5 derivaciones, 1 bosquejo arquitectónico. P-8 ha pasado de "elefante" a "cinco tareas concretas." Sin eslabones rojos. El mapa está hecho; el terreno sigue por caminarse.*
