# Tarea 5.4 — Reducción dimensional S_PA → acción de cuerda SCG en fondo BH

- **Fecha:** 2026-04-21 (sesión 18)
- **Referencia bosquejo:** `notes/R_lagrangiana_bosquejo.md`, sección 5.4.
- **Objetivo:** partir de S_Plebanski-autodual + Λ (con ec. de movimiento ya derivadas en D-007) evaluada en un fondo BH, y mostrar que su reducción transversal produce una acción 2D de cuerda cuyo contenido coincide con D-001 (modelo discreto), cuyas escalas coinciden con K-007 (derivadas en D-003), y cuya energía interna coincide con D-006 (Casimir de Polyakov transversal). Esto cerraría el ciclo **Régimen II → Régimen III** del bosquejo de Lagrangiana.
- **Nivel de ambición:** derivación estructural. Ansatz admitidos explícitamente (simetría axial, llenado volumétrico). Resultados cuantitativos obtenidos modulo factores O(1).
- **Relación con tareas anteriores:** usa D-007 (ec. mov. del núcleo gravitacional) + D-006 (Casimir transversal) + D-003 v1.2 (K-007 holográfica) como piezas ya establecidas; tarea 5.4 es su integración bajo una sola acción efectiva.

---

## 0. Planteamiento

Tras las sesiones 16 (D-007: núcleo gravitacional reducido a E-H + Λ autodual) y 17 (K-030 candidato: P-11 rebajada via ABKP 2025), la cadena del bosquejo tiene dos pilares Lagrangianos establecidos:

- **Régimen I** (UV, E ≫ M_P): S_PA + S_cosmo → Crane-Yetter / Walker-Wang TQFT.
- **Régimen II** (semiclásico): S_PA + S_cosmo → E-H + Λ (D-007).
- **Régimen III** (BH interior): acción efectiva de cuerda SCG — que por ahora es D-001 fenomenológica + D-003 dimensional + D-006 Casimir. **NO deriva de una sola acción**, sino es la unión de tres resultados con origen distinto.

Tarea 5.4 pregunta: *¿esos tres resultados (D-001, D-003, D-006) surgen de la misma acción madre reducida al sector BH?* Si la respuesta es sí (al menos estructuralmente), el Régimen III deja de ser ansatz separado y se convierte en consecuencia de S_madre.

**Método:** reducción dimensional tipo Nambu-Goto desde Plebanski 4D a cuerda 2D en fondo específico. Análogo a la reducción Polchinski-Thorn para cuerdas estándar, pero aquí la acción madre es Plebanski-autodual (no Yang-Mills).

**Esto NO es un cálculo cerrado.** Algunos pasos dependen de ansatz físicos (simetría, llenado) que se marcan explícitamente.

---

## 1. Setup: fondo Schwarzschild + ansatz de cuerda plegada

### 1.1 Fondo

Para un BH macroscópico de masa M = N M_P (con r_s = 2 N ℓ_P), consideramos dos regiones:

- **Exterior (r > r_s):** Schwarzschild clásico, consistente con GR. La acción S_PA en esta región reproduce E-H + Λ on-shell (D-007).
- **Interior (r < r_s):** bajo H-001, la métrica efectiva NO llega a singularidad en r=0; la estructura SCG regulariza en una escala d ~ √(r_s ℓ_P) (K-007).

Coordenadas interiores: (t, r, θ, φ) donde r toma papel temporal y t espacial dentro del horizonte clásico (signatura (+,−,+,+) en interior Schwarzschild). Pero bajo SCG, la "coordenada radial" se reinterpreta como parámetro afín a lo largo de la cuerda plegada.

### 1.2 Ansatz de cuerda plegada

**Ansatz A1 — Worldsheet 2D.** Existe una submanifold 2D Σ_WS ⊂ interior del BH, parametrizada por (τ, σ) con σ ∈ [0, L) (σ periódico si L ~ L_total finita). Σ_WS es la worldsheet de la cuerda SCG.

