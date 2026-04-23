# K-032 — Sesión 32: M3 paso 1 — Plebanski-Holst + frontera CS

- **Fecha:** 2026-04-22 (sesión 32).
- **Objetivo:** derivar el nivel CS efectivo de frontera desde la acción Plebanski-autodual + Holst + Λ, identificar la dependencia con γ_Immirzi, y verificar si la forma α = γ/(4π) emerge limpiamente (K-032.S) o requiere refinamiento (K-032.W o rutas alternativas).
- **Relación con sesión previa:** `notes/K-032_sesion31_formalizacion.md` seleccionó M3 como mecanismo candidato; esta sesión ataca su paso 1.
- **Ingredientes:** D-007 (núcleo Plebanski-autodual + Λ con frontera CS k₀ = 2π/(κΛ)); Holst 1996; Randono 2006 (β real); Thiemann 2007 (formulación BI canónica); Baez 2000 (BF↔CS frontera).

---

## 0. Estrategia

El ataque procede en 4 sub-pasos:

1. **Setup (§1-§2):** escribir la acción Plebanski-autodual + Holst + Λ en forma compatible con variables Barbero-Immirzi (β real, Randono 2006).
2. **Descomposición (§3):** proyectar en sector self-dual/anti-self-dual y simplificar a componentes reales.
3. **Frontera (§4):** aplicar Baez 2000 extendido; identificar el término CS de frontera y su dependencia con γ.
4. **Diagnóstico (§5-§7):** comparar con K-032.S (k = 4π/γ); evaluar si la forma emerge limpia o requiere hipótesis adicional sobre Λ_efectiva.

**Disclaimer previo:** el cálculo completo de Plebanski-Holst con frontera es un ejercicio técnico no-trivial (requiere manipulación cuidadosa de formas auto/anti-auto-duales en so(3,1), integraciones por partes con condiciones de frontera, tratamiento de los multiplicadores ψ y cross-terms). Lo que sigue es una **derivación esquemática rigurosa en estructura pero no exhaustiva en factores**, diseñada para identificar la dependencia funcional en γ y señalar los pasos que requerirían trabajo técnico adicional.

---

## 1. Acción Plebanski-Holst-Λ

### 1.1 Forma de Holst directa (vierbein)

En variables vierbein real con spin connection ω^{IJ}:

```
S_Holst = (1/(2κ)) ∫_M ε_{IJKL} e^I ∧ e^J ∧ R^{KL}(ω)      (Palatini)
        + (1/(2γκ)) ∫_M e^I ∧ e^J ∧ R_{IJ}(ω)              (Holst term)
        - (Λ/(2κ)) · (1/12) ∫_M ε_{IJKL} e^I ∧ e^J ∧ e^K ∧ e^L   (cosmo)
```

El término de Holst, que multiplica (1/γ), es **topológico en vacío** (∂M = ∅; torsión nula on-shell), pero **contribuye a la frontera** cuando ∂M ≠ ∅.

En variables canónicas (Barbero-Immirzi): la conexión canónica es:
```
A^i_a = ω^{0i}_a + γ · ε^i_{jk} ω^{jk}_a/2 = Γ^i_a + γ · K^i_a
```
donde Γ = spin connection 3D, K = curvatura extrínseca. El parámetro γ controla la mezcla — a β = -i (γ → -i) recuperamos Ashtekar puro; a γ real, formulación Barbero-Immirzi estándar.

### 1.2 Forma Plebanski (self-dual)

Equivalentemente, en variables Plebanski con Σ^{IJ} (2-forma autodual):
```
S_PH = (1/κ) ∫_M [ Σ^{IJ} ∧ F_{IJ}(ω) 
                  - (1/(2γ)) Σ^{IJ} ∧ *R_{IJ}(ω)
                  - (1/2) Φ^{IJKL} Σ_{IJ} ∧ Σ_{KL}
                  - (Λ/6) Σ^{IJ} ∧ Σ_{IJ} ]
```
donde *R es el dual en índices internos y Φ es el multiplicador de simplicidad.

Esta es la formulación **Plebanski-Holst-Randono**: con Σ en so(3,1) completo (no proyectado autodual), γ real, y Φ forzando Σ = e ∧ e (sector geométrico).

