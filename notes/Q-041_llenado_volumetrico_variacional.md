# Q-041 — Derivación variacional del llenado volumétrico (A2)

- **Fecha:** 2026-04-21 (sesión 20)
- **Pregunta abordada:** ¿cómo emerge L·d² ≈ V_BH (ansatz A2 de D-008) desde un principio variacional?
- **Relación con K-031:** si el ansatz se deriva, K-031 (candidato, sesión 18) se promueve a confirmado estructuralmente.
- **Relación con P-8:** cierra la pieza más débil de la Tarea 5.4 del bosquejo.
- **Nivel de ambición:** argumento variacional cualitativo (minimización bajo restricciones). Factores O(1) no se cierran.

---

## 0. Planteamiento

En D-008 (sesión 18) se hizo la reducción dimensional S_PA → S_SCG-2D bajo tres ansatz:
- A1 (worldsheet 2D).
- **A2 (llenado volumétrico):** L·d² ≈ V_BH.
- A3 (saturación entrópica): S_cuerda = S_BH. Derivada de D-007 + frontera, no ansatz.

A2 fue la pieza NO-derivada. Q-041 pregunta si A2 emerge de un principio de minimización.

**Hipótesis de trabajo:** la configuración de cuerda plegada de mínima energía total, bajo la restricción geométrica de confinamiento V_cuerda ≤ V_BH, **satura** la desigualdad. Es decir, A2 es consecuencia variacional, no postulado adicional.

---

## 1. Funcional energético total

Identificamos cuatro contribuciones a la energía total de la cuerda plegada en el BH:

### 1.1 Término Casimir (D-006)

```
E_Casimir(L, d) = 2π ℏc · L / d²                                       (1.1)
```

Positiva. Diverge cuando d → 0. Es la "presión cuántica de exclusión" que impide colapso infinito.

### 1.2 Término de tensión (Nambu-Goto)

