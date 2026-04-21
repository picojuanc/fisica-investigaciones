# Análisis: constantes de acoplamiento en el marco SCG

**Fecha:** 2026-04-19 (sesión 10)
**Pregunta:** ¿Son las constantes de acoplamiento del SM consistentes con el marco SCG, donde SU(2) y SU(3) tienen origen geométrico/gravitacional?

---

## 1. Datos: acoplamientos del SM a la escala de Planck

### Valores medidos (PDG 2024, escala M_Z = 91.19 GeV)

| Cantidad | Valor | 1/α_i |
|---|---|---|
| α_EM(M_Z) | 1/127.95 | — |
| sin²θ_W(M_Z) | 0.23122 | — |
| α_s(M_Z) | 0.1180 | 8.47 |
| α₁(M_Z) [GUT] | 0.01695 | 59.00 |
| α₂(M_Z) | 0.03381 | 29.57 |
| α₃(M_Z) | 0.1180 | 8.47 |

### Running a 1 loop (SM, 3 generaciones, 1 Higgs)

Coeficientes: b₁ = −41/10, b₂ = +19/6, b₃ = +7
(Convención: α_i⁻¹(μ₂) = α_i⁻¹(μ₁) + b_i/(2π) × ln(μ₂/μ₁))

Con ln(M_P/M_Z) = 39.44:

| Factor | α_i⁻¹(M_Z) | Δ(α_i⁻¹) | α_i⁻¹(M_P) | **α_i(M_P)** |
|---|---|---|---|---|
| U(1)_Y | 59.00 | −25.73 | 33.27 | **0.0301** |
| SU(2)_L | 29.57 | +19.87 | 49.44 | **0.0202** |
| SU(3)_c | 8.47 | +43.93 | 52.40 | **0.0191** |

### Resultado clave

```
α₂(M_P) ≈ 0.020
α₃(M_P) ≈ 0.019
α₁(M_P) ≈ 0.030
```

**α₂ y α₃ casi convergen a la escala de Planck.** α₁ queda aparte.

(Nota: esto es un hecho conocido del SM — la "near-miss" de unificación gauge sin SUSY. En el MSSM convergen exactamente a M_GUT ~ 2×10¹⁶ GeV.)

---

## 2. ¿Qué predice el marco SCG?

### Predicción cualitativa

En el marco SCG:
- **SU(2)_L** viene de la conexión gravitacional de Ashtekar → su acoplamiento debe estar relacionado con G.
- **SU(3)** viene de Z₃ + quiralidad → mismo origen geométrico que SU(2) → acoplamiento similar.
- **U(1)_Y** viene de los modos transversales → origen diferente → acoplamiento independiente.

**Predicción:** α₂(M_P) ≈ α₃(M_P), con α₁(M_P) diferente. ✓ (cualitativamente confirmado)

### Predicción cuantitativa: ¿cuánto vale α a M_P?

En D-004 y E-009, asumimos "CS a nivel k=1 en la escala de Planck" (acoplamiento fuerte). Pero el RG running del SM da α ≈ 0.02 a M_P, que es **perturbativo**, no fuerte.

Esto genera una **tensión**: si k=1, α debería ser O(1). Pero α ≈ 0.02 implica k ~ 300.

---

## 3. La coincidencia del parámetro de Immirzi

### Dato

El parámetro de Immirzi en LQG, fijado por la entropía de BH:

```
γ = 0.2375
```

### Coincidencia numérica

```
γ / (4π) = 0.2375 / 12.566 = 0.01890
```

Comparar con:

```
α₂(M_P) = 0.0202    →  discrepancia: 7%
α₃(M_P) = 0.0191    →  discrepancia: 1%
```

**α₃(M_P) ≈ γ/(4π) al 1%.** α₂(M_P) está a un 7%.

### ¿Coincidencia o conexión?