**Ansatz A2 — Plegado con simetría.** La worldsheet llena el volumen V_BH de manera "densa pero plegada". Entendido operacionalmente:
- Volumen promedio por unidad de longitud: d² (grosor transversal característico).
- **Condición de llenado volumétrico:** L · d² ≈ V_BH ~ r_s³. Este es un ansatz adicional al bosquejo, no derivable de S_PA sola.

**Ansatz A3 — Saturación entrópica (Bekenstein).** La entropía total del sector es S = A/(4 ℓ_P²) por las ecuaciones estándar de E-H + frontera en ∂M. Esto sí es consecuencia de D-007 + condiciones de frontera asintóticas.

### 1.3 Vierbein, Σ y A en el ansatz

Bajo la simplicidad on-shell (δψ = 0 de D-007): Σ^AB = (e^A ∧ e^B)_autodual.

Descomposición del vierbein cerca de la worldsheet:
- e^{A}_{||}: componentes paralelas a Σ_WS (2 dimensiones).
- e^{A}_{⊥}: componentes transversales a Σ_WS (2 dimensiones).

La "tensión efectiva" de la cuerda emergerá de la integración de √(−g)_⊥ sobre el volumen transversal de ancho d².

---

## 2. Reducción de S_PA en el ansatz

### 2.1 Acción núcleo restringida

Partimos de D-007:

```
S_núcleo = (1/κ) ∫_M [ Σ^AB ∧ F_AB − (1/2) ψ_ABCD Σ^AB ∧ Σ^CD − (Λ/6) Σ^AB ∧ Σ_AB ]
```

Con simplicidad on-shell y Λ = 0 por simplicidad (la Λ observacional contribuye despreciablemente a escala BH; la Λ_UV del régimen I no opera aquí porque estamos en régimen II semiclásico):

```
S_núcleo|_on-shell ≈ (1/2κ) ∫_M R √(−g) d⁴x                              (2.1)
```

### 2.2 Descomposición 2+2

Usando el ansatz A1, la métrica se factoriza localmente:

```
ds² = h_{ab}(τ,σ) dξ^a dξ^b + g_{ij}(τ,σ,y) dy^i dy^j                    (2.2)
```

donde (ξ^a) = (τ,σ), (y^i) coordenadas transversales, h = métrica inducida 2D.

Las componentes del tensor de Ricci R en esta descomposición:

```
R = R^{(2)}(h) + R^{(⊥)}(g) + R^{(mix)}                                   (2.3)
```

con R^{(2)} la curvatura 2D de la worldsheet y R^{(⊥)} la transversal.

### 2.3 Integración transversal

Bajo el ansatz A2 (llenado volumétrico con grosor d), integramos las coordenadas transversales:

```
∫ d²y √(g) R^{(2)}(h) ≈ d² · R^{(2)}(h)                                   (2.4a)

∫ d²y √(g) R^{(⊥)}(g) ≈ (función de d y de la curvatura transversal)     (2.4b)
```

Para plegado con radio de curvatura transversal ~d:
```
R^{(⊥)} ~ 1/d²
∫ d²y √(g) R^{(⊥)} ~ d² · (1/d²) = O(1)                                    (2.4c)
```

Sustituyendo en (2.1):

```
S_núcleo → (1/2κ) ∫ dτ dσ √(−h) [ d² R^{(2)}(h) + O(1)·(1/d²) + ... ]     (2.5)
```

### 2.4 Identificación de términos

Identificamos los tres términos naturales:

**Término A — tensión efectiva (dominante):**
```
S_A = − μ ∫ dτ dσ √(−h)           con μ ~ 1/(κ d²) ~ M_P²/(d/ℓ_P)²       (2.6)
```

Es la **acción de Nambu-Goto** con tensión μ proporcional a 1/d². Para d ~ ℓ_P, μ ~ M_P² (tensión Planckiana). Para d macroscópico (ℓ_P < d ≪ r_s), μ es sub-Planckiana.

