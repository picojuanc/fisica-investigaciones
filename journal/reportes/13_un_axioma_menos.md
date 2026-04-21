# Reporte 13: Un axioma menos

**Fecha:** 2026-04-20 (sesión 13)

---

## La apuesta

El reporte anterior terminó con una apuesta concreta. El bosquejo de la Lagrangiana había identificado cinco tensiones, y una de ellas — la T-5 — tenía una resolución candidata demasiado atractiva para posponerla.

La apuesta: **la "presión de degeneración gravitacional" que H-001 postula, bautizada A-003, no es un principio nuevo.** Quizá no hace falta postularla. Quizá está ya contenida en algo más básico: la cuantización estándar de una cuerda con un corte UV a escala Planck.

Si la apuesta salía, H-001 perdía un axioma. Si no, al menos sabríamos que A-003 tiene contenido genuinamente nuevo. Cualquiera de las dos direcciones era información útil.

Hoy hicimos el cálculo.

---

## El cálculo en una frase

Tomamos la acción de Polyakov — la más básica que tiene una cuerda en el vacío — la cuantizamos canónicamente en el gauge conforme, restringimos al sector transversal (dos modos, perpendiculares al movimiento de la cuerda), y sumamos las contribuciones de zero-point energy de cada modo hasta la frecuencia máxima permitida por el corte físico d.

Resultado:

```
E_vac = 2π ℏc L / d²
```

La forma de A-003 v1.1 es:

```
E_info = N ℏc L / d²
```

**Coinciden exactamente.** Con la identificación N ↔ 2π.

---

## Lo que esto significa

El número 2π importa menos que la forma. Lo que importa es que la dependencia en la longitud total (L) y el espaciamiento (d) — ese cociente L/d² que aparece en ambas expresiones — no es un resultado independiente de cada teoría. Es un resultado que la cuantización de Polyakov **produce sola**, sin que tengamos que postular nada extra.

Dicho en términos más ásperos: la "presión de degeneración gravitacional" que H-001 necesitaba postular desde el día 1 no era una pieza nueva del mundo. Era el **efecto Casimir**. El mismo Casimir que hizo famoso a Hendrik Casimir en 1948, cuando predijo (y después se verificó) que dos placas conductoras paralelas se atraen por la simple cuantización del campo electromagnético entre ellas.

Aquí la geometría es distinta: en vez de dos placas separadas por distancia *d*, tenemos una cuerda de longitud *L* con modos transversales confinados a escala *d*. La fórmula cambia de *L²/d* (tres dimensiones de placa) a *L/d²* (una dimensión de cuerda). Pero el mecanismo es idéntico: cuantizar modos confinados produce una energía que depende de las dimensiones del confinamiento.

Lo gravitacional de A-003 es el origen de los modos (son grados de libertad del espacio-tiempo, no del campo electromagnético). Pero la matemática es la misma.

---

## La lección que ya teníamos

En la sesión 2 aprendimos una lección que bautizamos K-005: **la buena teoría es más modesta, no más exótica**. Esa lección se aplicó entonces a A-003 cuando la reinterpretamos de "presión de entrelazamiento informacional" (exótico, poco claro) a "presión cinética cuántica de modos gravitacionales" (Heisenberg aplicado al régimen Planck). Ya había sido una simplificación entonces.

Hoy la aplicamos otra vez. A-003 deja de ser un axioma. Se convierte en un **teorema** — una proposición que se sigue de los axiomas restantes (A-001 = corte Planck) más la mecánica estándar (cuantización de Polyakov).

Tiene nombre oficial: D-006, "A-003 como presión de Casimir de Polyakov transversal." Vive en la carpeta de derivaciones, no en la de axiomas.

**La teoría SCG pasa de tener 3 axiomas a tener 2.**

Esto no es solo un ejercicio de contabilidad. Significa que todos los resultados que habíamos derivado suponiendo A-003 — la dimensionalidad 1D (D-002), la conservación de entropía (D-003), la escala interior del BH (K-007) — ahora descansan sobre una base más pequeña. Son más robustos en el sentido de que requieren menos suposiciones independientes.

---

## Lo que se gana y lo que no

**Se gana:**

- Un axioma menos. La teoría se vuelve más modesta.
- La constante N, que era parámetro libre, queda fijada por el cálculo (es 2π para cuerda cerrada, π/2 para cuerda abierta — en cualquier caso, de orden uno).
- Identidad con un fenómeno conocido: el efecto Casimir, que ha sido medido experimentalmente desde los años 50.
- Reabre, con mucha más claridad, la comparación con teoría de cuerdas estándar. La cuerda SCG ahora se identifica, en el IR del defecto Walker-Wang, con una cuerda estándar tipo Polyakov. La correspondencia BH-cuerda de Horowitz-Polchinski puede compararse directamente.

