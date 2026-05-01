# H-004 — Sesión 81: Definición operacional de $\mathcal{C}_0$ + operación primitiva mínima

**Fecha:** 2026-05-01 (sesión 81, cierre formal sub-tarea α)
**Propósito:** dar contenido matemático preciso al axioma A-005 antes de iniciar la sub-tarea β. Define qué es exactamente "estructura informacional categorial primitiva" y cuál es el "verbo" fundamental del marco H-004.

---

## 1. La pregunta operacional

A-005 afirma: existe una estructura informacional categorial primitiva $\mathcal{C}_0$ tal que toda magnitud, escala y partícula del universo es invariante derivable de $\mathcal{C}_0$.

**¿Pero qué es exactamente $\mathcal{C}_0$?** Sin esta precisión, A-005 corre dos riesgos opuestos:

1. **Subdeterminación:** "estructura informacional" puede significar cualquier cosa (set, grupo, grafo, etc.) → A-005 vacío.
2. **Sobre-especificación:** elegir `Spin(10)_1` directamente → A-005 deja de derivar `Spin(10)_1`, lo postula.

La sub-tarea α resuelve esta tensión definiendo $\mathcal{C}_0$ a un **nivel de abstracción intermedio**: suficientemente preciso para que A-005 tenga contenido operacional, suficientemente abstracto para que la UBFC específica sea **derivable** (no postulada) en sub-tarea δ.

---

## 2. Definición operacional de $\mathcal{C}_0$

### 2.1 Definición principal (camino B, S81)

> **Definición α.1 — Estructura informacional categorial primitiva.**
>
> $\mathcal{C}_0$ es una **categoría modular tensorial unitaria** ($\dagger$-MTC) **sobre $\mathbb{C}$** equipada con:
> - **Tensor monoidal** $\otimes: \mathcal{C}_0 \times \mathcal{C}_0 \to \mathcal{C}_0$.
> - **Unidad** $\mathbf{1} \in \mathcal{C}_0$.
> - **Asociador** $\alpha_{a,b,c}: (a \otimes b) \otimes c \xrightarrow{\sim} a \otimes (b \otimes c)$ satisfaciendo el axioma del pentágono.
> - **Estructura rígida** (objetos duales): para todo $a \in \mathcal{C}_0$, existe $a^* \in \mathcal{C}_0$ con morfismos coevaluación / evaluación.
> - **Estructura unitaria** $\dagger$: cada hom-espacio es Hilbert finito-dimensional; $\otimes$ y $\alpha$ son $\dagger$-functoriales.
> - **Trenzado** $\beta_{a,b}: a \otimes b \xrightarrow{\sim} b \otimes a$ satisfaciendo el axioma del hexágono.
> - **Twist (spin)** $\theta_a: a \to a$ con $\theta_{a \otimes b} = \beta_{b,a} \beta_{a,b} (\theta_a \otimes \theta_b)$.
> - **Modularidad** (matriz $S$ no-degenerada): $S_{ab} = \text{tr}(\beta_{a^*,b} \beta_{b,a^*})$, $\det(S) \neq 0$.
> - **Pivotal / esférica**: dimensiones cuánticas $d_a = \text{tr}(\text{id}_a)$ son números reales positivos.
> - **Finitud**: número finito de clases de isomorfismo de objetos simples (etiquetas).

**Notación:** $\mathcal{C}_0 = (\mathcal{C}_0, \otimes, \mathbf{1}, \alpha, \beta, \theta, \dagger, \text{rig})$.

**Equivalencia:** dos $\dagger$-MTCs son **equivalentes** si existe equivalencia $\dagger$-monoidal trenzada entre ellas. Definimos:

$$[\mathcal{C}_0] \in \dagger\text{-MTC} / \sim_{\text{equiv}}$$

A-005 afirma la **existencia** de un representante; sub-tarea δ derivará la **unicidad** del representante mínimo compatible con SM observable.

### 2.2 Justificación de la elección $\dagger$-MTC

**¿Por qué $\dagger$-MTC y no estructuras más simples / más complejas?**

| Estructura | ¿Captura cuántica? | ¿Captura topología? | ¿Captura información? | Veredicto |
|---|---|---|---|---|
| Set | ✗ | ✗ | parcial (información clásica) | Demasiado pobre |
| Grupo | ✗ | ✗ | parcial (simetrías) | Demasiado pobre |
| Espacio Hilbert | ✓ | ✗ | parcial (estados) | Sin topología |
| Categoría monoidal | ✗ | parcial | ✓ | Sin cuántica completa |
| Categoría tensorial | ✓ | parcial | ✓ | Sin trenzado |
| Categoría tensorial trenzada | ✓ | ✓ (parcial) | ✓ | Sin modularidad |
| **$\dagger$-MTC** | **✓✓** | **✓✓** | **✓✓** | **Mínima compatible** |
| Categoría tensorial trenzada modular fermionic | ✓ | ✓ | ✓ | Subcaso $\dagger$-MTC |
| ∞-categoría con monoidal estructura | ✓ | ✓ | ✓ | Generalización (sub-tareas avanzadas) |

