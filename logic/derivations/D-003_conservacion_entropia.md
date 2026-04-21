# D-003: Conservación entrópica de la transición BH ↔ cuerda SCG

- **ID:** D-003
- **Fecha:** 2026-04-16
- **Hipótesis asociada:** H-001 v1.1
- **Estado:** derivación dimensional; no rigurosa dinámicamente, pero suficiente para establecer consistencia de escalas.

## Objetivo

Mostrar que la transición propuesta en H-001 v1.1 (BH macroscópico ↔ cuerda SCG plegada en el interior) **conserva la entropía** y **satura la cota holográfica sin violarla**.

## Enunciado del resultado

> **Teorema (conservación entrópica):** bajo H-001 v1.1, si el interior del BH macroscópico es una cuerda SCG plegada con densidad de entropía Planckiana longitudinal (1 bit por ℓ_P), su longitud total L y su escala transversal d están fijadas por:
>
> ```
> L ~ r_s² / ℓ_P
> d ~ √(r_s · ℓ_P)
> ```
>
> Con estas escalas, S_cuerda = S_BH = A/(4ℓ_P²) exactamente.

## Derivación

### Dato 1: entropía de Bekenstein–Hawking

```
S_BH = A / (4 ℓ_P²) = π r_s² / ℓ_P²
     = 4π N²          con N = M/M_P, r_s = 2 N ℓ_P
```

### Dato 2: entropía de la cuerda SCG

La densidad máxima de entropía a lo largo de la cuerda es **1 bit por ℓ_P** (factor O(1) absorbido).

**Justificación (v1.2, 2026-04-20 sesión 14):** la cuerda SCG es un defecto 1D de la red Walker-Wang con espaciamiento ~ℓ_P. En cada sitio de la red hay una categoría de fusión con un número finito (O(1)) de objetos. Por tanto el número de bits por unidad de longitud es O(1)/ℓ_P.

**Justificación anterior (v1.0, 2026-04-16):** "por A-003' (presión de degeneración Planckiana) y holografía 1D". Esta justificación era heurística y en retrospectiva motivacional, no esencial: la densidad 1 bit/ℓ_P se sigue directamente de A-001 + red WW, sin A-003. Ver `notes/Q-036_K-007_sin_A-003.md` para la auditoría completa.

```
S_cuerda = L / ℓ_P    (en SI)
         = L          (en unidades Planck)
```

### Paso 1. Longitud requerida

Imposición S_cuerda = S_BH:

```
L = 4π N² ℓ_P        (SI)
L = 4π N²             (Planck)
```

### Paso 2. Plegado en el volumen interior

El volumen del interior del BH:

```
V_BH = (4/3) π r_s³ = (4/3) π (2N ℓ_P)³ = (32π/3) N³ ℓ_P³
```

Si la cuerda está plegada densamente en V_BH con grosor transversal d², su volumen ocupado es L · d². Igualando (saturación del volumen):

```
L · d² = V_BH
d² = V_BH / L = (32π/3 · N³ ℓ_P³) / (4π N² ℓ_P)
d² = (8/3) N ℓ_P²
d = √(8N/3) · ℓ_P
```

### Paso 3. Escala transversal en forma invariante

Con r_s = 2N ℓ_P:
```
N = r_s / (2ℓ_P)
d² = (8/3) · r_s / (2ℓ_P) · ℓ_P² = (4/3) · r_s · ℓ_P
d = √((4/3) r_s ℓ_P) ≈ √(r_s · ℓ_P)     (a factor O(1))
```

**Escala transversal: d ~ √(r_s ℓ_P).** Media geométrica entre el horizonte y Planck.

### Paso 4. Verificación holográfica

La cota de Bekenstein es S ≤ A/4 (en unidades Planck):
```
A / (4 ℓ_P²) = 4π N² = L = S_cuerda ✓
```

La cuerda **satura exactamente** la cota. No viola.

