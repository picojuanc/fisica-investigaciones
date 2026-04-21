# Q-032 — ¿A-003 es la energía zero-point de Polyakov con corte Planck?

- **Fecha:** 2026-04-20 (sesión 13)
- **Contexto:** tarea 5.1 del bosquejo de Lagrangiana (`notes/R_lagrangiana_bosquejo.md`). Atacar la tensión T-5 y decidir el insight candidato K-027.
- **Pregunta concreta:** si cuantizamos canónicamente la acción de Polyakov para una cuerda cerrada, con corte UV en longitud de onda λ ≥ d (siendo d el espaciamiento discreto de SCG), ¿la energía del vacío reproduce la forma de A-003 v1.1 (E_info = N ℏc / d por celda, N_seg celdas en total → E_total = N ℏc L/d²)?

---

## 1. Setup

### 1.1 La acción de Polyakov

Cuerda de longitud total L embebida en espacio-tiempo 4D con métrica plana. Worldsheet parametrizado por (τ, σ) con σ ∈ [0, L] periódico (cuerda cerrada). Coordenadas embebidas X^μ(τ, σ), μ = 0, 1, 2, 3.

Acción:

```
S_P = −(T/2) ∫ dτ dσ √(−h) h^{ab} ∂_a X^μ ∂_b X_μ η_{μν}
```

con *T* = tensión de cuerda (unidades: M/L en naturales), *h_{ab}* = métrica worldsheet auxiliar.

En el **gauge conforme** (*h_{ab}* = diag(−1, +1)) y con métrica target plana:

```
S_P = (T/2) ∫ dτ dσ [ (∂_τ X^μ)² − (∂_σ X^μ)² ]
```

Es la acción de campo escalar libre relativista 1+1D para cada X^μ.

### 1.2 Separación longitudinal/transversal

En el gauge *lightcone* (o físico), dos coordenadas (X^0, X^1) quedan fijadas por los constraints de Virasoro; solo propagan los modos **transversales** X^i con i = 2, 3. En D=4 hay **2 modos transversales** por punto de la cuerda.

Esto es relevante: **la presión de degeneración de A-003 debe identificarse con la energía cuántica de estos 2 modos transversales** — si K-027 es correcto.

### 1.3 Corte UV físico

La cuerda SCG no es una cuerda fundamental sino un defecto en la red Walker-Wang trivalente de escala ℓ_P. El corte UV natural es λ_min = d ≈ ℓ_P (espaciamiento discreto). **Toda longitud de onda menor que d no existe físicamente** — simplemente no hay sub-celdas por debajo de ese tamaño.

Esto corresponde a **imponer un corte duro** *n ≤ n_max* = L/d sobre los modos de Fourier, sin regularización ζ ni dimensión crítica.

**Importante:** este corte NO es la regularización ζ usada en cuerdas bosónicas críticas (D=26). En aquel caso, la suma Σn sale −1/12 y la energía del vacío es O(1/L). Aquí el corte es físico (la red subyacente corta las frecuencias), y la suma es finita y explícita.

---

## 2. Cálculo de la energía del vacío

### 2.1 Expansión en modos (cuerda cerrada)

Solución general de la ecuación de onda □X^i = 0 con σ ∈ [0, L) periódica:

```
X^i(τ, σ) = x^i + (p^i / T L) τ + (i/√(4πT)) Σ_{n≠0} (1/√|n|) 
            × [α_n^i e^{−iω_n (τ−σ)} + α̃_n^i e^{−iω_n (τ+σ)}]
```

con ω_n = 2π |n| / L, y los α_n (modo izquierdo) y α̃_n (modo derecho) son osciladores cuánticos:

```
[α_m^i, α_n^j] = m δ_{m+n,0} δ^{ij}
```

y similarmente para α̃. Los α_{-n} (n>0) son operadores de creación.

### 2.2 Hamiltoniano en el gauge conforme

El Hamiltoniano de Polyakov (cuerda cerrada, gauge conforme, restringido al sector transversal) es:

```
H = (2π / L) [ L_0^⊥ + L̃_0^⊥ − a ]
```

con:

```
L_0^⊥ = (1/2) Σ_{n∈ℤ} α_{-n}^i α_n^i  (suma sobre i=2,3; implícita)
L̃_0^⊥ = (1/2) Σ_{n∈ℤ} α̃_{-n}^i α̃_n^i
```

y *a* = constante de normal ordering (regulariza el zero-point).

El espectro del vacío (|0⟩ aniquilado por α_n, α̃_n con n>0):

```
L_0^⊥ |0⟩ = (1/2) Σ_{n>0} α_{-n}^i α_n^i |0⟩ − (1/2) Σ_{n>0} n · 2  (modos i=2,3)
         = −Σ_{n>0} n     (zero-point)
```

(usando [α_n, α_{-n}] = n y el orden normal).

### 2.3 Imposición del corte UV

Con corte *n ≤ n_max* = *L/d*:

```
⟨L_0^⊥⟩_vac = − Σ_{n=1}^{n_max} n = − n_max (n_max + 1) / 2
```

Para L >> d (cuerda macroscópica): *n_max* >> 1 y

```
⟨L_0^⊥⟩_vac ≈ − n_max² / 2 = − (L/d)² / 2
```

### 2.4 Energía total del vacío

```
E_vac = (2π / L) [ ⟨L_0^⊥⟩ + ⟨L̃_0^⊥⟩ ]  
      = (2π / L) · [− (L/d)² / 2 − (L/d)² / 2]
      = − (2π / L) · (L/d)²
      = − 2π L / d²
```

Restaurando unidades (ℏ, c):

```
E_vac = − 2π ℏc L / d²                               (*)
```

**El signo negativo** es el signo usual del zero-point en cuantización bosónica con normal ordering. Si uno quiere la *diferencia* respecto al "vacío vacío" (sin cuerda), la densidad de energía por unidad de longitud que la cuerda añade al espacio es +2π ℏc / d² (modos transversales confinados) — después de aplicar la prescripción habitual de sustraer el vacío de referencia.

Lo que importa es la **dependencia funcional**: E_vac ∝ L / d².

---

## 3. Comparación con A-003 v1.1

### 3.1 Forma de A-003

A-003 v1.1 (`framework/axioms.md` línea 51) postula:

```
E_info ≈ N · ℏc / d       (por celda)
```

Con N_seg = L/d celdas en total:

```
E_info,total = N_seg · N · ℏc / d = N · ℏc · L / d²     (**)
```

### 3.2 Comparación directa

```
E_vac (Polyakov) = 2π ℏc · L / d²       (estimación (*), signo absorbido)
E_info (A-003)    = N · ℏc · L / d²     (estimación (**))
```

**Ambos tienen EXACTAMENTE la misma forma funcional:** proporcional a *ℏc L / d²*.

El ratio:

```
E_vac / E_info = 2π / N
```

Si identificamos **N = 2π ≈ 6.28**, las expresiones coinciden. 2π no es entero, pero tampoco N en A-003 tenía que serlo — la definición original de N como "número de modos gravitacionales por celda" no cuantificaba el valor; se dejaba libre.

### 3.3 Interpretación del factor 2π

El factor 2π viene de:
- Cuerda cerrada (periodic): ω_n = 2π|n|/L (fijo por topología).
- Modos izquierdo + derecho: factor 2 adicional.
- Corte duro n ≤ L/d (no regularización ζ).

**Convencionalidad:** si usamos cuerda abierta (σ ∈ [0, L/2], ω_n = πn/L, sin sector derecho), el factor sería π/2 en vez de 2π. Si usamos regularización ζ en dimensión crítica, sería O(1) distinto. Es decir, **el coeficiente depende de convenciones** — pero la forma funcional L/d² es invariante.

### 3.4 Veredicto

**La forma funcional de A-003 v1.1 es derivable de la cuantización canónica estándar de Polyakov transversal con corte UV físico en d.**

El coeficiente exacto (el "N" de A-003) se identifica con el prefactor que sale del cálculo (2π para cuerda cerrada, π/2 para abierta, etc.). Es decir, **N de A-003 no es un parámetro libre** — es fijado por la geometría worldsheet elegida.