---

## 2. Descomposición self-dual / anti-self-dual

Proyectar en sectores (+, -):
```
Σ^{IJ} = Σ_+^{IJ} + Σ_-^{IJ},     con *Σ_± = ±i Σ_±    (Lorentziano; Euclídeo: ±1)
F(ω) = F_+ + F_-
```

La acción se descompone:
```
S_PH = (2/κ)(1 - i/γ) ∫ Σ_+ ∧ F_+   +   (2/κ)(1 + i/γ) ∫ Σ_- ∧ F_-
      + simplicidad + cosmo
```

**Nota clave:** los factores (1 ∓ i/γ) mezclan las dos chiralidades con peso complejo. Para γ real (Randono), esta forma es **compleja por unidad**; la acción física real se obtiene tomando Re(S_PH) (o, equivalentemente, sumando con complejo conjugado — ambos sectores contribuyen en SCG).

**Convenciones de módulo:**
```
|1 - i/γ|² = 1 + 1/γ² = (γ² + 1)/γ²
```
Este factor aparecerá en la normalización de los términos de frontera.

---

## 3. Variables canónicas reales (Barbero-Immirzi)

Introducir:
```
A^i = (A_+^i + A_-^i)/2     (conexión real su(2), = ω^{0i} + γ K^i en 3D)
K^i = (A_+^i - A_-^i)/(2i)  (curvatura extrínseca, imaginaria en (+,-))
```
con:
```
A_+^i = A^i + i K^i
A_-^i = A^i - i K^i
```

Chern-Simons:
```
CS(A_+) = tr[ A_+ ∧ dA_+ + (2/3) A_+ ∧ A_+ ∧ A_+ ]
CS(A_-) = CS(A_+)*      (conjugado en su(2)_C)
```

Identidades:
```
CS(A_+) + CS(A_-) = 2·CS_R  (CS real en ω y K, cuadrático)
CS(A_+) - CS(A_-) = 2i·CS_I (CS imaginario, cruzado ω-K)
```

---

## 4. Frontera vía Baez 2000 extendido

### 4.1 Setup

Partimos de la acción en el sector self-dual:
```
S_+ = (2/κ)(1 - i/γ) ∫_M Σ_+ ∧ F_+ - (Λ/6) ∫_M Σ_+ ∧ Σ_+ + simplicidad
```

**Resultado Baez 2000 (BF + Λ puro):** con simplicidad on-shell (F_+ = (Λ/3) Σ_+), integrando por partes:
```
∫_M Σ_+ ∧ F_+ = (3/Λ) ∫_M F_+ ∧ F_+ 
              = (3/Λ) · ∫_∂M CS(A_+)       (Pontryagin → Chern-Simons boundary)
```

Restando la contribución de volumen (cosmo → también se reduce a ∫ F_+ F_+ bajo simplicidad):
```
S_+|_on-shell = (2/κ)(1 - i/γ) · (3/Λ) · (1 - Λ/something) ∫_∂M CS(A_+)
             = (6/(κΛ)) (1 - i/γ) ∫_∂M CS(A_+)       (esquemático)
```

(El "something" es un factor O(1) que depende de la normalización exacta de cosmo vs Pontryagin; ver Baez 2000, Randono 2006 para el factor preciso. No afecta la dependencia funcional en γ).

**Completando con el sector (-):**
```
Re(S|∂) = (6/(κΛ)) · Re[(1 - i/γ) CS(A_+) + (1 + i/γ) CS(A_-)]
        = (6/(κΛ)) · Re[(CS_+ + CS_-) - (i/γ)(CS_+ - CS_-)]
        = (6/(κΛ)) · [2 CS_R + (2/γ) CS_I]
        = (12/(κΛ)) CS_R + (12/(γκΛ)) CS_I
```

### 4.2 Identificación de los dos términos

El término CS_R (spin connection + extrinsic curvature, simétrico) corresponde al sector "Palatini" clásico de la frontera — esto ya estaba en D-007 (k₀ = 2π/(κΛ) en el límite γ → ∞ / Holst despreciable).

**El término CS_I es la contribución específica de Holst.** Su nivel es:
```
k_Holst = 12/(γκΛ)           (en normalización CS = (1/(2π)) ∫ tr(AdA + ...))
```

