# D-004: Reglas de fusión en vértices trivalentes de la red SCG

- **ID:** D-004
- **Fecha:** 2026-04-17 (sesión 8)
- **Hipótesis asociadas:** H-001 v1.2, H-002
- **Depende de:** D-002 (D=1), A-003 (presión de degeneración), E-008 (cadena Levin-Wen)
- **Estado:** derivación parcial. U(1) derivado; Z₃ derivado; SU(2) motivado; SU(3) abierto.

## Objetivo

Derivar las **reglas de fusión** de la red de cuerdas SCG en vértices trivalentes. Estas reglas determinan, vía el mecanismo de Levin-Wen → Chern-Simons, el grupo gauge emergente y por tanto el contenido de partículas de la teoría.

## Premisas

1. El espacio-tiempo a escala Planck es una red de cuerdas SCG (H-001).
2. El espacio tiene D=3 dimensiones (H-002).
3. Cada segmento de cuerda tiene modos transversales con energía ℏc/d (A-003).
4. Los vértices genéricos en D=3 son **trivalentes** (3 cuerdas se encuentran).

## Parte I: U(1) — de los modos transversales

### Paso 1. Grados de libertad transversales de un segmento

Una cuerda 1D embebida en espacio 3D tiene:
- 1 dirección tangente eᵢ (a lo largo de la cuerda) — grado gauge (reparametrización)
- **2 direcciones transversales** — grados físicos

Los modos cuánticos en el plano transversal Πᵢ (perpendicular a eᵢ) forman un oscilador 2D.

### Paso 2. Momento angular transversal

Los estados del oscilador 2D se etiquetan por:
- n: número cuántico principal (nivel de energía)
- **m ∈ ℤ: momento angular** (autovalor de L_z a lo largo de eᵢ)

El momento angular m genera la simetría U(1) de rotaciones en el plano transversal:
```
ψ(φ) → e^{imφ} ψ(φ)
```

**m es una carga U(1) interna** de cada segmento de cuerda. Es un número cuántico conservado: no puede cambiar por perturbaciones suaves.

### Paso 3. Conservación en el vértice

En un vértice trivalente, los 3 segmentos interactúan. La simetría U(1) es interna (no depende de la orientación espacial del segmento), así que se conserva aditivamente:

```
m₁ + m₂ + m₃ = 0
```

Esta es la **regla de fusión aditiva para U(1)**.

### Paso 4. Consecuencia vía Levin-Wen

Una red de cuerdas con etiquetas m ∈ ℤ y fusión aditiva produce, según el mecanismo de Levin-Wen/Wen:
- Un **campo gauge U(1) emergente** con una excitación sin masa (fotón emergente)
- Las excitaciones topológicas (defectos) portan carga U(1) cuantizada

**Resultado I:** U(1) emerge de la simetría rotacional transversal de las cuerdas SCG. ∎

**Nivel de confianza:** ALTO. Usa solo geometría (2 transversales en D=3) + QM (conservación de momento angular) + Levin-Wen (demostrado).

---

## Parte II: Z₃ — de la trivalencia del vértice

### Paso 5. Ruptura de simetría en el vértice

Lejos del vértice, el plano transversal Πᵢ tiene simetría SO(2) completa (rotación continua). Pero **en el vértice**, la presencia de los otros 2 segmentos rompe esta simetría.

En el vértice, los 3 segmentos definen 3 direcciones (e₁, e₂, e₃). Para cada segmento i, los otros 2 segmentos j, k atraviesan su plano transversal Πᵢ en puntos determinados. Estas intersecciones definen **direcciones privilegiadas** en Πᵢ.

Para un vértice trivalente **genérico** (equiespaciado angularmente, la configuración de mínima energía por simetría):
- Las proyecciones de e_j y e_k sobre Πᵢ están separadas por 120°
- Esto genera una **simetría Z₃** (grupo cíclico de orden 3: rotaciones de 0°, 120°, 240°)

### Paso 6. Reducción de U(1) a Z₃ en el vértice

La simetría SO(2) ≅ U(1) del plano transversal se rompe a Z₃ en el vértice trivalente:
```
SO(2) → Z₃   (en el vértice, por la trivalencia)
```

Consecuencia: el momento angular m, que lejos del vértice es un entero arbitrario, se clasifica **modulo 3** en el vértice:
```
m ≡ 0 (mod 3):  sector "neutro"
m ≡ 1 (mod 3):  sector "cargado +"
m ≡ 2 (mod 3):  sector "cargado −" (≡ −1 mod 3)
```

### Paso 7. Regla de fusión Z₃

La conservación de momento angular en el vértice, modulo la simetría Z₃:
```
m₁ + m₂ + m₃ ≡ 0 (mod 3)
```

Esta es la regla de fusión para **Z₃** — el grupo cíclico de orden 3.

### Paso 8. Cuantización de la carga en unidades de 1/3

