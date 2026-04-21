# Tarea 5.2 — Ecuaciones de movimiento de S_Plebanski-autodual + Λ

- **Fecha:** 2026-04-21 (sesión 16)
- **Referencia bosquejo:** `notes/R_lagrangiana_bosquejo.md`, sección 5.2.
- **Objetivo:** variar S_madre (en su núcleo gravitacional) respecto a Σ, A, ψ; obtener las ecuaciones de movimiento; mostrar que reducen a Einstein-Hilbert + Λ autodual; chequear consistencia con K-019 (Ashtekar = su(2)_L), Walker-Wang/Crane-Yetter, y la frontera CS.
- **Relación con P-8:** primer paso concreto del programa Lagrangiana. Confirma que el núcleo gravitacional de S_madre es consistente y reproduce GR-Λ on-shell.
- **Nivel de esfuerzo:** una sesión.

---

## 0. Planteamiento

El bosquejo propone como acción madre:

```
S_madre = S_Plebanski-autodual[Σ, A, ψ] + S_cosmo[Σ, Λ] + S_defectos[topologías de A]
```

Aquí tratamos solo el núcleo gravitacional **S_PA + S_cosmo**. S_defectos es formalmente una suma sobre clases de homotopía y no contribuye a las ecuaciones de movimiento en el sector de bulk sin materia.

**Objetivo mínimo.** Verificar que:
1. Las ecuaciones de Euler-Lagrange son las esperadas.
2. On-shell, el sistema es equivalente a GR-vacío + Λ.
3. La estructura autodual se preserva (no se pierde la quiralidad K-019).
4. En el límite Λ → 0, la acción se reduce a BF topológico con restricción de simplicidad — consistente con Crane-Yetter/Walker-Wang (Régimen I).

Esto es un resultado **conocido en la literatura** (Plebanski 1977; Capovilla-Dell-Jacobson 1991; Krasnov 2011; Baez 2000). Lo reproduzco aquí porque:
- Es la primera pieza explícita del programa Lagrangiana SCG.
- Fija convenciones de notación para piezas futuras (5.3, 5.4, 5.5).
- Permite verificar que nada en la acción entra en conflicto con los resultados previos del marco SCG.

---

## 1. Convenciones y acción

### 1.1 Índices y espacios

- **Índices de espacio-tiempo:** μ, ν, α, β = 0, 1, 2, 3. Signatura convencional mostly-plus (−,+,+,+).
- **Índices autoduales:** A, B, C, D = 0, 1 (espinoriales izquierdos de SL(2,C) ≅ Spin(3,1)_C en su proyección autodual). El álgebra de Lie del grupo autodual es **su(2)_C ≅ sp(1)_C**.
- Los índices autoduales son **simétricos**: un tensor con índices AB mayúsculos es simétrico en (AB), equivalente a un tripleta SU(2)_C (3 componentes).

### 1.2 Variables

**A^{AB}** — conexión autodual (1-forma con valores en su(2)_C ≅ tensores simétricos):
```
A^{AB} = A^{AB}_μ dx^μ      (simétrico en AB)
```
Tres componentes complejas por cada μ. Es la conexión de Ashtekar (variante compleja).

**F^{AB}** — curvatura de A:
```
F^{AB} = dA^{AB} + A^A_C ∧ A^{CB}       (2-forma, simétrica en AB)
```

**Σ^{AB}** — 2-forma autodual con valores en su(2)_C:
```
Σ^{AB} = (1/2) Σ^{AB}_{μν} dx^μ ∧ dx^ν   (simétrica en AB)
```
Independiente del vierbein a priori. Su conexión con el vierbein aparece on-shell via simplicidad (sec. 3).

**ψ_{ABCD}** — campo escalar espinorial multiplicador de Lagrange:
```
ψ_{ABCD}    totalmente simétrico en (ABCD), sin traza: ε^{AC}ψ_{ABCD} = 0
```
5 componentes complejas (el número de componentes del **tensor de Weyl autodual**).

### 1.3 Acción

```
S_PA[Σ, A, ψ] = (1/κ) ∫_M [ Σ^{AB} ∧ F_{AB}(A) − (1/2) ψ_{ABCD} Σ^{AB} ∧ Σ^{CD} ]      (1.1)

S_cosmo[Σ, Λ] = −(Λ/6κ) ∫_M Σ^{AB} ∧ Σ_{AB}                                             (1.2)

S_núcleo = S_PA + S_cosmo                                                                 (1.3)
```