En teoría de cuerdas estándar, la tensión μ = 1/(2π α') con α' = ℓ_s² (longitud de cuerda al cuadrado). Para la cuerda SCG como defecto Walker-Wang:
```
α' ~ d²     (identificación efectiva: la escala de cuerda es el grosor transversal)
⇒ μ(d) ~ 1/d²                                                          (1.2a)
```

Por lo tanto:
```
E_tens(L, d) = μ(d) · L ~ ℏc L / d²                                    (1.2b)
```

**Observación importante:** tanto E_Casimir como E_tens dependen como L/d². La suma es:
```
E_Cas + E_tens = (2π + 1) · ℏc L/d² · (factores O(1))                  (1.2c)
```

Mismo escalamiento funcional. Ambos empujan d → grande.

### 1.3 Término gravitacional (autointeracción)

La cuerda plegada ES el contenido de masa del BH. Su energía gravitacional de autoatracción es capturada globalmente por la masa ADM:
```
E_grav_total = -G M² / r_s = -(1/2) M c²                               (1.3a)
```

**Esto es constante en d y en L** (una vez fijada M). No contribuye a la derivada respecto a d:
```
∂E_grav/∂d = 0     (a M fija)                                          (1.3b)
```

La energía gravitacional entra como "fondo fijo", no como fuerza dinámica sobre el plegado.

### 1.4 Restricción de confinamiento

La cuerda plegada ocupa efectivamente un volumen efectivo V_cuerda = L·d² (cilindro de longitud L y sección transversal d²). Debe caber dentro del BH:
```
L · d² ≤ V_BH                                                          (1.4)
```

Esta es restricción geométrica genuina: la cuerda no puede estar fuera del horizonte porque por definición el interior del BH es donde vive.

### 1.5 Funcional lagrangiano extendido

Con multiplicador de Lagrange λ para la restricción (1.4):

```
L(L, d; λ) = E_Cas(L,d) + E_tens(L,d) + E_grav + λ · (L·d² − V_BH)    (1.5)
```

La restricción es activa cuando λ ≠ 0 en el óptimo.

---

## 2. Análisis variacional

### 2.1 Variación respecto a d (L fija por saturación entrópica)

Derivamos (1.5) respecto a d:
```
∂L/∂d = −2 · (2π + 1) · ℏc L/d³ + 0 + 2 λ L d
      = 2 L · [ −(2π+1) ℏc/d³ + λ d ]                                  (2.1)
```

En el óptimo (∂L/∂d = 0):
```
λ = (2π+1) ℏc / d⁴                                                      (2.2)
```

**λ > 0.** La restricción es activa: físicamente, λ representa la "presión de confinamiento geométrico" que ejerce el horizonte sobre la cuerda.

### 2.2 Interpretación

Sin restricción (1.4), el sistema preferiría d → ∞ (para minimizar E_Cas + E_tens, ambos ~ 1/d²). La existencia del horizonte del BH impone que la cuerda no pueda expandirse más allá de V_BH. Por tanto la configuración de mínima energía es la que satura el volumen:

```
L · d² = V_BH                                                          (2.3)
```

**Esto es A2 derivado.** No ansatz — consecuencia variacional.

### 2.3 Combinación con saturación entrópica (A3)

De D-007 + frontera, la entropía del BH es S_BH = A/(4ℓ_P²) = 4πN². La densidad entrópica de la cuerda como defecto WW es 1 bit/ℓ_P (D-003 v1.2). Saturación S_cuerda = S_BH:

```
L = 4π N² ℓ_P = π r_s² / ℓ_P                                           (2.4)
```

### 2.4 Equilibrio: K-007 emerge

Sustituyendo (2.4) en (2.3) con V_BH = (32π/3) N³ ℓ_P³:

```
d² = V_BH / L = (32π/3 · N³ ℓ_P³) / (4π N² ℓ_P) = (8/3) N ℓ_P²
d² = (8/3) · (r_s/(2 ℓ_P)) · ℓ_P² = (4/3) r_s ℓ_P                      (2.5)

d ≈ √(r_s · ℓ_P) = **K-007**
```

**K-007 emerge como consecuencia variacional de minimizar E_total bajo restricciones, sin ansatz A2 adicional.**

---

## 3. ¿Es A2 estrictamente saturada?

### 3.1 Pregunta sutil

El argumento variacional muestra que el mínimo de E está en el borde de la restricción (L·d² = V_BH). Pero:
- ¿Es realmente un mínimo global, no solo un óptimo local?
- ¿Hay configuraciones alternativas (no-cilíndricas, fractales) que den menor energía?

### 3.2 Respuesta parcial

**Para configuraciones cilíndricas ideales:** el argumento es correcto. La geometría "cuerda plegada uniforme con grosor constante" llena V_BH densamente, y esa es la configuración de mínima energía bajo (1.1)-(1.4).

**Para configuraciones alternativas** (cuerda con grosor variable, fractales, etc.): el argumento requeriría extensión. Concretamente:
- Un grosor variable d(σ,τ) podría reducir E_Cas localmente en regiones grandes, pero pagar en regiones delgadas. El balance global sobre σ, τ probablemente da el mismo resultado — grosor uniforme es óptimo por convexidad del funcional Casimir.
- Configuraciones fractales tendrían dimensiones intermedias entre 1D y 3D. Su análisis energético requiere renormalización de las integrales — tarea técnica no abordada aquí.

**Asunción adicional (tácita):** la configuración cilíndrica uniforme es el mínimo global. Esto no se demuestra, pero es consistente con D-001 (modelo discreto) y con la imagen holográfica (saturación Bekenstein).

### 3.3 Factor de empaquetamiento O(1)

En (1.4) se escribió L · d² ≤ V_BH con igualdad en el óptimo. En realidad:
```
L · d² = (factor de empaquetamiento) · V_BH                             (3.3.1)
```

El factor depende de la geometría precisa del plegado (empaquetamiento óptimo de cilindros en esfera). Para plegado "cuadrado" (bobinado cilíndrico), factor ≈ 1. Para plegado óptimo al estilo Kepler (esferas dispuestas), factor ≈ π/(3√2) ≈ 0.74.

**En nuestra convención (D-003 v1.2, D-008):** factor = 1 estricto. Esto introduce un factor O(1) en K-007 que no hemos cerrado rigurosamente.

---

## 4. ¿Promoción de K-031 a confirmado?

### 4.1 Lo que Q-041 establece

1. **A2 emerge variacionalmente bajo tres asunciones controladas:**
   - (i) Funcional energético total es E_Cas + E_tens + E_grav (constantes) + restricción.
   - (ii) E_Cas + E_tens son monotónicamente decrecientes en d (ambas van como 1/d²).
   - (iii) Configuración cilíndrica uniforme es mínimo global (asunción tácita).
2. **La restricción L·d² ≤ V_BH está activa en el óptimo** (multiplicador λ > 0, interpretable como presión de confinamiento geométrico).
3. **K-007 emerge como consecuencia variacional**, no ansatz adicional.

### 4.2 Lo que Q-041 NO establece

1. **Configuración cilíndrica uniforme es mínimo global:** asunción. Alternativas fractales/variables no exploradas.
2. **Factor de empaquetamiento O(1)** no cerrado. En K-007 hay un factor (4/3) que puede cambiar bajo empaquetamiento Kepler-óptimo.
3. **Dependencia de μ(d):** asumí μ ~ 1/d² como en cuerdas estándar. En SCG, la relación α' ~ d² es razonable pero no derivada.
4. **Ausencia de otras contribuciones:** podría haber términos sub-dominantes (curvatura de la worldsheet, etc.) que afecten el balance fino.

### 4.3 Decisión

**K-031 se promueve de candidato a "confirmado estructuralmente"** con los caveats anteriores. El argumento variacional cierra el ansatz principal A2; las asunciones residuales (plegado cilíndrico uniforme; factor de empaquetamiento) son subordinadas al argumento principal.

**Q-041 se cierra parcialmente.** Lo que queda abierto es cuantificación fina (factores O(1) y alternativas topológicas).

### 4.4 Formalización

**Sí merece D-009.** El argumento tiene estructura de derivación (funcional + restricciones + extremo), aunque con asunciones explícitas.

---

## 5. Implicaciones

- `memory/key_insights.md`: **K-031 pasa de candidato a confirmado** (estructural; mismo nivel que K-029).
- `notes/R_lagrangiana_bosquejo.md`: sub-tarea 5.4 pasa de "parcial con K-031 candidato" a "confirmada estructuralmente con K-031 confirmado". A2 derivado como D-009.
- `memory/open_questions.md`: Q-041 parcialmente cerrada (A2 derivado; factores O(1) y alternativas topológicas pendientes).
- `logic/refutations/debilidades_H-001.md`: P-8 refinada; 3/5 cerradas + 2/5 parciales (cambio de 2/5+3/5 a 3/5+2/5).

---

## 6. Relación con literatura

- **Chandrasekhar (1931, 1935):** configuraciones de equilibrio de enanas blancas por balance presión de degeneración vs gravedad. Análogo directo al argumento aquí (Casimir cuántica vs confinamiento geométrico).
- **Oppenheimer-Volkoff (1939):** estrellas de neutrones. Misma lógica.
- **Polchinski (1998):** α' ~ ℓ_s², identificación usada aquí.
- **Mathur fuzzballs:** la imagen de interior-lleno es análoga; aquí derivado variacionalmente.
- D-006, D-007, D-008 (internos).

---

## 7. Honestidad epistémica

**Lo que es argumento cerrado:**
- Monotonicidad de E_Cas + E_tens en d.
- Restricción activa en el óptimo.
- Saturación (L · d² = V_BH) como consecuencia variacional.

**Lo que es asunción tácita:**
- Plegado cilíndrico uniforme óptimo.
- μ(d) ~ 1/d² (α' ~ d²).
- Factor de empaquetamiento ≈ 1 estricto.

**Lo que no se aborda:**
- Alternativas topológicas al plegado cilíndrico (fractales, toros anidados, etc.).
- Cálculo riguroso del factor O(1) de empaquetamiento.
- Estabilidad dinámica de la configuración (Q-017, P-7.1 siguen abiertas).

---

## 8. Conclusión

**Q-041 parcialmente resuelta.** El ansatz A2 (llenado volumétrico) emerge variacionalmente bajo minimización de E_total sujeta a la restricción geométrica del horizonte. **K-031 se promueve de candidato a confirmado estructuralmente.** **D-009 formaliza el argumento.**

La imagen física: la cuerda SCG plegada es **el análogo cuántico-gravitacional de una enana blanca**. La presión cuántica de Casimir (análoga a la degeneración electrónica) balancea el confinamiento geométrico (análogo a la gravedad). El equilibrio es d ~ √(r_s ℓ_P).

**P-8 refinada:** 3/5 sub-tareas del bosquejo ahora cerradas o con resultado estructural sólido; 2/5 parciales restantes (5.3 → K-030 candidato sigue por promover; 5.5 → K-032 candidato sigue por promover).

Próximo paso natural de la Ruta A: **Q-039** (cuantificar Λ_UV en régimen I) — promovería K-030 si Λ_UV > 384 M_P². O **matching II→IV** explícito — promovería K-032.
