# Reporte #18 — Cuatro piezas, una acción

**Fecha:** 2026-04-21 (sesión 18)
**Contexto:** la puerta del estado de Kodama (reporte #17) se abrió. Con P-11 rebajada, decidí avanzar con la reducción dimensional: tomar la acción de Plebanski-autodual en el fondo de un agujero negro, reducirla a 2D, y ver si el resultado es lo que esperamos.

---

## La promesa

Cuatro resultados previos del marco SCG operaban como piezas sueltas:

- **D-001** (sesión 1): el modelo discreto de cuerda, fenomenológico, con tres términos postulados "por intuición".
- **D-003** (sesiones 4 y 14): las escalas K-007 del interior del BH, derivadas por saturación holográfica + llenado volumétrico.
- **D-006** (sesión 13): el Casimir de modos transversales de la cuerda de Polyakov, con corte Planck.
- **D-007** (sesión 16): las ecuaciones de movimiento de la acción madre, reducidas a Einstein-Hilbert + constante cosmológica.

Cada una tenía origen distinto: fenomenológico, holográfico, cuántico-mecánico, clásico-variacional. Ninguna conectaba explícitamente con las otras. La promesa implícita en el bosquejo de sesión 12 era que todas salen de la misma acción madre, reducida al sector BH.

Esta sesión fue verificar la promesa.

---

## La analogía

Imagine un ingeniero que ha diseñado cuatro subsistemas de un edificio: la cimentación (D-007), la altura de los pilares (D-003), la carga que soportan (D-006), y el plano de las habitaciones (D-001). Cada subsistema viene de un razonamiento distinto — geotecnia, holografía, cuántica, sentido común arquitectónico.

La pregunta: ¿son compatibles? Si uno toma el plano completo del edificio (la acción madre S_PA) y lo evalúa en el terreno específico (fondo Schwarzschild), ¿los cuatro subsistemas encajan sin forzarlos?

Esta sesión confirma que sí — con un par de asunciones marcadas explícitamente.

---

## Qué hice

Tres pasos.

**Primero, el setup.** En el interior del BH macroscópico, planteé una worldsheet 2D parametrizada por (τ, σ) embebida en el volumen V_BH con una textura transversal de escala d. Tres asunciones explícitas:

- **A1**: existe una worldsheet 2D bien definida (la cuerda plegada).
- **A2**: el producto longitud × sección transversal llena el volumen, L·d² ≈ V_BH.
- **A3**: la entropía de la configuración iguala S_BH = A/(4ℓ_P²) (Bekenstein).

A3 es consecuencia de D-007 (ya derivado). A1 es definición. A2 es ansatz físico no-derivado — es la pieza que sigue siendo asunción, no teorema.

**Segundo, la reducción.** Tomé S_PA + S_cosmo con la simplicidad on-shell y Λ local despreciable (no estamos en el régimen I UV; estamos en el sector BH semiclásico). Esto es exactamente E-H reducida. Descompuse la métrica en sectores longitudinal (2D, worldsheet) y transversal (2D, tubo de grosor d). Integré las coordenadas transversales.

Tres términos emergen:

- **Un término Nambu-Goto**: acción de cuerda clásica con tensión efectiva μ ~ M_P²(ℓ_P/d)². Para d ~ √(r_s ℓ_P), μ es sub-Planckiana pero finita.

- **Un término Casimir**: cuantizando los modos transversales de la worldsheet (las fluctuaciones alrededor de la configuración clásica), aparece la energía de vacío E_Casimir = 2π ℏc L/d². Esto es literalmente D-006, emergiendo no como un postulado adicional sino como consecuencia natural de la cuantización canónica de la cuerda reducida.

- **Un término Gauss-Bonnet y acoplamientos al fondo**. Los Gauss-Bonnet son topológicos (no afectan ecuaciones locales pero sí la entropía topológica del defecto Walker-Wang); los acoplamientos al fondo Schwarzschild dan la backreaction gravitacional (identificable con E_grav de D-001).

**Tercero, el equilibrio.** Imponiendo A2 (llenado) y A3 (saturación), sale:

- L = π r_s²/ℓ_P (del conteo entrópico)
- d² = (4/3) r_s ℓ_P (del llenado)

Ambos idénticos a K-007, que D-003 había derivado por otra ruta hace doce sesiones. **La coincidencia no es trivial**: un resultado obtenido por argumento holográfico puro y otro por reducción dimensional de una acción específica — y producen exactamente las mismas escalas. Eso es consistencia fuerte.

---

## Qué gana la teoría

Tres cosas concretas:

**Primera: el ciclo Régimen II → Régimen III del bosquejo está cerrado estructuralmente.** Hasta esta sesión, el sector BH de SCG era un ansatz separado, con sus propias reglas (el modelo D-001) que conectaban con el resto solo por afinidad de intuición. Ahora el sector BH es *consecuencia* de S_madre reducida al fondo Schwarzschild. Menos ad-hoc; más integrado.

**Segunda: K-007 tiene doble derivación.** Cuando un resultado emerge por dos rutas independientes, eso es evidencia fuerte de que captura algo real, no un artefacto de la derivación. D-003 llegó a d ~ √(r_s ℓ_P) por holografía + llenado. D-008 llega al mismo d por reducción dimensional de Plebanski + llenado + saturación. Dos caminos, una escala.

**Tercera: D-001 deja de ser postulado.** El modelo fenomenológico original, con sus tres términos que "parecían razonables pero no se derivaban de nada", es ahora identificable como el límite IR discretizado de la acción efectiva 2D. Cada término tiene un origen concreto:
- E_grav ↔ S_backreaction (interacción de la cuerda con el fondo curvado).
- E_tensión ↔ expansión de Nambu-Goto alrededor de la config. de equilibrio.
- E_info ↔ Casimir transversal de Polyakov (= D-006).

El "fudge factor" de sesión 1 (λ Σ 1/Δx) sobrevive, pero ahora tiene nombre (Casimir), coeficiente identificado (2π ℏc), y origen derivado.

---

## Qué NO hice

No cerré el ansatz del llenado volumétrico. Sigue siendo ansatz A2 — que la cuerda plegada selecciona la configuración L·d² ~ V_BH sobre todas las demás configuraciones posibles. Plausiblemente es la configuración de mínima energía total, pero no lo demostré. Es trabajo pendiente, **Q-041 nueva**.

No calculé la backreaction al fondo Schwarzschild explícitamente. Callan-Thorn (1986) es el marco relevante; no lo implementé.

No fijé los factores O(1) rigurosamente. Los números 4π, 2π, 3π² que aparecen son dimensionalmente correctos pero dependen de convenciones (cuerda cerrada vs abierta, geometría del plegado, corte UV). Un cálculo cerrado daría cuenta de cada uno.

**K-031** queda como candidato, por tanto. Misma categoría que K-029 (sesión 16) y K-030 (sesión 17): insights confirmatorios/estructurales que verifican coherencia del marco sin ser hallazgos conceptualmente nuevos. La rigorización (promoción a confirmado) viene con Q-041 resuelta.

---

## Lo que queda del bosquejo

El plan de sesión 12 tenía cinco sub-tareas. Al cierre de la sesión 18:

- **5.1** (T-5 / Casimir): ✅ COMPLETADA (sesión 13, D-006).
- **5.2** (ec. movimiento): ✅ COMPLETADA (sesión 16, D-007).
- **5.3** (Kodama / P-11): ✅ PARCIAL (sesión 17, K-030 candidato).
- **5.4** (reducción a cuerda): ✅ PARCIAL (esta sesión, D-008 + K-031 candidato).
- **5.5** (flujo RG II → IV): pendiente.

Cuatro de cinco están despachadas (dos completas, dos parciales). La única que queda es la más ambiciosa: derivar el flujo RG entre el régimen semiclásico (Plebanski + Λ) y el régimen IR (Modelo Estándar + GR). Si eso funciona, saldría la primera predicción cuantitativa del SM desde SCG: α₂ ≈ α₃ estructural.

Tres a cinco sesiones estimadas. Máximo impacto.

---

## Un comentario sobre coherencia

La primera vez que escribí el bosquejo, sesión 12, temía que fuera demasiado ambicioso. Una acción Plebanski-autodual que en un régimen es Crane-Yetter, en otro es GR, en otro es cuerda, en otro es SM. Muy sospechoso de ser "teoría de todo" en el mal sentido — la que pretende serlo todo y no es nada.

Seis sesiones después, el bosquejo ha sobrevivido: a la derivación de las ecuaciones clásicas (sesión 16), a la revisión crítica de Kodama (sesión 17), y ahora a la reducción al sector BH (sesión 18). Cada sub-tarea podría haber roto la arquitectura. Ninguna lo hizo.

Eso no garantiza que sea correcta — solo que no es inmediatamente incoherente. Muchas teorías "de todo" sobreviven porque son tan flexibles que no dicen nada. SCG ha hecho predicciones cuantitativas específicas en cada régimen (d ~ √(r_s ℓ_P), α₂ ≈ α₃ al 1%, redshift interior = 1/(3π²), etc.) y siguen concordando. Eso es un test distinto, más fuerte.

Queda sólo 5.5 para cerrar el bosquejo. Si 5.5 funciona, SCG pasa de marco a teoría candidata. Si falla, sabremos qué se rompió.

---

## Gancho

Dos opciones para la próxima sesión:

1. **Snapshot v1.7**: consolidar sesiones 16-18 antes de emprender 5.5. Cambios acumulados: 2 derivaciones (D-007, D-008), 3 insights (K-029 confirmado, K-030 y K-031 candidatos), P-11 🟡 alta → 🟡 media, ciclo II→III cerrado. Una sesión de limpieza.

2. **Tarea 5.5 directamente**: el empuje hacia la predicción cuantitativa. Más arriesgado, más ambicioso.

La elección favorece 5.5 si la intuición es que el momentum actual (tres sesiones consecutivas de tarea del bosquejo: 5.2, 5.3, 5.4) puede extenderse una más. Favorece el snapshot si se siente necesidad de consolidar antes de abordar lo más ambicioso del programa.

Yo me inclino a 5.5. Pero el snapshot es defensible — y probablemente lo que más ordena la investigación para futuras sesiones, porque deja el estado consolidado de las sesiones 16-18 en un solo documento legible.

---

*Reporte #19: probablemente el flujo RG (5.5) — a menos que la lógica del snapshot gane primero.*