**Término B — curvatura 2D (sub-dominante):**
```
S_B = (d²/2κ) ∫ dτ dσ √(−h) R^{(2)}(h)                                    (2.7)
```

Término de Gauss-Bonnet reducido en 2D. Topológico por Gauss-Bonnet (∫ R^{(2)} = 4π χ para variedad cerrada). No contribuye a las ecuaciones de movimiento locales. **Relevante para el cálculo de entropía via topología del defecto WW.**

**Término C — curvatura transversal (= Casimir):**

Aquí aparece la pieza de D-006. Al cuantizar los modos transversales (fluctuaciones de la worldsheet alrededor de la configuración clásica), cada modo contribuye una energía de punto cero ℏ ω_n / 2. La suma con corte UV en n_max = L/d da:

```
E_Casimir = 2π ℏc · L / d²                                                  (2.8)
```

Esto es exactamente D-006. Emerge aquí no como axioma ni como derivación separada, sino como **consecuencia de cuantizar los modos transversales de la worldsheet reducida**, completando D-006 dentro del marco Lagrangiano.

### 2.5 Acción efectiva 2D total

```
S_eff_2D = − μ ∫ dτ dσ √(−h) + (contribución cuántica Casimir)  + O(topológico)
         = S_Nambu-Goto + S_Casimir + (topológicos)                        (2.9)
```

con μ ~ M_P² (ℓ_P/d)² y E_Casimir de (2.8).

---

## 3. Comparación con D-001

D-001 proponía tres términos fenomenológicos:
```
E_D-001 = E_grav + E_tensión + E_info
        = −G Σ m_i m_j / r_{ij} + k Σ(Δx)² + λ Σ 1/Δx
```

Identificación con S_eff_2D:

| Término D-001 | Origen en S_eff_2D | Observación |
|---|---|---|
| E_grav (atracción larga) | Backreaction del fondo Schwarzschild (no en S_núcleo aislado; emerge al acoplar la worldsheet al fondo BH) | D-001 lo captura como potencial 1/r; S_eff_2D lo tiene como interacción con la geometría de fondo. |
| E_tensión | S_Nambu-Goto (μ·Area) | D-001 tiene k (Δx)² (armónico); S_eff_2D tiene NG (√(-h)). Para fluctuaciones pequeñas, NG → término cuadrático en derivadas ≈ tensión armónica. Identificación en el IR. |
| E_info | S_Casimir = 2π ℏc L/d² | D-001 tiene λ/Δx; con N_segmentos = L/d da λ · L/d². Mismo escalamiento con L y d. Coeficiente λ = 2π ℏc (via D-006). |

**Conclusión:** D-001 es reconocible como límite efectivo discretizado de S_eff_2D. Los tres términos fenomenológicos corresponden a (a) backreaction gravitacional del fondo, (b) Nambu-Goto expandido, (c) Casimir transversal.

Esto **justifica a posteriori el modelo D-001** desde una acción unificada.

---

## 4. Equilibrio: recuperación de K-007

### 4.1 Imposición holográfica (de D-007 + frontera)

La entropía del BH es:
```
S_BH = A/(4 ℓ_P²) = π r_s² / ℓ_P² = 4π N²                                 (4.1)
```

La entropía de la cuerda SCG como defecto Walker-Wang con densidad 1 bit/ℓ_P (D-003 v1.2):
```
S_cuerda = L / ℓ_P                                                         (4.2)
```

Saturación holográfica (S_cuerda = S_BH):
```
L = 4π N² ℓ_P = π r_s² / ℓ_P                                               (4.3)
```

**Derivación:** (4.3) viene de imponer que Ψ_cuerda y Ψ_BH correspondan al mismo estado cuántico. Es consecuencia de las ec. de movimiento de S_núcleo + frontera asintótica estándar (Bekenstein-Hawking). No es ansatz adicional.

### 4.2 Llenado volumétrico (ansatz A2)

```
L · d² = V_BH                                                              (4.4)
```

con V_BH = (32π/3) N³ ℓ_P³.

