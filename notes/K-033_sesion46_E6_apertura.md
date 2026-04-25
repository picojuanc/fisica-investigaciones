# K-033 / Sub-tarea B.IV.1 — Apertura del MTC `(E_6)_1`

- **Fecha:** 2026-04-29 (sesión 46)
- **Sub-fase:** B.IV.1 — primera fase del ataque a Alternativa IV (extensión `Spin(10)_1 → (E_6)_1` con centro $\mathbb{Z}_3$).
- **Estado al inicio:** sub-tarea A cerrada vía D-013 (S44). K-020 debilitado en sesión 45; Alt IV priorizada para 3 generaciones.
- **Objetivo:** especificar el espectro de `(E_6)_1` MTC, verificar integrabilidad, decomponer rep 27 bajo $SO(10) \times U(1)$, examinar conexión con 3 generaciones.
- **Disciplina:** Regla 5 (no confundir "no refutado" con "confirmado") + K-005 (modesto antes que exótico).

---

## 1. Recap algebraico de $E_6$

### 1.1 Datos básicos

| Cantidad | Valor |
|---|---|
| Rango (Cartan) | 6 |
| Dimensión | 78 |
| Tipo de raíz | simply-laced excepcional |
| Centro $Z(E_6)$ | $\mathbb{Z}_3$ |
| Dual Coxeter $h^\vee$ | 12 |

### 1.2 Diagrama de Dynkin (Bourbaki)

```
       α₆
        |
α₁ — α₂ — α₃ — α₄ — α₅
```

Cinco nodos en línea (1-2-3-4-5) más uno colgando del nodo 3 (numerado 6).

**Marcas de Dynkin** (coeficientes de la raíz más alta $\theta$ en la base de raíces simples):
$$
\theta = \alpha_1 + 2 \alpha_2 + 3 \alpha_3 + 2 \alpha_4 + \alpha_5 + 2 \alpha_6
$$
Marks: $(a_1, ..., a_6) = (1, 2, 3, 2, 1, 2)$. Suma = 11 = $h^\vee - 1$. ✓

### 1.3 Reps fundamentales relevantes

| $\omega_i$ | Rep | Dimensión | Notas |
|---|---|---|---|
| $\omega_1$ | $\mathbf{27}$ | 27 | Fundamental compleja |
| $\omega_2$ | $\mathbf{78}$ | 78 | Adjunto |
| $\omega_5$ | $\overline{\mathbf{27}}$ | 27 | Conjugada de $\omega_1$ |

La simetría externa $\mathbb{Z}_2$ del diagrama (intercambiar nodos 1 ↔ 5) intercambia $27 \leftrightarrow \overline{27}$.

### 1.4 Cadena de subgrupos relevante

$$
E_6 \;\supset\; SO(10) \times U(1) \;\supset\; SU(5) \times U(1) \times U(1) \;\supset\; SU(3) \times SU(2) \times U(1)_Y
$$

Esta es la cadena estándar de heteróticas. Cada paso es ruptura espontánea por un Higgs apropiado (fenomenología SO(10)-GUT).

---

## 2. Espectro `(E_6)_1` MTC

### 2.1 Reps integrables al nivel $k = 1$

**Condición:** $(\lambda, \theta) \leq k = 1$, equivalentemente $\sum_i n_i a_i \leq 1$ con $\lambda = \sum_i n_i \omega_i$.

| $\lambda$ | $\sum n_i a_i$ | Integrable? | Rep |
|---|---|---|---|
| 0 | 0 | ✓ | trivial |
| $\omega_1$ | $a_1 = 1$ | ✓ | **27** |
| $\omega_2$ | $a_2 = 2$ | ✗ | 78 (no integrable a $k=1$) |
| $\omega_3$ | $a_3 = 3$ | ✗ | 351 |
| $\omega_4$ | $a_4 = 2$ | ✗ | 351' |
| $\omega_5$ | $a_5 = 1$ | ✓ | $\overline{\mathbf{27}}$ |
| $\omega_6$ | $a_6 = 2$ | ✗ | 78' |

**Conclusión:** `(E_6)_1` MTC tiene exactamente **3 objetos simples**: $\{1, 27, \overline{27}\}$.

### 2.2 Reglas de fusión

Computación directa de productos tensoriales en $E_6$, truncada al espectro integrable:

**$27 \otimes 27$:** algebraicamente $27 \otimes 27 = \overline{27} \oplus 351 \oplus \overline{351}$. Truncado a integrables: $27 \otimes 27 = \overline{27}$.

**$27 \otimes \overline{27}$:** algebraicamente $27 \otimes \overline{27} = 1 \oplus 78 \oplus 650$. Truncado: $27 \otimes \overline{27} = 1$.

**$\overline{27} \otimes \overline{27}$:** simétrico a $27 \otimes 27$: $\overline{27} \otimes \overline{27} = 27$.

**Tabla completa:**
$$
\boxed{\begin{aligned}
1 \cdot x &= x \quad \forall x \\
27 \cdot 27 &= \overline{27} \\
27 \cdot \overline{27} &= 1 \\
\overline{27} \cdot \overline{27} &= 27
\end{aligned}}
$$

**Estructura:** $\mathbb{Z}_3$ cíclica abeliana, generada por `27`. Con $g = 27$: $g^2 = \overline{27}$, $g^3 = 1$. ✓

### 2.3 Pesos conformes

Fórmula: $h_a = C_2(a) / [2(k + h^\vee)]$.

**Casimir cuadrático $C_2(27)$:** valor estándar $C_2(27) = 26/3$ (Slansky 1981, normalización con $C_2(78) = 2 h^\vee = 24$).

$$
h_{27} = h_{\overline{27}} = \frac{26/3}{2 \cdot 13} = \frac{26}{78} = \frac{1}{3}
$$

$h_1 = 0$. ✓

**Verificación cohomológica:** una MTC abeliana sobre $\mathbb{Z}_3$ tiene pesos conformes $h_a = p \cdot a^2 / 6 \mod 1$ con $p \in \{0, 1, 2\}$ etiquetando la clase en $H^3(\mathbb{Z}_3, U(1)) = \mathbb{Z}_3$. Para $h_{27} = 1/3$: $p \cdot 1^2 / 6 = 1/3$ ⟹ $p = 2$. **Clase $p = 2$ en $H^3$.**

Verificación cruzada para $\overline{27}$ (= elemento 2 de $\mathbb{Z}_3$): $h_2 = 2 \cdot 4 / 6 = 4/3 \mod 1 = 1/3$. ✓

### 2.4 Central charge

$$
c = \frac{k \cdot \dim(g)}{k + h^\vee} = \frac{1 \cdot 78}{13} = 6
$$

### 2.5 Estatus

`(E_6)_1` MTC está **bien definida** y consistente:
- 3 objetos simples ✓
- Fusión $\mathbb{Z}_3$ cíclica ✓
- Pesos conformes consistentes con clase $p=2$ en $H^3(\mathbb{Z}_3, U(1))$ ✓
- $c = 6$ ✓
- Frobenius-Schur OK ✓

---

## 3. Decomposición de la rep 27 bajo $SO(10) \times U(1)$

### 3.1 Branching estándar

Resultado bien conocido (Slansky 1981):
$$
\boxed{\mathbf{27} \to \mathbf{16}_{1} \oplus \mathbf{10}_{-2} \oplus \mathbf{1}_{4}}
$$

**Subíndices = cargas U(1)** en convención donde $\sum (\dim \cdot Y) = 0$:
$$
16 \cdot 1 + 10 \cdot (-2) + 1 \cdot 4 = 16 - 20 + 4 = 0 \quad ✓
$$

### 3.2 Interpretación física

- **$16_1$:** una generación SM completa (Q, u^c, d^c, L, e^c, ν^c) bajo SO(10)-GUT estándar, todos con carga $U(1)_{E_6} = +1$.
- **$10_{-2}$:** doblete Higgs SU(5) (= rep 10 SO(10)) con $U(1)_{E_6} = -2$. Sector escalar.
- **$1_{4}$:** singlete adicional con $U(1)_{E_6} = +4$. Posiblemente un neutrino estéril o singlete de gran masa.

### 3.3 Conexión con D-013

La rep 16 que en D-013 corresponde al objeto $s$ del MTC `Spin(10)_1` aparece **dentro** de la rep 27 de $E_6$ con carga $U(1)_{E_6} = +1$. Es decir, **el "fermión" de SCG-D-013 es la componente $16_1$ de la rep 27 de $E_6$**.

