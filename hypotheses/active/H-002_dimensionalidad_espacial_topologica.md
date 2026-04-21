# H-002: La dimensionalidad del espacio emerge de la topología de objetos 1D

- **ID:** H-002
- **Fecha de propuesta:** 2026-04-16 (sesión 7)
- **Estado:** activa, formulación inicial.
- **Depende de:** H-001 v1.1 (objetos fundamentales son 1D), A-001 (escala Planck).
- **Contradice a:** — (complementaria, no competidora)

## Enunciado

> **El espacio macroscópico tiene exactamente 3 dimensiones espaciales porque D = 3 es la única dimensionalidad en la cual objetos 1D (cuerdas SCG) poseen topología de nudos no trivial. En D = 2, los objetos 1D dividen el espacio (sobre-restricción). En D ≥ 4, todos los nudos de objetos 1D son triviales (se desanudan). Solo en D = 3 los objetos 1D pueden formar nudos y enlaces persistentes que codifican información topológica robusta.**

Forma compacta:

```
Objetos fundamentales de dimensión p ⟹ espacio de dimensión D = p + 2
                                        (codimensión 2: mínima para nudos)

H-001: p = 1 (cuerdas SCG)  ⟹  D = 1 + 2 = 3 ✓
```

## Motivación

H-001 v1.1 establece que a escala Planck los objetos fundamentales son 1D (cuerdas gravitacionales estabilizadas). Pero H-001 **asume** que viven en un espacio 3D — no lo deriva.

H-002 cierra el hueco: la dimensionalidad del espacio no es axioma, es **consecuencia** de la dimensionalidad de los objetos fundamentales más un principio topológico (la información topológica requiere codimensión 2).

## Base matemática

### Teoría de nudos en dimensiones D

Un hecho de la topología algebraica:

- **D = 2:** una curva cerrada 1D en un plano 2D siempre divide el espacio en "dentro" y "fuera" (teorema de Jordan). No hay nudos; solo hay separación. La curva sobre-restringe la dinámica.

- **D = 3:** una curva cerrada 1D en 3D puede formar nudos no triviales (trefoil, figure-eight, etc.) y enlaces con otras curvas. El grupo fundamental π₁(S³ \ K) es no trivial para nudos K genuinos. Los nudos son estables bajo deformaciones continuas: no se desatan sin cortarse.

- **D ≥ 4:** toda curva cerrada 1D en ℝ⁴ (o superior) es isotópica al unknot. Es decir, **todos los nudos se desatan** en D ≥ 4 (consecuencia de la teoría de posición general: codimensión ≥ 3 implica trivialidad topológica).

### Principio general: codimensión 2

Para objetos de dimensión p en espacio de dimensión D:
- Codimensión = D − p.
- Codimensión 1: el objeto divide el espacio → sobre-restricción.
- **Codimensión 2: nudos y enlaces no triviales existen y persisten.**
- Codimensión ≥ 3: toda embedding es desanudable → no hay topología persistente.

Regla: **D = p + 2** es el punto óptimo topológico.

Para p = 1 (cuerdas): D = 3.
Para p = 2 (membranas): D = 4.
Para p = 0 (puntos): D = 2 (pero puntos no tienen "forma" topológica → argumento degenerado).

## Consecuencias lógicas (si H-002 es correcta)

### C1. El número de dimensiones no es un parámetro libre

Pasa de ser un dato empírico (observamos 3D) a ser una consecuencia: p = 1 ⟹ D = 3.

### C2. Conexión con teoría de cuerdas (crítica)

En teoría de cuerdas, las cuerdas son 1D pero el espacio es 10D (o 11D). La solución estándar: 6 o 7 dimensiones están "compactificadas" a escala microscópica, dejando 3+1 macroscópicas.

H-002 ofrece una **explicación alternativa** de por qué son 3 las macroscópicas: 3 = 1 + 2 (codimensión topológica). Las dimensiones extra, si existen, serían aquellas donde la topología de nudos es trivial (codimensión > 2) y por tanto no generan "espacio percibible".

### C3. Si existieran membranas fundamentales (p = 2), D = 4

H-002 predice que un universo dominado por membranas (2-branas) tendría 4 dimensiones espaciales. Esto es consistente con la observación de que no vivimos en ese universo (nuestros objetos fundamentales son 1D, no 2D — según H-001).

### C4. Relación con anyones y estadística cuántica

En D = 2+1 (2D espacio + 1D tiempo), las worldlines de partículas son 1D en 3D espacio-tiempo → pueden trenzarse no trivialmente → anyones (estadística fraccional).

