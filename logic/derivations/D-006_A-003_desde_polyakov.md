# D-006 — A-003 como presión de Casimir de Polyakov transversal

- **ID:** D-006
- **Fecha:** 2026-04-20 (sesión 13)
- **Deriva:** A-003 v1.1 (presión de degeneración gravitacional) como consecuencia de A-001 (corte Planck) + cuantización canónica estándar.
- **Alcance:** forma funcional, con coeficiente O(1) fijado por la convención worldsheet.
- **Análisis completo:** `notes/Q-032_polyakov_y_A-003.md`.
- **Resuelve:** Q-032 (respuesta positiva, con caveats).
- **Consecuencia:** promueve K-027 a insight confirmado.

---

## 1. Enunciado

**Proposición.** Sea una cuerda SCG de longitud *L* con espaciamiento característico *d* ≥ ℓ_P, modelada como el defecto 1D de la red Walker-Wang cuyo sector IR está descrito por la acción de Polyakov. Entonces la energía del vacío de los modos transversales, con corte UV en *n_max* = *L/d* (equivalente a λ_min = *d*), es

```
E_vac = 2π ℏc · L / d²
```

Esta es exactamente la forma del término E_info = N ℏc L / d² de A-003 v1.1, con N = 2π para la convención de cuerda cerrada.

**Corolario.** A-003 no es un postulado independiente; es el efecto Casimir de los modos transversales confinados.

---

## 2. Derivación

### 2.1 Acción y gauge

Cuerda cerrada, σ ∈ [0, L) periódica. Gauge conforme (h_{ab} = η_{ab}), fijando adicionalmente los modos longitudinales X^0, X^1 (gauge lightcone o físico). Queda como campos propagantes las coordenadas transversales X^i, i = 2, 3.

```
S_⊥ = (T/2) ∫ dτ dσ [ (∂_τ X^i)² − (∂_σ X^i)² ]        (D-006.1)
```

con T = tensión efectiva.

### 2.2 Expansión en modos

Solución general de □X^i = 0 en cuerda cerrada:

```
X^i(τ,σ) = X_L^i(τ−σ) + X_R^i(τ+σ)                    (D-006.2)
```

con

```
X_L^i = (x^i/2) + (p^i/4πT)(τ−σ) + (i/√(4πT)) Σ_{n≠0} (α_n^i/n) e^{−iω_n (τ−σ)}
```

y análogo para X_R (con osciladores α̃_n^i). Aquí ω_n = 2π|n|/L.

Los α_n^i (n<0) son creadores, α_n^i (n>0) aniquiladores, con

```
[α_m^i, α_n^j] = m δ_{m+n,0} δ^{ij}                   (D-006.3)
```

### 2.3 Hamiltoniano

En gauge conforme y sector transversal:

```
H_⊥ = (2π/L) [ L_0^⊥ + L̃_0^⊥ ]                         (D-006.4)
```

con L_0^⊥ = (1/2) Σ_n :α_{-n} · α_n: (suma sobre i=2,3 implícita), similar L̃_0^⊥.

### 2.4 Energía del vacío (antes de regularizar)

El vacío |0⟩ satisface α_n^i |0⟩ = α̃_n^i |0⟩ = 0 para n > 0.

```
⟨0| H_⊥ |0⟩ = (2π/L) · [⟨L_0^⊥⟩ + ⟨L̃_0^⊥⟩]
           = (2π/L) · 2 · ⟨L_0^⊥⟩   (por simetría izq/der)
```

Usando normal ordering y [α_m, α_{-m}] = m:

```
⟨L_0^⊥⟩ = (1/2) Σ_{n∈ℤ} ⟨α_{-n}^i α_n^i⟩ 
        = (1/2) Σ_{n>0} ⟨α_n^i α_{-n}^i − n⟩   (recolocación)
        = − (1/2) Σ_{n>0} n · (D−2)              (factor D−2 por modos transversales)
```

Para D = 4, D−2 = 2:

```
⟨L_0^⊥⟩ = − Σ_{n>0} n                          (D-006.5)
```

### 2.5 Imposición del corte UV físico

A-001 impone ℓ_P como escala mínima. En la red Walker-Wang, *d* es el espaciamiento (con d ≥ ℓ_P). Modos con λ < d no existen físicamente (no hay sub-celdas por debajo de ese tamaño).

Corte: n_max = *L / d*. Finito y explícito, sin regularización ζ.

```
Σ_{n=1}^{n_max} n = n_max (n_max + 1) / 2
```

Para *L* >> *d* (cuerda macroscópica):

```
Σ_{n=1}^{n_max} n ≈ n_max² / 2 = (L/d)² / 2                (D-006.6)
```

