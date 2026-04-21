# D-007 — Ecuaciones de movimiento de S_Plebanski-autodual + Λ

- **ID:** D-007
- **Fecha:** 2026-04-21 (sesión 16)
- **Deriva:** las ecuaciones clásicas de movimiento del núcleo gravitacional del bosquejo de Lagrangiana SCG (S_madre sin defectos, sin materia), y muestra que on-shell son equivalentes a Einstein-Hilbert + Λ autodual.
- **Alcance:** formal. Reproduce un resultado conocido (Plebanski 1977; Baez 2000; Krasnov 2009–2011) en las convenciones SCG.
- **Análisis completo:** `notes/Tarea_5.2_ec_movimiento_plebanski.md`.
- **Resuelve:** primera pieza concreta de P-8 (la debilidad estructural "sin Lagrangiana"). Aborda parcialmente Q-033.
- **Consecuencia:** primer paso del programa Lagrangiana — el núcleo es consistente con GR + Λ, con la conexión autodual = su(2)_L (K-019).

---

## 1. Enunciado

**Proposición.** Sea la acción núcleo del bosquejo SCG:

```
S_núcleo = (1/κ) ∫_M [ Σ^{AB} ∧ F_{AB}(A) − (1/2) ψ_{ABCD} Σ^{AB} ∧ Σ^{CD} − (Λ/6) Σ^{AB} ∧ Σ_{AB} ]
```

con κ = 8πG, variables (Σ^{AB}, A^{AB}, ψ_{ABCD}) como 2-forma autodual, conexión autodual y multiplicador de Lagrange simétrico sin traza respectivamente.

Entonces las ecuaciones clásicas de Euler-Lagrange son:

1. δψ → **Σ^{(AB} ∧ Σ^{CD)}_{sin-traza} = 0** (restricción de simplicidad)
2. δΣ → **F_{AB}(A) = ψ_{ABCD} Σ^{CD} + (Λ/3) Σ_{AB}** (ec. de curvatura)
3. δA → **d_A Σ^{AB} = 0** (torsión autodual nula)

Y, sobre el sector geométrico (Σ = e ∧ e autodual), el sistema es equivalente on-shell a las ecuaciones de Einstein en vacío con constante cosmológica:

```
R_{μν} = Λ g_{μν}                 (con signatura Lorentziana (−,+,+,+))
```

donde la conexión autodual A coincide con la parte autodual de la conexión de spin del vierbein — es decir, con la **conexión de Ashtekar autodual** (K-019).

**Corolario estructural.** El núcleo gravitacional de S_madre es consistente con GR + Λ autodual. No hay conflicto con los resultados previos del marco SCG (K-019, K-024, K-026). La frontera del bulk es Chern-Simons autodual con nivel

```
k_CS = 2π / (κ Λ)
```

(Baez 2000, aplicado a nuestro núcleo).

---

## 2. Derivación

### 2.1 Variación respecto a ψ (simplicidad)

La única dependencia en ψ es el término cuadrático. Variando δψ_{ABCD} (totalmente simétrico, sin traza):

```
0 = δS / δψ_{ABCD} = −(1/2κ) Σ^{(AB} ∧ Σ^{CD)}_{sin-traza}
```

De donde sale la **restricción de simplicidad de Plebanski**:

```
Σ^{(AB} ∧ Σ^{CD)}_{sin-traza} = 0                                       (D-007.1)
```

Soluciones:
- **Sector geométrico (i):** Σ^{AB} = e^{A}_μ e^{B}_ν dx^μ ∧ dx^ν (proyección autodual), con e^A_μ un vierbein espinorial real.
- **Sector no-geométrico (ii):** descartado por convención física (necesitamos un vierbein para recuperar GR).

En SCG adoptamos el sector (i). La traza de Σ ∧ Σ (parte sin restringir por ψ) queda libre.

### 2.2 Variación respecto a Σ (ec. de curvatura)

Variando δΣ^{AB}:

```
0 = δS / δΣ^{AB} = (1/κ)[ F_{AB}(A) − ψ_{ABCD} Σ^{CD} − (Λ/3) Σ_{AB} ]
```

De donde:

```
F_{AB}(A) = ψ_{ABCD} Σ^{CD} + (Λ/3) Σ_{AB}                              (D-007.2)
```

Esta es la ecuación de curvatura autodual de Plebanski. Descomposición on-shell:
- Parte proporcional a Σ: da la **ecuación de traza**, R = 4Λ.
- Parte sin traza: identifica ψ con el **tensor de Weyl autodual** C^+_{ABCD}.

### 2.3 Variación respecto a A (torsión nula)

Variando δA^{AB}, solo el término Σ ∧ F contribuye. Tras integración por partes en el bulk:

```
0 = δS / δA^{AB} ⇒ d_A Σ^{AB} = 0                                       (D-007.3)
```

Aquí d_A es la derivada covariante con la conexión A. Sustituyendo Σ = e ∧ e (on-shell por 2.1):

```
d_A(e^A ∧ e^B) = 0
```

La solución única para e no degenerado es que A sea la parte autodual ω_+ de la conexión de spin ω del vierbein:

```
A^{AB} = ω^{AB}_{+} = (1/2)(ω^{AB} + *ω^{AB})                           (D-007.4)
```

Esto es la **definición original de la conexión de Ashtekar** (Ashtekar 1986, Jacobson-Smolin 1988).

### 2.4 Reducción a Einstein-Hilbert + Λ

Combinando (D-007.1)–(D-007.4):
- Σ = e ∧ e → la acción ∫ Σ ∧ F es Einstein-Hilbert en variables de Ashtekar.
- F = (Λ/3)Σ + C_+ Σ → ecuaciones de Einstein R_{μν} = Λ g_{μν}.
- A = ω_+ → conexión autodual compatible con e.