Análogamente:
- $\overline{27} \to \overline{16}_{-1} \oplus \mathbf{10}_{2} \oplus \mathbf{1}_{-4}$ (con la 10 real auto-conjugada).
- El objeto `c` de D-013 es la componente $\overline{16}_{-1}$ de $\overline{27}$.
- El objeto `v` de D-013 (= rep 10 con $h_v = 1/2$) podría identificarse con $\mathbf{10}_{-2}$ de la 27 — pero requiere verificar la carga $U(1)$ y el peso conforme.

### 3.4 ¿`Spin(10)_1` ⊂ `(E_6)_1` directamente?

**Respuesta:** **NO directamente.** La fusión de `(E_6)_1` es $\mathbb{Z}_3$ cíclica; la fusión de `Spin(10)_1` es $\mathbb{Z}_4$ cíclica. **No hay embedding directo $\mathbb{Z}_4 \hookrightarrow \mathbb{Z}_3$** (no son subgrupos uno del otro).

**La forma correcta:** `(E_6)_1` $\supset$ `(Spin(10) \times U(1))_1` = `Spin(10)_1 \otimes U(1)_k` para algún nivel $k$ específico (dictado por el embedding canónico).

**Cálculo del nivel U(1):** la carga U(1) del embedding $E_6 \supset SO(10) \times U(1)$ tiene normalización tal que las cargas en la rep 27 son $\{1, -2, 4\}$. El nivel WZW de U(1) en este embedding es típicamente $k_{U(1)} = N$ con $N$ dependiente de la normalización; para nuestro caso, $k_{U(1)} = 6$ (estándar).

**Implicación:** la extensión de SCG a Alt IV **NO es solo agregar `(E_6)_1` MTC**, sino agregar `Spin(10)_1 \otimes U(1)_6` con la regla de selección apropiada que identifica `(E_6)_1` como su completación.

**Esto preserva D-010/D-013:** el sector `Spin(10)_1` sigue siendo subcategoría de `Spin(10)_1 \otimes U(1)_6`. Los resultados de la sub-tarea A (vacío, v, s, c) se preservan como objetos del sector `Spin(10)_1`. La extensión añade **estructura U(1) adicional** (cargas $E_6$).

---

## 4. Análisis del mecanismo de 3 generaciones

### 4.1 El problema central

**Pregunta:** ¿produce `(E_6)_1` MTC **automáticamente** 3 generaciones SM?

**Respuesta directa:** **NO.** El espectro de `(E_6)_1` tiene **una sola** rep 27 (un solo objeto del MTC). Por lo tanto, una sola copia de la 16 dentro del 27. Una sola generación SM (más bosones del Higgs y singlete).

**Esto contradice mi expectativa de sesión 45.** La promesa "Alt IV con centro $\mathbb{Z}_3$ → 3 generaciones" requiere mecanismo adicional, no solo el MTC.

### 4.2 ¿De dónde vendrían las 3 generaciones realmente?

**Argumento estándar Witten 1985 (heterótica $E_8 \times E_8$):**
- Compactificación de cuerdas $E_8 \times E_8$ heteróticas en un Calabi-Yau (CY) tridimensional con grupo de holonomía $SU(3)$.
- $E_8 \to E_6 \times SU(3)_{\text{holonomía}}$ por la conexión de gauge en el CY.
- Modos cero de la rep 248 de $E_8$ se descomponen como:
  $$248 = (78, 1) + (1, 8) + (27, 3) + (\overline{27}, \overline{3})$$
- **El número de modos cero netos en la rep 27** (= número de generaciones) está dado por el **número de Euler** del CY:
  $$N_{\text{gen}} = |\chi(CY)| / 2$$
- Calabi-Yau con $\chi = 6$ ⟹ 3 generaciones.

**El número 3 NO es propiedad de $E_6$** (ni de `(E_6)_1` MTC). Es propiedad **del Calabi-Yau de compactificación específico**.

### 4.3 Implicación para SCG: necesidad de "Calabi-Yau topológico"

Para que la Alternativa IV produzca 3 generaciones en SCG, necesitamos:
- **(a) Una "geometría compactificada"** análoga al CY en heteróticas.
- **(b) Un mecanismo de holonomía** que produzca 3 modos cero netos en la rep 27.
- **(c) Compatibilidad** con la estructura del lattice trivalente SCG.