(Ajustar por factores 2π según convención: si k = 2π · coeficiente_acción, entonces k_Holst = 12/(γκΛ) · 1/(2π) = 6/(πγκΛ). La dependencia en γ es lo relevante: **k_Holst ∝ 1/(γκΛ)**.)

### 4.3 Dependencia funcional

**Resultado principal sesión 32:**
```
k_Holst(γ, Λ) = C / (γ κ Λ)       con C = constante O(1) de convención
```

El término de Holst **introduce** un segundo CS en la frontera, con coeficiente **proporcional a 1/γ**.

El coupling gauge asociado a este CS (identificando α ≡ 1/k en alguna normalización):
```
α_Holst-emergent = (γ κ Λ) / C
```

Lineal en γ · κ · Λ.

---

## 5. Comparación con K-032.S

### 5.1 Requisito K-032.S

K-032.S postula: α_gauge(M_P) = γ/(4π). Comparando con §4.3:
```
γ κ Λ_efectiva / C = γ/(4π)
   ⟹    κ Λ_efectiva = C/(4π)
   ⟹    Λ_efectiva = C / (4π κ) = C/(32π²·ℓ_P²)   (usando κ = 8π ℓ_P²)
```

Para C = 1 (convención natural): Λ_efectiva ≈ 0.032 M_P² ≈ (3/(8π²)) M_P².
Para C = 2π: Λ_efectiva ≈ 0.25 M_P² ≈ (1/4) M_P².
Para C = 12 (si el factor completo del cálculo §4.1 se preserva): Λ_efectiva ≈ 3/(8π) M_P² ≈ 0.12 M_P².

En todos los casos, **Λ_efectiva ≲ O(0.1) M_P²** — **mucho menor que Λ_Planck ~ M_P² y mucho mayor que Λ_observada ~ 10⁻¹²² M_P²**.

### 5.2 Reducción del problema

**Lo positivo:** M3 paso 1 demuestra estructuralmente que γ entra en el nivel CS de frontera del núcleo gravitacional. La forma α ∝ γ es consistente con K-032.S en su dependencia funcional.

**Lo pendiente:** K-032.S requiere Λ_efectiva ≈ 10⁻¹·M_P² (para el factor C apropiado). **Esta Λ_efectiva es una predicción no-trivial de SCG que requeriría justificación independiente.**

**Reducción:** K-032.S se convierte en:
```
K-032.S ≡  "Λ_efectiva en régimen II (escala Planck, sector gravitacional SCG) 
            es del orden de C/(32π²) · M_P² ≈ 0.03–0.3 M_P²."
```

### 5.3 Compatibilidad con Q-039

Q-039 (sesión 21) tuvo resultado NEGATIVO respecto a la ruta ABKP (Λ > 384/ℓ_P² = 384 M_P²), que es **muchísimo mayor** que el valor requerido por K-032.S aquí (0.03–0.3 M_P²). Por tanto:

- La ruta ABKP no produce K-032.S (consistente con Q-039 negativo).
- La ruta Randono β real (adoptada en v2.0) es compatible con cualquier Λ_efectiva; no impone un valor concreto.
- **K-032.S requiere Λ_efectiva ~ 0.03–0.3 M_P², valor no determinado por SCG v2.0 hasta ahora.**

---

## 6. Diagnóstico honesto

### 6.1 Lo que M3 paso 1 establece

1. **P-M3.1 verificada (positiva):** el término de Holst es estructuralmente compatible con el núcleo Plebanski-autodual-Randono. Su contribución a la frontera es un CS adicional con nivel k_Holst ∝ 1/(γκΛ).

2. **Identificación del mecanismo:** γ entra linealmente en el coupling gauge emergente asociado al CS de frontera del sector gravitacional (vía Holst). La forma funcional es **consistente con K-032.S** si y solo si Λ_efectiva ~ O(0.1) M_P².

3. **Reducción del problema K-032.S a Λ_efectiva:** cerrar K-032.S requiere determinar Λ_efectiva en régimen II desde primeros principios SCG, no derivarla retroactivamente desde α_observado.

### 6.2 Lo que M3 paso 1 NO establece