**$\dagger$-MTC es la estructura mínima que combina:**
1. **Cuántica:** $\dagger$ + Hilbert estructura + dimensiones cuánticas.
2. **Topología:** trenzado + twist + modularidad.
3. **Información:** fusión $\otimes$ + cargas conservadas (etiquetas) + composicionalidad.

Es el lenguaje natural para órdenes topológicos en (2+1)D y fronteras de TQFTs en (3+1)D — exactamente lo que SCG ya usa con `Spin(10)_1`.

### 2.3 Extensión fermiónica (super-modularidad)

Para acomodar fermiones del SM, $\mathcal{C}_0$ admite **extensión fermiónica** vía condensación del fermión transparente $f$ con $\theta_f = -1$, dando una **super-MTC**.

Esta extensión es **opcional** en la definición α.1: A-005 admite tanto $\mathcal{C}_0$ bosónica como super-modular. Sub-tarea δ determinará cuál es seleccionada por el criterio de auto-consistencia + correspondencia SM.

### 2.4 Extensión a ∞-categorías (camino B avanzado)

Si sub-tareas δ-ζ requieren identidades de orden superior (asociadores de asociadores, etc.), $\mathcal{C}_0$ se eleva naturalmente a una **(∞,1)-MTC monoidal trenzada** en el sentido de Lurie HTT. Esta extensión preserva todas las propiedades anteriores y añade homotopía coherente.

**Trigger para ∞-elevación:** sub-tarea ε o ζ requiere identidades coherentes que no encajen en $\dagger$-MTC ordinaria.

### 2.5 Lo que $\mathcal{C}_0$ NO es (delimitación)

- **NO es Set ni grupo** — pobreza estructural.
- **NO es necesariamente discreta** — admite estructuras continuas vía colimits filtrados.
- **NO es teoría de cuerdas** — no requiere worldsheet ni compactificación.
- **NO es álgebra no-conmutativa pura** (camino C secundario, NCG Connes) — aunque puede contenerla.
- **NO es hypergraph evolutivo** (camino C primario, Wolfram) — aunque puede emerger de uno.
- **NO es información subjetiva** (QBism) — es objetiva categorial.

---

## 3. Operación primitiva mínima del marco H-004

### 3.1 La pregunta

¿Cuál es el "verbo" fundamental del marco — la operación de la que toda la dinámica, geometría y predicción debe seguirse?

### 3.2 Candidatos evaluados

| Candidato | Tipo | Pros | Contras |
|---|---|---|---|
| **Fusión $\otimes$** | binaria | Composición de información directa | Subdetermina cargas conservadas |
| **Regla de fusión $N_{ab}^c$** | dato categorial | Codifica cargas + composición | Requiere objetos simples primitivos |
| **Asociador $\alpha$** | dato | Identidades de orden superior | No genera dinámica |
| **Trenzado $\beta$** | dato | Topología emergente | Sin modular es insuficiente |
| **Condensación de anyones** | proceso | Transiciones de fase, Higgs | Derivada de $\otimes$ y dualidad |
| **Drinfeld center $Z(\mathcal{C}_0)$** | functor | Modularización | Más complejo que $\otimes$ |
| **F-mover** | recoupling | Asociatividad de fusión | Datos secundarios |
| **Composición categorial $\circ$** | binaria | Universal | Demasiado genérico |

### 3.3 Decisión S81

> **Operación primitiva mínima: la regla de fusión categorial.**
>
> $$\boxed{N: \text{Obj}(\mathcal{C}_0) \times \text{Obj}(\mathcal{C}_0) \to \mathbb{N}^{\text{Obj}(\mathcal{C}_0)}, \quad (a, b) \mapsto N_{ab}^{\bullet}}$$
>
> donde $N_{ab}^c = \dim_{\mathbb{C}} V_{ab}^c$ es la multiplicidad del objeto simple $c$ en la fusión $a \otimes b = \bigoplus_c N_{ab}^c \, c$.

### 3.4 Justificación

**Por qué la regla de fusión es la operación primitiva:**

1. **Captura cargas conservadas:** los $c$ con $N_{ab}^c > 0$ son los productos accesibles desde $a, b$. Las cargas (Q, color, espín, etc.) son etiquetas que se preservan en fusiones $N$-permitidas.

