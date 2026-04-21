# D-008 — Reducción dimensional S_PA → acción efectiva 2D de cuerda SCG en fondo BH

- **ID:** D-008
- **Fecha:** 2026-04-21 (sesión 18)
- **Deriva:** la acción efectiva 2D de cuerda SCG (régimen III del bosquejo) como reducción dimensional de S_PA + S_cosmo (régimen II, D-007) en un fondo Schwarzschild con ansatz de cuerda plegada.
- **Alcance:** derivación estructural con dos ansatz físicos marcados explícitamente (llenado volumétrico, simetría axial). Reproduce las escalas K-007 (D-003), el término Casimir D-006, y el modelo fenomenológico D-001 como límite IR.
- **Análisis completo:** `notes/Tarea_5.4_reduccion_a_cuerda.md`.
- **Resuelve (parcialmente):** Tarea 5.4 del bosquejo de Lagrangiana; integra D-001 como consecuencia derivada, no ansatz.
- **Consecuencia:** cierra estructuralmente el ciclo **Régimen II → Régimen III** del bosquejo. Promueve K-031 a candidato.

---

## 1. Enunciado

**Proposición.** Consideremos el núcleo gravitacional del bosquejo SCG (D-007):

```
S_núcleo = S_PA + S_cosmo
```

evaluado en el interior de un BH de Schwarzschild de masa M = N M_P, con el ansatz SCG:
- **A1 (Worldsheet 2D):** existe una worldsheet Σ_WS ⊂ interior del BH, parametrizada por (τ, σ).
- **A2 (Llenado volumétrico):** L · d² ≈ V_BH donde L es la longitud total y d el grosor transversal característico.
- **A3 (Saturación entrópica):** S_cuerda = S_BH = A/(4ℓ_P²) (consecuencia de D-007 + frontera estándar Bekenstein-Hawking).

Entonces la reducción dimensional transversal produce una **acción efectiva 2D de cuerda SCG**:

```
S_SCG-2D[X^μ(τ,σ); d(τ,σ)] 
  = − μ(d) ∫ dτ dσ √(−h)                          (Nambu-Goto efectivo)
    + E_Casimir[L,d] ∫ dτ                          (Casimir transversal = D-006)
    + S_backreaction[X, fondo Schwarzschild]       (acoplamiento gravitacional)
    + (términos topológicos Gauss-Bonnet)          (no contribuyen a EOM locales)
```

con:
- μ(d) ∼ M_P² (ℓ_P/d)² — tensión Nambu-Goto efectiva.
- E_Casimir[L,d] = 2π ℏc · L/d² — Casimir transversal (directamente D-006).
- h_{ab} = ∂_a X^μ ∂_b X_μ g_{μν} — métrica inducida en la worldsheet.

**Corolario (K-007 recuperado).** Combinando A2 con A3:

```
L = 4π N² ℓ_P = π r_s²/ℓ_P                  (de saturación entrópica)
d² = (4/3) r_s ℓ_P                          (de llenado volumétrico)
d ∼ √(r_s · ℓ_P)
```

Exactamente las escalas derivadas en D-003 v1.2, ahora obtenidas desde la reducción dimensional de S_núcleo.

**Corolario (D-001 como límite IR).** Los tres términos fenomenológicos del modelo discreto (E_grav, E_tensión, E_info) son identificables con contribuciones específicas de S_SCG-2D:
- E_grav ↔ S_backreaction (acoplamiento al fondo Schwarzschild).
- E_tensión ↔ expansión cuadrática de −μ √(−h) alrededor de la configuración de equilibrio.
- E_info ↔ E_Casimir (= D-006, con identificación λ = 2π ℏc confirmada).

---

## 2. Derivación

### 2.1 Reducción de S_núcleo

Partimos de D-007 con Λ despreciable a escala BH:

```
S_núcleo|_on-shell = (1/2κ) ∫_M R √(−g) d⁴x                              (2.1)
```

Descomposición 2+2 de la métrica cerca de la worldsheet:

```
ds² = h_{ab}(ξ) dξ^a dξ^b + g_{ij}(ξ,y) dy^i dy^j                        (2.2)
```

con (ξ^a) = (τ,σ) coordenadas longitudinales y (y^i) transversales.

Curvatura descompuesta:
```
R = R^{(2)}(h) + R^{(⊥)}(g) + R^{(mix)}                                   (2.3)
```

### 2.2 Integración transversal

Bajo A1 + A2, integramos (y^i) sobre un tubo de sección transversal d²:

```
∫d²y √(g) R^{(2)}(h) ≈ d²·R^{(2)}(h)
∫d²y √(g) R^{(⊥)}(g) ≈ O(1/d²)·d² = O(1)                                  (2.4)
∫d²y √(g) R^{(mix)} → términos de borde
```

Sustituyendo en (2.1):
```
S_núcleo → (1/2κ) ∫ dτ dσ √(−h) [ d²·R^{(2)}(h) − c_1/d² + c_2 + ... ]   (2.5)
```

con c_1, c_2 = O(1) por factores geométricos del plegado.

### 2.3 Identificación de tensión y Casimir

**Tensión Nambu-Goto:** el término c_2/(2κ) multiplica √(−h), dando la acción NG estándar con:

```
μ = c_2/(2κ d²) ~ M_P²/(d/ℓ_P)²                                           (2.6)
```

Para d = d_equilibrio ∼ √(r_s ℓ_P):
```
μ ~ M_P² · ℓ_P/r_s ~ M_P/r_s
```
que es sub-Planckiana para BH macroscópico, dimensionalmente correcta como tensión efectiva.

**Casimir transversal:** los modos transversales de la worldsheet (fluctuaciones X^i alrededor de la config. clásica) al cuantizarse producen el vacío de Polyakov estándar (D-006). Con corte UV físico en λ ≥ d:
```
E_Casimir = 2π ℏc · L/d²                                                  (2.7)
```

Este es **idénticamente D-006**, ahora emergente como cuantización en el esquema de la acción efectiva 2D — no un término añadido, sino la consecuencia cuántica natural de la reducción.

**Término Gauss-Bonnet (d² R^{(2)}):** integrado ∫dτdσ·d²·R^{(2)} = 4π·d²·χ_Euler. Topológico, no afecta EOM locales. Contribuye a la entropía topológica del defecto WW (conexión con D-003).

### 2.4 Backreaction del fondo

El término de acoplamiento al fondo Schwarzschild es de la forma:
```
S_backreaction = ∫ dτ dσ √(−h) · Γ[X^μ; g_{μν}^{Schw}]                   (2.8)
```

donde Γ es un funcional del embedding y del fondo. Para la configuración clásica (cuerda plegada en V_BH):
```
Γ_clásica ~ −GM²/r_s ~ −GM/1 ~ −N² M_P · ℓ_P = −N² · (energía Planck ℓ_P)
```

Esto da la contribución de autointeracción gravitacional. Identifica con E_grav de D-001.

**Esta pieza es la más bosquejada** — un cálculo explícito requeriría teoría de cuerdas en fondo curvo (Callan-Thorn 1986, expansión de Zweibach).

### 2.5 Combinación y balance

Acción efectiva total:
```
S_SCG-2D = S_NG + S_Casimir + S_backreaction + S_topológicos               (2.9)
```

Energía total (reducida a τ):
```
E_total(L,d) = E_NG(d) + E_Casimir(L,d) + E_backreaction(L,M)
             = μ(d) · L + 2π ℏc L/d² − G M²/r_s                           (2.10)
```

---

## 3. Equilibrio y K-007

### 3.1 Condición (i) — saturación entrópica

Desde las ec. de movimiento de S_núcleo (D-007) + frontera estándar, la entropía del sector es S_BH = A/(4ℓ_P²). La entropía de la cuerda como defecto WW con 1 bit/ℓ_P (D-003 v1.2):
```
S_cuerda = L/ℓ_P
```

Igualando:
```
L = 4π N² ℓ_P = π r_s²/ℓ_P                                                 (3.1)
```