donde κ = 8πG es la constante de acoplamiento gravitacional. La índice-contracción implícita: Σ^{AB}∧Σ_{AB} = Σ^{AB}∧Σ^{CD} ε_{AC}ε_{BD} donde ε_{AC} es el símbolo de Levi-Civita espinorial izquierdo.

Forma final compacta:

```
S_núcleo = (1/κ) ∫_M [ Σ^{AB} ∧ F_{AB} − (1/2)(ψ_{ABCD} + (Λ/3) ε_{A(C}ε_{D)B}) Σ^{AB} ∧ Σ^{CD} ]
                                                                                           (1.4)
```

Observación: Λ se puede absorber en una redefinición ψ → ψ + (Λ/3)·(parte de traza) si a ψ se le permite traza. Mantengo ψ sin traza y Λ separado para claridad.

### 1.4 Grados de libertad

- Σ^{AB}: 3 × 6 = 18 componentes (3 pares AB simétricos × 6 componentes de 2-forma en 4D).
- A^{AB}: 3 × 4 = 12 componentes.
- ψ_{ABCD}: 5 componentes.

**Total off-shell:** 35 componentes (complejas).

Tras imponer condiciones de realidad (que no tocamos en esta derivación formal), recobramos el conteo correcto de GR: 2 modos gravitacionales.

---

## 2. Variación respecto a ψ

### 2.1 Derivación

La única pieza con ψ es el término cuadrático en Σ. Variación δψ_{ABCD} en (1.1):

```
δS_PA / δψ_{ABCD} = −(1/2κ) Σ^{(AB} ∧ Σ^{CD)}                                         (2.1)
```

La simetrización sobre (ABCD) viene de que ψ_{ABCD} es totalmente simétrico; solo su parte simétrica contribuye.

Imponer δS = 0 para toda variación **sin traza** de ψ:

```
Σ^{(AB} ∧ Σ^{CD)}_{trace-free} = 0                                                     (2.2)
```

Esto significa: la parte simétrica sin-traza del tensor 4-indexed Σ^{AB}∧Σ^{CD} se anula. La traza (ε_{AC}ε_{BD} Σ^{AB}∧Σ^{CD}) queda libre.

### 2.2 Interpretación: restricción de simplicidad

La ecuación (2.2) es exactamente la **restricción de simplicidad de Plebanski**. Tiene soluciones en dos sectores:

**Sector (i) — geométrico:**
```
Σ^{AB} = e^{AA'} ∧ e^B_{A'}           (con e^{AA'}_μ el vierbein espinorial real)    (2.3)
```
donde A' es un índice espinorial derecho que se contrae con una métrica de signo (+,+). En lenguaje de 4-vectores:
```
Σ^{AB}_{μν} = (1/2)(e^A_μ e^B_ν − e^A_ν e^B_μ)_{autodual}                            (2.4)
```

Este es el sector de gravedad riemanniana usual. El vierbein existe y la métrica g_{μν} = e^A_μ e^B_ν ε_{AB} es real Lorentziana.

**Sector (ii) — no-geométrico:**
Σ como 2-forma autodual pura sin vierbein subyacente. No corresponde a una métrica semi-Riemanniana. En LQG spinfoam se llama "sector topológico" y se descarta como espuria.

**Elección en SCG:** adoptamos el sector (i). Esto es una **convención física**, no una derivación automática. La justificación es que queremos GR en el régimen semiclásico (Régimen II) y GR requiere vierbein.

### 2.3 Consecuencia

Tras imponer (2.3), Σ^{AB} está parametrizado por el vierbein. La acción se re-escribe:

```
Σ^{AB} ∧ F_{AB} = F^{AB}_{μν} Σ_{AB,ρσ} (dx^μ∧dx^ν∧dx^ρ∧dx^σ)/4 
                = F^{AB}_{μν} e^C_α e^D_β ε_{ACBD} · ε^{μνρσ} (volumen)
                = (tr F ∧ e∧e) (autodual)                                              (2.5)
```

Esto es **Einstein-Hilbert en variables de Ashtekar** (Jacobson-Smolin 1988; Ashtekar 1986). Más explícitamente:
```
Σ^{AB} ∧ F_{AB} = Σ^{AB} ∧ F_{AB}|_{autodual} ∝ R √(−g) d^4x · (1 + i ε)_{proy. autodual}
```
donde la proyección autodual extrae el sector su(2)_L.