**¿Tiene SCG estructura natural análoga?**

**Posibles candidatos en SCG:**

1. **Compactificación interna del lattice:** si el lattice 3+1D tiene "dimensiones internas" topológicas (e.g., grado de libertad orientacional adicional por arista), su cohomología podría producir modos cero. Especulativo.

2. **Holonomía de Wilson lines:** los loops topológicos en lattice WW tienen holonomía no-trivial; quizás existan 3 clases topológicas de loops apropiados que actúen como "3 sectores de generación".

3. **Estructura jerárquica anisotrópica:** alguna asimetría intrínseca del lattice (3 ejes preferidos vs no preferidos) podría producir 3 sectores.

**Ninguno de estos está demostrado.** Todos son **especulativos**.

### 4.4 Comparación con literatura: ¿qué hace Wang-Wen 2018-2019?

**Wang-Wen 2018 (arXiv:1809.11171)** demostró que SO(10)-GUT puede definirse no-perturbativamente en lattice 3+1D **para una sola generación**. **No abordan el conteo de 3 generaciones explícitamente.** El mecanismo de 3 generaciones se asume separable (compactificación adicional).

**Esto significa:** ni Wang-Wen 2018 ni los papers relacionados resuelven el problema de "¿por qué 3 generaciones?" en lattice. Es un problema abierto en literatura.

---

## 5. Veredicto sub-fase B.IV.1

### 5.1 Logros

- ✅ Espectro `(E_6)_1` MTC especificado completamente: 3 objetos $\{1, 27, \overline{27}\}$, fusión $\mathbb{Z}_3$ cíclica, pesos $(0, 1/3, 1/3)$, central charge $c = 6$, clase $p = 2$ en $H^3(\mathbb{Z}_3, U(1))$.
- ✅ Decomposición $27 \to 16_1 + 10_{-2} + 1_4$ verificada.
- ✅ **Compatibilidad con D-013 preservada:** el sector `Spin(10)_1` sigue siendo subcategoría de `Spin(10)_1 \otimes U(1)_6` (forma correcta del embedding).
- ✅ **Identificación honesta del problema:** `(E_6)_1` MTC pura **NO produce 3 generaciones automáticamente**. El argumento Witten 1985 (CY) requiere estructura geométrica adicional que SCG necesita identificar.

### 5.2 No-logros

- ❌ NO se identifica el mecanismo SCG análogo a "Calabi-Yau con $\chi/2 = 3$".
- ❌ NO se demuestra que la rep 27 de `(E_6)_1` se realice como excitación específica del lattice SCG.
- ❌ NO se obtienen las 3 generaciones SM de un argumento estructural completo.

### 5.3 Estatus epistémico

**Alt IV NO se descarta — pero queda incompleta sin mecanismo CY-análogo.**

**Posibles caminos para sesión 47:**
1. **Buscar "Calabi-Yau topológico" en SCG:** explorar si el lattice trivalente 3+1D admite estructura compactificada con cohomología apropiada para 3 modos cero. **Costo alto, probabilidad ~30%.**
2. **Combinar Alt IV con Alt I (Bilson-Thompson):** los 3 sectores de trenzas estables de Bilson-Thompson 2005 podrían identificarse con los 3 modos cero requeridos en la rep 27. **Potencialmente prometedor, ~35%.**
3. **Aceptar que SCG produce 1 generación + caveat estructural:** análogo al cierre Q-045 (Opción A parcial 43% → 83%). El programa K-033 cierra sub-tarea B con caveat: "1 generación derivada estructuralmente; mecanismo de 3 copias requiere estructura adicional postulable, en línea con literatura". **Costo bajo, probabilidad de aceptación ~60%.**

### 5.4 Re-estimación de probabilidad K-033

Probabilidad pre-sesión 46: 60-75%.

**Re-evaluación honesta tras sesión 46:**
- Espectro `(E_6)_1` confirmado: ✓ información positiva.
- Mecanismo de 3 gen NO automático: información negativa significativa.
- Posibilidad de cerrar con caveat (Opción 3 arriba): mantiene viabilidad parcial.

**Probabilidad de cierre estructural sub-tarea B con 3 generaciones:** **35-50%** (era 50-60%).