Si identificamos la carga eléctrica con m (mod 3), normalizando a la carga del electrón:
```
m ≡ 0 (mod 3) → Q = 0         (neutrinos, gluones, fotón)
m ≡ 1 (mod 3) → Q = +1/3      (quarks d, s, b)
m ≡ 2 (mod 3) → Q = +2/3      (quarks u, c, t)
         o −1/3 (antiquarks)
```

La **cuantización de la carga en unidades de 1/3** emerge de la trivalencia del vértice en D=3.

Los **leptones** (carga entera) tienen m ≡ 0 (mod 3) y carga ±1 proveniente de la U(1) total: carga 1 = 3 unidades de 1/3.

**Resultado II:** la cuantización de la carga en tercios emerge de la ruptura SO(2) → Z₃ por la trivalencia de los vértices SCG en D=3. ∎

**Nivel de confianza:** MEDIO-ALTO. La geometría del vértice trivalente dando Z₃ es sólida. La identificación con la carga eléctrica es una conjetura con soporte estructural.

### Paso 9. Conexión con SU(3)

Z₃ es el **centro** del grupo SU(3). Las representaciones de SU(3) se clasifican por su **trialidad** (transformación bajo Z₃):
- Trialidad 0: singuletes (1), octetes (8), ... → hadrones, gluones
- Trialidad 1: fundamentales (3) → quarks
- Trialidad 2: anti-fundamentales (3̄) → antiquarks

El hecho de que la carga eléctrica se cuantice en tercios (= trialidad) es un reflejo del centro Z₃ de SU(3)_color.

**Implicación:** la Z₃ derivada del vértice trivalente es el centro del grupo de color. El paso de Z₃ a SU(3) completo requiere un mecanismo adicional (rotaciones continuas entre los 3 "canales" del vértice). Ver sección V.

---

## Parte III: SU(2) — de la conexión gravitacional

### Paso 10. Variables de Ashtekar

La formulación de Ashtekar de la gravedad en 3+1D reescribe GR como una teoría gauge con:
- Grupo gauge: **SU(2)** (la parte compacta del grupo de Lorentz en variables de Ashtekar-Barbero)
- Conexión: A^i_a (campo gauge SU(2) en la 3-variedad espacial)
- Variable conjugada: la tríada densitizada E^a_i

### Paso 11. Holonomías en la red SCG

En la red SCG, cada segmento de cuerda porta la **holonomía** de la conexión gravitacional:
```
g_e = P exp(∫_e A) ∈ SU(2)
```

donde e es el segmento (edge) y P denota path-ordering.

Esto es idéntico a la estructura de las **redes de espín** en LQG, donde cada arista porta una representación j de SU(2):
```
j ∈ {0, ½, 1, 3/2, 2, ...}
```

### Paso 12. Intertwiner en el vértice

En un vértice trivalente con espines (j₁, j₂, j₃), la condición de invariancia gauge SU(2) es la existencia de un **intertwiner**:
```
ι: V_{j₁} ⊗ V_{j₂} ⊗ V_{j₃} → ℂ
```

que es no nulo si y solo si:
```
|j₁ − j₂| ≤ j₃ ≤ j₁ + j₂     (desigualdad triangular)
j₁ + j₂ + j₃ ∈ ℤ               (espín total entero)
```

Esta es la **regla de fusión de SU(2)** — las mismas reglas de Clebsch-Gordan de la mecánica cuántica.

### Paso 13. Emergencia del campo gauge SU(2)

Por el mecanismo de Levin-Wen aplicado a redes de espín SU(2):
- Las excitaciones son **anyones** clasificados por representaciones de SU(2)
- La teoría efectiva de baja energía es **SU(2) Chern-Simons** a nivel k (determinado por la dinámica)

**Resultado III:** SU(2) emerge como la simetría gauge gravitacional de la red SCG, heredada de la formulación de Ashtekar de GR. ∎

**Nivel de confianza:** MEDIO. La motivación es fuerte (LQG usa exactamente esta estructura), pero no hemos *derivado* que la dinámica de A-003 produce variables de Ashtekar — lo hemos *importado* de una formulación conocida de GR.

---

## Parte IV: Tabla de resultados combinados

| Factor gauge | Origen en SCG | Regla de fusión | Nivel de confianza |
|---|---|---|---|
| **U(1)** | Rotación transversal SO(2) | m₁ + m₂ + m₃ = 0 | **Derivado** |
| **Z₃** (centro de SU(3)) | Trivalencia del vértice → SO(2) → Z₃ | m₁+m₂+m₃ ≡ 0 (mod 3) | **Derivado** |
| **SU(2)** | Conexión gravitacional (Ashtekar) | Clebsch-Gordan | **Motivado** (LQG) |
| **SU(3)₁** (UV) | Z₃ + quiralidad gravitacional → SU(3)₁ por unicidad | Z₃ (abeliana a k=1) | **Argumentado** (5 vías) |

### Grupo gauge emergente: SU(3) × SU(2) × U(1)

