# Teoría SCG — Resumen para física teórica

Panorama accesible del marco SCG (Stabilized Gravitational String) para un lector con formación en física teórica: gravedad cuántica, teoría de cuerdas, LQG o fenomenología de partículas. La intención es que en 20–30 minutos puedas evaluar si merece tu atención y, en caso afirmativo, adónde mirar a continuación.

**Estado:** 22 sesiones de desarrollo (abril 2026). Snapshot maestro: [`journal/2026-04-21_snapshot_v1.8.md`](journal/2026-04-21_snapshot_v1.8.md).

**Advertencia preliminar:** esto no es un paper. Es el registro vivo de una investigación en curso. Las afirmaciones están marcadas explícitamente como *derivadas*, *argumentadas*, *propuestas* o *candidatas*. Ningún resultado se presenta como cerrado si no lo está.

---

## 1. Punto de partida

El Modelo Estándar y la Relatividad General coinciden con la observación al 1% o mejor, pero ninguno de los dos explica:

- Por qué hay exactamente 3 dimensiones espaciales y 1 temporal.
- Por qué el grupo gauge es SU(3) × SU(2) × U(1) y no otro.
- Por qué la carga eléctrica se cuantiza en 1/3.
- Por qué existe confinamiento de color.
- Por qué sólo SU(2) viola paridad.
- Qué pasa en el interior de un agujero negro.
- Por qué α₂(M_P) ≈ α₃(M_P) ≈ 0.02 pero α₁(M_P) ≈ 0.03 (near-convergence sin SUSY).

La hipótesis SCG: todos estos hechos admiten una explicación estructural común si se postulan sólo dos axiomas.

---

## 2. Los dos axiomas

**A-001 — Corte Planck.** Existe una escala ℓ_P ≈ 1.6×10⁻³⁵ m por debajo de la cual la descripción continua del espacio-tiempo deja de ser válida.

**A-002 — Transición de fase gravitacional.** A densidades ρ ~ ρ_P, la configuración de mínima energía de la materia pasa de una red difusa a un objeto extendido 1D (una "cuerda gravitacional").

Eso es todo. No se postula nada más. El resto se deriva o se argumenta desde ahí.

Lo que se postulaba inicialmente como tercer axioma — un término repulsivo estabilizador — se demostró que es el efecto Casimir estándar de los modos transversales de Polyakov con corte Planck ([D-006](logic/derivations/D-006_A-003_desde_polyakov.md)). Por lo tanto deja de ser axioma.

---

## 3. Arquitectura en una página

La acción madre propuesta, como bosquejo:

```
S_madre = S_Plebanski-autodual[Σ, A, ψ] + S_cosmo[Σ, Λ] + S_defectos[topologías de A]
```

Se reduce a cuatro regímenes según la escala de energía:

| Régimen | Energía | Descripción |
|---|---|---|
| **I** | E ≫ M_P | Walker-Wang / Crane-Yetter TQFT topológica |
| **II** | E ~ M_P | Einstein-Hilbert + Λ autodual (derivado, [D-007](logic/derivations/D-007_ec_movimiento_plebanski.md)) |
| **III** | densidad ~ ρ_P | Cuerda 2D efectiva en fondo BH (derivado, [D-008](logic/derivations/D-008_reduccion_a_cuerda_SCG.md) + [D-009](logic/derivations/D-009_llenado_volumetrico_variacional.md)) |
| **IV** | E ≪ M_P | SM + GR semiclásica |

El programa de **5 sub-tareas** para pasar del bosquejo a la Lagrangiana derivada está abierto. Al cierre de sesión 22: 2 sub-tareas con derivación cerrada (5.1, 5.2), 1 con derivación confirmada estructuralmente (5.4), 2 con análisis estructural + insight candidato (5.3, 5.5).

---

## 4. Lo que se deriva desde A-001 + A-002

Con 9 derivaciones formales ([D-001 a D-009](logic/derivations/)):

### 4.1 Dimensionalidad {1, 3, 1} como punto fijo