2. **Determina cuántas teorías son posibles:** dada la regla $N$, el resto de la estructura ($\alpha, \beta, \theta, S$) está fuertemente constreñida por las relaciones pentágono-hexágono-modular. **$N$ codifica la mayor parte del contenido informacional de $\mathcal{C}_0$**.

3. **Es lo único primitivamente "no derivable":** los datos $\alpha, \beta, \theta$ se derivan de $N$ por procedimiento sistemático (Moore-Seiberg, Etingof-Nikshych-Ostrik, etc.) modulo **clase de equivalencia gauge**. La regla $N$ es lo que distingue MTCs no equivalentes.

4. **Compatible con criterio (6) auto-consistencia:** dada $N$, la consistencia categorial completa es problema de existencia/unicidad de solución a ecuaciones polinómicas (pentágono + hexágono); auto-consistencia matemática como criterio.

5. **Operacionalmente "preguntar"**: $N_{ab}^c$ responde a "¿en qué estado puede aterrizar la información $a$ combinada con $b$, conservando todas las cargas?" — lectura informacional natural.

### 3.5 Datos derivados de $N$ (no primitivos)

| Dato | Cómo se deriva de $N$ |
|---|---|
| Asociador $\alpha$ | Solución de la ecuación pentágono dado $N$ (modulo gauge). |
| Trenzado $\beta$ | Solución de la ecuación hexágono dado $N + \alpha$. |
| Twist $\theta$ | Auto-trenzado: $\theta_a \otimes \theta_b = \theta_{a\otimes b} \beta_{a,b}^{-1} \beta_{b,a}^{-1}$. |
| Dimensiones cuánticas $d_a$ | Auto-valor positivo de la matriz de fusión $N_a$ (Perron-Frobenius). |
| Matriz $S$ | $S_{ab} = \frac{1}{D} \sum_c N_{ab^*}^c \frac{\theta_c}{\theta_a \theta_b} d_c$. |
| Carga central $c$ | Anomalía: $\frac{1}{D} \sum_a d_a^2 \theta_a = e^{2\pi i c / 8}$. |

**Esta jerarquía es estándar en la literatura categorial** (Etingof, Nikshych, Ostrik, Moore-Seiberg). H-004 la adopta como su núcleo operacional.

### 3.6 ¿Y la dinámica?

La regla $N$ no es dinámica directa — es estructura combinatoria. **¿De dónde sale la dinámica?**

**Respuesta camino B:** la dinámica emerge en régimen II via:
1. **Walker-Wang sobre $\mathcal{C}_0$ modular:** TQFT 4D con fronteras (2+1)D quirales.
2. **Crane-Yetter:** invariante topológico → frontera CS.
3. **Plebanski-autodual + Λ:** ecuaciones de movimiento (D-007).
4. **Variables Ashtekar:** geometría dinámica.
5. **Régimen IV:** GR clásica + SM dinámica.

**La cadena sigue siendo:** estructura categorial $\mathcal{C}_0$ + regla $N$ → TQFT → frontera dinámica → geometría → SM. Sin postular dinámica adicional.

**Consistente con framework/ontology.md sección 10 (S79):** mecanismo de emergencia tipo III estructural categorial.

### 3.7 Observación importante: cierre auto-consistente

La regla $N$ es **constreñida** por:
- **Asociatividad** de $\otimes$ → ecuación pentágono soluble.
- **Trenzado** consistente → ecuación hexágono soluble.
- **Modularidad** → matriz $S$ invertible.
- **Unitariedad** → todos los datos $\dagger$-compatibles.

Estas son **restricciones algebraicas no-triviales** sobre $N$. Una regla $N$ arbitraria NO produce $\mathcal{C}_0$ válida. La consistencia matemática selecciona drásticamente.

**Esta es exactamente la auto-consistencia derivable** del criterio (6) epistémico: **la matemática selecciona, no la observación**.

---

## 4. Estatus formal de $\mathcal{C}_0$ tras S81

### 4.1 Lo que está fijado

- **Tipo:** $\dagger$-MTC sobre $\mathbb{C}$ (con posible extensión super-modular).
- **Contenido:** etiquetas (objetos simples) + regla de fusión $N$.
- **Operación primitiva:** $N: \text{Obj}^2 \to \mathbb{N}^{\text{Obj}}$.
- **Datos derivados:** $\alpha, \beta, \theta, S$ por solución de pentágono-hexágono-modular dada $N$.

### 4.2 Lo que NO está fijado todavía

- **Etiquetas específicas** (por ejemplo, $\{1, v, s, c\}$ de `Spin(10)_1`).
- **Regla específica $N$** (Z_4 cíclica de `Spin(10)_1`).
- **Tamaño** del conjunto de etiquetas.