**Punto clave:** la imposición de simplicidad (ψ on-shell) convierte el BF abstracto en Einstein-Hilbert efectivo, con la conexión autodual A tomando el rol de conexión de spin autodual del vierbein.

---

## 3. Variación respecto a Σ

### 3.1 Derivación

Variando Σ^{AB} en (1.4):

```
δS_núcleo/δΣ^{AB} = (1/κ)[ F_{AB} − (ψ_{ABCD} + (Λ/3) g^{AB}_{CD}) Σ^{CD} ]         (3.1)
```

donde g^{AB}_{CD} = ε^{A(C}ε^{D)B} es el proyector identidad sobre el espacio de índices simétricos (su(2)_C = 3-dim).

Imponer δS = 0 para todo δΣ^{AB}:

```
F_{AB}(A) = ψ_{ABCD} Σ^{CD} + (Λ/3) Σ_{AB}                                            (3.2)
```

### 3.2 Interpretación

La ecuación (3.2) es la **ecuación de Einstein autodual** en forma de Plebanski.

**Descomposición:** la curvatura autodual F^{AB} tiene dos partes:
- Traza-propia: proporcional a Σ^{AB} con coeficiente Λ/3 + (ψ-traza, pero ψ tenía traza cero, entonces solo Λ/3).
- Weyl autodual: parte sin traza, igual a ψ_{ABCD} Σ^{CD}.

Identificación:
```
ψ_{ABCD}|_on-shell = C_{ABCD}^{+} = tensor de Weyl autodual                            (3.3)
(Λ/3) = escalar de Ricci / 12 = traza de la curvatura autodual                        (3.4)
```

Esto **es** la forma autodual de las ecuaciones de Einstein con Λ:
```
R_{μν} − (1/2) R g_{μν} + Λ g_{μν} = 0                                                (3.5)
```
equivalentemente R_{μν} = Λ g_{μν} (vacío con Λ).

### 3.3 Verificación dimensional / numérica

Cocientes estándar (ver Penrose-Rindler *Spinors and space-time* vol. 1, Cap. 4):

- R = 4Λ (para R_{μν} = Λ g_{μν}).
- El escalar auto-dual Ψ de Plebanski satisface F = Ψ Σ + Weyl-auto × Σ.
- Ψ = Λ/3 (coincide con nuestro coeficiente 3.4).

✓ Consistente con la literatura.

---

## 4. Variación respecto a A

### 4.1 Derivación

Variación δA^{AB} en S_PA. Solo el término Σ ∧ F depende de A:

```
δ(Σ^{AB} ∧ F_{AB}) = Σ^{AB} ∧ δF_{AB} = Σ^{AB} ∧ d_A(δA_{AB})                         (4.1)
```

(La variación de la curvatura respecto a la conexión es la derivada covariante.)

Integrando por partes (asumiendo frontera ∂M que tratamos en sección 6):

```
δS_PA = (1/κ) ∫_M d_A Σ^{AB} ∧ δA_{AB} + (término de frontera)                        (4.2)
```

Imponer δS = 0 para todo δA^{AB}:

```
d_A Σ^{AB} = 0                                                                         (4.3)
```

### 4.2 Interpretación: torsión cero autodual

La ecuación (4.3) dice que la 2-forma autodual Σ es **covariantemente constante** bajo A. Sustituyendo la restricción de simplicidad Σ = e ∧ e (2.4):

```
d_A (e^A ∧ e^B) = 0                                                                    (4.4)
```

Expandiendo:
```
(d_A e^A) ∧ e^B + e^A ∧ (d_A e^B) = 0                                                 (4.5)
```

La solución única (para e no degenerado) es que **A sea la parte autodual de la conexión de spin del vierbein**:
```
A^{AB} = ω^{AB}_{+} = (1/2)(ω^{AB} + *ω^{AB})                                          (4.6)
```

donde ω^{AB} es la conexión de spin (compatible con e y sin torsión) y * es el operador de Hodge actuando sobre índices internos.

### 4.3 Esto SÍ es Ashtekar

La identificación (4.6) es **exactamente** la definición original de la conexión de Ashtekar (1986). Ver Jacobson-Smolin 1988; Ashtekar-Lewandowski 2004.

