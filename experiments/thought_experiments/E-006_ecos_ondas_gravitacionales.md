# E-006: Ecos de ondas gravitacionales como firma distintiva

- **ID:** E-006
- **Fecha:** 2026-04-16 (sesión 6)
- **Hipótesis asociadas:** H-001 v1.1
- **Estado:** activo. Es el puente entre la teoría y la física experimental.

## Escenario

Considere una fusión de dos BHs detectada por LIGO/Virgo. Tras el *ringdown* principal, ¿podría haber ecos tardíos de la onda gravitacional (GW) cuyo retraso temporal distinguiría entre:
- el BH clásico de GR (sin ecos),
- un fuzzball de Mathur (ecos con retraso Δt_fuzzball),
- la cuerda plegada SCG de H-001 v1.1 (ecos con retraso Δt_SCG)?

## Marco físico

Un Exotic Compact Object (ECO) con una "superficie reflectante efectiva" a distancia δ por dentro del horizonte clásico produce ecos GW tras el ringdown. El retraso entre ecos consecutivos, en coordenadas tortoise, se aproxima por:

```
Δt_eco ≈ 2 · (r_s / c) · ln(r_s / δ)
```

La expresión viene de integrar el tortoise coordinate r* = r + r_s · ln((r - r_s)/r_s) desde la superficie (r = r_s + δ) hasta el máximo del potencial efectivo (cerca de la photon sphere a r ~ 3M).

## Predicción diferencial

Para los tres modelos, δ es distinto:

| Modelo | δ | Δt_eco |
|---|---|---|
| GR clásico | ∞ (sin superficie) | **no hay ecos** |
| Fuzzball / Stretched horizon | ~ ℓ_P | 2(r_s/c)·ln(r_s/ℓ_P) |
| **H-001 v1.1 (SCG)** | ~ √(r_s·ℓ_P) | **(r_s/c)·ln(r_s/ℓ_P)** |

**Factor clave:** Δt_SCG / Δt_fuzzball ≈ 1/2.

En H-001 v1.1 la "pared efectiva" está a la media geométrica horizonte–Planck, no a Planck. Esto **reduce a la mitad** el retraso de ecos.

## Números concretos (BH 30 M_☉, fusión típica LIGO)

- r_s = 2GM/c² ≈ 88 km
- r_s/c ≈ 2.9 × 10⁻⁴ s
- ln(r_s/ℓ_P) ≈ ln(5.6 × 10³⁹) ≈ 91.4

**Predicciones:**

```
Δt_fuzzball ≈ 2 × 2.9×10⁻⁴ × 91.4 ≈ 53 ms
Δt_SCG     ≈     2.9×10⁻⁴ × 91.4 ≈ 27 ms
```

**Diferencia observable:** ~26 ms en el primer eco tras el ringdown.

## Tabla de predicciones para distintas masas

| M_BH | r_s | Δt_fuzzball | Δt_SCG | Diferencia |
|---|---|---|---|---|
| 5 M_☉ | 15 km | ~8.7 ms | ~4.4 ms | 4.3 ms |
| 30 M_☉ | 88 km | ~53 ms | ~27 ms | 26 ms |
| 100 M_☉ | 295 km | ~180 ms | ~91 ms | 89 ms |
| 10⁶ M_☉ (LISA) | 3 Gm | ~17 min | ~8.5 min | 8.5 min |

Las diferencias son porcentualmente constantes (~50%) pero absolutamente crecen con M.

## Test observacional: ¿es esto detectable?

### Actualidad (LIGO O3/O4, Virgo)
- Sensibilidad marginal a ecos; las reclamaciones existentes (Abedi & Afshordi) son controvertidas.
- **Test preliminar:** analizar señales existentes para ver si preferencia estadística de Δt_SCG vs Δt_fuzzball emerge al acumular muchas fusiones.

### Cercano plazo (LIGO A+, Virgo+, KAGRA)
- Mejora de sensibilidad por factor ~2-3.
- Posible separación estadística entre modelos si los ecos existen.

### Largo plazo (Einstein Telescope, Cosmic Explorer, LISA)
- Detectores 3G podrán distinguir Δt_SCG de Δt_fuzzball **fusión a fusión**, no solo estadísticamente.
- LISA para BHs supermasivos daría retrasos del orden de minutos — fácilmente resoluble si existen.

## ¿Cuándo se reflejaría realmente una onda GW en la maraña interior?

Depende del régimen:

- **λ_GW >> √(r_s·ℓ_P):** la GW "ve" la maraña como medio efectivo; reflexión parcial tipo medio denso uniforme. Régimen típico para LIGO (λ_GW ~ 1000 km ≫ 1 fm).
- **λ_GW ~ √(r_s·ℓ_P):** resonancia con modos transversales. Absorción fuerte.
- **λ_GW << √(r_s·ℓ_P):** la GW se propaga entre los hilos sin reflexión notable.

En LIGO estamos **muy en el primer régimen**. La maraña actúa como medio uniforme efectivo; la "pared reflectante" es efectiva, no discreta. El modelo de tortoise-coordinate con δ = √(r_s·ℓ_P) es una aproximación razonable.

## Caveats importantes

1. **La existencia misma de ecos GW es debatida.** Si no existen (la GR es estricta), todo este análisis es moot.
2. **El factor ½ es una predicción dimensional**, no un cálculo GR completo. Análisis riguroso requeriría resolver la ecuación de onda en un fondo con estructura interior efectiva.
3. **Fuzzballs y stretched horizon** no predicen exactamente el mismo Δt; sus "superficies reflectantes" tienen naturalezas diferentes. El cálculo fino varía.
4. **Correcciones de rotación (Kerr)**, carga, y masa del compañero pueden desplazar los números. El análisis aquí es para Schwarzschild-like.
5. **Resolución temporal de LIGO** ~1 ms, suficiente en principio para las diferencias predichas a masas ≥ 30 M_☉.

## Interpretación

Si los ecos GW existen y los datos actuales los muestran ambiguamente:
- H-001 v1.1 predice un **Δt específico** (factor ½ del modelo Planck).
- Una preferencia estadística por Δt/2 sobre Δt en el stack de fusiones LIGO sería **evidencia indirecta de H-001 v1.1**.
- Lo contrario (Δt consistente con modelos Planck-scale) **refutaría H-001 v1.1** en su formulación actual.

Es un test falsable con tecnología disponible, con datos ya existentes.

## Otras firmas (secundarias)

Derivadas como exploración pero menos observables hoy:
- **QNMs adicionales** a ω ~ 10²³ Hz (no observables con LIGO).
- **Love numbers** (deformabilidad tidal) — accesible con detectores 3G.
- **Picos discretos en Hawking** de BHs primordiales (si existen).
- **Absorción anómala en inspiral** tardío.

Estas se documentan en `notes/F_analisis_ringdown.md`.

## Conclusión

**H-001 v1.1 es una teoría falsable en principio**, con una predicción cuantitativa distintiva: el retraso de ecos de GW es la **mitad** que en modelos donde la estructura está a escala Planck.

Esto es el primer paso concreto hacia la contrastación empírica. No es una victoria ni una derrota — es el momento en que la hipótesis deja la pizarra y pide datos.

## Historial

- 2026-04-16 (sesión 6): registrado. Primera conexión de H-001 v1.1 con datos observacionales.