Estos son **outputs** de la sub-tarea δ, NO inputs de A-005.

### 4.3 Criterio de selección (sub-tarea δ)

Entre todas las posibles $\dagger$-MTC, sub-tarea δ debe demostrar:

> **La $\dagger$-MTC mínima compatible con frontera (2+1)D que admite 16 espinores Weyl + cancelación de anomalías 't Hooft por cobordismo es `Spin(10)_1`.**

Argumento ya parcialmente disponible en D-010 (Q-043 cerrada estructuralmente, S30). Sub-tarea δ debe **re-derivar D-010 desde A-005** + criterio (6), sin asumir SCG/Walker-Wang en el input.

---

## 5. Lo que sigue (sub-tareas β-ζ)

### 5.1 Sub-tarea β (S82-S84)

Re-derivar A-001 (corte Planck $\ell_P$) desde A-005 + regla $N$.

**Hipótesis técnica:** $\ell_P$ es el invariante mínimo de longitud asociado a la dimensión cuántica total $D = \sqrt{\sum_a d_a^2}$:

$$\ell_P^2 \propto \frac{1}{(\ln D)^?}$$

o relación con peso conforme mínimo $h_{\min} > 0$.

### 5.2 Sub-tarea γ (S85-S87)

Re-derivar A-002 (transición de fase $\rho_c$) como condensación de anyones (Bais-Slingerland) en $\mathcal{C}_0$.

### 5.3 Sub-tarea δ (S88-S92, MÁS SENSIBLE)

Re-derivar `Spin(10)_1` específica como mínimo compatible con SM observable + cancelación anomalías.

### 5.4 Sub-tarea ε (S93-S96)

Re-derivar (1, 3, 1) + signatura (3, 1) desde la estructura categorial pura.

### 5.5 Sub-tarea ζ (S97-S104, MÁS LARGA)

Re-derivar K-033 completo (SM + Higgs + Yukawa + Cabibbo) desde $\mathcal{C}_0$ + regla $N$.

---

## 6. Compatibilidad con SCG operativo (premisa dual v2.5)

**Importante:** durante el programa H-004, SCG sigue plenamente operativa con A-001, A-002, lattice WW + UBFC `Spin(10)_1`. La definición α.1 de $\mathcal{C}_0$ es **propositiva** — no reemplaza SCG hasta que sub-tareas β-γ tengan éxito.

**Coexistencia operativa:**
- **SCG operativo:** la UBFC `Spin(10)_1` ES un representante específico de $\mathcal{C}_0$.
- **H-004 propositivo:** A-005 dice que $\mathcal{C}_0$ es **primitiva**, no postulada como `Spin(10)_1`.
- **Si H-004 ✅:** SCG queda como caso particular derivado.
- **Si H-004 ✗ parcial:** SCG y H-004 coexisten dualmente como hasta ahora.
- **Si H-004 ✗ total:** retreat ordenado, mantener SCG estándar.

---

## 7. Disciplina K-005 + D1 anti-vacuidad

**Verificación honesta S81:**

¿Esta definición de $\mathcal{C}_0$ es genuina o circular?

- **Genuina:** la $\dagger$-MTC es la estructura matemática mínima que combina cuántica + topología + información. Su elección está justificada por (i) compatibilidad con SCG (heredado), (ii) capacidad de generar TQFT 4D + frontera, (iii) conexión con literatura matemática madura.
- **No circular:** A-005 + α.1 + operación primitiva $N$ NO presuponen `Spin(10)_1` ni ninguna UBFC específica. La selección viene en sub-tarea δ.
- **Falsable:** si sub-tarea δ no logra derivar `Spin(10)_1` como única solución mínima, A-005 pierde su poder selectivo.

**No hay K nuevo postulado.** $\mathcal{C}_0$ y $N$ son herramientas técnicas, no insights.

**K-005 ejemplar 19ma vez consecutiva preservada en S81.**

---

## 8. Conclusión sub-tarea α

**Sub-tarea α ✅ CERRADA.** Logros:

1. ✅ A-005 propuesto formalmente (S80, `framework/axioms.md`).
2. ✅ Criterio epistémico (6) auto-consistencia derivable (S80, `framework/epistemology.md`).
3. ✅ Definición operacional de $\mathcal{C}_0$ como $\dagger$-MTC (S81, este documento).
4. ✅ Operación primitiva mínima: regla de fusión $N$ (S81, este documento).
5. ✅ Mapa de deuda + matemáticas candidatas + plan programa (S80).

**Próximo paso:** sub-tarea β (S82) — re-derivar $\ell_P$ desde A-005 + $\mathcal{C}_0$ + $N$.

---

**Fin del cierre formal sub-tarea α — A-005 con contenido operacional preciso.**