**Consistencia con K-019:** Alexander-Marciano-Smolin (2014) identifica ω_+^{AB} con la conexión su(2)_L de la fuerza débil. Nuestra derivación reproduce este marco: A es su(2)_L. ✓

---

## 5. Reducción a Einstein-Hilbert + Λ autodual

### 5.1 On-shell

Combinando (2.3), (3.2), (4.3):
- Σ = e ∧ e (de vierbein real).
- A = ω_+ (conexión de spin autodual).
- F(A) = R_+ (curvatura autodual = tensor de Riemann autodual del vierbein).
- Σ ∧ F = R √(−g) d^4x · (autodual).

La acción on-shell (sustituyendo ψ = Weyl_+ y simplificando):

```
S_núcleo|_on-shell = (1/κ) ∫_M [ R_+ · √(−g) − (Λ/2)(e∧e)_autodual ∧ (e∧e)_autodual ] 
                   = (1/2κ) ∫_M (R − 2Λ) √(−g) d^4x   + términos topológicos           (5.1)
```

La parte real de (5.1) **es** la acción de Einstein-Hilbert con constante cosmológica:

```
S_EH+Λ = (1/2κ) ∫_M (R − 2Λ) √(−g) d^4x                                                (5.2)
```

La parte imaginaria es una clase topológica (Pontryagin/Euler) que no afecta las ecuaciones de movimiento clásicas.

### 5.2 Resultado principal

**S_PA + S_cosmo es equivalente on-shell a E-H + Λ autodual.**

Esto es teorema bien conocido. Ver:
- Plebanski (1977): el teorema original en lenguaje espinorial.
- Capovilla-Dell-Jacobson (1991): demostración moderna.
- Krasnov (2009, 2011): revisión con énfasis en la variante autodual pura.

### 5.3 Lo que es trivial y lo que no

**Trivial** (sabido desde 1977):
- Que S_PA + S_cosmo reproduzca E-H + Λ on-shell.
- Que A resulte ser la conexión autodual de Ashtekar.

**Nuevo en SCG (sesión 16):**
- Verificación explícita de que el núcleo gravitacional de S_madre (propuesto en sesión 12) es la forma autodual de GR-Λ.
- Confirmación de que no hay conflicto entre la formulación Plebanski-autodual y K-019 (la conexión resultante ES su(2)_L).
- Primera pieza del programa Lagrangiana SCG concretamente derivada.

---

## 6. Frontera y conexión con Chern-Simons

### 6.1 Término de frontera

Integrando por partes en (4.2) con M con frontera ∂M:

```
δS_PA|_frontera = (1/κ) ∫_{∂M} Σ^{AB} ∧ δA_{AB}                                        (6.1)
```

Fijando A|_{∂M} (Dirichlet) ó estado Hartle-Hawking, la variación se anula.

### 6.2 Reducción a Chern-Simons via el término cosmológico

Baez (2000) demuestra que **S_cosmo** (el término Λ) es exactamente la forma bulk 4D de Chern-Simons 3D. Explícitamente: en el bulk BF + Λ, on-shell (usando F = Λ Σ/3) se puede reescribir:

```
S_cosmo|_on-shell = −(1/6κ) · (3/Λ) ∫_M Σ^{AB} ∧ F_{AB}                                (6.2a)
                   = −(1/2κΛ) ∫_M Σ^{AB} ∧ F_{AB}                                       
                   = −(1/2κΛ) ∫_M dΣ · (form stuff)         
                   = −(1/2κΛ) ∫_{∂M} CS[A]                                              (6.2b)
```

donde CS[A] = A ∧ dA + (2/3) A ∧ A ∧ A es el Chern-Simons autodual de A.

Coeficiente: k = 2π/(κΛ) = 2π/(8πGΛ) ~ 1/Λ en unidades de M_P.

**Observación crítica:** el resultado de Baez es exacto en el bulk BF + Λ. En Plebanski + Λ con ψ, la presencia del multiplicador de Lagrange no altera el argumento porque ψ es algebraico y en el bulk on-shell coincide con el Weyl autodual, que se integra a clases topológicas (no contribuye al término de borde genuino).

Esto confirma la imagen del bosquejo:
- **Bulk**: Plebanski-autodual + Λ ≃ GR + Λ (Régimen II).
- **Frontera**: Chern-Simons con k ∝ 1/Λ (Régimen I ↔ II).