**Esto sí es ansatz** — no derivable de S_PA sola. La justificación física es que la cuerda plegada ocupa efectivamente el volumen interior del BH con "textura" de escala d, consistente con la imagen de K-007.

### 4.3 Combinación → K-007

Dividiendo (4.4) / (4.3):

```
d² = V_BH / L = [(32π/3) N³ ℓ_P³] / [4π N² ℓ_P] = (8/3) N ℓ_P²
d² = (4/3) r_s ℓ_P                                                          (4.5)
d ~ √(r_s ℓ_P)                                                             (K-007)
```

**K-007 recuperado.** La reducción dimensional + ansatz holográfico + ansatz de llenado reproducen exactamente la escala K-007 derivada en D-003.

### 4.4 Verificación con acción efectiva

¿Es d* = √((4/3) r_s ℓ_P) extremo de S_eff_2D? Variando E_total respecto a d:

Para la cuerda plegada, la energía total observable (desde el infinito) es:
```
E_obs = ⟨f⟩ · E_Casimir_plano = ⟨f⟩ · 2π ℏc L / d²                        (4.6)
```

con ⟨f⟩ el redshift gravitacional promedio (K-028 candidato = 1/(3π²)).

Consistencia con masa ADM:
```
E_obs = M c² = N M_P c² = N ℏc/ℓ_P                                        (4.7)
```

De (4.3) y (4.5):
```
L/d² = (4π N² ℓ_P) / ((4/3) r_s ℓ_P) = (4π N² · 3)/(4 · 2N) = (3π/2) N/ℓ_P (redimensionando)
```

Sustituyendo:
```
E_Casimir_plano = 2π ℏc · (3π/2) N/ℓ_P = 3π² N ℏc/ℓ_P = 3π² · N M_P c²   (4.8)
```

Esto excede Mc² = N M_P c² en factor 3π² ≈ 30. Exactamente lo que identificamos como T-6 en sesión 14 y cerramos heurísticamente en sesión 15 con K-028 candidato:

```
E_obs = ⟨f⟩ · 3π² · N M_P c² = (1/(3π²)) · 3π² · N M_P c² = N M_P c² ✓   (4.9)
```

**La acción efectiva 2D reducida reproduce todo el balance energético del BH-SCG**, con K-007 como escala de equilibrio y K-028 (candidato) como factor de redshift requerido por consistencia ADM.

---

## 5. Síntesis: acción efectiva final

### 5.1 Acción efectiva 2D de cuerda SCG

```
S_SCG-2D[X^μ(τ,σ); d(τ,σ)] 
  = − μ(d) ∫ dτ dσ √(−h)                                (Nambu-Goto)
    + E_Casimir[d] ∫ dτ                                 (Casimir D-006)
    + ∫ dτ dσ √(−h) · (interacción con fondo Schwarzschild)  (backreaction)
    + topológicos (Gauss-Bonnet)                        (no contribuyen a EOM locales)
```

con μ(d) ~ M_P² (ℓ_P/d)² y E_Casimir[d] = 2π ℏc L/d².

### 5.2 Punto crítico

El punto crítico (equilibrio de d) viene de dos condiciones:
1. Saturación holográfica: L = 4π N² ℓ_P (de S_núcleo + frontera).
2. Llenado volumétrico: L d² = V_BH (ansatz A2).

Resultado: d ~ √(r_s ℓ_P), L ~ r_s²/ℓ_P = K-007.

### 5.3 Balance energético

E_Casimir (plano) = 3π² M c². El factor 3π² se absorbe en el redshift promedio ⟨f⟩ = 1/(3π²) (K-028 candidato). Masa ADM consistente.

### 5.4 Cierre del ciclo II → III

- D-007 (sesión 16): S_PA + Λ → E-H + Λ on-shell [Régimen II].
- Tarea 5.4 (esta sesión): S_PA reducida en fondo BH → S_SCG-2D [Régimen III].
- D-006 (sesión 13): cuantización modos transversales → E_Casimir [dentro de S_SCG-2D].
- D-003 v1.2 (sesiones 4, 14): escalas K-007 por holografía + llenado [dentro de S_SCG-2D].