On-shell (ver Plebanski 1977, Capovilla-Dell-Jacobson 1991):

```
S_núcleo |_on-shell = (1/2κ) ∫_M (R − 2Λ) √(−g) d^4x + términos topológicos     (D-007.5)
```

La parte real es **Einstein-Hilbert + Λ**. La parte imaginaria es una clase topológica (Pontryagin/Euler) que no afecta las ecuaciones clásicas.

---

## 3. Alcance y limitaciones

### 3.1 Lo que D-007 establece

1. Las ecuaciones de movimiento clásicas del núcleo gravitacional SCG son GR autodual + Λ.
2. La conexión A emergente es la conexión de Ashtekar autodual = su(2)_L (K-019 reconfirmado desde primeros principios clásicos).
3. La frontera en una región finita es CS autodual con k = 2π/(κΛ).
4. El límite Λ → 0 + ψ relajado produce BF topológico, consistente con el régimen I de SCG (Crane-Yetter/Walker-Wang).

### 3.2 Lo que D-007 NO establece

1. **No cuantiza** la acción. Las patologías del estado Kodama (Witten 2003) y la no-normalizabilidad no se tratan.
2. **No incluye materia.** La S_madre completa del bosquejo tiene S_defectos (configuraciones topológicas de A que corresponden a fermiones); aquí solo el núcleo gravitacional sin defectos.
3. **No resuelve las tensiones** T-1 (k topológico vs k dinámico) ni T-2 (P-11, condiciones de realidad complejas) ni T-4 (matter de red vs S_matter).
4. **No predice ninguna constante del SM.**
5. La identidad *Lagrangiana continua Plebanski* ↔ *state-sum Crane-Yetter* ↔ *lattice Walker-Wang* se usa vía Baez 2000. Su rigorización en el contexto SCG con UBFC específica sigue abierta (parte de T-3).

### 3.3 Estado epistémico

- **Teorema** (sabido 1977–2011): la equivalencia on-shell S_PA + S_cosmo ≡ E-H + Λ.
- **Consolidación SCG**: verificación de compatibilidad con K-019, K-024, K-026.
- **Cálculo de borde** (parcial): aplicación estándar de Baez 2000 al núcleo SCG. Correcciones por ψ argumentadas como sub-dominantes, no computadas explícitamente.

---

## 4. Conclusión

**El núcleo gravitacional del bosquejo de Lagrangiana SCG (sesión 12) es internamente consistente y reproduce GR + Λ autodual on-shell.**

Primera pieza concreta del programa Lagrangiana. La debilidad P-8 se reduce desde "sin Lagrangiana" a "Lagrangiana parcial: núcleo gravitacional ya derivable; materia y tensiones k/realidad pendientes".

---

## 5. Implicaciones

- `notes/R_lagrangiana_bosquejo.md`: **Tarea 5.2 COMPLETADA**. Restantes: 5.3 (Kodama/P-11), 5.4 (reducción a cuerda SCG), 5.5 (flujo RG).
- `logic/refutations/debilidades_H-001.md`: P-8 se refina de "parcial" a "parcial, núcleo gravitacional derivado".
- `hypotheses/active/H-001_...`: el núcleo de S_madre tiene ya derivación — piezas 5.4 y 5.5 conectarán con el sector BH (D-003) y las constantes del SM respectivamente.
- `memory/open_questions.md`: Q-033 (frontera CS = k=2π/Λ) se marca **parcialmente resuelta** — argumento estructural ok, rigorización de correcciones por ψ pendiente.

**Insight candidato K-029 (estructural, confirmatorio):** *El núcleo gravitacional de S_madre reduce on-shell a Einstein-Hilbert + Λ con conexión autodual de Ashtekar, y su frontera es Chern-Simons con k = 2π/(κΛ).* No es un hallazgo nuevo per se; es la verificación de que el bosquejo de sesión 12 es estructuralmente consistente.

---

## 6. Relación con la literatura

- **Plebanski 1977:** teorema fundacional (BF + simplicidad = E-H).
- **Capovilla-Dell-Jacobson 1991:** tratamiento moderno espinorial.
- **Baez 2000:** BF + Λ ↔ CS en frontera; base de la reducción k = 2π/(κΛ).
- **Krasnov 2009, 2011:** revisión moderna de la formulación Plebanski y variante pura conexión.
- **Alexander-Marciano-Smolin 2014:** A autodual = su(2)_L, confirma K-019.
- **Crane-Yetter 1993; Walker-Wang 2011:** versión cuantizada del núcleo gravitacional; conexión vía Baez (2000).

Ningún resultado clásico es original de esta derivación. La originalidad está en la *aplicación explícita* al contexto SCG: fijar convenciones, verificar compatibilidad con K-019/K-024/K-026, e identificar explícitamente la tarea 5.2 del bosquejo como *técnicamente cerrada*.

---

## 7. Firma

D-007 cierra la Tarea 5.2 del bosquejo de Lagrangiana SCG. Núcleo gravitacional S_PA + S_cosmo ≡ E-H + Λ autodual on-shell; frontera CS(k=2π/κΛ); A = su(2)_L (K-019 reconfirmado).

Pieza técnica, no hallazgo conceptual. Aplicación de K-005: "la teoría no necesita más estructura, solo verificar que los piezos encajen". Aquí encajan.

Siguiente paso natural del programa Lagrangiana: Tarea 5.3 (Kodama/P-11) o Tarea 5.4 (reducción a cuerda SCG).
