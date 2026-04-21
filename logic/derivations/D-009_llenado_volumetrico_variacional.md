# D-009 — El llenado volumétrico L·d² = V_BH emerge variacionalmente

- **ID:** D-009
- **Fecha:** 2026-04-21 (sesión 20)
- **Deriva:** el ansatz A2 de D-008 (llenado volumétrico, L·d² ≈ V_BH) como consecuencia de minimización de la energía total bajo restricción geométrica.
- **Alcance:** argumento variacional con asunciones explícitas (plegado cilíndrico uniforme; μ ~ 1/d²; factor de empaquetamiento O(1)).
- **Análisis completo:** `notes/Q-041_llenado_volumetrico_variacional.md`.
- **Resuelve (parcialmente):** Q-041; promueve K-031 de candidato a confirmado estructuralmente.
- **Consecuencia:** D-008 deja de depender del ansatz A2 y pasa a ser consecuencia de D-009 + D-007 + saturación entrópica.

---

## 1. Enunciado

**Proposición.** Sea la configuración de cuerda SCG plegada dentro de un BH de masa M = N M_P, radio de Schwarzschild r_s = 2N ℓ_P, volumen V_BH = (32π/3) N³ ℓ_P³. Sea E_total(L, d) la energía total:

```
E_total(L, d) = E_Casimir(L, d) + E_tens(L, d) + E_grav(total)

  E_Casimir = 2π ℏc · L/d²                     (D-006)
  E_tens    = μ(d) · L,   μ(d) ~ ℏc / d²       (α' ~ d² en cuerda SCG)
  E_grav    = −GM²/r_s = −(1/2) Mc²            (constante en L, d)
```

sujeta a la restricción geométrica V_cuerda = L·d² ≤ V_BH (confinamiento por el horizonte).

Entonces el mínimo de E_total a L fija satura la restricción:
```
L · d² = V_BH                                                           (D-009.1)
```

Este es **exactamente A2 de D-008**, ahora derivado como extremo variacional.

**Corolario (combinando con saturación entrópica derivada de D-007 + frontera):**
```
L = 4π N² ℓ_P     (de S_cuerda = S_BH = A/(4ℓ_P²))                    (D-009.2)
d² = V_BH / L = (4/3) r_s ℓ_P      ⇒   d ~ √(r_s · ℓ_P)     (= K-007)
```

K-007 **emerge como consecuencia variacional doble** (ya derivado también en D-003 v1.2 por holografía directa).

---

## 2. Derivación

### 2.1 Monotonicidad de E_total(d) a L fija

Por construcción, E_Casimir = 2π ℏc · L/d² y E_tens = μ(d)·L con μ ~ 1/d². Ambos son decrecientes en d:

```
∂E_Casimir/∂d = −4π ℏc · L/d³ < 0                                     (D-009.3a)
∂E_tens/∂d = −2 ℏc · L/d³ < 0  (coeficiente exacto O(1))              (D-009.3b)
∂E_grav/∂d = 0                  (constante, depende sólo de M)        (D-009.3c)
```

Por tanto:
```
∂E_total/∂d < 0   ∀ d > 0                                              (D-009.4)
```

El mínimo sin restricción es d → ∞. Con restricción (1.4), el mínimo está en el borde.

### 2.2 Restricción activa

Introducimos multiplicador de Lagrange λ para la restricción V_cuerda = L·d² ≤ V_BH:

```
L(L, d; λ) = E_total + λ · (L·d² − V_BH)                              (D-009.5)
```

Condición estacionaria:
```
∂L/∂d = ∂E_total/∂d + 2 λ L d = 0
     ⇒ λ = −(1/(2Ld)) · ∂E_total/∂d                                   (D-009.6)
```

De (D-009.4): ∂E_total/∂d < 0 ⇒ **λ > 0**.

**Interpretación física:** λ > 0 es la "presión de confinamiento geométrico" que ejerce el horizonte sobre la cuerda. Análogo al multiplicador asociado a una partícula confinada en una caja: la pared empuja.

Por complementariedad slackness (condición KKT): si λ > 0, entonces la restricción es igualdad:
```
L · d² = V_BH                                                          (D-009.7)
```

**Q.E.D. de (D-009.1).**

### 2.3 Combinación con saturación entrópica

L fija por saturación entrópica (consecuencia de D-007 + condiciones de frontera Bekenstein-Hawking):
```
L = 4π N² ℓ_P = π r_s²/ℓ_P                                             (D-009.8)
```