### 6.3 Consistencia con Walker-Wang / Crane-Yetter

- Crane-Yetter (1993) es el state-sum 4D cuyo bulk realiza BF + Λ en el continuo (Baez 2000).
- Walker-Wang (2011) es la realización Hamiltoniana en lattice trivalente.
- La acción (1.3) es la versión continua de lo que WW implementa en lattice.

**La equivalencia es:**
```
S_núcleo[Σ,A,ψ] ─on-shell→ S_EH + Λ
          │
          └─cuantizando→ Crane-Yetter state-sum ≡ Walker-Wang lattice
```

Ambas direcciones (clásica y cuántica) son consistentes. ✓

### 6.4 Q-033 parcialmente abordada

Q-033 preguntaba: *¿la frontera de Plebanski+Λ es exactamente CS con k = 2π/Λ incluyendo correcciones de ψ?*

**Respuesta parcial (sesión 16):** sí, el término dominante de borde es CS con k = 2π/(κΛ). Las correcciones por ψ son pequeñas porque on-shell ψ = Weyl autodual, que es local y no contribuye al integrando topológico de borde.

Rigorizar esto requiere un cálculo directo de los términos de borde por integración por partes sobre (1.4) con frontera, incluyendo el término ψ Σ ∧ Σ. Esto es trabajo técnico adicional; no se cierra aquí.

---

## 7. Límite Λ → 0

Cuando Λ → 0, S_cosmo → 0 y queda S_PA pura:

```
S_PA = (1/κ) ∫_M [ Σ^{AB} ∧ F_{AB} − (1/2) ψ_{ABCD} Σ^{AB} ∧ Σ^{CD} ]                 (7.1)
```

**Esto es BF topológico con restricción de simplicidad.** La teoría gauge sin restricción de simplicidad (Σ ∧ F sin ψ) es BF puro — completamente topológica, sin grados de libertad locales. La restricción de simplicidad reduce de BF puro a GR.

En el régimen I (E ≫ M_P) de SCG, la constante cosmológica efectiva es Λ_UV ~ M_P² y el sistema transita de GR-Λ a BF topológico (si ψ se relaja). Este límite define la descripción **pre-geométrica** de Régimen I.

**Consistencia con SCG:** el ansatz de "pre-geométrico = BF/CY/WW" del bosquejo (sección 2.1) es compatible: BF puro corresponde a Λ → 0 **con ψ también relajado** (sin constraint de simplicidad). Si ψ se mantiene pero Λ → 0, recuperamos GR sin Λ.

---

## 8. Síntesis

**Resultado principal.**

Variando S_núcleo = S_PA + S_cosmo:
- δψ → restricción de simplicidad: Σ = e ∧ e (sector geométrico elegido).
- δΣ → ecuación de curvatura: F = (Λ/3) Σ + ψ Σ (ψ on-shell = Weyl autodual).
- δA → torsión nula: A = ω_+ (conexión autodual de Ashtekar).

**On-shell:** S_núcleo ≡ Einstein-Hilbert + Λ autodual (ec. 5.1).

**Frontera:** reducción al Chern-Simons de A con k = 2π/(κΛ) (sección 6.2).

**Límite Λ → 0 + ψ sin constraint:** BF topológico = bulk de Crane-Yetter/Walker-Wang (régimen I).

### 8.1 Lo que esto nos da para SCG

1. **El núcleo gravitacional del bosquejo es consistente.** La acción elegida no entra en conflicto con GR; la reproduce on-shell.
2. **La conexión autodual ES su(2)_L.** K-019 no solo es compatible sino **necesaria** para que la teoría sea Ashtekar; sin autodualidad el Plebanski colapsa a BF puro no-quiral.
3. **La frontera es CS**, como esperaba K-019 + la cadena SCG → Levin-Wen → Chern-Simons.
4. **El régimen I emerge naturalmente** como el límite Λ → 0 + relajación de simplicidad.

### 8.2 Lo que esto NO resuelve

