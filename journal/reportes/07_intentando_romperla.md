# Reporte 7 — Intentando romperla: el stress-test

*Sesión 9 · 18 de abril de 2026*

---

Después del sprint de la sesión 8 (donde derivamos el grupo gauge del Modelo Estándar), las reglas de auto-mejoramiento exigían una pausa para intentar destruir nuestro propio resultado. Si no podemos romperlo, es más fuerte de lo que pensábamos. Si lo rompemos, mejor saberlo ahora que después de construir tres pisos más encima.

## Las cuatro preguntas incómodas

### 1. "Tu U(1)... ¿es la U(1) correcta?"

En el Modelo Estándar hay dos U(1) distintas: la hipercarga (U(1)_Y, antes de la ruptura electrodébil) y el electromagnetismo (U(1)_EM, después del Higgs). ¿Cuál derivamos?

La buena noticia: es la hipercarga. La cuantización en 1/3 que obtuvimos del vértice trivalente coincide exactamente con la relación conocida entre la trialidad de SU(3) y la cuantización de la hipercarga en el SM. No es casualidad — es la misma estructura matemática vista desde dos ángulos.

El electromagnetismo "real" (el que produce la luz) emerge después de la ruptura electrodébil, que mezcla la hipercarga con el isospín débil mediante la fórmula Q = T₃ + Y/2. Eso requiere entender el Higgs en nuestro marco, que todavía no hemos hecho. Pero no invalida nada.

**Veredicto: pasa el test.**

### 2. "Tu SU(2)... ¿no es la gravedad, no la fuerza débil?"

Esta era la pregunta que más me preocupaba. En nuestra derivación, el SU(2) viene de la formulación de Ashtekar de la gravedad. Pero en el SM, SU(2)_L es la fuerza nuclear débil — la que hace que los neutrones se desintegren. ¿Cómo puede ser lo mismo?

Aquí vino la sorpresa de la sesión: **resulta que sí pueden ser lo mismo**, y no es una idea nueva.

La conexión de Ashtekar (1986) es literalmente la parte "levógira" (left-chiral) de la álgebra de Lorentz. No por analogía — por definición matemática. El grupo de Lorentz (que describe las simetrías del espacio-tiempo) se descompone en dos mitades quirales:

```
Lorentz  =  SU(2)_L  ×  SU(2)_R
               ↑
        Ashtekar vive aquí
```

Y hay un hecho de la teoría de representaciones que dice: cuando un fermión se mueve en un espacio-tiempo curvo, su componente levógira se acopla a la mitad SU(2)_L y su componente dextrógira a la mitad SU(2)_R. Esto no se postula — sale de las matemáticas del grupo de Lorentz.

Alexander, Marciano y Smolin publicaron en 2012 (Physical Review D) exactamente esta propuesta: la quiralidad de la fuerza débil *tiene origen gravitacional*. La razón de que solo los fermiones levógiros sientan la fuerza débil es que la fuerza débil ES la mitad levógira de la gravedad.

Es una idea audaz pero tiene base sólida. Los problemas están en los detalles: las constantes de acoplamiento (la gravedad es mucho más débil que la fuerza débil a bajas energías), y el hecho de que nadie ha derivado las masas del W y el Z desde esta perspectiva.

**Veredicto: pasa el test, y además se fortalece. Lo que parecía el eslabón más débil resulta ser una identificación publicada por físicos serios.**

### 3. "¿No hay anomalías que te rompen la teoría?"

En el SM, las anomalías gauge (inconsistencias cuánticas) se cancelan gracias al contenido específico de partículas. Si nuestra estructura tiene anomalías no canceladas, está muerta.

Resultado: las teorías definidas en una red (como nuestro marco de Levin-Wen) son inherentemente libres de anomalías, porque las anomalías son un artefacto del continuo. La red es auto-consistente por construcción.

**Veredicto: probablemente pasa. No hay señal de alarma.**

### 4. "¿Tu argumento para SU(3) es circular?"

Argumentamos: Z₃ (del vértice) + quiralidad (de Ashtekar) → SU(3)₁. ¿No estamos asumiendo la quiralidad porque la necesitamos?

No. La quiralidad viene de elegir la conexión autodual de Ashtekar, que elegimos por la razón independiente de que da SU(2)_L (la fuerza débil). La quiralidad de SU(3)₁ es un bonus, no un input.

**Veredicto: pasa. No es circular.**

## La decisión que el stress-test forzó

El stress-test reveló que toda la derivación del grupo gauge depende de una elección: usar la conexión **autodual** (compleja, quiral) de Ashtekar, no la versión **real** de Barbero-Immirzi que usa la LQG moderna.

Con la conexión autodual:
- ✓ SU(2) es automáticamente levógira → fuerza débil
- ✓ La teoría es quiral → violación de paridad
- ✓ El estado de Kodama existe → Chern-Simons quiral

Con la conexión real (Barbero-Immirzi):
- ✗ SU(2) pierde la quiralidad → ya no es la fuerza débil
- ✗ La teoría no distingue izquierda de derecha
- ✗ La identificación con el SM falla

**Decisión: el marco SCG usa la formulación autodual de Ashtekar.** Esto nos separa de la LQG mainstream (que usa Barbero-Immirzi) pero nos conecta con la visión original de Ashtekar y con el programa de Alexander-Marciano-Smolin.

El precio: la conexión compleja tiene problemas técnicos (normalización, condiciones de realidad) que la LQG ha evitado precisamente por eso. Pero para nosotros, la quiralidad no es opcional — es lo que hace que la fuerza débil sea quiral.

## Lo que descartamos (cementerio actualizado)

A la lista de ideas descartadas se añade:

| Idea | Por qué se descartó |
|---|---|
| Formulación de Barbero-Immirzi para SCG | Pierde la quiralidad → SU(2) ya no es SU(2)_L |

## El resultado del stress-test

D-004 **sobrevive intacta** y sale fortalecida en un punto (SU(2)). Ningún eslabón se rompió. Se identificaron problemas nuevos (separación de constantes, fenomenología electrodébil) pero ninguno es fatal.

La cadena ahora dice:

```
Red SCG con conexión autodual de Ashtekar
    ├── Segmentos → U(1)_Y (hipercarga)              [derivado]
    ├── Vértices → Z₃ → carga en 1/3                  [derivado]
    ├── Conexión autodual → su(2)_L (fuerza débil)     [fuertemente motivado]
    ├── Z₃ quiral → SU(3)₁ → SU(3) (color)            [argumentado]
    └── Q = T₃ + Y/2 (electromagnetismo)               [requiere Higgs — abierto]
```

Es la primera vez que intentamos destruir un resultado y sale más fuerte. Eso es buena señal.

---

*Siguiente reporte: por determinar. Opciones: las 3 generaciones, D_tiempo=1, o el mecanismo de Higgs en el marco SCG.*