**Argumentos a favor de conexión:**
1. En LQG, γ determina el espectro de área: a₀ = 8πγ l_P². Es el parámetro que relaciona la geometría cuántica con la gravedad clásica.
2. Si el acoplamiento gauge a la escala de Planck es α = γ/(4π), esto significaría que el gap de área del espacio-tiempo determina la intensidad de las fuerzas gauge. Ontológicamente coherente con el marco SCG.
3. El nivel CS correspondiente sería k = 2π/α = 8π²/γ ≈ 332. Nivel grande → semiclásico → perturbativo. Consistente.

**Argumentos en contra:**
1. Hay muchos números O(0.02) que se pueden construir con combinaciones de constantes.
2. La fórmula α = γ/(4π) no se ha derivado — es una observación numérica.
3. El running del SM a 1 loop tiene incertidumbres (2 loops, umbrales, física desconocida entre M_Z y M_P).
4. El valor de γ depende del modelo de BH usado. γ = 0.2375 asume el cálculo de Dreyer/Domagala-Lewandowski con SU(2) y j_min = 1/2.

### Evaluación

**Nivel: SUGERENTE pero NO DERIVADO.** La coincidencia α₃(M_P) ≈ γ/(4π) al 1% merece atención, pero no es una predicción de la teoría (aún). Si se pudiera derivar α(M_P) = γ/(4π) desde primeros principios SCG, sería un resultado cuantitativo mayor.

---

## 4. El problema del acoplamiento gravitacional

### La cuestión central

Si SU(2)_L = SU(2)_gravedad, ¿cómo se explica que G y g_W difieran tan enormemente a bajas energías?

### Lo que dicen Alexander-Marciano-Smolin (PRD 2014)

Reconocen el problema pero argumentan:
1. La identificación se hace a la escala de Planck, donde ambos son O(1).
2. El running desde M_P hasta M_Z los separa.
3. La naturaleza dimensionful de G complica la comparación directa.

**No resuelven el problema cuantitativamente.** Lo dejan abierto.

### Lo que dice Krasnov (CQG 2018)

Identifica g²_grav ~ G·Λ, donde Λ es la constante cosmológica. Con Λ ~ 10⁻¹²² M_P⁴, esto da g²_grav ~ 10⁻¹²². Absurdamente pequeño. El problema de la constante cosmológica aparece disfrazado.

### Nuestra situación

En el marco SCG, la relación es más sutil:
- G determina la escala de Planck (cuándo la red SCG se vuelve relevante).
- g_W determina la intensidad de la interacción SU(2) entre excitaciones topológicas de la red.
- No son el mismo "acoplamiento" en el sentido de QFT. Son manifestaciones diferentes de la misma estructura geométrica.

**Analogía:** en un cristal, la velocidad del sonido y la constante elástica están ambas determinadas por la red cristalina, pero no son "la misma constante". Similarmante, G y g_W podrían estar ambos determinados por la red SCG sin ser numéricamente iguales.

---

## 5. Tensiones y resoluciones

### Tensión 1: k=1 vs k~300

| Lo que asumimos | Lo que el RG da |
|---|---|
| SU(3)₁ a escala Planck (k=1) | α₃(M_P) ≈ 0.019 → k ≈ 330 |
| Acoplamiento fuerte a M_P | Acoplamiento perturbativo |

**Posible resolución:** la escala donde k=1 (CS "puro") no es M_P sino una escala más alta. El "Planck scale" es donde la red SCG se vuelve relevante, pero la transición CS→perturbativo podría ocurrir a una escala sub-Planckiana. Esto es consistente si la red tiene una escala interna menor que l_P.

**Posible resolución alternativa:** k=1 nunca fue correcto. El CS a escala Planck tiene k~300 desde el principio. La derivación de Q-026 (Z₃ + quiralidad → SU(3)₁) no depende estrictamente de k=1 — SU(3)_k con k≥1 también tiene fusión Z₃. Lo que cambia es el espectro de anyones.