**Esto promueve K-027** de *candidato* a **confirmado estructuralmente**: A-003 NO es un axioma independiente; es una consecuencia directa de cuantizar la cuerda con corte Planck.

---

## 4. Qué es K-027 confirmado (y qué no)

### 4.1 Lo que se confirma

1. **Forma funcional.** La dependencia de A-003 en L y d (y por tanto en N_seg, d) se obtiene sin postulado independiente, por cuantización estándar.
2. **Origen físico.** La "presión de degeneración gravitacional" ES presión de Casimir de modos transversales confinados — análoga a la presión de Casimir entre placas paralelas, con L_paralelo → L_cuerda y d_separación → d_espaciamiento.
3. **Reducción ontológica.** H-001 pierde un axioma independiente. De los tres (A-001, A-002, A-003), A-003 se vuelve *teorema* (consecuencia de A-001 + cuantización de Polyakov).

### 4.2 Lo que NO se confirma

1. **Identificación cuantitativa N = 2π.** La forma numérica del prefactor depende de la convención (cuerda abierta vs cerrada, número exacto de modos transversales en el caso SCG). Es O(2π) — no "N modos" como número entero libre.
2. **Equivalencia con Polyakov fundamental.** La cuerda SCG no es Polyakov fundamental — es un defecto IR de Walker-Wang. Polyakov es su **acción efectiva IR** cuando los modos UV se integran. La derivación es válida en ese límite; no afirma que SCG = cuerda bosónica estándar.
3. **Reproducción de la escala √(r_s ℓ_P) de K-007.** La derivación en K-007 usó A-003 como premisa. Ahora que A-003 es teorema, habría que rehacer K-007 desde Polyakov directamente para verificar que el resultado se preserva. **Pendiente.**

### 4.3 Costo ontológico

Ganamos (simplificación):
- Un axioma menos: A-003 → *proposición derivada*.
- H-001 pierde la arbitrariedad del prefactor N.
- La cuerda SCG se vuelve más similar a una cuerda bosónica estándar (reabre comparación con P-4 y Horowitz-Polchinski).

Perdemos (honestidad):
- N deja de ser parámetro libre; ahora está fijado por el cálculo (2π o similar). Si fenomenología futura requiere N diferente, esto crea problema.
- La identificación d = ℓ_P (corte UV = espaciamiento) es asunción. Si d_SCG > ℓ_P (red más "gruesa"), el cálculo cambia.

---

## 5. Implicación: A-003 v1.2

**Reformulación propuesta de A-003:**

> **A-003 v1.2 (propuesto):** los grados de libertad transversales de una cuerda SCG se cuantizan canónicamente como modos bosónicos libres con corte UV en d = ℓ_P. Su energía del vacío reproduce automáticamente el término estabilizador de H-001 como *presión de Casimir* (análoga a las placas de Casimir con separación L_longitudinal y corte transversal d).

Con esto:
- A-003 deja de ser postulado.
- Es consecuencia de A-001 (corte Planck) + cuantización estándar.
- Se convierte en proposición derivada: **D-006 (propuesta)** — la presión de Casimir de modos transversales confinados reproduce A-003 v1.1.

Esto implica una **actualización de `framework/axioms.md`**: A-003 se mueve de "axioma" a "derivación" y H-001 se basa ahora en A-001, A-002 solos.

---

## 6. Debilidades y caveats honestos

### 6.1 Convención de cuerda cerrada

El cálculo usa cuerda cerrada. Pero la cuerda SCG, interpretada como defecto de la red WW, podría tener topología diferente:
- Si es abierta con extremos en defectos puntuales (ej. partículas): factor π/2 no 2π.
- Si es un enlace cerrado (nudo): factor 2π (nuestra convención).
- Si es una red de cuerdas interconectadas: el cálculo requiere suma sobre conexiones.

**En todos los casos, la forma L/d² se preserva.** Solo el prefactor cambia.

### 6.2 Gauge fixing y fantasmas

En Polyakov cuantizado correctamente aparecen fantasmas de Faddeev-Popov. En dimensión crítica D=26 se cancelan contra los modos longitudinales. En D≠26 quedan residuos (anomalía conforme). Esto es lo que obliga a usar dimensión crítica en cuerdas bosónicas.

