# Reporte 9 — ¿Por qué un solo tiempo?

*Sesión 10 · 19 de abril de 2026*

---

Hasta ahora, la investigación había explicado dos hechos dimensionales: por qué los objetos fundamentales son 1D (sesión 3, balance de fuerzas) y por qué el espacio tiene 3 dimensiones (sesión 7, nudos). Pero faltaba una pieza: ¿por qué hay exactamente una dimensión temporal?

## La pregunta que nadie quiere tocar

La dimensión temporal es el dato más básico de la física y el que menos se cuestiona. Todo el mundo asume que el tiempo es 1D — lo da por sentado. Pero ¿por qué no podrían existir dos tiempos? ¿O ninguno?

La primera respuesta seria la dio Max Tegmark en 1997: con cero tiempos no hay dinámica; con dos o más tiempos, las ecuaciones de la física se vuelven "ultrahiperbólicas" — un tipo de ecuación diferencial que no tiene soluciones bien definidas dado un estado inicial. En lenguaje más simple: con dos tiempos, no puedes predecir el futuro a partir del presente. El universo sería impredecible no por complejidad, sino por estructura matemática.

Tegmark concluía: observamos un tiempo porque si hubiera más (o menos), no habría observadores.

Es un argumento potente pero insatisfactorio. No explica *por qué* hay un solo tiempo — explica por qué *tenemos que observar* un solo tiempo. Es como decir que el agua está mojada porque de lo contrario no la llamaríamos agua.

## Lo que encontramos: un accidente algebraico que no es accidental

La respuesta que emerge de nuestra teoría no es antrópica. Es algebraica, y viene de un lugar inesperado: la clasificación de las álgebras de Lie.

En la sesión 9 descubrimos que la fuerza débil es quiral — solo actúa sobre fermiones levógiros — porque la conexión gravitacional de Ashtekar es la parte "autodual" (levógira) del álgebra de Lorentz. Esta descomposición en parte izquierda y parte derecha es posible porque el álgebra de Lorentz en 4 dimensiones tiene una propiedad especial:

```
so(3,1) complexificada  ≅  sl(2,C) × sl(2,C)
                             ↑ izquierda    ↑ derecha
```

Se factoriza en un producto de dos piezas. Izquierda y derecha. Es esta factorización la que permite que exista quiralidad — que la naturaleza distinga entre izquierda y derecha.

Aquí está el punto clave: **esta factorización es un accidente**. En la clasificación de Dynkin de todas las álgebras de Lie simples y semisimples, so(n) factoriza como producto **solo para n = 4**. Para cualquier otro n — 3, 5, 6, 7, lo que sea — so(n) es *simple* (una pieza indivisible). No hay izquierda ni derecha.

Es como si, de todos los números naturales, solo el 4 tuviera la propiedad de factorizarse de la forma correcta. Y lo tiene porque en la clasificación de Dynkin, el diagrama D₂ son dos puntos desconectados (A₁ + A₁), mientras que D₃, D₄, D₅... son todos diagramas conexos.

## La derivación

El argumento es entonces muy corto:

1. La teoría requiere la conexión autodual de Ashtekar (lo necesitamos para la fuerza débil quiral — sesión 9).
2. La autodualidad requiere que el álgebra de Lorentz se factorice en izquierda × derecha.
3. Esta factorización solo existe en dimensión total 4 (clasificación de Dynkin).
4. Dimensión total = D_espacio + D_tiempo = 4.
5. D_espacio = 3 (derivado en sesión 7).
6. D_tiempo = 4 − 3 = 1.

Hay un segundo argumento, independiente, que usa el operador de Hodge (el operador matemático que distingue los campos autodual y anti-autodual). En signatura (3,1) — tres dimensiones de espacio, una de tiempo — el Hodge star al cuadrado da −1 en 2-formas. En signatura (2,2) o (4,0), da +1. La diferencia es crucial: −1 significa que la descomposición en izquierda y derecha requiere números complejos, lo que hace que las dos mitades estén ligadas por conjugación compleja. Esto es lo que genera la quiralidad *irreductible* — la que no puedes deshacer con ninguna transformación real.

Solo en signatura (3,1) los espinores izquierdos y derechos están ligados de esta manera. En las otras signaturas, o son equivalentes (no se distinguen) o son completamente independientes (no interactúan). Ninguna de esas opciones reproduce la física que observamos.

## Lo que esto significa

La dimensionalidad completa del espacio-tiempo queda explicada:

| Dimensionalidad | Origen | Sesión |
|---|---|---|
| Objetos 1D | Balance gravedad/degeneración | 3 |
| Espacio 3D | Codimensión 2 para nudos | 7 |
| **Tiempo 1D** | **Factorización de Dynkin + quiralidad** | **10** |
| **Total: 3+1** | **Todo desde QM + GR** | |

No son cuatro hechos independientes. Es una cadena: la presión de degeneración (A-003) da objetos 1D, los objetos 1D dan espacio 3D por topología, y el espacio 3D + la necesidad de quiralidad dan tiempo 1D por álgebra.

La signatura (3,1) del espacio-tiempo — que durante un siglo ha sido tratada como un dato empírico sin explicación — resulta ser una consecuencia de que los objetos fundamentales son cuerdas gravitacionales estabilizadas.

## El eslabón débil (honestidad)

El argumento depende de K-019: la identificación de SU(2)_L con la conexión autodual de Ashtekar. Si esa identificación fuera incorrecta — si la fuerza débil no tiene origen gravitacional — el argumento para D_tiempo = 1 se debilita. No colapsa del todo (Tegmark sigue funcionando como argumento de well-posedness), pero pierde su carácter derivativo.

K-019 es "fuertemente motivado" (identidad matemática del grupo de Lorentz, propuesta por Alexander-Marciano-Smolin), no "derivado". Así que D_tiempo = 1 hereda ese nivel de confianza.

También es un argumento de consistencia algebraica, no de selección dinámica. D-002 explica por qué los objetos son 1D *dinámicamente* (minimizan energía). H-002 explica D_espacio = 3 *topológicamente* (los nudos lo requieren). D-005 explica D_tiempo = 1 *algebraicamente* (la quiralidad lo requiere). Los tres argumentos son de naturaleza diferente, y el temporal es el que tiene menos sabor "físico" — es más un constraint de consistencia.

Pero cuatro argumentos convergentes (Dynkin, Hodge, espinores, evolución de red) apuntando todos a q = 1 son difíciles de ignorar.

---

*Siguiente reporte: por determinar. La historia dimensional está ahora completa. Los frentes que quedan son más cuantitativos: constantes de acoplamiento, acción Lagrangiana, fenomenología electrodébil.*