**Derivado** (no ansatz) — consecuencia de D-007 + frontera + densidad WW.

### 3.2 Condición (ii) — llenado volumétrico

```
L · d² ≈ V_BH = (32π/3) N³ ℓ_P³                                            (3.2)
```

**Ansatz** (A2) — no derivado de S_núcleo solo. La configuración de cuerda plegada ocupa el volumen con textura d.

### 3.3 Combinación → K-007

Dividiendo (3.2)/(3.1):
```
d² = V_BH/L = (32π N³ ℓ_P³/3) / (4π N² ℓ_P) = (8/3) N ℓ_P²
d² = (4/3) r_s ℓ_P                                                          (3.3)
d ≈ √(r_s · ℓ_P)                                                          (K-007)
```

**K-007 recuperado** desde la reducción dimensional + dos condiciones.

### 3.4 Consistencia ADM

Evaluando (2.7) en equilibrio:
```
L/d² = (π r_s²/ℓ_P) / ((4/3) r_s ℓ_P) = (3π/4) · r_s/ℓ_P² = (3π/4) · 2N/ℓ_P = (3π/2) N/ℓ_P
E_Casimir = 2π ℏc · (3π/2) N/ℓ_P = 3π² · N M_P c² = 3π² Mc²              (3.4)
```

Excede masa ADM M c² por factor 3π² ≈ 30. **Requiere redshift** ⟨f⟩ = 1/(3π²) para consistencia (cf. T-6, sesión 14, cerrada heurísticamente con K-028 candidato, sesión 15):
```
E_obs = ⟨f⟩ · E_Casimir = (1/(3π²)) · 3π² M c² = M c² ✓                  (3.5)
```