En D = 3+1 (3D espacio + 1D tiempo), las worldlines son 1D en 4D espacio-tiempo → se desanudan → solo fermiones y bosones (grupo de permutación, no de trenzas).

H-002 es compatible: la topología *espacial* (nudos de cuerdas a tiempo fijo) opera en D = 3; la topología *espacio-temporal* (trenzas de worldlines) opera en D+1 = 4 donde el trenzado es trivial → justifica que observemos solo estadística de Bose/Fermi, no anyónica, en 3+1D.

### C5. Las partículas podrían ser nudos

Si las cuerdas SCG son los constituyentes del espacio-tiempo, y los nudos son invariantes topológicos, entonces **distintos tipos de nudos corresponden a distintos tipos de partículas**. Un nudo trefoil ≠ un nudo figure-eight ≠ un enlace Hopf → diferentes partículas con diferentes propiedades.

Esta idea tiene ecos de la **teoría de vórtices de Kelvin** (1867, átomos como nudos en el éter) y de los modelos topológicos modernos (TQFTs, Chern-Simons).

**Precaución:** esto es conjetura dentro de conjetura. Muy especulativo. Registrado para exploración futura, no como predicción.

## Predicciones

### Predicción fuerte

> **D = 3 dimensiones espaciales.**

Esto ya es un hecho observado, así que no es "predictivo" en sentido estricto. Pero es **explicativo**: reduce un dato empírico a una consecuencia derivable.

### Predicción condicional

> Si algún día se descubriera que los objetos fundamentales no son 1D sino p-dimensionales, el espacio macroscópico tendría D = p + 2 dimensiones.

### Predicción de compatibilidad

> Las dimensiones extra (si existen) son "topológicamente triviales" (codimensión > 2 respecto a las cuerdas) y por ello no generan estructura macroscópica.

## Experimentos mentales asociados

- [E-007: ¿Qué pasaría en un universo 4D con cuerdas?](../../experiments/thought_experiments/E-007_universo_4D.md) (por crear)

## Problemas abiertos

1. **"La información topológica robusta requiere codimensión 2" — ¿es axioma o se puede derivar?** Actualmente es un hecho matemático (topología algebraica), no un principio físico. ¿Por qué la naturaleza "elegiría" la dimensionalidad que maximiza la información topológica? Necesitamos un principio de selección.

2. **¿Cómo se "construye" el espacio 3D desde una red de cuerdas?** H-002 dice por qué D = 3, pero no cómo las cuerdas forman una red que "es" el espacio. Esto requiere un modelo de emergencia espacial (tipo redes de espín / redes de tensores).

3. **¿Qué pasa con la dimensión temporal?** H-002 aborda D_espacio = 3 pero no D_tiempo = 1. ¿Por qué hay exactamente 1 dimensión temporal?

4. **Relación con la compactificación de cuerdas.** Si la teoría de cuerdas fundamental tiene 10D, ¿H-002 explica por qué 3 son macroscópicas? Depende de si los 10D "originales" son fundamentales o emergentes.

5. **(Nuevo, sesión 8)** **¿Cuáles son las reglas de fusión de la red SCG? (Q-025)** Las reglas de fusión determinan el grupo gauge emergente (vía Levin-Wen → Chern-Simons). Si producen SU(3)×SU(2)×U(1), las partículas del SM serían excitaciones topológicas de la red SCG. Este es el eslabón más importante para conectar H-002 con la materia.

## Extensión: partículas como excitaciones topológicas → H-003

El material sobre partículas topológicas, originalmente desarrollado como extensión C5 de H-002 (sesiones 7–9), ha sido formalizado como hipótesis independiente:

> **Ver [H-003: Partículas topológicas SCG](H-003_particulas_topologicas_SCG.md)**

H-003 incluye: la cadena SCG → Levin-Wen → Chern-Simons → partículas, la derivación del grupo gauge SU(3)×SU(2)×U(1) (D-004), la propuesta de 3 generaciones (Z₃ dual), y el mecanismo de Higgs (condensación de anyones).

## Historial

- **2026-04-16 (sesión 7):** formulación inicial.
- **2026-04-17 (sesión 8):** extensión C5 → análisis completo de nudos como partículas. Cadena SCG → Levin-Wen → Chern-Simons establecida. Pregunta crítica Q-025 identificada.
- **2026-04-18 (sesión 10):** extensión de partículas formalizada como hipótesis independiente **H-003**.
