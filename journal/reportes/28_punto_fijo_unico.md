# 28 — El punto fijo único: cómo (1, 3, 1) dejó de ser circular

*Sesión 39 — 2026-04-23 (con epílogo sesión 40)*

## Dónde estábamos

El reporte anterior (#27) cerró tres sesiones de TOV en el interior del agujero negro: sesión 36 setup honesto, sesión 37 refutación de K-028, sesión 38 cierre parcial de Q-045 al 83% con K-035 candidato (concentración holográfica). Tres sesiones técnicas seguidas, dos de ellas con resultados negativos disfrazados de refinamiento positivo.

Al final de sesión 38 había cuatro caminos abiertos para los 17% de masa ADM no cubiertos: extender al régimen $h > 1$ (tensión radial), shell delgada Israel, EOS no-Casimir, o aceptar el resultado parcial y girar a otro frente. Recomendé la última opción, con dos candidatos para girar: K-033 (programa SO(10)-GUT, 10+ sesiones) o **Q-030 (unicidad formal del punto fijo dimensional, 2-3 sesiones).**

Elegimos Q-030. Y resultó cerrarse en una sola sesión.

## La pregunta vieja

Q-030 nació en el stress-test de la sesión 11. Antes de eso, la cadena dimensional de SCG se presentaba como una derivación lineal:

```
A-003 (presión Casimir) → D-002 → D_objeto = 1
                        → H-002 → D_espacio = 3
                        → D-005 → D_tiempo = 1
```

El stress-test sesión 11 destapó la circularidad: D-002 *asume* que D_ambient = 3 para derivar D_objeto = 1; H-002 *asume* D_objeto = 1 para derivar D_ambient = 3; D-005 *asume* Ashtekar autodual (definido en (3+1)D) para derivar D_tiempo = 1. La cadena no era una cascada — era un **punto fijo auto-consistente**, lo que K-025 llamó "auto-consistencia" en aquella sesión.

Pero auto-consistencia no es lo mismo que unicidad. Ningún punto fijo es necesariamente único: pueden coexistir varios puntos fijos del mismo sistema. La pregunta seria es: **¿el sistema admite otra solución, o $(1, 3, 1)$ es la única?**

Análisis preliminar de la sesión 11 sugirió unicidad. Faltaba la demostración formal. Quedó como Q-030 abierta. Llevaba abierta 28 sesiones.

## La estrategia

La intuición que perseguí era simple: si la cadena tiene varios argumentos (D-002, H-002, D-005, K-019, D-004), quizás no todos son necesarios. Quizás uno o dos bastan para fijar $(1, 3, 1)$, y el resto son consistencias automáticas.

Si era así, podría reformular: en lugar de "argumento A + argumento B + ... → punto fijo", diría "argumentos mínimos A + B fijan el punto fijo, los demás lo confirman automáticamente". Eso es **estructuralmente más fuerte** que la presentación original — análogo a cómo en cuerdas no se dice "la dimensión emerge de Yamada+Polchinski+Witten+...", sino "la dimensión emerge de la cancelación de la anomalía de Weyl, único requisito".

## La demostración

Empecé enumerando todas las restricciones físicas que SCG impone sobre $(D_{obj}, D_{amb}, D_{tmp})$:

- **R1a** (D-002 §3): balance marginal de la energía de degeneración vs gravitatoria en N. Da $1 + 1/D_{obj} = 2 \Rightarrow D_{obj} = 1$.
- **R1b** (D-002 §4): balance marginal en L. Esto requiere análisis cuidadoso porque la gravedad en $D_{amb}$ dimensiones tiene la forma $E_{grav} \propto 1/L^{D_{amb}-2}$ para $D_{amb} \geq 3$ (logarítmica para $D_{amb}=2$, lineal para $D_{amb}=1$). Para que $E_{grav}$ y $E_{deg} \propto 1/L$ tengan el mismo exponente, **necesitamos $D_{amb} = 3$ exactamente**.
- **R2** (H-002): codim 2 para nudos no triviales. Da $D_{amb} - D_{obj} = 2$.
- **R3** (D-005 Arg A): Dynkin requiere $p + q = 4$ para que so(p,q)_C factorice como producto.
- **R4** (D-005 Arg B): Hodge $\star^2 = (-1)^q = -1$ para quiralidad compleja. Da $q$ impar.
- **R5** (D-004): trivalencia geométrica.
- **R6** (Asgeirsson 1936 + Tegmark 1997): well-posedness PDE. Da $D_{tmp} = 1$ (única).

Aplicando individualmente: R1a fija $D_{obj} = 1$. R6 fija $D_{tmp} = 1$. **R1b sola fija $D_{amb} = 3$ — sin necesidad de invocar codim 2, ni Dynkin, ni Hodge.**

El argumento de R1b lo hice con cuidado. La energía gravitacional binding en $D_{amb}$ dimensiones espaciales depende de la solución de Poisson en $D_{amb}$:

| $D_{amb}$ | $\Phi(r)$ | $E_{grav}$ con masa $L$ |
|---:|---|---|
| 1 | $\propto r$ | $\propto L$ — sistema crece sin límite |
| 2 | $\propto \ln r$ | $\propto \ln L$ — escala logarítmica |
| 3 | $\propto -1/r$ | $\propto -1/L$ — **balance perfecto con $E_{deg}$** |
| 4 | $\propto -1/r^2$ | $\propto -1/L^2$ — colapso a L pequeña, dispersión a L grande |
| ≥5 | $\propto -1/r^{D-2}$ | inestabilidad creciente |

**Solo en $D_{amb} = 3$** las dos energías tienen mismo exponente en L. En cualquier otra dimensión, hay una escala $L^*$ fija o el sistema es inestable. Pero SCG necesita acomodar BHs de cualquier tamaño cosmológico — desde Planck hasta supermasivos. **La marginalidad multiscala es físicamente requerida**, no opcional.

Entonces: el sistema mínimo {R1a, R1b, R6} fija $(1, 3, 1)$ unívocamente. Las restricciones R2-R5 son **consistencias automáticas**. Verifiqué que cada una individualmente NO es suficiente:
- R2 (codim 2) sola admite $(1, 3), (2, 4), (3, 5), \ldots$
- R3 (Dynkin) sola admite $(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)$.
- R4 (Hodge) sola admite $q = 1, 3, 5, \ldots$
- R5 (trivalencia) sola admite $D_{amb} \geq 2$.

Ninguna selecciona $(1, 3, 1)$ unívocamente. Solo el conjunto unificado lo hace. **La sobre-determinación es robustez estructural, no circularidad.**

## La analogía con cuerdas

Cuando terminé el análisis, el resultado tenía un sabor familiar. En teoría de cuerdas bosónicas, la dimensión $D = 26$ no se deriva de algo más fundamental: emerge como **única** dimensión donde la anomalía de Weyl cancela. En superstrings, $D = 10$ emerge de modular invariance. En M-teoría, $D = 11$ emerge porque el supergravity 11D es único.

Nadie llama esto "circularidad". La dimensionalidad emerge como **único punto fijo de consistencia interna**, y es una de las virtudes formales de cuerdas.

SCG sigue exactamente el mismo patrón. La diferencia es que SCG llega a $D = 4$ — la dimensión observada — sin requerir compactificaciones extras. El punto fijo (1, 3, 1) coincide con la realidad observacional **sin ajuste libre**.

Pasé K-025 de "auto-consistente" a "punto fijo único estructuralmente". Lo registré como **K-036 candidato** (la promoción a confirmado requiere extensiones a fractales, compactificaciones K-K y geometrías curvas; postpuesto). Escribí **D-012**: la doceava derivación formal del marco, una página corta sintética.

## Lo que esto significa

Tres cosas:

1. **La objeción de circularidad de la cadena dimensional queda cerrada.** No con "no hay circularidad" — eso sería deshonesto, sí la hay en sentido lógico — sino con "la circularidad es estructural y la cadena tiene una única solución, comparable con cómo $D=26$ es punto fijo único en cuerdas".

2. **H-002 y D-005 quedan reposicionadas.** Ya no son "premisas adicionales" sino **consecuencias** del punto fijo único. SCG es estructuralmente más modesta que parecía: necesita solo {R1a, R1b, R6} para la dimensionalidad; lo demás se sigue.

3. **Ningún axioma nuevo introducido.** D-012 es síntesis pura de elementos preexistentes. La novedad metodológica es identificar el sistema mínimo. K-005 aplicada ejemplarmente: la teoría es más modesta, no más exótica.

## Caveats honestos

Documenté tres limitaciones serias:

- **El argumento es sobre $\mathbb{Z}_{>0}^3$.** Si la naturaleza admite dimensiones fractales (Mandelbrot, geometría no-conmutativa), R1a y R1b siguen funcionando (las ecuaciones lineales tienen solución única en $\mathbb{R}_{>0}$ también), pero R6 requiere análisis adicional con PDEs de orden fraccionario.
- **No aborda "selección dinámica".** Que $(1, 3, 1)$ sea el único punto fijo no explica POR QUÉ la naturaleza está en este punto fijo y no vacía. Esto sigue como pregunta meta-filosófica abierta (Q-005, Q-001, Q-044).
- **R6 supone formulación lagrangiana estándar.** Formulaciones no-locales (Craig-Weinstein 2009) podrían admitir $D_{tmp} \geq 2$ con restricciones exóticas; improbables físicamente pero formalmente posibles.

Cada caveat es honesto. Ninguno destruye el resultado central.

## Epílogo (sesión 40)

Al día siguiente — tras tres sesiones consecutivas de cierre estructural (37 refutación, 38 cierre parcial, 39 cierre completo) — tomé una sesión documental para consolidar.

Escribí el **snapshot v2.2** (~750 líneas, autocontenido) cubriendo todo el estado de SCG sesiones 0-39: resumen, cadena de razonamiento global, ontología, axiomas, las 12 derivaciones formales, las 3 hipótesis, los 30 K confirmados + 3 candidatos, predicciones falsables, comparación con literatura (8 sub-secciones: cuerdas, LQG, CST, CDT, fuzzballs, holografía, gravastars, Wang-Wen), debilidades, preguntas abiertas, próximos pasos, apéndice con terminología.

Y, para hacer las simulaciones más comunicables, escribí `plot_simulations.py` — un generador de gráficas SVG manual (matplotlib no estaba disponible y ya no quería seguir leyendo números crudos en .dat). Salieron 6 gráficas:

- El atractor singular isothermal de sim002 ($y(x)$ numérico vs $1/(7x^2)$ analítico, en log-log).
- La saturación universal en compactness 3/7 de sim002.
- La comparación de compactness sim003 entre isotrópico y varios anisotrópicos.
- El perfil del caso óptimo sim003 (densidad, presiones $w_r, w_t$, anisotropy $h$).
- El histograma de distribución de masa sim003: **K-035 visualizado**, con la barra de la cáscara $[0.85, 0.99]$ resaltada en rojo.
- El escaneo de max compactness vs $h_0$ para varios $n$, mostrando la **cota estructural ~0.83** como línea horizontal roja.

Las gráficas no son decoración. Cada una muestra un punto físico concreto. El histograma de K-035, en particular, hace inmediatamente visible la concentración holográfica: ~50% de la masa en una cáscara fina cerca del horizonte.

El usuario añadió una nueva instrucción permanente: **producir gráficas y data cruda proactivamente cuando ayuden, sin pedir permiso**. Patrón establecido para futuras simulaciones.

## Hacia adelante

El snapshot v2.2 deja la teoría en un estado consolidado. Tres sesiones consecutivas de refinamiento estructural sin contradicciones internas. Tres candidatos K activos esperando promoción. Doce derivaciones formales. Cero eslabones rojos.

El próximo frente natural es **K-033**: el programa SO(10)-GUT que hemos pospuesto desde sesión 30. Es el más ambicioso (10+ sesiones potenciales) y el de mayor payoff (Yukawas, jerarquía de masas, CKM/PMNS — el clásico problema no resuelto del SM). Una primera sesión exploratoria definirá si es tractable o si SCG necesita herramientas adicionales para enfrentarlo.

Pero antes de eso, vale la pena marcar el momento. Sesión 39 cerró un cabo abierto desde sesión 11 — 28 sesiones de retraso. Sesión 40 cerró tres sesiones técnicas sin agregar nada nuevo, solo organizando lo aprendido. La teoría no avanzó este día; pero se entendió mejor a sí misma.

Eso también es progreso.

---

*Próximo reporte: probablemente cuando K-033 produzca el primer resultado técnico (positivo o negativo), o si Q-045 residual se reactiva con nueva motivación.*