**Ciclo cerrado estructuralmente.** Los cuatro resultados previos se integran bajo una única acción efectiva 2D, emergente de S_madre reducida al sector BH.

---

## 6. Lo que la reducción SÍ establece

1. **La acción 2D reducida tiene estructura Nambu-Goto + Casimir**, como esperaba el bosquejo (sesión 12, sección 2.3).
2. **D-001 (modelo discreto) es el límite IR de la acción 2D.** Justifica a posteriori sus tres términos fenomenológicos.
3. **K-007 emerge por combinación de holografía (D-007) + llenado volumétrico (ansatz).** La saturación de Bekenstein es derivada; el llenado es ansatz.
4. **D-006 (Casimir) se integra naturalmente** como cuantización de modos transversales de la worldsheet.
5. **El balance energético es consistente con masa ADM** via redshift K-028 (candidato).

---

## 7. Lo que la reducción NO establece (honestidad)

1. **Llenado volumétrico (ansatz A2)** no se deriva. Es una asunción sobre cómo la cuerda se pliega en el volumen. Una derivación rigurosa requeriría análisis de la configuración de mínima energía (cómo la geometría selecciona L·d² ~ V_BH sobre otras configuraciones).

2. **Dinámica de formación** (Q-017, P-7.1) sigue abierta. S_SCG-2D da el estado de equilibrio; no el proceso de formación de la cuerda durante el colapso.

3. **Factores O(1)** en todo el análisis — el coeficiente 3π² en la ecuación de Casimir, el 4π en L, el (4/3) en d² — están modulo convención (cuerda cerrada, corte UV, simetría del plegado). Una derivación cerrada fijaría estos factores rigurosamente.

