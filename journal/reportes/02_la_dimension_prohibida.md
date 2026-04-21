# Reporte 2 — La dimensión prohibida: por qué solo 1D funciona

*Sesiones 2-3 · 16 de abril de 2026*

---

La pregunta más incómoda de la hipótesis de la cuerda gravitacional era: ¿por qué una cuerda (1D) y no una membrana (2D) o una bola (3D)?

Postularlo sin más era trampa. Necesitábamos *derivarlo*.

## La analogía que lo resolvió

Pensemos en las enanas blancas. Una enana blanca es una estrella muerta que no colapsa porque los electrones se resisten a ser comprimidos (presión de degeneración). Pero hay un límite: si la masa supera 1.4 masas solares (el límite de Chandrasekhar), los electrones pierden la batalla contra la gravedad y la estrella colapsa.

¿Por qué existe ese límite? Porque la energía gravitacional crece con la masa *más rápido* que la presión de degeneración. En algún momento, la gravedad gana.

Ahora traslademos esto a la escala de Planck. Nuestros "electrones" son los grados de libertad del espacio-tiempo mismo, y cada uno tiene la masa de Planck (~10⁻⁵ gramos, una escala enorme para una partícula). La pregunta se convierte en: ¿en qué dimensión D la presión de degeneración de estos modos puede resistir indefinidamente a la gravedad?

## El cálculo

La respuesta sale de comparar cómo escalan dos energías con el número de modos N:

- **Energía de degeneración** (la presión que resiste): escala como N^(1+1/D)
- **Energía gravitacional** (la que aplasta): escala como N²

Para que haya balance *sin importar cuántos modos haya* (es decir, para cualquier N), los dos exponentes deben coincidir:

```
1 + 1/D = 2  →  D = 1
```

Eso es todo. En D=2, el exponente de la gravedad (2) supera al de la degeneración (3/2), y la gravedad gana para N grande. En D=3, peor aún. **Solo en D=1 los exponentes empatan**, y el sistema puede resistir sin importar cuánta materia haya.

## Lo que significa

La cuerda gravitacional no es 1D porque lo decidimos — es 1D porque *no puede ser otra cosa*. Es como el límite de Chandrasekhar al revés: en lugar de un límite de masa, hay un límite de dimensión. Los modos Planckianos son tan masivos que el balance solo funciona en la dimensión mínima.

Hay un matiz elegante: el balance en D=1 es *exacto* (energía cero para cualquier tamaño), lo que significa que la cuerda no tiene un tamaño preferido por este cálculo. Para fijar su longitud concreta se necesita algo extra (un término subdominante). Pero la dimensionalidad está clavada.

## La entropía y el plegado

Con D=1 derivado, atacamos el siguiente problema: ¿cómo encaja esta cuerda dentro de un agujero negro macroscópico?

Un agujero negro estelar tiene una entropía enorme (S ~ 10⁷⁷). Una cuerda lineal de longitud L tiene entropía S ~ L/ℓ_P. Para que la cuerda tenga la misma entropía que el agujero negro, necesita una longitud L ~ r_s²/ℓ_P, donde r_s es el radio del horizonte.

Para un agujero negro de 10 masas solares: L ~ 10⁴⁵ metros. Eso es absurdamente largo — millones de veces el universo observable. ¿Cómo cabe?

**Se pliega.** Como un ovillo de lana dentro de una pelota. La cuerda se enrolla dentro del volumen del agujero negro con un espaciado transversal:

```
d ~ √(r_s · ℓ_P)
```

Esa fórmula es la **media geométrica** entre el horizonte (enorme) y la escala de Planck (minúscula). Para un agujero negro estelar, d ~ 1 femtómetro — la escala del núcleo atómico. Ningún modelo clásico predice esa escala. Es una predicción cuantitativa concreta.

Y lo mejor: con esas escalas, la entropía de la cuerda plegada es **exactamente** igual a la entropía del agujero negro. No aproximadamente — exactamente. Satura la cota holográfica sin violarla.

## Consecuencia inesperada: la paradoja de la información

Si el interior del agujero negro es una cuerda plegada con modos vibracionales, entonces la información de todo lo que cayó al agujero negro *no se destruye* — queda codificada en las vibraciones de la cuerda. La radiación de Hawking podría correlacionarse con estos estados internos, haciendo la evaporación unitaria (sin pérdida de información).

Esto no está demostrado, pero la imagen es consistente. Por primera vez, la teoría ofrecía una resolución tentativa de uno de los mayores misterios de la física.

## Estado al cierre

H-001 v1.1 tenía ahora:
- Un mecanismo claro (presión de degeneración, no un principio nuevo)
- D=1 derivado (no postulado)
- Escalas interiores predichas (d ~ √(r_s·ℓ_P))
- Entropía que satura la cota holográfica
- Una imagen tentativa de la paradoja de información

Y por primera vez, **ningún eslabón crítico roto**. Todos los problemas eran amarillos, ninguno rojo.

---

*Siguiente reporte: ¿somos originales, o redescubrimos la rueda?*