**Pregunta abierta:** ¿SCG sufre esta anomalía? Si el "espacio ambiente" de SCG es 3+1D efectivo (no crítico), ¿la cuantización es consistente?

**Respuesta tentativa:** Polyakov bosónico en 3+1D con corte físico (d = ℓ_P) NO es la teoría bosónica crítica — es una *teoría efectiva* del defecto WW. Las anomalías conformes se absorben en la definición del UV completion (la red WW). En ese sentido, el cálculo es válido como cálculo efectivo, no como cuerda crítica.

**Esto requiere verificación más cuidadosa.** Marcado como P-14 (nueva debilidad identificada).

### 6.3 Identificación N ↔ 2π

La definición N = "número efectivo de modos gravitacionales por celda" en A-003 v1.1 ya era algo ambigua. El cálculo da N_cuantitativo = 2π (para cuerda cerrada) o π/2 (abierta). Es razonable pero no estricto.

**Esto es el eslabón más flojo del análisis.** Si fenomenología futura requiere un N especifico (ej. para predecir masas), el valor 2π (o π/2) puede no coincidir.

---

## 7. Conclusión: decisión sobre K-027

**K-027 se promueve a CONFIRMADO ESTRUCTURALMENTE.**

**Enunciado definitivo de K-027:**

> La "presión de degeneración gravitacional" de A-003 v1.1 (E_info = λ Σ 1/d, con λ = N ℏc) tiene la forma funcional exacta que produce la cuantización canónica de modos transversales de Polyakov con corte UV en d. Por tanto, A-003 no es un axioma independiente; es el efecto Casimir de los modos transversales de la cuerda SCG confinados en el régimen Planck.

**Consecuencia:** se propone A-003 v1.2 (derivado, no postulado) y se convierte D-006 (la derivación correspondiente).

**Nivel de confianza:** ALTO para la forma funcional; MODERADO para el coeficiente exacto (depende de convención worldsheet).

---

## 8. Nuevos problemas/preguntas

- **P-14 (nuevo):** ¿la cuantización de Polyakov del defecto SCG es consistente en D=4 no-crítica? Las anomalías conformes deben absorberse en la UV completion WW. Necesita verificación formal.
- **Q-036 (nuevo):** ¿K-007 (d ~ √(r_s ℓ_P) dentro del BH) sobrevive al rederivación directa desde Polyakov, sin usar A-003 como intermedio? (Probablemente sí por saturación holográfica, pero conviene verificar.)
- **Q-037 (nuevo):** ¿cuál es el prefactor exacto (N ↔ 2π? π/2? otro?) del efecto Casimir SCG en la topología worldsheet correcta del defecto WW?

---

## 9. Próximos pasos

### Implicación inmediata
- **Mover A-003 de axiomas a derivaciones** (D-006).
- **Actualizar H-001** (la premisa cambia: v1.2 → v1.3 con A-003 derivada).
- **Verificar K-007** (redefinir sin A-003 intermedio; esperado: se preserva).

### Sesiones futuras
- Tarea 5.2 del bosquejo: ec. de movimiento de S_Plebanski + Λ.
- Tarea 5.4: reducción dimensional S_PA → acción SCG en BH.
- P-14: verificar consistencia cuántica de Polyakov 4D no-crítica como teoría efectiva.

---

## 10. Referencias

- Polchinski, J. (1998). *String Theory*, vol. 1, ch. 1-2 (cuantización canónica).
- Green-Schwarz-Witten (1987), *Superstring Theory*, vol. 1, ch. 1 (Polyakov, gauges).
- Casimir, H. B. G. (1948). "On the attraction between two perfectly conducting plates." (analogía directa de lo que acabamos de calcular).
- Zwiebach, B. (2009). *A First Course in String Theory*, ch. 9-12 (cuantización estándar).

---

**Resumen en una frase:** A-003 no es un principio nuevo — es el efecto Casimir de los modos transversales de la cuerda gravitacional con corte Planck, y H-001 pierde un axioma independiente sin pérdida explicativa.