- **D-002**: balance presión de degeneración ↔ gravedad da D_object = 1 como única dimensión con balance marginal independiente del número de modos.
- **H-002**: objetos 1D requieren codimensión 2 para topología no trivial (nudos), lo cual fija D_espacio = 3.
- **D-005**: so(4,C) es la única álgebra de Lorentz compleja que factoriza en productos simples (Dynkin: D₂ = A₁ + A₁). Con D_espacio = 3 se fuerza D_tiempo = 1.

La terna {D_obj = 1, D_espacio = 3, D_tiempo = 1} no es cadena causal sino **punto fijo auto-consistente único** ([K-025](memory/key_insights.md)).

### 4.2 Grupo gauge SU(3) × SU(2) × U(1)

Derivado en [D-004](logic/derivations/D-004_reglas_fusion_vertices_SCG.md) desde la geometría trivalente de la red Walker-Wang en 3+1D:

- **U(1)_Y**: modos transversales de cada segmento (SO(2) ≅ U(1)). Derivado.
- **Z₃ → carga en 1/3**: trivalencia del vértice rompe SO(2) a Z₃. Derivado. Z₃ = centro de SU(3), y las representaciones de trialidad 0/1/2 son exactamente leptones/quarks/antiquarks.
- **SU(2)_L**: conexión autodual de Ashtekar = sector quiral del grupo de Lorentz complexificado (motivado por Alexander-Marciano-Smolin 2014).
- **SU(3)**: extensión continua de Z₃ por unicidad de braiding quiral + matching dimensional (6 argumentos convergentes).

### 4.3 Patrón α₂ ≈ α₃ ≠ α₁

El running 1-loop del SM da α₂(M_P) ≈ 0.0202, α₃(M_P) ≈ 0.0191, α₁(M_P) ≈ 0.0301. En SCG ([K-032 candidato](memory/key_insights.md)) esto es **estructural**: SU(2)_L y SU(3) son "gauge de vértice" (ambos emergen de vértices trivalentes de la red WW), mientras que U(1)_Y es "gauge de segmento". Mismo objeto geométrico → mismo acoplamiento a M_P.

Observación numérica sugerente: α₃(M_P) = 0.0191 ≈ γ_Immirzi / (4π) = 0.0189 al **1%**.

### 4.4 Interior no-singular de los agujeros negros

Derivado en [D-003 v1.2](logic/derivations/D-003_conservacion_entropia.md) por holografía + llenado, y en [D-008 + D-009](logic/derivations/) por reducción dimensional de la acción de Plebanski con minimización variacional:

- Interior = cuerda plegada con L ~ r_s²/ℓ_P y d ~ √(r_s·ℓ_P).
- Para un BH estelar de 30 M_☉: d ≈ 1 fm (escala nuclear, no Planck).
- Satura exactamente la cota de Bekenstein: S_cuerda = A/(4ℓ_P²).
- La cuerda SCG plegada es el análogo cuántico-gravitacional de una enana blanca — la presión de Casimir cuántica balanceada por el confinamiento geométrico del horizonte.

### 4.5 Una predicción falsable

Ecos de ondas gravitacionales en la fase de ringdown de fusiones BH-BH:
- Fuzzballs (Mathur) / stretched horizon (Susskind): Δt ≈ 2(r_s/c)·ln(r_s/ℓ_P).
- **SCG**: Δt ≈ (r_s/c)·ln(r_s/ℓ_P) — **la mitad**.

Para un BH de 30 M_☉: ~27 ms vs ~53 ms de fuzzballs. Diferencia de ~26 ms, resoluble con LIGO actual estadísticamente y con detectores 3G (Einstein Telescope, Cosmic Explorer) fusión a fusión.

---

## 5. Lo que se propone (con evidencia parcial)

### 5.1 Higgs como condensación topológica

La ruptura electrodébil es condensación de un anyón (j=½, Y=1) en la red WW. Por Fradkin-Shenker, Higgs = confinamiento de SU(2). Mecanismo demostrado en materia condensada (Bais-Slingerland 2009) aplicado a la red SCG. Ver [K-021](memory/key_insights.md).

### 5.2 Tres generaciones = Z₃ × Z₃