Sustituyendo en (D-009.7):
```
d² = V_BH / L = (32π/3 · N³ ℓ_P³) / (4π N² ℓ_P) = (8/3) N ℓ_P²
   = (4/3) r_s ℓ_P                                                     (D-009.9)
```

→ **K-007** reproducido.

---

## 3. Alcance y limitaciones

### 3.1 Lo que D-009 establece

1. **A2 (llenado volumétrico) emerge variacionalmente.** No es ansatz; es consecuencia de minimización.
2. **K-031 se promueve de candidato a confirmado estructuralmente.** La derivación D-008 deja de depender de un ansatz sin base.
3. **Imagen física clara:** la cuerda SCG es el análogo cuántico-gravitacional de una enana blanca. La presión de Casimir balancea el confinamiento geométrico del horizonte.
4. **Doble derivación de K-007:** D-003 v1.2 por holografía + D-008/D-009 por reducción dimensional variacional.

### 3.2 Lo que D-009 NO establece

1. **Configuración cilíndrica uniforme como mínimo global.** Asunción tácita: el plegado óptimo es cilíndrico uniforme, no fractal o variable. Alternativas no exploradas.
2. **Factor de empaquetamiento O(1):** en rigor L·d² = (factor) · V_BH con factor ≈ 0.74 (Kepler) o 1 (cuadrado). Convención: factor = 1.
3. **Dependencia μ(d) ~ 1/d²:** asumido por analogía con teoría de cuerdas estándar (α' ~ ℓ_s²). No derivado explícitamente desde S_PA.
4. **Términos sub-dominantes:** posibles contribuciones (curvatura worldsheet, acoplamientos al fondo Schwarzschild sub-dominantes) no incluidos.
5. **Estabilidad dinámica:** D-009 es estático. La formación dinámica de la cuerda plegada (Q-017, P-7.1) sigue abierta.

### 3.3 Estado epistémico

- **Derivación estructural:** argumento de optimización con restricciones. KKT estándar.
- **Asunciones tácitas:** plegado cilíndrico + μ ~ 1/d² + factor O(1).
- **Cálculo riguroso:** minimización es estándar; los factores O(1) son sub-dominantes al argumento.

---

## 4. Conclusión

**A2 de D-008 se deriva variacionalmente via D-009.** La cuerda SCG plegada es el mínimo de energía bajo restricción de confinamiento geométrico — análogo cuántico-gravitacional de la enana blanca.

**K-031 pasa de candidato a confirmado estructuralmente.** La reducción de S_PA a cuerda SCG (D-008) ya no depende de un ansatz sin justificación; depende de una derivación variacional controlada.

---

## 5. Implicaciones

- `memory/key_insights.md`: K-031 promovido a confirmado estructuralmente.
- `notes/R_lagrangiana_bosquejo.md`: sub-tarea 5.4 pasa de "parcial" a "confirmada estructuralmente con asunciones menores". Arquitectura de la Lagrangiana: 3/5 sub-tareas confirmadas (5.1, 5.2, 5.4) + 2/5 parciales (5.3, 5.5).
- `memory/open_questions.md`: Q-041 cerrada parcialmente. Residuales: alternativas topológicas al plegado cilíndrico; factor de empaquetamiento exacto.
- `logic/refutations/debilidades_H-001.md`: P-8 refinada. 3/5 completas/confirmadas estructuralmente + 2/5 parciales.

---

## 6. Relación con literatura

- **Chandrasekhar (1931, 1935):** balance presión degeneración ↔ gravedad en enanas blancas. Modelo análogo directo.
- **Oppenheimer-Volkoff (1939):** estrellas de neutrones. Misma lógica balance-por-restricción.
- **Polchinski (1998)** vol. 1: α' ~ ℓ_s².
- **Mathur fuzzballs:** imagen de interior-lleno análoga; D-009 deriva variacionalmente lo que fuzzballs postula.
- **Karush-Kuhn-Tucker (1951):** optimización con restricciones. Estándar.
- D-006, D-007, D-008 (internos).

---

## 7. Firma

D-009 cierra el ansatz A2 de D-008 variacionalmente. Promueve K-031 a confirmado estructuralmente. La cuerda SCG plegada = enana blanca cuántica (Casimir vs horizonte). Arquitectura Lagrangiana SCG: 3/5 sub-tareas con resultado estructural sólido; solo 5.3 y 5.5 quedan como "parciales con candidato".

Siguiente pieza natural: Q-039 (cuantificar Λ_UV en régimen I → promueve K-030) o matching II→IV explícito (→ promueve K-032).