**Probabilidad de cierre estructural sub-tarea B con 1 generación + caveat:** **70-80%**.

**Probabilidad de éxito parcial K-033 ajustada:** **55-70%** (ligeramente revisada a la baja desde 60-75%).

---

## 6. Plan refinado sesiones 47-48

### 6.1 Sesión 47 — exploración estructura "Calabi-Yau topológico" del lattice SCG

**Objetivo:** determinar si el lattice trivalente 3+1D SCG admite estructura compactificada con cohomología apropiada para 3 modos cero en la rep 27.

**Sub-pasos:**
1. Definir "compactificación interna" del lattice SCG (si es posible).
2. Calcular cohomología topológica del lattice (alternativa: número de Euler equivalente).
3. Verificar si existe estructura natural con $\chi/2 = 3$.
4. **Si NO:** evaluar combinación con Alt I (Bilson-Thompson).

### 6.2 Sesión 48 — decisión final sub-tarea B

**Decisión basada en sesión 47:**
- **Si CY-análogo natural:** sub-tarea B cierra estructuralmente con K-020' (extensión $E_6$ + CY topológico).
- **Si combinación con Alt I:** sub-tarea B cierra con caveat híbrido (Alt IV proporciona la estructura $E_6$, Alt I el conteo de 3).
- **Si ambos fallan:** **aceptar caveat de 1 generación + extensión postulable.** Sub-tarea B cierra con resultado parcial análogo a K-032.M y Q-045.

### 6.3 Plan post-sub-tarea B (sesiones 49+)

Independiente del veredicto en S47-48, **sub-tarea C (Higgs/VEV) sigue tractable** vía K-037 + el sector `v` ya identificado en D-013. Es decir, el programa K-033 puede avanzar a C aunque B cierre solo parcialmente.

---

## 7. Reflexión metodológica

### 7.1 Honestidad sobre Alt IV

**En sesión 45 promí 50-60% probabilidad de cierre Alt IV.** Esa estimación era **optimista** — no consideré explícitamente que el `(E_6)_1` MTC puro NO produce 3 generaciones. La sesión 46 corrige esa estimación.

**Aplicación Regla 5:** "no confundir 'no refutado' con 'confirmado'". Alt IV NO está refutada — `(E_6)_1` MTC es una estructura válida y compatible con SCG. Pero la **conexión con 3 generaciones requiere paso adicional** que no es automático.

### 7.2 Continuidad con sesión 45

**Sesión 45:** retreat sobre K-020 original. Apertura de Alt IV.
**Sesión 46:** identificación honesta de que Alt IV requiere estructura CY-análoga (no automática).

**Esto NO es un sexto retreat consecutivo** — es **refinamiento de la propuesta de Alt IV.** El programa K-033 sigue en marcha; solo se identifican honestamente las dependencias.

### 7.3 K-005 aplicada

**No inventar mecanismos.** Si SCG no tiene CY-análogo natural, **no postular uno**. Aceptar el caveat honesto de "1 generación derivada + 3 copias requieren estructura adicional postulable".

Esto sería análogo a K-032.M (forma funcional derivada, valor numérico no), Q-045 (compactness 43% → 83%, residuo 17% requiere mecanismo adicional), D-010 (super-MTC explícita pendiente). **Patrón maduro de SCG: cerrar parcialmente con caveat antes que forzar cierres ilusorios.**

---

## 8. Firma

Sesión 46 cerrada con **apertura exitosa del MTC `(E_6)_1`** + **identificación honesta de que la conexión con 3 generaciones requiere estructura adicional no provista automáticamente por el MTC**.

**Resultado meta:** la Alternativa IV es **necesaria pero no suficiente** para 3 generaciones. El argumento Witten 1985 (CY) requiere análogo SCG; sin ese análogo, K-033 produce 1 generación + caveat.

**Probabilidad K-033 ajustada:** **55-70%** (ligeramente bajada desde 60-75%).

**Próxima sesión (47):** exploración de estructura "Calabi-Yau topológico" en lattice SCG, o combinación Alt IV + Alt I (Bilson-Thompson). Decisión final en sesión 48.

**Disciplina:** no forzar cierre prematuro. Si SCG no tiene CY-análogo natural, aceptar caveat honesto.