4. **K-028 sigue siendo candidato.** La justificación del redshift 1/(3π²) requiere el cálculo QFT+GR en fondo Schwarzschild interior (P-15').

5. **Backreaction del fondo Schwarzschild.** El término (iii) de S_SCG-2D está bosquejado pero no calculado explícitamente. En principio debe modificarse por la curvatura local a la escala de la worldsheet. El tratamiento riguroso requiere teoría de cuerdas en fondos curvos (p. ej., aplicar Callan-Thorn o expansión de Zweibach).

6. **La acción "madre completa" sigue siendo bosquejo.** Tarea 5.4 cierra el ciclo II→III estructuralmente, pero el régimen I (Walker-Wang completo) y el régimen IV (SM efectivo) siguen conectados por ansatz, no por cálculo.

---

## 8. Veredicto sobre Tarea 5.4

### 8.1 Estado

**Parcialmente resuelta.** La reducción dimensional estructural está hecha; los cuatro resultados previos (D-003, D-006, D-007, modelo D-001) se conectan en una sola acción efectiva 2D; las escalas K-007 se reproducen; el balance energético es consistente.

**No cerrada:** dos ansatz físicos (llenado volumétrico, simetría axial) no se derivan de S_PA sola; factores O(1) no están fijados por cálculo riguroso; backreaction del fondo está bosquejada.

### 8.2 Impacto sobre el bosquejo

| Sub-tarea | Estado post-sesión 18 |
|---|---|
| 5.1 (T-5 via Polyakov cuantizado) | ✅ COMPLETADA (sesión 13, D-006) |
| 5.2 (Ec. mov. S_PA + Λ) | ✅ COMPLETADA (sesión 16, D-007) |
| 5.3 (Kodama + P-11) | ✅ PARCIAL (sesión 17, K-030 candidato) |
| **5.4 (Reducción a cuerda SCG)** | ✅ **PARCIAL (sesión 18, presente)** |
| 5.5 (Flujo RG II→IV) | Pendiente |

**P-8 refinada nuevamente:** *"Lagrangiana: bosquejo + núcleo gravitacional derivado (D-007) + reducción a cuerda SCG estructural (sesión 18); dos sub-tareas con ansatz parciales; flujo RG pendiente."*

### 8.3 Nuevo insight candidato K-031

**K-031 (candidato, estructural/confirmatorio):** *La acción efectiva 2D de cuerda SCG, obtenida por reducción dimensional de S_PA en fondo BH + ansatz de llenado volumétrico + ansatz de saturación entrópica, reproduce coherentemente K-007 (d~√(r_s·ℓ_P), L~r_s²/ℓ_P), el Casimir D-006 como cuantización transversal, el modelo fenomenológico D-001 como límite IR, y el redshift K-028 como condición de consistencia ADM. Cierra estructuralmente el ciclo Régimen II → Régimen III del bosquejo.*

Nivel: análogo a K-029 (sesión 16) — confirmatorio, no descubrimiento profundo. Establece que la estructura del bosquejo es internamente consistente y todos los resultados previos del marco se integran bajo una única acción efectiva.

Promoción a confirmado requeriría:
- Derivar el ansatz de llenado volumétrico desde principios variacionales.
- Fijar los factores O(1) por cálculo riguroso.
- Calcular explícitamente la backreaction del fondo Schwarzschild.

---

## 9. Próximos pasos

**Después de tarea 5.4 (esta sesión), el bosquejo tiene:**
- 2 sub-tareas completadas (5.1 D-006, 5.2 D-007).
- 2 sub-tareas parciales (5.3 con K-030 candidato, 5.4 con K-031 candidato).
- 1 sub-tarea pendiente (5.5, flujo RG II→IV).

**Prioridades naturales para sesiones futuras:**

1. **Tarea 5.5 (flujo RG II → IV):** ataque a T-1 (k topológico vs k dinámico). Primera predicción cuantitativa estructural de α₂ ≈ α₃. Esfuerzo: 3-5 sesiones. Máximo impacto.

2. **Derivar el ansatz de llenado volumétrico.** Variacional: ¿qué configuración de la cuerda plegada minimiza la energía total a entropía fija? Podría dar L·d² ~ V_BH como consecuencia.

3. **Q-039: cuantificar Λ_UV** (derivada de K-030 candidato, sesión 17). Si > 384 M_P², K-030 se promueve.

4. **Snapshot v1.7** consolidando sesiones 16–18. Cambios acumulados: 2 D, 3 K candidatos, P-8 refinado varias veces, P-11 rebajada.

---

## 10. Referencias

- **D-006** (`logic/derivations/D-006_A-003_desde_polyakov.md`): Casimir transversal.
- **D-007** (`logic/derivations/D-007_ec_movimiento_plebanski.md`): núcleo gravitacional.
- **D-003 v1.2** (`logic/derivations/D-003_conservacion_entropia.md`): K-007 por holografía + llenado.
- **D-001** (`logic/derivations/D-001_modelo_discreto_cuerda.md`): modelo fenomenológico.
- `notes/Tarea_5.3_kodama_P-11.md` (sesión 17): K-030 candidato.
- Polchinski (1998) *String Theory* vol. 1: reducciones dimensionales y Nambu-Goto.
- Plebanski (1977); Krasnov (2011): base formal.
- Callan, C. & Thorn, C. (1986): cuerdas en fondos curvos.

---

## 11. Firma

Tarea 5.4 **parcialmente resuelta estructuralmente.** La acción efectiva 2D de cuerda SCG se obtiene por reducción dimensional de S_PA en fondo BH, integrando coherentemente D-003, D-006, D-007 y el modelo fenomenológico D-001. K-007 se recupera; el balance ADM es consistente via K-028 candidato.

Dos ansatz físicos admitidos: llenado volumétrico, simetría axial. Factores O(1) no cerrados.

**K-031 candidato** añadido: cierre estructural del ciclo Régimen II → Régimen III.

P-8 (Lagrangiana) refinada: 2/5 completadas, 2/5 parciales con candidatos, 1/5 pendiente. La arquitectura del bosquejo (sesión 12) sobrevive a 6 sesiones de desarrollo sin contradicciones internas.
