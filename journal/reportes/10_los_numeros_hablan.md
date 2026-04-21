# Reporte 10 — Los números hablan

*Sesión 10 · 19 de abril de 2026*

---

Hasta ahora, la teoría SCG ha sido un edificio conceptual: derivaciones cualitativas, argumentos topológicos, cadenas lógicas. Hermoso pero aéreo. Hoy, por primera vez, la confrontamos con números reales.

## La prueba

La pregunta es simple: si SU(2) y SU(3) vienen de la misma estructura geométrica (la red SCG), sus constantes de acoplamiento deberían ser similares a la escala de Planck. Si U(1) viene de una fuente diferente (los modos transversales), la suya debería ser distinta.

¿Qué dicen los datos?

Las tres constantes de acoplamiento del Modelo Estándar están medidas con gran precisión a la escala del bosón Z (91 GeV). Usando las ecuaciones del grupo de renormalización — que describen cómo los acoplamientos cambian con la energía — las extrapolamos hasta la escala de Planck (10¹⁹ GeV), cruzando 17 órdenes de magnitud.

Resultado:

```
α₂(M_Planck) ≈ 0.020    (fuerza débil)
α₃(M_Planck) ≈ 0.019    (fuerza fuerte)
α₁(M_Planck) ≈ 0.030    (hipercarga)
```

**Las fuerzas débil y fuerte casi convergen a la escala de Planck.** La hipercarga queda aparte.

Esto es exactamente el patrón que la teoría SCG predice: SU(2) y SU(3) comparten origen geométrico → acoplamientos similares. U(1) tiene origen distinto → acoplamiento diferente.

## La coincidencia inquietante

Hay algo más. En LQG, existe un número llamado el parámetro de Immirzi (γ = 0.2375), que determina el espectro de áreas del espacio-tiempo cuántico. Es el "quantum" mínimo de área, por así decirlo.

Si dividimos γ entre 4π:

```
γ/(4π) = 0.2375 / 12.566 = 0.01890
```

Comparar con α₃(M_P) = 0.0191. Coinciden al 1%.

¿Coincidencia? Quizá. Hay muchos números cercanos a 0.02 que se podrían construir. Pero si no es coincidencia, significaría que la intensidad de la fuerza fuerte está determinada por el mismo parámetro que fija la geometría cuántica del espacio-tiempo. En una teoría donde las partículas SON el espacio-tiempo deformado, esto tendría sentido profundo.

No lo hemos derivado. Es una observación numérica que espera una explicación.

## El problema que apareció (y se resolvió)

Los números también revelaron un problema. En la sesión 8 habíamos argumentado que a escala de Planck, la teoría de Chern-Simons del color está en su nivel mínimo (k=1). Pero un acoplamiento de α ≈ 0.02 implica un nivel k ≈ 300, no k = 1.

A nivel 1, solo existen 3 tipos de anyones (los tres "colores"). A nivel 300, existen unas 45,000 representaciones. El argumento de unicidad que usamos para derivar SU(3) — "el único orden topológico quiral con fusión Z₃ es SU(3)₁" — solo funciona a k = 1.

Por un momento, pareció que los números habían roto el eslabón SU(3).

Pero la resolución resultó ser más simple y más profunda de lo esperado: **el grupo gauge y el nivel de Chern-Simons son datos independientes.** El grupo gauge (SU(3)) es un dato topológico — dice QUÉ simetría tiene la teoría. El nivel k es un dato dinámico — dice cuán FUERTE es el acoplamiento. Cambiar k de 1 a 300 no cambia SU(3) en SU(5) ni en E₆. Solo cambia cuántas representaciones participan en la dinámica.

Es como un piano: tiene 88 teclas (las representaciones), pero la melodía (el grupo gauge) es la misma sin importar cuántas teclas estés usando en un momento dado.

Además, encontramos un argumento nuevo que no teníamos: la **correspondencia dimensional**. El vértice de la red SCG tiene 3 patas. La representación fundamental de SU(3) tiene dimensión 3. No es coincidencia — las 3 patas SON los 3 colores. Para SU(6) necesitaríamos vértices de 6 patas; para E₆, algo aún más complejo. La trivalencia del vértice en D=3 selecciona SU(3) directamente, sin necesidad de argumentos de unicidad.

## Los tres regímenes

La resolución del problema k=1 vs k~300 reveló una imagen nueva de la teoría:

**Régimen I — Topológico** (E >> M_Planck, k ≈ 1): no hay métrica, no hay distancias. Solo datos topológicos puros. Aquí se determinan el grupo gauge, la quiralidad, la cuantización de la carga. Es la fase "pre-geométrica" del universo.

**Régimen II — Semiclásico** (E ~ M_Planck, k ~ 300): la métrica emerge. Las distancias se vuelven significativas. El acoplamiento es débil (α ~ 0.02). El grupo gauge es el mismo, pero ahora tiene un espectro rico de excitaciones.

**Régimen III — Perturbativo** (E << M_Planck, k → ∞): QFT estándar sobre espacio-tiempo curvo. QCD con confinamiento. El SM tal como lo conocemos.

El grupo gauge no cambia nunca. Solo cambia la "resolución" — cuántas de sus representaciones están activas.

## Lo que aprendimos

Esta fue la primera vez que la teoría se midió contra números, y el resultado es mixto pero esperanzador:

- **Predicción cualitativa confirmada:** α₂ ≈ α₃ ≠ α₁ ✓
- **Coincidencia numérica sugerente:** α₃ ≈ γ/(4π) al 1%
- **Problema encontrado y resuelto:** k=1 inconsistente con α~0.02, resuelto por la independencia grupo/nivel
- **Imagen nueva ganada:** los tres regímenes de la teoría

Los números no rompieron la teoría. Tampoco la confirmaron. Pero la obligaron a ser más precisa sobre lo que dice y lo que no dice. Eso es progreso.

---

*Siguiente reporte: stress-test de la cadena completa. La cadena es ahora más larga que nunca — hora de intentar romperla otra vez.*