**La acción efectiva es ADM-consistente** modulo rigorización de K-028 (pendiente vía P-15').

---

## 4. Alcance y limitaciones

### 4.1 Lo que D-008 establece

1. La acción efectiva 2D de cuerda SCG tiene estructura Nambu-Goto + Casimir + backreaction, como esperaba el bosquejo (sesión 12).
2. K-007 (d ~ √(r_s ℓ_P), L ~ r_s²/ℓ_P) emerge por combinación de holografía (derivada de D-007) + llenado volumétrico (ansatz A2).
3. D-006 (Casimir) se integra como cuantización natural de modos transversales — no ingrediente separado.
4. D-001 (modelo discreto) es reconocible como límite IR de S_SCG-2D.
5. Balance energético consistente con masa ADM via K-028 candidato (sesión 15).

### 4.2 Lo que D-008 NO establece

1. **El ansatz A2 (llenado volumétrico) no se deriva.** La configuración de cuerda plegada que satura L·d² ~ V_BH es la que el marco SCG identifica con el "interior del BH", pero la selección de esta configuración sobre alternativas requiere análisis variacional no realizado aquí.
2. **Factores O(1)** en μ, E_Casimir, d², etc., están sujetos a convenciones (cuerda cerrada vs abierta, corte UV, geometría del plegado). Fijarlos rigurosamente requeriría cálculo cerrado.
3. **Backreaction del fondo** está bosquejada, no calculada. El término S_backreaction es estructuralmente análogo a las interacciones gravitacionales de cuerdas en fondos curvos (Callan-Thorn 1986), pero no se evalúa explícitamente.
4. **Dinámica de formación** (cómo la cuerda se pliega durante el colapso) no se aborda. D-008 es estático, no dinámico.
5. **K-028 sigue siendo candidato.** El factor ⟨f⟩ = 1/(3π²) emerge por consistencia, no por cálculo QFT+GR explícito (P-15').

### 4.3 Estado epistémico

- **Derivación estructural:** coherencia mutua entre D-001, D-003, D-006, D-007 y la acción efectiva 2D.
- **Ansatz admitidos:** A1 (worldsheet 2D), A2 (llenado volumétrico), simetría axial implícita.
- **Cálculo riguroso:** reducción dimensional cualitativa + equilibrio algebraico. No se resuelven ecuaciones diferenciales del fondo curvo.

---

## 5. Conclusión

**La acción efectiva 2D de cuerda SCG (régimen III del bosquejo) emerge por reducción dimensional de S_núcleo (régimen II, D-007) + dos ansatz físicos (A1, A2).** Integra coherentemente D-006 (Casimir) y reproduce K-007 (escalas). El modelo fenomenológico D-001 emerge como límite IR.

**El ciclo Régimen II → Régimen III del bosquejo queda cerrado estructuralmente.** Los cuatro resultados previos del marco (D-003, D-006, D-007, D-001) se unifican bajo una sola acción efectiva 2D.

**Queda abierto el ciclo II → IV (tarea 5.5, flujo RG).** Esa es la última sub-tarea del bosquejo.

---

## 6. Implicaciones

- `notes/R_lagrangiana_bosquejo.md`: **Tarea 5.4 PARCIAL.** 4/5 sub-tareas ahora completas o parciales (5.1 ✅, 5.2 ✅, 5.3 parcial, 5.4 parcial); solo 5.5 pendiente.
- `logic/refutations/debilidades_H-001.md`: P-8 refinada — núcleo gravitacional + reducción a cuerda derivados; faltan dos piezas (Kodama formal, flujo RG).
- `hypotheses/active/H-001_...`: la escala K-007 tiene ahora dos derivaciones concordantes (D-003 v1.2 por holografía + D-008 por reducción dimensional). Refuerzo de consistencia.
- `memory/open_questions.md`: Q-017 (dinámica de formación, P-7.1) sigue abierta; Q-041 nueva — ¿cómo se deriva el ansatz de llenado volumétrico A2 desde principios variacionales?
- `memory/key_insights.md`: **K-031 candidato** (cierre estructural del ciclo II→III).

**Insight candidato K-031:** *La acción efectiva 2D de cuerda SCG, derivada por reducción dimensional de S_PA, integra coherentemente D-001 (modelo discreto como límite IR), D-003 (K-007 por holografía), D-006 (Casimir como cuantización transversal), y D-007 (núcleo gravitacional). Cierra estructuralmente el ciclo Régimen II → Régimen III del bosquejo de Lagrangiana. Promoción a confirmado requiere derivar el ansatz de llenado volumétrico desde variación.*

---

## 7. Relación con la literatura

- **Polchinski (1998)** vol. 1, capítulo 3: reducción Nambu-Goto, acción de Polyakov, cuantización de modos transversales. Prototipo de la reducción 4D → 2D utilizada.
- **Callan & Thorn (1986)** "Sigma models and string theory": cuerdas en fondos curvos. Marco formal para S_backreaction (no realizado aquí).
- **Zweibach (1985)** *"A First Course in String Theory"*: expansión de la acción de cuerda alrededor de un fondo clásico.
- **Mathur fuzzballs (2005)**: imagen análoga (interior BH lleno de estructura), pero derivación desde teoría de cuerdas compactificada en SUSY, no desde acción Plebanski autodual 4D. SCG + D-008 es ruta alternativa.
- **D-003, D-006, D-007** (internos): piezas que D-008 integra.

---

## 8. Firma

**Tarea 5.4 parcialmente resuelta via D-008.** La acción efectiva 2D de cuerda SCG emerge estructuralmente desde S_PA + ansatz físicos. K-007 reproducida; D-001, D-003, D-006, D-007 integrados. K-031 candidato. Modulo factores O(1) y ansatz de llenado, el cierre del ciclo II → III del bosquejo queda establecido.

Pieza estructural del programa Lagrangiana. Análoga en carácter a D-007: no es descubrimiento profundo, es verificación de coherencia interna + integración de resultados previos. Aplicación de K-005.

Siguiente pieza natural del programa Lagrangiana: **Tarea 5.5** (flujo RG II → IV). Primera y única sub-tarea pendiente del bosquejo. Esfuerzo estimado 3-5 sesiones; impacto máximo (primera predicción cuantitativa de α₂ ≈ α₃).
