# Análisis F: predicciones observables distintivas de H-001 v1.1

- **Fecha:** 2026-04-16 (sesión 6)
- **Objetivo:** identificar qué medidas reales distinguirían H-001 v1.1 de fuzzballs, stretched horizon, o del BH clásico de GR.
- **Criterio:** una teoría sin predicción falsable es decoración; una teoría con predicciones observables es ciencia. Quiero saber en qué lado cae H-001 v1.1.

## Panorama de firmas posibles en ondas gravitacionales

Tras una fusión BH-BH, la señal GW tiene tres fases:
1. **Inspiral** — órbita decreciente (dominante lejos del merger).
2. **Merger** — la fusión propiamente dicha.
3. **Ringdown** — el BH final se estabiliza emitiendo quasinormal modes (QNMs).

En GR pura, el ringdown decae exponencialmente y se acaba.

Si el objeto final **no es un BH clásico** (ECO — Exotic Compact Object), la onda puede:
- reflejarse parcialmente en la "superficie" interna,
- generar **ecos tardíos** tras el ringdown principal,
- modificar los **QNMs**,
- alterar la **deformabilidad tidal** (Love numbers).

## Firmas candidatas

### F.1 — Ecos de ondas gravitacionales

Si existe una "pared reflectante" a distancia δ por dentro del horizonte clásico, el tiempo de retraso entre ecos (en coordenadas tortoise) es:

```
Δt_eco ≈ 2 (r_s / c) · ln(r_s / δ)
```

**Para distintos modelos:**

| Modelo | δ (profundidad desde horizonte) | Δt_eco |
|---|---|---|
| GR clásico | — (sin superficie) | no hay ecos |
| Fuzzball (Mathur) | ~ ℓ_P | 2(r_s/c)·ln(r_s/ℓ_P) |
| Stretched horizon | ~ ℓ_P | 2(r_s/c)·ln(r_s/ℓ_P) |
| **H-001 v1.1** | ~ √(r_s·ℓ_P) | **(r_s/c)·ln(r_s/ℓ_P)**  ← **factor ½** |

La diferencia clave: en H-001 v1.1, la "superficie reflectante efectiva" está a escala intermedia (la maraña empieza a ser "densa" a √(r_s·ℓ_P) del horizonte, no a ℓ_P). El retraso es aproximadamente **la mitad** del modelo fuzzball.

**Estimación numérica para un BH de 30 M_☉ (típico LIGO):**
- r_s ≈ 90 km → r_s/c ≈ 3×10⁻⁴ s
- ln(r_s/ℓ_P) ≈ ln(10⁴⁰) ≈ 92

| Modelo | Δt_eco |
|---|---|
| Fuzzball / Susskind | ≈ 55 ms |
| H-001 v1.1 | ≈ 28 ms |

**Diferencia de ~27 ms.** Potencialmente distinguible con análisis estadístico acumulado de muchas fusiones en LIGO/Virgo — si los ecos existen.

**Nota honesta sobre el estado actual:** los ecos en GW son un tema controvertido. Hay reclamaciones (Abedi–Afshordi, 2016) y contramedidas (Westerweck et al., 2018). Sin señal clara confirmada. Es un campo abierto pero tenue.

### F.2 — Espectro QNM modificado

Los quasinormal modes de un BH de Kerr en GR están determinados únicamente por (M, J). Un objeto con estructura interior tendría **modos adicionales** relacionados con los grados de libertad internos.

**H-001 v1.1 predice:**
- QNMs dominantes de Kerr (macroscópicos) casi invariables.
- Modos adicionales a frecuencias ω ~ c/√(r_s·ℓ_P), correspondientes a vibraciones de la maraña interior.

Para BH estelar: ω ~ c / 10⁻¹⁵ m = 10²³ Hz. **Mucho más altas que las observables** por LIGO (10²-10³ Hz).

⇒ **Esta firma no es observable** con tecnología actual ni cercana. Solo con detectores hipotéticos de altísima frecuencia.

### F.3 — Tidal Love numbers