La red trivalente tiene dos Z₃ independientes: una del vértice primal (color, trialidad) y una del vértice dual (generación). N_gen = N_color = 3 porque ambas Z₃ vienen de la trivalencia (D = 3). Ver [K-020](memory/key_insights.md). **Especulativo** — sin cálculo cuantitativo todavía.

### 5.3 Redshift promedio del interior BH

Por consistencia ADM (la energía Casimir plana excede Mc² por factor ~30), el redshift promedio del interior de un BH-SCG es ⟨f⟩ ≈ 1/(3π²) ≈ 0.034. Ver [K-028 candidato](memory/key_insights.md). Cálculo QFT+GR riguroso pendiente.

### 5.4 Resolución tentativa de la paradoja de información

Los estados de vibración de la cuerda plegada pueden codificar la información de la materia caída; la radiación de Hawking se correlacionaría con ellos via el horizonte. Consistente con unitariedad. Mecanismo microscópico pendiente.

---

## 6. Lo que NO se predice (honestidad)

- Masas fermiónicas (electrón, quarks, neutrinos).
- Yukawas.
- v = 246 GeV.
- Matrices CKM/PMNS.
- Λ cosmológica observada.
- Valor numérico exacto de α_gauge (aunque α_3(M_P) ≈ γ/(4π) al 1% es sugerente).
- La **asimetría máxima** de SU(2)_L con β real: parcialmente resuelta, pendiente de mecanismo adicional ([Q-042](memory/open_questions.md)).

Es decir: la teoría tiene estructura cualitativa robusta pero aún no ofrece predicciones numéricas concretas comparables con el SM.

---

## 7. Debilidades reconocidas

Ver [`logic/refutations/debilidades_H-001.md`](logic/refutations/debilidades_H-001.md) para la lista completa. Las principales:

- **P-11 (🟡 media):** la formulación depende de la conexión de Ashtekar-Barbero-Immirzi con β específico. Con β = −i (autodual), la identificación SU(2)_L del Lorentz complexificado es literal pero el estado de Kodama tiene las patologías de Witten 2003. Con β real (Randono 2006), el estado es sano pero la asimetría máxima del SM no emerge automáticamente. **Ninguna de las dos rutas está completamente cerrada.**
- **P-8 (🟡 media):** la Lagrangiana completa no existe; sólo la arquitectura + 3/5 sub-tareas cerradas.
- **P-14 (🟡 media):** consistencia cuántica de Polyakov 4D no-crítica como teoría efectiva del defecto Walker-Wang. Plausible pero no demostrada.
- **P-12, P-13:** hipercarga Y = 1/6 y estadística fermiónica no se derivan directamente.

Sin eslabones rojos en la cadena lógica, pero varios amarillos maduros.

---

## 8. Lo que la Ruta A de cuantificación ha rendido

Tras cerrar el bosquejo de Lagrangiana estructuralmente (sesión 19), se intentó promover los 4 insights candidatos a confirmados (sesiones 20–22):

- **K-031 (llenado volumétrico):** ✅ promovido ([D-009](logic/derivations/D-009_llenado_volumetrico_variacional.md) por argumento variacional).
- **K-030 vía ABKP 2025 ([Q-039](notes/Q-039_Lambda_UV_regimen_I.md)):** ❌ resultado negativo. Λ_UV en régimen I de SCG es O(M_P²), muy por debajo del umbral Λ_c = 384 M_P².
- **K-030 vía Randono 2006 ([Q-040](notes/Q-040_compatibilidad_randono_K-019.md)):** ⚠️ parcial. Preserva viabilidad del estado pero no la asimetría máxima del SM.
- **K-032 (matching II→IV) y K-028 (redshift riguroso):** pendientes.

En tres sesiones: una promoción, dos resultados no-promoción. El marco sobrevivió pero K-030 quedó más débil que antes. La investigación continuará pero está en fase de consolidación antes de invertir en las dos piezas pendientes.

---

## 9. Qué es original y qué es aplicación

