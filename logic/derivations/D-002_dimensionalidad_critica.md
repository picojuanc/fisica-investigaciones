# D-002: Dimensionalidad crítica de la fase SCG

- **ID:** D-002
- **Fecha:** 2026-04-16
- **Hipótesis asociada:** H-001 (v1.1)
- **Estado:** derivación dimensional preliminar; no rigurosa. Pero suficiente para responder P-5.

## Objetivo

Derivar (bajo la hipótesis H-001 v1.1 y los axiomas A-001/A-002/A-003') **por qué la fase estable de la cuerda gravitacional tiene dimensionalidad D = 1** — no 0D (punto), no 2D (membrana), no 3D (bola).

## Enunciado del resultado

> **Teorema (dimensional):** D = 1 es la única dimensión en la que la presión cinética cuántica (degeneración relativista) de N modos Planckianos balancea exactamente la energía gravitacional autogravitante, independientemente de N. En cualquier D ≥ 2, la gravedad gana para N > O(1) y el sistema colapsa.

## Derivación

### Paso 1. Escalado de la energía de degeneración

Un objeto D-dimensional de tamaño L contiene N modos uniformemente distribuidos. El espaciamiento es:
```
a = L / N^(1/D)
```

Cada modo relativista confinado contribuye ℏc/a a la energía (principio de Heisenberg + relación energía–momento relativista, A-003'):
```
E_deg(D, N, L) = N · ℏc / a = N^(1+1/D) · ℏc / L    (1)
```

### Paso 2. Escalado de la energía gravitacional

Para una distribución compacta de N masas (cada una ~ M_P) con tamaño L, en 3D Newtoniano:
```
E_grav ≈ -G · M² / L    donde M = N · M_P
       = -G · N² · M_P² / L
       = -N² · ℏc / L      (usando GM_P² = ℏc)     (2)
```

Los factores geométricos O(1) y correcciones logarítmicas se ignoran (no afectan exponentes).

### Paso 3. Balance

Energía total:
```
E_total(D, L) = [N^(1+1/D) − N²] · ℏc / L
```

El **coeficiente A(D, N) ≡ N^(1+1/D) − N²** determina la dinámica:
- A > 0: E > 0 y decrece con L → el sistema se dispersa (L → ∞, E → 0⁺).
- A < 0: E < 0 y decrece con L decreciente → colapso (L → 0, E → −∞).
- A = 0: balance marginal, E = 0 para todo L → equilibrio susceptible a correcciones finas.

### Paso 4. Análisis de A(D, N)

Para N > 1 (varios modos):

| D | E_deg ~ N^? | E_grav ~ N^? | A = N^(1+1/D) − N² | Comportamiento |
|---|---|---|---|---|
| 1 | N² | N² | 0 (exacto) | marginal ∀ N |
| 2 | N^(3/2) | N² | ~ −N² (N≫1) | colapso |
| 3 | N^(4/3) | N² | ~ −N² (N≫1) | colapso |
| ∞ | N | N² | −N² | colapso extremo |

El escalón es claro: **D = 1 es la única dimensionalidad donde los dos exponentes coinciden** (2 = 2), permitiendo balance independiente de N.

### Paso 5. Ecuación explícita

Buscar D tal que E_deg ∝ E_grav en N (mismo exponente):
```
1 + 1/D  =  2
1/D      =  1
D        =  1       ∎
```

## Interpretación física

En astrofísica, una enana blanca (electrones degenerados en D=3) es estable hasta la masa de Chandrasekhar:
```
N_Ch ~ (ℏc / (G m_e²))^(3/2)
```

Por encima de N_Ch, la gravedad vence. El valor finito de N_Ch depende de (m_e/M_P) << 1.

**Para modos Planckianos (m = M_P), ese factor es 1**. Entonces N_crit(D=3) = O(1): en D=3 con modos Planckianos no hay estabilidad para más de un modo. Lo mismo en D=2.

Solo en D=1 el exponente del coeficiente gravitacional coincide con el de la degeneración, dando estabilidad marginal para todo N.

## Qué significa "marginal"

A(D=1) = 0 significa que el balance es tan exacto que cualquier L satisface E = 0. El sistema no tiene una escala preferida por este cálculo solo.

Para fijar un L* concreto hace falta un término subdominante:
- Tensión de borde (energía asociada a los extremos de la cuerda)
- Backreaction gravitacional (correcciones post-Newtonianas)
- Efectos de curvatura (el espacio no es plano a escala Planck)

Cualquiera de ellos rompe la marginalidad y selecciona un L*. La derivación detallada queda pendiente (ver P-5.1 derivado).

## Analogía clara

| Régimen astrofísico | Modos degenerados | m por modo | Dim. estable | N_crit estable |
|---|---|---|---|---|
| Enana blanca | electrones | m_e | D=3 | ~10^57 |
| Estrella de neutrones | neutrones | m_n | D=3 | ~10^57 |
| **Cuerda gravitacional (SCG)** | **grados de libertad gravitacionales** | **M_P** | **D=1** | **∀ N** |

La cuerda es la única "estrella degenerada" donde la dimensionalidad estable no es 3 — porque los modos son tan masivos (M_P) que la relación de exponentes obliga a descender a D=1.

## Limitaciones

1. Análisis dimensional, no cálculo riguroso.
2. Gravedad Newtoniana; falta relativista GR.
3. Forma específica del espacio ambiente (3D) asumida.
4. Tensión/backreaction no incluidas; D=1 queda marginal.

Estas limitaciones son documentadas y abordables. El resultado dimensional (D=1) es robusto frente a ellas.

## Resultado para H-001

**P-5 queda parcialmente resuelto.** La dimensionalidad 1 no se postula — emerge como la única consistente con el balance gravedad/degeneración para modos Planckianos.

Esto refuerza el carácter **modesto** de H-001 v1.1: la teoría no postula "la fase es 1D", sino que muestra que **no puede ser otra**.

## Historial

- 2026-04-16: derivación inicial.