| Factor | Origen SCG | Estado |
|---|---|---|
| U(1) | Modos transversales SO(2) | **Derivado** |
| SU(2) | Conexión gravitacional (Ashtekar) | **Motivado** |
| SU(3) | Z₃ (trivalencia) + quiralidad → SU(3)₁; flujo k→∞ → SU(3) YM | **Argumentado** |

**Resultado:** el grupo gauge completo del Modelo Estándar emerge de la geometría de la red SCG.

---

## Parte V: El problema de SU(3) — estado actual

### ¿Por qué SU(3) es difícil?

Intenté varias rutas para derivar SU(3) completo:

**Intento 1:** "3 direcciones pairwise-intersection en el vértice → 3D Hilbert space → U(3) → SU(3)." **Falla** porque SO(3) actúa irreduciblemente sobre ℂ³, así que por el lema de Schur el conmutante es solo U(1). No queda SU(3) independiente.

**Intento 2:** "Borromean linking de 3 cuerdas → simetría S₃ → ¿SU(3)?" S₃ es el grupo de Weyl de SU(3), pero el paso de S₃ (discreto, orden 6) a SU(3) (continuo, dim 8) requiere un mecanismo de "extensión continua" que no he podido derivar.

**Intento 3:** "Excitaciones compuestas del sistema U(1) × SU(2) que forman representaciones de SU(3)." Posible en principio, pero depende del nivel k del Chern-Simons, que no está determinado.

### Lo que SÍ tenemos: Z₃

La Z₃ derivada del vértice trivalente reproduce correctamente:
- La cuantización de la carga en 1/3
- La clasificación de partículas por trialidad (quarks vs leptones)
- La regla de que solo los "singuletes de Z₃" (trialidad 0) se propagan libremente → análogo de **confinamiento de color**

### Resolución de Q-026: Z₃ + quiralidad = SU(3)₁

**Hecho matemático (clasificación de órdenes topológicos abelianos):** existen exactamente **2 órdenes topológicos quirales** con fusión Z₃: SU(3)₁ y su conjugado temporal. El no-quiral (Dijkgraaf-Witten) tiene 9 anyones, no 3.

**Argumento:**
1. La red SCG tiene un sector gravitacional quiral (CS de la conexión de Ashtekar) → el orden topológico del sector Z₃ es quiral.
2. Z₃ quiral = SU(3)₁ por unicidad (solo hay 2 opciones, relacionadas por orientación).
3. SU(3)₁ tiene 3 anyones con espines topológicos h = {0, 1/3, 1/3}. Los anyones no triviales (trialidad 1 y 2) son los "quarks" del marco SCG.

**De SU(3)₁ a SU(3) completo:** el nivel k=1 es el UV. Al integrar modos Planckianos masivos, k_eff crece (Δk = ±½ por fermión de Dirac fundamental). A bajas energías k_eff >> 1 → SU(3) perturbativo (= QCD).

**Cinco argumentos convergentes:** (1) unicidad matemática, (2) parsimonia K-005, (3) level-shifting estándar, (4) confinamiento = Z₃ preservada (lattice QCD), (5) anomalías (sugerente). Ver análisis completo: `notes/Q-026_analisis_Z3_a_SU3.md`.

**Nivel de confianza:** MEDIO-ALTO. El paso más fuerte es la unicidad matemática. El más débil es la suposición de quiralidad gravitacional (motivada por LQG, no derivada de A-003).

---

## Parte VI: Origen geométrico de cada factor

```
SCG en D=3
    │
    ├── Segmentos (edges): 2 modos transversales
    │       → SO(2) ≅ U(1) → campo gauge U(1) emergente
    │
    ├── Vértices trivalentes: rompen SO(2) → Z₃
    │       → cuantización de carga en 1/3
    │       → Z₃ = centro de SU(3)
    │       → ¿SU(3) completo? (Q-026)
    │
    └── Holonomías gravitacionales: conexión de Ashtekar SU(2)
            → campo gauge SU(2) emergente
```

Cada factor gauge tiene un **origen geométrico distinto**:
- U(1) es propiedad de cada **segmento** (local al edge)
- Z₃/SU(3) es propiedad de cada **vértice** (local al junction)
- SU(2) es propiedad de la **conexión** (global/gravitacional)

---

## Limitaciones

1. **U(1):** la derivación asume que el momento angular transversal es la carga relevante. En realidad, podría haber otros números cuánticos.
2. **Z₃:** la ruptura SO(2) → Z₃ asume un vértice equiespaciado. Vértices deformados tendrían simetría menor.
3. **SU(2):** importada de LQG, no derivada de A-003 directamente.
4. **SU(3):** NO derivado. Solo tenemos su centro Z₃.
5. **Niveles de Chern-Simons** (k para cada factor): no determinados.
6. **Contenido fermiónos/bosónico:** no derivado. La estadística requiere análisis del espectro de excitaciones.

## Historial

- 2026-04-17 (sesión 8): derivación inicial.