En GR, un BH tiene Love number = 0 exactamente (no se deforma bajo marea externa).
Un ECO con estructura interior tiene Love number ≠ 0, incluso pequeño.

**H-001 v1.1 predice** una rigidez efectiva de la maraña proporcional a la densidad interior (saturación holográfica). La deformabilidad tidal k₂ escala dimensionalmente como:

```
k₂ ~ (ℓ_P / r_s)^α    para algún α > 0
```

Para BH estelar: k₂ muy pequeño. **Difícil de detectar** con precisión LIGO actual, pero **posible con LISA y detectores 3G** (Einstein Telescope, Cosmic Explorer).

**Diferencia con fuzzballs:** ambos predicen k₂ ≠ 0. El cálculo del valor numérico **debería diferir**, porque la estructura interior es distinta (volumen lleno vs cap off). Pero esto requiere modelado detallado.

### F.4 — Espectro de radiación de Hawking en BHs pequeños

Para BHs primordiales o mini-BHs (si existen):
- En GR: espectro puramente térmico de Hawking.
- En H-001 v1.1: modos vibracionales de la cuerda interior se acoplan a la radiación → **picos discretos** superpuestos al térmico.

Frecuencia de los picos: ω ~ c/L_modo donde L_modo son las longitudes de resonancia de la cuerda plegada.

**Para BHs primordiales de 10¹² kg** (candidatos para detección): T_Hawking ~ 10¹⁰ K, frecuencia típica ~ 10²⁰ Hz (rayos gamma de alta energía).

**Firma potencial:** cuellos de botella espectrales o modulación sobre el espectro térmico — observable si detectamos evaporación de BHs primordiales (misiones futuras).

### F.5 — Absorción selectiva durante inspiral

Durante el inspiral de una fusión BH-BH, la onda GW saliente pasa cerca de los horizontes. Si hay estructura interior, la onda se **acopla a los modos internos**:

- GR: absorción = 0 (horizonte perfecto).
- Fuzzballs: reflectividad casi total (cap off actúa como pared).
- **H-001 v1.1:** absorción parcial a frecuencias resonantes con los modos de la maraña.

Esto podría manifestarse como una **disipación anómala** en la fase tardía del inspiral, distinta del predicho por GR.

## Tabla resumen de observables potenciales

| Firma | LIGO actual | LIGO+ / Virgo (≤2030) | Einstein Telescope / LISA (≥2035) | Detectores de rayos-γ / evaporación BH primordial |
|---|---|---|---|---|
| Ecos GW (F.1) | Marginal (sin confirmación) | Posible con stacking | **Muy accesible** | — |
| QNM extra (F.2) | No | No | No | — |
| Love numbers (F.3) | No | Marginal | **Accesible** | — |
| Hawking modulado (F.4) | — | — | — | **Accesible si existen PBHs** |
| Absorción inspiral (F.5) | No | Posible | Accesible | — |

## Decisión de foco

**La firma más prometedora para falsabilidad actual/próxima es F.1 (ecos GW).**

Razones:
- Diferencia cuantitativa concreta entre H-001 (Δt/2) y fuzzballs (Δt).
- Análisis existente de datos LIGO; método conocido.
- Sensibilidad mejorable con estadística acumulada.

**La firma más interesante teóricamente es F.4 (Hawking modulado).** Pero requiere detectar BHs primordiales, que quizá no existen.

## Prognóstico honesto

H-001 v1.1 **es falsable en principio**, pero no con los datos GW actuales con certeza. Los ecos de GW son un tema con datos ruidosos y reclamos controvertidos. Una predicción distintiva cuantitativa (factor ½ en Δt_eco) es un avance.

**No es ciencia "robustamente falsable" aún**, pero está en el territorio donde **puede volverse falsable** en los próximos 10-15 años con detectores 3G.

En el intermedio:
- Publicar la predicción cuantitativa (factor ½) sería meaningful.
- Buscar métodos de análisis GW específicamente diseñados para distinguir Δt vs Δt/2 sería el siguiente paso.