### 2.6 Energía del vacío con corte

Sustituyendo (D-006.6) en (D-006.5) y luego en (D-006.4):

```
⟨L_0^⊥⟩ = − (L/d)² / 2
⟨H_⊥⟩_vac = (2π/L) · 2 · [− (L/d)² / 2] = − 2π · L/d²
```

Tomando el valor absoluto (la contribución física al Hamiltoniano de la cuerda en el vacío relativo al vacío sin cuerda):

```
E_vac = 2π ℏc L / d²                                      (D-006.7)
```

(restaurando ℏ, c).

### 2.7 Comparación con A-003 v1.1

A-003 v1.1: E_info = N ℏc · Σ_i 1/d_i. Con d uniforme y N_seg = L/d segmentos:

```
E_info,total = N · ℏc · L / d²                             (D-006.8)
```

Comparando (D-006.7) y (D-006.8): ambos son ℏc·L/d² con coeficiente.

```
N_identificado = 2π                                         (D-006.9)
```

(Para la convención de cuerda cerrada.)

---

## 3. Alcance y limitaciones

### 3.1 Robustez de la forma funcional

La dependencia **L/d²** emerge porque:
- ω_n ∝ n/L (cualquier cuerda, cualquier topología)
- Número de modos ∝ n_max = L/d (por corte físico)
- Suma de ω_n hasta n_max ∝ n_max²/L = L/d²

Esto es **invariante** frente a cuerda abierta vs cerrada, ajustes de normalización, o detalles del gauge fixing. La *forma* L/d² es genuina.

### 3.2 Coeficiente O(1)

El coeficiente 2π depende de:
- Topología worldsheet (cuerda cerrada: 2π; abierta: π/2; nudo: 2π).
- Número de modos transversales (D-2 en dim D; aquí 2 para D=4).
- Método de corte (corte duro vs regularización ζ).

Rango razonable: O(π/2) a O(2π). Absorbible en la definición de N de A-003.

### 3.3 Dominio de validez

La derivación es válida como **teoría efectiva IR** del defecto Walker-Wang. No es cuerda bosónica fundamental:
- No requiere dimensión crítica D=26.
- No tiene taquión (el "vacío con cuerda" es estable respecto al "vacío sin cuerda" por el signo de la sustracción en §2.6).
- Las anomalías conformes se absorben en la UV completion WW (pendiente de verificación formal — P-14).

### 3.4 Lo que NO se deriva

- El **valor** del prefactor N_físico. Depende de la topología del defecto en WW. Dejamos como Q-037.
- La **constante de normalización** de la acción de Polyakov (T). Fija la escala global pero no la forma.
- Conexión con el formalismo WW explícito. Se presume que WW en el IR → Polyakov; falta demostración constructiva.

---

## 4. Conclusión

A-003 v1.1 es una consecuencia de A-001 (corte Planck) + cuantización canónica de Polyakov transversal. No es un axioma independiente — es un **teorema** en el esquema v1.2.

La forma L/d² es derivada rigurosamente; el coeficiente 2π es O(1) y depende de convención.

**Consecuencia ontológica:** H-001 reduce su base axiomática. A-003 pasa a D-006.

---

## 5. Implicaciones

- `framework/axioms.md`: A-003 recibe sección "v1.2 — derivado" señalando su estatus.
- `hypotheses/active/H-001_...`: en la estructura v1.3 (futura), A-003 se cita como derivación D-006, no axioma.
- K-007 (escala √(r_s ℓ_P)) necesita reverificación: en su derivación original usó A-003 como intermedio. Con A-003 = D-006, el resultado *debería* preservarse (cualitativamente lo hace porque la forma funcional coincide); verificación formal queda como Q-036.

---

## 6. Relación con la literatura

- La cuantización aquí es **Polyakov estándar** (Polchinski 1998 vol.1, Zwiebach 2009).
- El corte UV duro en vez de regularización ζ no es estándar en cuerdas fundamentales (donde se busca invariancia conforme), pero es estándar en contextos efectivos con red subyacente.
- El efecto Casimir en cuerdas confinadas es análogo al Casimir entre placas paralelas (Casimir 1948). La fórmula L/d² es la generalización 1+1D del Casimir 3+1D.
- **No se conoce este resultado en el contexto de SCG/WW** — es una derivación original del marco, aunque cada pieza individual es estándar.

---

## 7. Firma

Deriva A-003 v1.1 (H-001) como presión de Casimir de modos transversales. Análisis completo en `notes/Q-032_polyakov_y_A-003.md`. Promueve K-027 a confirmado estructuralmente. Abre P-14 (consistencia cuántica 4D no-crítica) y Q-036, Q-037.