### Paso 5. Factor de llenado del volumen

La cuerda plegada con grosor d² llena el volumen:
```
(L · d²) / V_BH = 1   (por construcción)
```

Es decir, la cuerda ocupa todo el volumen interior, pero con "textura" de escala d.

### Paso 6. Densidad de cuerda vs densidad de información

- Densidad de cuerda (longitud por volumen): L / V_BH = 1/d² ~ 1/(r_s ℓ_P).
- Densidad de información (bits por volumen): S / V_BH = L / (ℓ_P · V_BH) = 1/(d² ℓ_P) ~ 1/(r_s ℓ_P²).

La densidad volumétrica de información **no** es constante (no es 1/ℓ_P³); decrece con el tamaño del BH como 1/r_s. Esto es **holografía** operando en la derivación.

## Escalas para BHs conocidos

| BH | M | r_s | d ~ √(r_s ℓ_P) | L ~ r_s²/ℓ_P |
|---|---|---|---|---|
| Planck | M_P | ℓ_P | ℓ_P | ℓ_P |
| Primordial hipotético | 10^12 kg | 10⁻¹⁵ m | 10⁻²⁵ m | 10⁵ m |
| Estelar | 10 M_☉ | 3×10⁴ m | 10⁻¹⁶ m (~1 fm) | 10⁴⁴ m |
| Supermasivo (Sgr A*) | 4×10⁶ M_☉ | 1.2×10¹⁰ m | 4×10⁻¹³ m | 1.4×10⁵⁵ m |

### Observaciones

- Para M = M_P: d = ℓ_P. En ese régimen, "cuerda" coincide con "BH de Planck" — no hay maraña, es un solo punto Planckiano.
- Para M >> M_P: d crece pero sigue siendo microscópico. El "fuzziness" interior es sub-nuclear.
- La longitud L alcanza valores absurdos (10^44 m para un BH estelar), pero dentro de la topología plegada, sin contradicción física.

## Consecuencias para la paradoja de información

La imagen del interior como maraña no singular sugiere una resolución de la paradoja de pérdida de información:

1. La materia que cae en el BH **no desaparece en una singularidad**. Se reorganiza como modos de la cuerda interior.
2. La radiación de Hawking, emitida desde el horizonte, puede estar **correlacionada con estados internos** de la cuerda.
3. Esto permite que el estado final (después de evaporación completa) preserve la información del estado inicial — en coherencia con la unitaridad de la mecánica cuántica.

Esto es consistente con la imagen fuzzball de Mathur y con la "ER=EPR" de Maldacena–Susskind. H-001 v1.1 ofrece una ruta complementaria para llegar a esa imagen.

## Limitaciones

1. **Dimensional, no dinámico.** No resuelto: cómo *se forma* la cuerda plegada durante el colapso gravitacional.
2. **Densidad máxima asumida.** Se asume que la cuerda satura 1 bit/ℓ_P. Podría ser menor; entonces habría información externa adicional.
3. **Grosor uniforme.** Asumí d constante; la cuerda real podría tener variación de grosor.
4. **Ignoré contribuciones de campos exteriores** (horizonte, ergosfera en BHs rotantes).

## Conclusión

**P-7 pasa de 🔴 a 🟡.** La conservación entrópica es geométricamente viable; la cuerda plegada satura holografía y sugiere resolución de la paradoja de información.

## Historial
- 2026-04-16: derivación inicial (v1.0).
- 2026-04-20 (sesión 14, v1.2): auditoría Q-036. Se clarifica que A-003 era motivacional en el Paso 2, no esencial. La derivación se basa en A-001 + red WW + holografía + geometría. K-007 preservada. Tensión T-6 identificada: E_Casimir con estas escalas excede Mc² factor ~30 en cálculo Polyakov plano — requiere fondo curvo (Q-038). K-007 (geométrico) no se ve afectado.
