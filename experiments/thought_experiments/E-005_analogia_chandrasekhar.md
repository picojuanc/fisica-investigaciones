# E-005: Analogía con Chandrasekhar para la cuerda gravitacional

- **ID:** E-005
- **Fecha:** 2026-04-16
- **Hipótesis asociadas:** H-001 (refinamiento v1.1)
- **Estado:** activo; es el pilar cuantitativo del refinamiento.

## Motivación

Tras reformular E_info como presión cinética cuántica (ver `notes/P-1_analisis.md`), emerge una analogía directa con las presiones de degeneración que estabilizan objetos astrofísicos compactos. Esta analogía permite, por primera vez, una **estimación cuantitativa** del régimen en el que la cuerda gravitacional puede existir.

## El experimento mental

Imagina una secuencia de objetos cada vez más densos:

1. **Estrella ordinaria**: presión térmica (kT gas) vs gravedad. Se estabiliza porque el gas es caliente.
2. **Enana blanca** (estrella muerta, M < M_Ch ≈ 1.4 M_☉): sin combustión, la presión térmica desaparece. Lo que la salva del colapso es la **presión de degeneración electrónica** (principio de Pauli + Heisenberg). Por encima de M_Ch, esta presión no basta → colapso a estrella de neutrones.
3. **Estrella de neutrones** (M < M_TOV ≈ 2–3 M_☉): presión de degeneración neutrónica. Por encima de M_TOV, colapso a BH.
4. **Agujero negro**: no hay presión conocida suficiente → horizonte + singularidad.

**Pregunta:** ¿hay un **cuarto tipo** de presión de degeneración, operando a escala Planck, que pueda detener el colapso antes de la singularidad?

## Razonamiento paso a paso

### Paso 1. ¿Por qué es razonable esperar otra presión?

Cada escalón anterior involucra los grados de libertad disponibles al régimen:
- térmica → grados térmicos del plasma
- electrónica → electrones degenerados (fermiones)
- neutrónica → neutrones degenerados (fermiones)
- **¿Planckiana? → grados de libertad del propio espacio-tiempo**

El argumento es puramente estadístico: si el espacio-tiempo es cuántico (A-001), tiene grados de libertad. Cualquier colección de modos cuánticos en una caja pequeña manifiesta presión cinética (por Heisenberg, no necesariamente por Pauli).

### Paso 2. Estimación dimensional

Una presión de degeneración relativista para N modos en volumen V:

```
P_deg ~ N · (ℏc) / V^(4/3)     [modos relativistas]
```

La presión gravitacional en una bola de radio R y masa M:

```
P_grav ~ G M² / R⁴
```

Igualándolas (criterio de equilibrio) a escala Planck (R ~ ℓ_P, M ~ M_P):

```
G M² / ℓ_P⁴ ~ N ℏc / ℓ_P⁴
G M² ~ N ℏc
M ~ √(N ℏc/G) = √N · M_Planck
```

**Resultado:** la presión de degeneración planckiana estabiliza masas hasta **M ~ √N · M_P**, donde N es el número efectivo de grados de libertad gravitacionales por volumen de Planck.

### Paso 3. ¿Qué es N?

Aquí entra la física más incierta. Tres hipótesis:

- **N ≈ 1** (grados mínimos): la cuerda gravitacional solo estabiliza objetos de masa de Planck. Para masa mayor → colapso macroscópico, pero el interior queda estabilizado localmente.
- **N ~ 10¹⁹** (grados intermedios, conjetura holográfica en volumen pequeño): M_crit macroscópico pero todavía muy pequeño (nanogramos).
- **N → ∞** en algún límite emergente: el sistema escala arbitrariamente. Poco probable; violaría holografía.

El caso 1 es el más conservador y el más **compatible con la observación** (no vemos cuerdas gravitacionales macroscópicas).

### Paso 4. Reconciliación con BHs macroscópicos

Bajo esta analogía, un BH macroscópico M >> M_P:
- A nivel macro: la gravedad domina, se forma un horizonte clásico. Coincide con GR. ✅
- En el interior, cerca de lo que sería la "singularidad": la densidad alcanza valores planckianos.
- A esas densidades, la presión de degeneración gravitacional opera localmente.
- El resultado interior no es una singularidad, sino una estructura 1D (cuerda) o una maraña de cuerdas (fuzzball).

Esto **no** contradice la observación (la observación solo ve el horizonte y su exterior). Y resuelve parcialmente **P-3**.

### Paso 5. Predicciones cualitativas distintas de un BH clásico

1. **No hay singularidad.** La información no se "pierde" en ella; queda codificada en la estructura interior.
2. **Evaporación modificada:** en fases tardías (M → M_P), el BH se acerca al régimen donde la cuerda domina. La radiación deja de ser puramente térmica y gana estructura espectral.
3. **Límite de compresión universal:** no se puede comprimir cualquier masa en cualquier volumen arbitrariamente pequeño. Hay un "volumen mínimo" por masa, dado por la presión de degeneración gravitacional.

## Diferencia observable

- En radiación de Hawking final (mini-BH): espectro con picos de cuerda en lugar de térmico puro.
- En procesos de gran energía (BH primordiales, colisiones hipotéticas): firmas de estructura interior no singular.

## Conclusión

- La analogía con Chandrasekhar **transforma la presión de entrelazamiento metafísica en presión cinética cuántica convencional**.
- Permite una estimación dimensional: M_crit ~ √N · M_P.
- Explica por qué no vemos cuerdas gravitacionales macroscópicas (la gravedad vence a nivel macro) y simultáneamente resuelve la singularidad interior.
- **Cierra parcialmente P-1 y P-3.**
- **Abre Q-014:** ¿cuál es N? (es decir, ¿qué cuenta como "grado de libertad gravitacional"?)

## Historial

- 2026-04-16: registrado como consecuencia del refinamiento v1.1 de H-001.