1. **No demuestra α = γ/(4π) limpiamente.** La forma α ∝ γ emerge, pero la constante numérica 1/(4π) depende del valor de Λ_efectiva, que no se ha fijado.
2. **No identifica qué edge mode WW se acopla al CS de frontera.** Si la coupling es indirecta (via una presunta "frontera compartida", cf. §3.3 de sesión 31), esto no lo resolvemos aquí.
3. **No trata correcciones sub-dominantes** (2-loops, thresholds, discrepancia 7% entre α_2 y α_3).
4. **La derivación es esquemática.** Los factores numéricos exactos (C en §5.1) requieren cálculo detallado con convenciones consistentes, 1-2 sesiones adicionales de trabajo técnico.

### 6.3 Estado de M3

**M3 paso 1: POSITIVO PARCIAL.** El mecanismo es estructuralmente consistente con K-032.S, pero no la cierra; la reduce a una pregunta concreta sobre Λ_efectiva.

**No es refutación (la forma funcional sale bien).** No es cierre limpio (falta Λ_efectiva).

### 6.4 Tensiones identificadas

1. **Λ_efectiva ≠ Λ_observada:** la Λ requerida por K-032.S es O(10⁻¹) M_P², no la Λ_observada ~ 10⁻¹²² M_P². Esto significa que K-032.S describe una escala **distinta** al Λ cosmológico observado — es el Λ del régimen II (escala Planck), no el del régimen IV (cosmológico). Consistente con interpretar κΛ como "curvatura efectiva del sector gravitacional en régimen II", no la constante cosmológica cosmológica.

2. **Normalización de la constante C:** la ambigüedad de factor O(1)–O(10) en C traduce en ambigüedad del factor numérico en α. Sin fijar C rigurosamente, K-032.S es una "forma funcional", no un valor exacto.

---

## 7. Decisiones post-sesión 32

### 7.1 M3 sigue vivo (pero no cerrado)

No retrocedemos a K-032.W aún. M3 paso 1 es positivo parcial; la reducción a "Λ_efectiva ~ O(0.1) M_P²" es una hipótesis concreta, no vacía.

### 7.2 Sesión 33 — dos ataques paralelos

**Opción A:** determinar Λ_efectiva desde SCG.
- Tareas: revisar la literatura LQG sobre Λ "running" en régimen I/II; explorar si `Spin(10)_1` MTC y la estructura de frontera imponen un valor concreto; considerar relación con el espectro de área (A = 8π γ ℓ_P²) y escalas emergentes.
- Esfuerzo: 1-2 sesiones.
- Output esperado: (i) Λ_efectiva derivable y ≈ 0.1 M_P² → K-032.S cerrada; (ii) Λ_efectiva derivable pero distinta → K-032.S refinada o refutada; (iii) Λ_efectiva indeterminable → K-032.W como veredicto.

**Opción B:** derivar el edge mode coupling WW al CS gravitacional (presunción P-M3.3 de sesión 31).
- Tareas: estudiar cómo los edge modes quirales de `Spin(10)_1` WW se acoplan al CS gravitacional de frontera. Identificar si el coupling efectivo es k_Holst directamente o involucra factor adicional.
- Esfuerzo: 1-2 sesiones.
- Output esperado: (i) acoplamiento directo con factor O(1) → K-032.S avanza; (ii) factor adicional que complica la forma → refinamiento; (iii) desacople total (edge modes y CS grav no se "ven") → M3 falla, retroceder.

**Recomendación:** Opción A primero (más tractable; ataca la ambigüedad más problemática). Opción B como siguiente paso si A cierra positivamente.

### 7.3 Plan revisado

- **Sesión 33:** ataque a Λ_efectiva (Opción A).
- **Sesión 34:** si A cerró: edge mode coupling (Opción B). Si A negativo: retreat a K-032.W + consolidación.
- **Sesión 35:** veredicto global.

---

## 8. Presunciones: status actualizado

| Presunción | Status tras sesión 32 |
|---|---|
| P-M3.1 (Holst + Plebanski-Randono compatibles) | ✅ **Verificada** en estructura. |
| P-M3.2 (fronteras grav y top coinciden) | 🟡 Asumida sin verificación; tarea pendiente. |
| P-M3.3 (edge mode WW se acopla a k_Holst) | 🟡 No abordada; sesión 34 si procede. |