**No se gana:**

- El valor exacto del prefactor (2π vs π/2) depende de la topología worldsheet del defecto WW, que no tenemos clasificada. Es Q-037, una pregunta nueva.
- La consistencia cuántica de Polyakov en 4D (no 26) es delicada. En cuerdas bosónicas fundamentales, D=4 tiene anomalías conformes que no se cancelan. En nuestro caso, asumimos que las anomalías se absorben en la UV completion WW. Plausible pero sin demostración formal — es la nueva debilidad P-14.
- La escala interior de los BHs K-007 (d ~ √(r_s ℓ_P), que predice ~1 fm para BHs estelares) fue derivada usando A-003 como intermedio. Debería rederivarse directamente desde Polyakov/Casimir. Esperamos que se preserve — la forma funcional es la misma — pero conviene verificar. Q-036.

---

## La ruta desdoblada

Lo más interesante, quizá, es cómo cambió el panorama.

Antes: "H-001 postula una presión cinética cuántica de grados de libertad gravitacionales. Es Heisenberg en régimen Planck. Eso es lo que da A-003."

Ahora: "Si la cuerda SCG es una cuerda de Polyakov en el IR, y cuantizas normalmente con corte físico a la escala de la red, obtienes automáticamente el efecto Casimir. La presión que llamábamos A-003 es ese Casimir. No hay principio adicional."

El cambio en cómo se describe la teoría es notable. A-003 era un enunciado específico a SCG. El Casimir es un fenómeno general. Identificarlos es decir: **la novedad de SCG no está en el mecanismo estabilizador** (que es conocido), **sino en las condiciones de confinamiento** (que son planckianas y vienen de la red WW). La parte nueva es la *red*, no la *presión*.

Eso es importante porque enfoca la atención: si alguien quiere discutir H-001, no debe discutir si hay o no presión de degeneración (hay Casimir, está verificado experimentalmente). Debe discutir si el escenario de confinamiento Planckiano via Walker-Wang es correcto. La crítica se vuelve más específica.

---

## Lo que viene

Tres pasos naturales, en orden:

1. **Verificar que K-007 sobrevive** — Q-036. La escala interior de los BHs, √(r_s ℓ_P), es una de las predicciones más concretas de H-001. Debería rederivarse desde Polyakov-Casimir directo sin usar A-003. Una sesión.

2. **Resolver P-14** — leer sobre effective string theory en gauge lattice. Polyakov mismo en 1970 introdujo la descripción efectiva de cuerdas como tubos de flujo en QCD. Lüscher corrigió la tensión con un término 1/L. Aharony-Komargodski (2013) clasificó effective string theories sistemáticamente. Hay literatura. Verificar compatibilidad con D-006.

3. **Seguir con el bosquejo de la Lagrangiana** — la tarea 5.2 sigue siendo obtener las ecuaciones de movimiento de S_Plebanski + Λ. Con D-006 en mano, la sección 2.3 del bosquejo (Régimen III) queda más firme: la acción de cuerda no es ansatz, es consecuencia.

Y en algún momento, un snapshot v1.6. Los cambios estructurales de estas dos sesiones (12 y 13) ameritan consolidación.

---

## Una nota personal sobre método

Las reglas de auto-mejoramiento que escribimos en CLAUDE.md (reglas 1-12) incluyen una que se aplica especialmente bien hoy:

> **Regla 9:** preferir destruir un resultado propio a defenderlo por inercia. Si encuentras un error, celébralo: acabas de evitar construir más sobre arena.

Hoy no destruimos exactamente — promovimos. Pero el espíritu es parecido. A-003 era un axioma desde la sesión 1. Lo habíamos reformulado una vez (v1.1) y podríamos haberlo dejado ahí. En vez de eso, la sesión 12 planteó la pregunta: ¿es realmente necesario como axioma? Y la sesión 13 contestó: no.

El resultado no es que H-001 está "menos bien" porque perdió un axioma. Es que está **mejor**. Es más modesta. Requiere menos para decir lo mismo.

K-005 aplicada dos veces al mismo postulado. No es mala marca.

---

*La investigación tiene 27 insights confirmados (K-001 a K-027), 3 hipótesis activas, 6 derivaciones (la D-006 nueva), y — por primera vez desde que empezamos — **dos axiomas**, no tres. P-14 es nueva pero concreta. Q-036 y Q-037 marcan el camino inmediato. Sin eslabones rojos.*
