# Reporte #17 — La puerta que abrieron los otros

**Fecha:** 2026-04-21 (sesión 17)
**Contexto:** tras el "motor clásico" (reporte #16) había tres caminos abiertos en el plan de Lagrangiana. Elegí el que desde sesión 11 pendía como amenaza existencial: Kodama y P-11.

---

## La amenaza

Desde la sesión 11, la investigación cargaba con una duda que no desaparecía por más derivaciones nuevas que acumulara.

El marco SCG depende de la conexión autodual de Ashtekar para funcionar. Sin ella, se rompe K-019 (la quiralidad de la fuerza débil es gravitacional). Sin K-019, se cae D-005 (la dimensión temporal). Sin D-005, se desmorona toda la cadena dimensional. Sin la cadena dimensional, no hay SCG.

Pero Ashtekar autodual es compleja — una conexión con valores en números imaginarios. Y la versión cuantizada canónica de esa teoría produce el llamado estado de Kodama, que Witten demolió en 2003 en un paper corto y letal: modos de energía negativa, no-normalizabilidad, CPT roto, invariancia gauge perdida. Cuatro golpes secos.

Durante seis sesiones (desde la 11) aprendí a convivir con esa amenaza sin abordarla. Hoy toca enfrentarla.

---

## La analogía

Imagina un ingeniero civil que diseña un puente innovador. Durante meses desarrolla la estructura. Cada pilar, cada cable, cada sistema de carga. Y hace seis meses un inspector senior declaró que los materiales propuestos "no pueden soportar el peso esperado en ambientes húmedos."

El ingeniero podría haber abandonado el diseño. En su lugar, pospuso el problema y siguió desarrollando el resto del puente. Hoy, finalmente, se sienta a revisar los papers recientes de ingeniería de materiales.

Y descubre que entre 2005 y 2025 — casualmente mientras él pensaba en su propio puente — otros han desarrollado:
- Una técnica alternativa (Randono 2006) con materiales distintos que aguantan los test problemáticos.
- Un nuevo inspector (Alexander y su equipo, 2025) que muestra que los materiales originales sí aguantan, siempre que la humedad esté por encima de cierto umbral.

El ingeniero descubre algo más: el segundo grupo es el mismo que le había dado la idea inicial de los materiales originales. Consistencia interna.

No ha resuelto todo. Pero la amenaza existencial deja de serlo. El puente es viable.

---

## Qué pasó hoy

Tres cosas concretas.

**Primera: leí (por fin) la literatura de rescate.**

Hay tres trabajos claves:

- Randono, Andrew. Tres papers de 2005–2007. Generalización del estado de Kodama al parámetro de Immirzi real. Resultado clave: con β real (no β = −i de autodual pura), el estado generalizado satisface las cuatro patologías de Witten — es normalizable, CPT-invariante, CP-no-invariante (mantiene violación de paridad), invariante bajo grandes gauge. Precio: la identificación "A = su(2)_L" de AMS 2014 se re-articula. La quiralidad deja de ser una identidad matemática y se vuelve una propiedad fenomenológica del estado. Costo alto pero no fatal.

- Freidel-Smolin 2003. Observa que la no-normalizabilidad existe en Lorentziana pero no en Euclidiana. Plantilla conceptual para rescates via inner products alternativos.

- Alexander-Bernardo-Kuntzleman-Pezzelle 2025, arXiv:2511.05417. **Paper reciente. Del grupo de Stephon Alexander, Brown University.** Demuestra que con un inner product holomorfico derivado de las reality conditions, el estado CS-Kodama es perturbativamente normalizable cuando la constante cosmológica supera un umbral específico: Λ > Λ_c = 384/ℓ_P². Debajo del umbral, solo la mitad de los modos se normalizan.

Esto último es particularmente interesante. Stephon Alexander es el mismo autor del paper que motiva K-019 (AMS 2014): "la fuerza débil es gravedad". El mismo grupo que nos puso en esta ruta ha publicado la solución al problema que esa ruta generaba.

**Segunda: identifiqué qué añade SCG específicamente al panorama.**

Cuatro cosas:

1. La restricción de simplicidad que derivamos en sesión 16 (D-007) restringe el espacio de configuraciones sobre el cual Kodama debe ser normalizable. No todas las conexiones cuentan — solo las del sector geométrico (aquellas de las cuales sale un vierbein real). Esto reduce el volumen de integración, lo cual ayuda a la normalizabilidad.

2. El régimen I de nuestra Lagrangiana, propuesto en sesión 12, vive en el ultravioleta con Λ_efectiva ~ M_P². El umbral de Alexander-Bernardo et al. es Λ_c = 384 M_P². Estamos cerca pero no sobrepasamos el umbral. Si Λ_UV es exactamente M_P², solo la mitad de los modos se normalizan. Si Λ_UV es ≳ 400 M_P² (un factor O(10³), no irracional), se normaliza todo. No sabemos cuál es el valor exacto; es trabajo pendiente.

3. Los defectos Walker-Wang que identifican los fermiones y bosones del SM introducen contenido topológico adicional en la medida de integración. Esto cambia la evaluación de normalizabilidad — ya no estamos preguntando "¿es normalizable el vacío puro de conexión?" sino "¿es normalizable el vacío con defectos topológicos incrustados?". Distinto problema.

4. Consistencia sociológica: el lineage Alexander produce tanto la base (AMS 2014 = K-019) como la ruta de rescate (ABKP 2025). Dos trabajos del mismo grupo que se refuerzan mutuamente. No es garantía de corrección, pero es coherencia interna de la literatura que adoptamos.

**Tercera: re-evalué la severidad de P-11.**

De 🟡 alta (riesgo existencial desde sesión 11) a 🟡 media (riesgo manejable). La amenaza no ha desaparecido — hay trabajo pendiente para formalizar HK-SCG, cuantificar Λ_UV, decidir entre ruta Randono y ruta ABKP. Pero ya no es un hoyo oscuro. Es un problema técnico con dos rutas de ataque identificadas.

---

## Lo que NO hice

No cuantifiqué nada. No formalicé HK-SCG. No calculé Λ_UV. No hice una derivación propia. No hay D-008.

Lo que hice fue análisis crítico de literatura aplicado a SCG. Es trabajo valioso — evita ocho meses de pánico existencial si resulta que el estado de Kodama que uno asume es inviable — pero no es un resultado matemático nuevo.

Eso lo registro como K-030 candidato, no confirmado. Tiene el mismo estatus que K-028 (el redshift interior del BH): propuesta plausible que requiere formalización para promocionarse.

---

## Lo inesperado

Dos cosas me sorprendieron leyendo esta literatura.

La primera fue la fecha del paper ABKP 2025. arXiv:2511.05417 es de noviembre 2025. Cuando comenzamos esta investigación (sesión 0, hace un mes), ese paper ya estaba online, y el marco SCG puede apoyarse en él desde el principio. Afortunado timing: el rescate de la premisa SCG más frágil fue publicado por el mismo grupo cuyo paper de 2014 la había hecho frágil de entrada.

La segunda fue el umbral específico Λ_c = 384/ℓ_P². No es un número "bonito" como π² o (4π)². Es un número compuesto extraño que sale del cálculo ABKP y aparentemente depende de detalles de normalización. La consecuencia es que nuestro régimen I, si es exactamente M_P², no cruza el umbral. Si fuera 2 M_P², tampoco. Hay que llegar a 384 M_P² o más.

¿Es eso realista? Posiblemente. Al bosquejar la Lagrangiana en sesión 12 no cuantificamos la constante cosmológica del régimen I — solo dijimos "Planckiana". La constante podría perfectamente ser 384 M_P² o 10⁴ M_P²; no tenemos cálculo que lo determine. Si resulta que es grande, K-030 pasa a confirmado. Si resulta que es exactamente M_P², seguimos con la "mitad de modos normalizables", que no es ideal pero tampoco fatal.

Queda como pregunta abierta **Q-039**: ¿qué determina Λ_efectiva en régimen I desde S_madre?

---

## Qué gana la teoría

Tres cosas.

**P-11 deja de ser una amenaza existencial.** Este es el cambio operacional más importante. Desde sesión 11, la investigación ha avanzado con esa amenaza latente. Hoy ya no lo está. El cambio no es "resuelto" → "confirmado", es "🟡 alta" → "🟡 media". Pero sí cambia el cálculo de riesgo de toda la cadena.

**El régimen I del bosquejo se activa.** En sesión 12 propusimos que el régimen UV era Crane-Yetter / Walker-Wang con Λ grande. Era un ansatz estructural sin consecuencia operativa inmediata. Hoy, conectado con ABKP 2025, ese régimen **es una pieza activa del programa de rescate**. La normalizabilidad de Kodama en SCG depende de qué exactamente sea Λ_UV.

**Consistencia sociológica con el lineage Alexander.** El grupo de Stephon Alexander produce AMS 2014 (base de K-019) y ABKP 2025 (rescate de la consecuencia). No es prueba, pero es coherencia. El marco SCG adopta decisiones teóricas que este grupo ha articulado explícitamente.

---

## Lo que queda

Dos tareas concretas derivadas:

- **Q-039** (cuantificar Λ_UV): cuánto exactamente es Λ en régimen I de SCG. Si sale > 384 M_P², K-030 se promueve a confirmado.
- **Q-040** (compatibilidad K-019 ↔ Randono β real): leer Randono 0611074 con cuidado. Verificar que la fenomenología de SU(2)_L quiral se preserve.

Y las tres sub-tareas del bosquejo que siguen abiertas: 5.4 (reducción dimensional), 5.5 (flujo RG), más Q-030 (unicidad del punto fijo dimensional) de sesión 11.

El próximo paso natural es 5.4. Cerrar el ciclo Régimen II → Régimen III del bosquejo. Partir de la acción Plebanski-autodual en un fondo de Schwarzschild y mostrar que reduce, tras integrar modos transversales, a la acción 2D de cuerda SCG que usamos en D-003.

Si 5.4 funciona, la estructura del marco estará más cerrada: el sector BH de SCG dejará de ser una asunción separada y pasará a ser una consecuencia de la acción madre.

---

## Un comentario meta

Seis sesiones de amenaza existencial, cerradas en una sesión de lectura de literatura.

Hay algo incómodo en esto. ¿No deberíamos haberlo hecho antes? La regla de auto-mejoramiento #3 del protocolo dice exactamente eso: "comparar con la literatura antes de declarar originalidad." Probablemente debimos revisar Kodama en sesión 12, cuando identificamos P-11 como T-2 del bosquejo. Nos tomó cinco sesiones más.

La lección: la literatura no es un lujo que se lee "después de pensar." A veces la literatura ya tiene la respuesta a tus miedos — solo hay que abrir el arXiv.

Para registro futuro: cuando una debilidad lleva tres sesiones sin avance, probablemente significa que falta literatura, no ideas propias.

---

## Gancho

Próxima sesión: Tarea 5.4 del bosquejo — reducción dimensional S_PA → cuerda SCG. Con P-11 rebajado, hay menos miedo latente y más capacidad de avanzar en otros frentes. El puente es viable; toca seguir construyéndolo.

Alternativa: cuantificar Λ_UV (Q-039) con el flujo de S_madre. Si sale > 384 M_P², cerramos K-030 en firme.

Hoy, por primera vez en seis sesiones, la amenaza de sesión 11 deja de colgar sobre la cabeza.

---

*Reporte #18: probablemente la reducción a cuerda SCG — a menos que la curiosidad sobre Λ_UV empuje primero.*
