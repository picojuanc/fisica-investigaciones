# Reporte #16 — El motor clásico

**Fecha:** 2026-04-21 (sesión 16)
**Contexto:** tras el "peso de la luz" (reporte #15) quedó abierto un menú de caminos. Elegimos el más útil a corto plazo: confirmar que la acción propuesta en sesión 12 funciona como debería. No un descubrimiento — un chequeo.

---

## Qué veníamos acumulando

Desde la sesión 12 cargábamos con una promesa: un bosquejo de la Lagrangiana SCG. El "S_madre" candidato tenía tres ingredientes:

1. **S_Plebanski-autodual.** El núcleo gravitacional — la acción de Plebanski de 1977, pero en su variante autodual (compleja), que es la que Ashtekar hizo famosa a partir de 1986.
2. **S_cosmo.** El término de constante cosmológica, pero escrito de forma que, al llevarlo a una frontera, reproduce Chern-Simons.
3. **S_defectos.** No un término separado, sino una instrucción: "suma sobre todas las configuraciones topológicamente no-triviales de la conexión". Ahí vivirían los fermiones y los bosones del Modelo Estándar.

El bosquejo propuso cinco cálculos concretos para convertir esa arquitectura en teoría de verdad. La sesión 13 resolvió el primero (reinterpretar la "presión de información" como el efecto Casimir en la cuerda). Quedaban cuatro.

Esta sesión aborda el segundo.

---

## La pregunta de hoy

**¿Qué sale cuando uno deja que la acción vibre?**

Es decir: si tomo S = S_PA + S_cosmo y la hago variar respecto a cada uno de sus tres campos (Σ la "superficie autodual", A la conexión, ψ el multiplicador), ¿qué ecuaciones recupero? ¿Son las correctas? ¿Son consistentes con todo lo que he construido en sesiones anteriores?

Esta pregunta es menos glamurosa que "¿por qué hay tres dimensiones?" o "¿puede un agujero negro no tener singularidad?". No tiene titular dramático. Pero es exactamente lo que hay que hacer en este punto: verificar que los cimientos aguanten.

---

## La analogía

Imagínate a un ingeniero que ha diseñado un coche pieza por pieza durante meses. El motor lo compró a un proveedor conocido (Plebanski 1977). La carrocería la encargó a otro (Crane-Yetter 1993). La caja de cambios la adaptó de un modelo existente (Walker-Wang 2011). Nunca ha armado el conjunto.

Esta sesión fue enchufar las piezas y girar la llave. No fabricar nada nuevo — solo confirmar que el coche arranca.

---

## Qué hicimos

Las variaciones son rutina para un relativista. En nuestras convenciones:

- **Variando ψ** (un multiplicador de Lagrange): la ecuación que sale es la *restricción de simplicidad*. Es la condición matemática de que la "superficie" Σ venga de un vierbein real — es decir, que describa una geometría honesta y no un objeto matemático espurio. Seleccionamos ese sector; es la convención física de quien quiere recuperar gravedad usual.

- **Variando Σ**: sale la ecuación de curvatura. La curvatura autodual F(A) es proporcional a Σ, con un coeficiente que incluye la constante cosmológica y una parte libre. Esa parte libre, al ponerla on-shell, **es el tensor de Weyl autodual** — los modos gravitacionales radiativos de la teoría. La parte proporcional da R = 4Λ. Vacío con constante cosmológica.

- **Variando A**: sale d_A Σ = 0 — la ecuación de "torsión autodual nula". Eso fuerza que la conexión A sea la parte autodual de la conexión de spin del vierbein. Es decir: **A es literalmente la conexión de Ashtekar**, por definición. No como un postulado importado — como consecuencia de las ecuaciones de Euler-Lagrange.

Sumando todo: on-shell, la acción equivale a Einstein-Hilbert con Λ. La parte imaginaria que aparece en el camino es una clase topológica (un invariante, no dinámica), y se descarta como normalmente se hace.

---

## Qué gana la teoría con esto

Dos cosas concretas:

**Primera: reconfirma K-019 desde dentro.**
Hasta ahora, la identificación "conexión de Ashtekar = su(2)_L de la fuerza débil" venía importada de Alexander, Marciano y Smolin (2014). Una derivación externa. Esta sesión deriva la misma identificación sin usar AMS — solo variando la acción. El resultado: la ecuación δA = 0 fuerza A = ω_+, y ω_+ = su(2)_L por la estructura del grupo de Lorentz complejificado. K-019 deja de ser "importado" y pasa a ser "derivado clásicamente". Un eslabón más firme.

**Segunda: el núcleo del bosquejo no choca con nada.**
El miedo legítimo de cualquier programa Lagrangiana ambicioso es que, cuando finalmente escribas las ecuaciones, descubras que no reproducen GR, o que la conexión resultante no es la que necesitas, o que el término cosmológico entra con signo equivocado. Ninguno de esos miedos se materializó. El núcleo gravitacional de S_madre reproduce GR + Λ limpiamente, con la conexión correcta y la frontera correcta (Chern-Simons con nivel k = 2π/(κΛ), el clásico resultado de Baez 2000).

---

## Qué NO gana la teoría

**No gana ninguna predicción cuantitativa nueva.**

Esta sesión no predice masas, no explica ángulos de mezcla, no resuelve tensiones. Las cuatro tensiones del bosquejo de sesión 12 siguen igual de abiertas:

- **T-1** (k topológico vs k dinámico): si Baez dice que k = 2π/(κΛ), y Λ observado da k ~ 10¹²², pero la fenomenología del Modelo Estándar quiere k ~ 300, hay un agujero monumental entre escalas. No se toca aquí.
- **T-2** (P-11, la conexión compleja de Ashtekar): los problemas técnicos de la formulación siguen. Kodama no es normalizable. Witten 2003 sigue sin responder.
- **T-3** (cómo se conecta esto al lattice Walker-Wang): la equivalencia continua se usa a través de Baez 2000; la demostración constructiva para SCG sigue sin construirse.
- **T-4** (los fermiones como defectos de A): programa a la Bilson-Thompson, no teorema.

Y, por supuesto, cuantización. Nada de eso se aborda aquí.

---

## Honestidad: lo que esta sesión es y lo que no es

No es un hallazgo. El teorema "S_Plebanski + Λ autodual ≡ GR + Λ autodual" está en la literatura desde 1977. Lo que hicimos fue reproducirlo con las convenciones que usa nuestro marco y verificar que no colisiona con ningún resultado previo de SCG.

Esta clase de trabajo se siente a veces como "hacer los deberes" — sin la emoción de sesiones como la #11 (el muro dimensional) o la #13 (un axioma menos). Pero es el trabajo que evita que más adelante, cuando intentemos derivar algo genuinamente nuevo, nos demos cuenta de que lo habíamos construido sobre cimientos que no aguantaban.

Lo registramos como **K-029**, un insight confirmatorio. No de los que se anuncian; de los que permiten que los demás se anuncien luego.

---

## Qué queda

Tres sub-tareas del bosquejo por completar:

- **5.3 — El estado de Kodama y P-11.** Ahora que tenemos las ecuaciones clásicas, podemos escribir el estado Ψ_K = exp(i·S_CS/ℏ) y analizar con precisión por qué Witten 2003 lo declaró patológico. Lo interesante — y lo que justificaría dedicar 2-3 sesiones — es ver si el contenido adicional de SCG (la restricción de simplicidad; los defectos Walker-Wang) permite una versión no-patológica. Es el ataque directo a la debilidad existencial P-11. Si tiene éxito, el riesgo más grande del marco SCG se reduce sustancialmente.
- **5.4 — Bajar al BH.** Tomar S_PA en un fondo de Schwarzschild, hacer un ansatz con simetría axial y densidad saturada, integrar transversalmente, y ver si se recupera la acción de cuerda SCG del sector BH. Si funciona, el ciclo Régimen II → Régimen III queda cerrado, y D-003 (que dio la escala √(r_s·ℓ_P)) tendría derivación desde la acción madre.
- **5.5 — El flujo RG.** El más ambicioso. Integrar modos entre Régimen II y Régimen IV para ver si se recupera α₂ ≈ α₃ estructuralmente. Esto sería la primera predicción cuantitativa de una constante del Modelo Estándar desde SCG. Tres a cinco sesiones. La recompensa, enorme.

Y un candidato secundario: **Q-030**, la unicidad formal del punto fijo dimensional (1, 3, 1). Pendiente desde sesión 11. Un trabajo más formal, que cerraría la objeción epistémica de "¿y si la cadena dimensional es una circularidad disfrazada?".

---

## Gancho para la próxima

El próximo paso natural es 5.3. Hace falta ir a enfrentarse con Witten 2003: leer con cuidado qué exactamente falla en el estado de Kodama, y ver si el marco SCG ofrece alguna ruta que antes no existía. Es el escenario con más upside (resolver una debilidad existencial) y también con más riesgo metodológico (si no se resuelve, habremos gastado 2-3 sesiones en un callejón).

Alternativamente, 5.4 (bajar a la cuerda) cerraría la geometría del sector BH. Menos ambicioso, pero consolidante.

La elección depende del ánimo investigativo. Para mí la balanza se inclina a 5.3: la debilidad P-11 ha estado colgando desde sesión 11 sin ataque directo, y el bosquejo ya no tiene excusa para seguir postergándola. Pero es discutible.

Hoy, sin embargo, el motor arrancó. Eso ya es algo.

---

*Reporte #17: probablemente Kodama — o, si decidimos cautela, la reducción dimensional al BH.*