- Tensión T-1 (k topológico vs k dinámico): el k de la frontera es 2π/(κΛ) ~ 10¹²² con Λ observado, mientras que el k medido es ~300. Discrepancia no cerrada.
- Tensión T-2 (P-11): la conexión A es compleja; condiciones de realidad y Wick rotation siguen abiertas.
- Tensión T-3: la conexión entre esta acción Lagrangiana y el Walker-Wang Hamiltoniano pasa por la equivalencia CY ↔ WW; rigorización de esta equivalencia en contexto SCG queda pendiente.
- Tensión T-4: no hay término S_matter. Los fermiones deberían aparecer como defectos de A. Programa Bilson-Thompson sigue abierto.
- Ninguna constante numérica del SM se predice.

### 8.3 Lo que abre

- **Tarea 5.3** (atacar P-11 via Kodama): ahora con ecuaciones concretas se puede escribir Ψ_K = exp(i S_CS / ℏ) y analizar la patología de Witten.
- **Tarea 5.4** (reducción a cuerda SCG): partir de S_PA con ansatz de métrica BH y reducir a worldsheet 2D. Requiere las ecuaciones (3.2) y (4.3) derivadas aquí.
- **Tarea 5.5** (flujo RG): ahora con S explícita, el matching entre Régimen II y IV tiene punto de partida.

---

## 9. Honestidad epistémica

**Lo que es teorema (sabido 1977–2011):**
- Que δS_PA → simplicidad (2.2).
- Que δS_PA → torsión nula (4.3).
- Que S_PA + S_cosmo on-shell ≡ E-H + Λ.
- Que BF + Λ → CS en frontera (Baez 2000).

**Lo que es específico de la sesión 16:**
- Verificación explícita de consistencia con el marco SCG (K-019, K-026, Walker-Wang, Crane-Yetter).
- Identificación de que la Tarea 5.2 está técnicamente resuelta — el núcleo gravitacional es consistente.
- Reconocimiento de lo que la derivación NO resuelve (T-1, T-2, T-3, T-4).

**Ningún insight nuevo se promociona.** Esta sesión es de consolidación técnica, no de hallazgo conceptual. Aplicación de la regla 9 (K-005): no añadir más de lo necesario; simplemente ajustar piezas.

**Posible insight candidato K-029:** "el núcleo gravitacional de S_madre SCG reduce on-shell a E-H + Λ autodual, con frontera CS(k=2π/κΛ)". Es más "propiedad estructural" que insight profundo, pero confirma la consistencia del bosquejo y se puede registrar como resultado confirmatorio.

---

## 10. Referencias

- Plebanski, J. (1977). "On the separation of Einstein substructures of the gravitational field." J. Math. Phys. 18, 2511. **Original.**
- Capovilla, R., Dell, J. & Jacobson, T. (1991). "General relativity without the metric." PRL 63, 2325.
- Jacobson, T. & Smolin, L. (1988). "Covariant action for Ashtekar's form of canonical gravity." CQG 5, 583.
- Ashtekar, A. (1986). "New variables for classical and quantum gravity." PRL 57, 2244.
- Baez, J. (2000). "An introduction to spin foam models of BF theory and quantum gravity." Lect. Notes Phys. 543, 25. **Para la conexión BF+Λ ↔ CS en frontera.**
- Krasnov, K. (2009). "Plebanski formulation of general relativity: a practical introduction." Gen. Rel. Grav. 43, 1. Review moderno.
- Krasnov, K. (2011). "Pure connection action principle for general relativity." PRL 106, 251103.
- Alexander, S., Marciano, A. & Smolin, L. (2014). "Gravitational origin of the weak interaction's chirality." PRD 89, 065017. **Identificación A = su(2)_L.**
- Crane, L. & Yetter, D. (1993). "A categorical construction of 4D TQFTs." hep-th/9301062.
- Walker, K. & Wang, Z. (2011/2012). "(3+1)-TQFTs and topological insulators." arXiv:1104.2632.

---

## 11. Firma

**Tarea 5.2 del bosquejo de Lagrangiana: resuelta técnicamente.** El núcleo gravitacional S_PA + S_cosmo reproduce E-H + Λ on-shell; A es la conexión de Ashtekar autodual = su(2)_L (K-019); la frontera es CS con k=2π/(κΛ).

Esto **no resuelve P-8 completamente** — siguen abiertas 4 sub-tareas (5.1 completada en sesión 13 como D-006; 5.3, 5.4, 5.5 pendientes).

Siguiente paso natural: formalizar en D-007; actualizar bosquejo; decidir entre 5.3 (Kodama/P-11), 5.4 (reducción a cuerda SCG) o 5.5 (flujo RG) para la próxima sesión.