---

## 9. Lo que esta sesión garantiza vs no garantiza

**Garantiza:**
- El término de Holst contribuye estructuralmente a la frontera del núcleo gravitacional con un término CS de nivel k_Holst ∝ 1/(γκΛ).
- La forma funcional del acoplamiento gauge emergente es **consistente** con K-032.S (α ∝ γ).
- M3 paso 1 **reduce** K-032.S a una hipótesis concreta: Λ_efectiva ~ O(0.1) M_P² en régimen II.

**No garantiza:**
- Que Λ_efectiva tenga ese valor.
- El factor numérico exacto en α (depende de normalización C).
- Que los edge modes WW se acoplen a este CS (P-M3.3 pendiente).
- Que la discrepancia α_2 vs α_3 (7%) se absorba en 2-loops.

---

## 10. Honestidad epistémica

Regla 9 considerada y aplicada parcialmente: no se ha destruido nada previo, pero se ha **debilitado** la hipótesis M3 de "mecanismo directo limpio" a "mecanismo estructural consistente condicionado en Λ_efectiva". Este es el curso honesto después de ver que el cálculo directo no produce 4π/γ sin hipótesis adicional.

Regla 5 aplicada: K-032 sigue candidato. Ningún insight promovido.

K-005 aplicada: no se ha inventado mecanismo nuevo; todo el cálculo usa Plebanski (estándar), Holst (estándar desde 1996), Baez 2000 (estándar), Barbero-Immirzi (estándar). La originalidad es la aplicación al contexto SCG v2.0 + D-010.

**Nota meta:** si en sesión 33-34 se determina que Λ_efectiva no es derivable con rigor, el camino honesto es **retreat a K-032.W** y consolidar el pattern α₂ ≈ α₃ ≠ α₁ estructuralmente (Tarea 5.5) sin pretender derivar valores numéricos. Esta posibilidad debe mantenerse abierta.

---

## 11. Referencias

- Holst S. 1996, PRD 53, 5966. ("Barbero's Hamiltonian derived from a generalized Hilbert-Palatini action")
- Ashtekar A., Lewandowski J. 2004. Background Independent Quantum Gravity: A Status Report.
- Baez J. 2000. "An introduction to spin foam models of BF theory and quantum gravity." Lect. Notes Phys. 543, 25–93.
- Randono A. 2006. gr-qc/0504010, gr-qc/0611073, gr-qc/0611074. (Kodama β real)
- Thiemann T. 2007. *Modern Canonical Quantum General Relativity*. Cambridge UP.
- Krasnov K. 2011. "Plebanski gravity without the simplicity constraints." CQG 28, 235005.
- Mercuri S. 2006–2009. (γ como término topológico de frontera — Nieh-Yan)
- Wieland W. 2016. CQG 34, 045002. ("Immirzi parameter as topological term")
- Alexander-Marciano-Smolin 2014. PRD 89, 065017. (A_SD = su(2)_L)
- D-007 (interno, sesión 16).
- K-032 (candidato desde sesión 19; Tarea_5.5_flujo_RG.md).

---

## 12. Firma

**Sesión 32 cerrada.** M3 paso 1 = **positivo parcial**.

Estructura: γ entra linealmente en el nivel CS de frontera del sector gravitacional (Holst contribution). Forma funcional α ∝ γ consistente con K-032.S. **Reducción del problema:** K-032.S ≡ "Λ_efectiva en régimen II ~ O(0.1) M_P²".

**No refutación. No cierre limpio.** Progreso concreto: el problema se ha reducido de "probar α = γ/(4π) desde primeros principios" a "determinar Λ_efectiva en régimen II".

**Próxima sesión (33):** atacar Λ_efectiva (Opción A). Tentativa: derivar desde estructura `Spin(10)_1` + lattice SCG + espectro de área. Alternativa (si A falla): edge mode coupling (Opción B, sesión 34).

**Regla 9 pre-aplicada:** si sesión 33 no determina Λ_efectiva con rigor, retreat a K-032.W es el veredicto honesto.