**Evaluación de impacto:** si k~300, la unicidad de SU(3)₁ (argumento de Q-026) se debilita. A k grande, hay muchas más opciones de orden topológico. Necesitamos un argumento que seleccione SU(3) entre las opciones a k~300. **Esto es un problema serio.**

### Tensión 2: α₁ ≠ α₂ ≈ α₃

| Predicción SCG | Dato |
|---|---|
| U(1) tiene origen diferente → α₁ diferente | α₁(M_P) = 0.030 ≈ 1.5 × α₂ |

**Evaluación:** esto es consistente con el marco SCG, donde U(1) viene de los modos transversales (geometría del segmento, no gravitación). Que α₁ sea similar pero distinto es lo esperado. ✓

### Tensión 3: no hay unificación exacta

Los tres acoplamientos no convergen a un punto en el SM (sin SUSY). En el marco SCG, no necesitan converger — cada uno tiene un origen geométrico diferente. La near-convergencia de α₂ y α₃ se explicaría por su origen común (gravedad/geometría), no por un grupo GUT.

**Evaluación:** la ausencia de unificación GUT estándar es **compatible** con el marco SCG. De hecho, el marco SCG predice que α₂ ≈ α₃ ≠ α₁, lo cual es exactamente lo que el RG running da. ✓

---

## 6. Resultado: un nuevo insight y un nuevo problema

### Resultado positivo (K-023)

El running del SM a 1 loop da α₂(M_P) ≈ α₃(M_P) ≈ 0.02, con α₁(M_P) ≈ 0.03 distinto. Esto es consistente con el marco SCG donde SU(2) y SU(3) tienen origen geométrico común (gravedad + red), mientras que U(1) tiene origen diferente (modos transversales). La near-convergencia no requiere un grupo GUT — se explica por la estructura geométrica unificada de la red SCG.

### Resultado sugerente (observación numérica)

α₃(M_P) ≈ γ_Immirzi/(4π) al 1%. Si esta coincidencia es significativa, sugiere que el acoplamiento gauge a la escala de Planck está determinado por el parámetro de Immirzi — el mismo parámetro que fija el espectro de área en LQG.

### Problema nuevo (P-9)

La asunción de k=1 (CS "puro") a la escala de Planck es inconsistente con el RG running. El nivel efectivo es k~300, no k=1. Esto debilita el argumento de unicidad de Q-026 (Z₃ + quiralidad → SU(3)₁). Necesitamos un mecanismo que seleccione SU(3) entre las opciones a k grande.

---

## 7. Impacto en la teoría

### Lo que se fortalece

- La predicción cualitativa α₂ ≈ α₃ ≠ α₁ es correcta.
- El marco SCG da una explicación natural de la near-convergence que no requiere SUSY.
- La relación con γ_Immirzi abre una ruta hacia predicciones cuantitativas.

### Lo que se debilita

- La asunción k=1 de D-004/Q-026 necesita revisión.
- El argumento de unicidad SU(3)₁ pierde fuerza si k >> 1.
- No hay derivación de por qué α(M_P) = γ/(4π) (es una observación, no una predicción).

### Lo que queda igual

- La cuantización de la carga en 1/3 (Z₃) no depende de k.
- La quiralidad (CS quiral) no depende de k.
- El mecanismo de Higgs (condensación de anyones) funciona para cualquier k.
- La historia dimensional (D-002, H-002, D-005) es independiente de k.

---

## Referencias

- PDG 2024: valores de α_EM, sin²θ_W, α_s.
- Georgi, Quinn, Weinberg 1974: PhysRevLett 33, 451. Coeficientes de running.
- Amaldi, de Boer, Furstenau 1991: PhysLettB 260, 447. Unificación con precisión LEP.
- Alexander, Marciano, Smolin 2014: PRD 89, 065017. Origen gravitacional de la quiralidad.
- Krasnov, Percacci 2018: CQG 35, 143001. Gravedad y unificación.
- Dreyer 2003: PRL 90, 081301. Parámetro de Immirzi γ = 0.2375.