**Aplicación de mecanismos conocidos (ninguno inventado aquí):**
- Acción de Plebanski autodual (1977).
- Estado de Kodama con β real (Randono 2006).
- Walker-Wang lattice en 3+1D (2011).
- Crane-Yetter 4D TQFT (1993).
- String-net condensation (Levin-Wen 2005, Wen 2003).
- SU(2)_L gravitacional (Alexander-Marciano-Smolin 2014).
- Condensación de anyones (Bais-Slingerland 2009).
- Cuantización canónica de Polyakov.
- Efecto Casimir en cuerdas confinadas.

**Originalidad (en la medida en que la revisión de literatura lo respalde):**
- La **integración** de estos mecanismos en un marco único bajo S_Plebanski-autodual + Walker-Wang.
- La **doble derivación** de las escalas interiores del BH (holografía + reducción dimensional) con el mismo resultado.
- La **identificación** del patrón α₂ ≈ α₃ ≠ α₁ como estructural "vértice vs segmento" (no coincidencia).
- La derivación del **llenado volumétrico** como analogy cuántico-gravitacional de Chandrasekhar.
- La integración de la **signatura (3,1)** como consecuencia de la única factorización de Dynkin compatible con objetos 1D.

Cada mecanismo individual es estándar. La novedad es la conexión.

---

## 10. Qué invito a criticar

Dos niveles:

**Nivel 1 — fundamentos:**
- ¿Es A-002 (transición de fase gravitacional) justificable con más precisión? ¿Se puede derivar desde A-001 + principio variacional más general?
- La argumentación de [D-002](logic/derivations/D-002_dimensionalidad_critica.md) (dimensionalidad D = 1 como única dimensión con balance) ¿sobrevive a generalizaciones (cuerdas con masa, defectos de dimensión mayor)?
- La "enana blanca cuántica" ([D-009](logic/derivations/D-009_llenado_volumetrico_variacional.md)) asume plegado cilíndrico uniforme. ¿Es realmente el mínimo global?

**Nivel 2 — aplicación:**
- ¿Es la identificación del bosquejo con Walker-Wang 3+1D correcta? La UBFC específica que produciría la fenomenología del SM no está construida.
- El matching II→IV explícito (cálculo de loops + level shifting entre Plebanski-autodual + Λ y SM + GR) está pendiente. ¿Hay obstrucciones evidentes que no he visto?
- La coincidencia α_3(M_P) ≈ γ/(4π) al 1%: ¿es genuina o es artefacto del running SM a 1-loop?
- La ruta Randono (β real) pierde asimetría máxima. [Kaplan 2024](https://arxiv.org/abs/2312.01494) ofrece fermiones quirales en fronteras topológicas — ¿es ese el mecanismo de amplificación que falta ([Q-042](memory/open_questions.md))?

---

## 11. Cómo dialogar

- **Feedback técnico:** [Issues en GitHub](https://github.com/picojuanc/fisica-investigaciones/issues). Ideal para objeciones específicas con referencia al archivo que discute el punto.
- **Contribuciones:** por ahora el repo es de un solo autor, pero pull requests con correcciones, literatura adicional o contra-argumentos son bienvenidos.
- **Email:** picojuanc@gmail.com.

Si tienes un contra-ejemplo sólido que rompa la cadena lógica, es genuinamente útil: esta investigación adopta explícitamente la regla de que destruir un resultado propio es celebrable. El objetivo es construir conocimiento, no defender una posición.

---

## 12. Cómo seguir

- Los **22 reportes narrativos** en [`journal/reportes/`](journal/reportes/) cuentan la historia cronológica.
- El **snapshot v1.8** en [`journal/2026-04-21_snapshot_v1.8.md`](journal/2026-04-21_snapshot_v1.8.md) consolida el estado técnico actual.
- Las **9 derivaciones** en [`logic/derivations/`](logic/derivations/) son las piezas formales.
- Los **análisis por pregunta/tarea** en [`notes/`](notes/) son el trabajo detallado.

Referencias a la literatura en [`literature/references.md`](literature/references.md).

---

**Juan Pico** ([@picojuanc](https://github.com/picojuanc)) — en colaboración con Claude (Anthropic) como asistente de razonamiento.

Investigación en curso. Este documento se actualizará cuando haya progreso substantivo.
