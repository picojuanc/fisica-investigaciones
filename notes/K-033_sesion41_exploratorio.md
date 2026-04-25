# K-033 — Programa SO(10)-GUT en SCG: primer ataque exploratorio

- **Fecha:** 2026-04-24 (sesión 41)
- **Estado:** **exploratorio — primera sesión del programa.**
- **Objetivo de esta sesión:** (1) mapear el alcance del programa K-033; (2) catalogar sub-tareas con dependencias y costos; (3) seleccionar primera sub-tarea tractable; (4) emitir veredicto sobre viabilidad inicial.
- **Estado al inicio:** K-033 candidato formal activado en sesión 30 (D-010, sección 4.3). Sin trabajo técnico previo.
- **Filosofía de la sesión:** **K-005 + Regla 5.** No prometer cierre constructivo de Yukawas/jerarquía; solo determinar si hay un camino tractable de un paso a la vez.

---

## 1. Contexto y enunciado

### 1.1 K-033 — recap del estado actual

**Enunciado activado en sesión 30 (D-010 §4.3):**

> *"K-033: SCG + `Spin(10)_1` modular Walker-Wang + ruptura Wang-Wen provee marco natural para SO(10)-GUT no-perturbativo en lattice 3+1D. Cadena de inclusiones SO(10) ⊃ SU(5) ⊃ SU(3) × SU(2) × U(1) embebe el grupo gauge derivado en SCG (D-004). Programa asociado abierto: masas fermiónicas, Yukawas, CKM/PMNS via estructura SO(10). 10+ sesiones para desarrollo completo."*

**Lo que ya está cerrado (no es trabajo de K-033):**
- (D-010, sesión 30) UBFC = `Spin(10)_1` MTC; espectro {1, v(10), s(16), c(16̄)}; fusión Z_4; c=5.
- (D-010 §2.2, sesión 27) Cuantización Y en 1/6, Q en 1/3 vía decomposición 16 → 10 + 5̄ + 1 bajo SU(5). Doble derivación con K-015 (K-034 candidato).
- (D-011, sesión 35) Patrón α₂ ≈ α₃ ≠ α₁ derivado estructuralmente (vértice vs segmento).
- (D-010 §2.4) Sector gravitacional desacoplado del sector topológico.

**Lo que K-033 debe atacar (Yukawas y jerarquía):**
- ¿De qué objeto físico SCG salen los **3 generaciones** de fermiones? (no salen de Spin(10)_1 puro — solo da 1 copia).
- ¿Qué objeto SCG es el **Higgs** que rompe SO(10) → ... → SM y da masa? (K-021: condensación de anyones).
- ¿Cómo se calcula un **Yukawa concreto** (e.g., y_top) en este lattice? (acoplamiento topológico entre defectos).
- ¿De dónde sale la **jerarquía masas** (m_top / m_e ≈ 3 × 10⁵)?
- ¿De dónde salen las **mezclas CKM/PMNS** (3 ángulos + 1 fase)?

### 1.2 Por qué SO(10) y no otra GUT

(Esto ya está fijado por D-010 — recapitulamos para contexto del lector futuro.)

- **SU(5):** mínima GUT (Georgi-Glashow 1974). Pero su 5̄ + 10 no contiene ν_R. Y su anomalía global es no-trivial — incompatible con el mecanismo Wang-Wen 2018 de gap del mirror.
- **SO(10):** una sola rep 16 contiene la generación SM completa + ν_R. **Anomalía global trivial** (Ω⁵_Spin(BSpin(10)) clase trivial). **Esta es la elegida**.
- **E₆, SO(18), etc.:** anomalías y/o reps demasiado grandes; no minimales.

**Conclusión:** SO(10) no es elección estética. Es la única GUT compatible con (a) el contenido SM + ν_R, (b) Wang-Wen 2018-2019 sobre lattice 3+1D, (c) `Spin(10)_1` como MTC modular candidata.

### 1.3 Caveat honesto inicial

D-010 §3.2 dice explícitamente: *"D-010 NO predice Yukawas, masas, CKM/PMNS"*. Y advierte: *"K-033 activado abre el programa; D-010 no lo cierra"*.

Es decir: **estamos partiendo de cero técnicamente**. Lo único que tenemos son los andamios (la UBFC, el desacople, la cadena de ruptura). El cálculo concreto de masas/Yukawas en un lattice no-perturbativo SCG **no se ha hecho en ninguna parte de la literatura** (ni siquiera en Wang-Wen 2018 — ellos demuestran que el SM se *puede definir* en lattice 3+1D, no que ya tengan los Yukawas).

Esto significa: K-033 no es "aplicar literatura conocida" sino **abrir territorio nuevo con herramientas conocidas**. Riesgo alto de obstrucciones técnicas. Beneficio potencial alto: si funciona aunque sea para una masa, sería el primer cálculo no-perturbativo de un Yukawa SM desde lattice GUT.

---

## 2. Mapa del programa: 6 sub-tareas

Etiquetas A-F. Cada sub-tarea tiene:
- enunciado (qué se busca);
- dependencias (qué necesita estar resuelto antes);
- costo estimado;
- payoff si afirmativa;
- riesgo si bloquea.

### 2.1 Sub-tarea A — Caracterización del fermión SCG concretamente

**Enunciado:** identificar **qué objeto físico** del lattice SCG (defecto, anyón, par enlazado, configuración) corresponde al fermión SO(10) en la rep 16. Verificar que su carga topológica corresponde efectivamente al objeto `s` (16) o `c` (16̄) del MTC `Spin(10)_1`.

**Dependencias:** D-010 (espectro MTC), H-003 (defectos topológicos como partículas).

**Costo estimado:** 2-3 sesiones técnicas. Esencialmente un ejercicio de identificación; los ladrillos ya existen (Walker-Wang, Wen 2003, H-003). Pero requiere precisión sobre cómo el defecto SCG concreto se mapea a un objeto WW.

**Payoff si afirmativa:** consolida el "ladrillo cero" del programa. Probablemente da identificación canónica que después se reutiliza en B-F.

**Riesgo si bloquea:** alto — sin esto, A-F dependientes quedan suspendidas. Pero el bloqueo "duro" es improbable: H-003 ya postula que las partículas son defectos topológicos.

### 2.2 Sub-tarea B — Mecanismo de 3 generaciones

**Enunciado:** demostrar (o refutar) que el lattice SCG genera exactamente **3 copias** físicamente distinguibles de la rep 16 de Spin(10). Hipótesis de trabajo (K-020): Z₃_dual del grafo dual (junto con Z₃_primal de la trivalencia). Ver K-020 actualmente etiquetado como "especulativo".

**Dependencias:** A (caracterización del fermión); K-020 (Z₃_dual, sesión 9, especulativo); K-017 (Z₃_geom ≡ centro SU(3), v2.0).

**Costo estimado:** 2-4 sesiones técnicas. Requiere:
- definición precisa del "grafo dual" en lattice WW trivalente 3+1D;
- verificar si la simetría Z₃_dual conmuta o anticonmuta con Z₃_primal;
- contar órbitas de la acción combinada Z₃ × Z₃ sobre los objetos del MTC restringidos a la rep 16.

**Payoff si afirmativa:** **promueve K-020 candidato → K-020 confirmado estructuralmente**. Cierra una de las preguntas más antiguas del SM ("¿por qué 3 generaciones?"). Habilita C-F.

**Riesgo si bloquea:** medio. Si Z₃_dual no funciona exactamente, hay otros mecanismos disponibles (e.g., topología de la red en compactificación, multiplicidades de defectos). Pero el bloqueo *temporal* haría que C-F operen sobre "1 generación" como ejercicio académico (todavía útil).

### 2.3 Sub-tarea C — Higgs como condensación

**Enunciado:** identificar el campo Higgs (en la rep 10 o 126 de SO(10) que da masa Yukawa) como **condensación específica de un anyón** en el lattice SCG. Calcular el VEV en términos de parámetros SCG (ℓ_P, escala de transición de fase, ...).

**Dependencias:** A (qué es un anyón concreto); K-021 (Higgs = condensación, sesión 9); D-007 (sector gravitacional con Λ).

**Costo estimado:** 3-5 sesiones técnicas.

**Payoff si afirmativa:** explica jerarquía Planck-electroweak. Da escala de masas SM en términos de M_P y γ_Immirzi.

**Riesgo si bloquea:** alto. Sin VEV físico definido, Yukawas no tienen escala. Programa se estanca en "y_top adimensional sin masa".

### 2.4 Sub-tarea D — Cálculo de un Yukawa concreto (target: y_top)

**Enunciado:** calcular un acoplamiento Yukawa específico — preferiblemente **y_top** ≈ 1 — desde el acoplamiento topológico 16 ⊗ 16 ⊗ 10 en `Spin(10)_1` extendido. Comparar con el valor SM.

**Dependencias:** A + B + C. Más: cálculo de F-symbols (matrices de asociatividad) del MTC `Spin(10)_1` para los acoplamientos relevantes.

**Costo estimado:** 4-6 sesiones técnicas (asumiendo A-C cerradas previamente).

**Payoff si afirmativa:** **PRIMERA predicción cuantitativa de SCG en sector materia.** Resultado falsable (y_top ≈ 1 al ~10%).

**Riesgo si bloquea:** muy alto. Pero si A-C cierran limpiamente, D probablemente sigue al menos con caveat cuantitativo (análogo K-032.M).

### 2.5 Sub-tarea E — Jerarquía masas (m_top / m_e)

**Enunciado:** explicar la jerarquía m_top / m_e ≈ 3 × 10⁵ desde estructura SCG. Identificar el factor exponencial / power-law que la genera (e.g., ¿desde la estructura de la cadena de ruptura SO(10) → SU(5) → SM? ¿desde Z₃_dual? ¿desde compactificación efectiva en alguna dirección?).

**Dependencias:** A + B + D.

**Costo estimado:** 3-5 sesiones (después de D).

**Payoff si afirmativa:** **el santo grial parcial del SM.** Ningún programa BSM lo ha hecho desde primeros principios.

**Riesgo si bloquea:** alto, pero parcialmente aceptable — si predice los órdenes de magnitud, ya es ganancia.

### 2.6 Sub-tarea F — CKM/PMNS

**Enunciado:** predecir las matrices de mezcla CKM (quarks) y PMNS (leptones) desde estructura SCG. 3 ángulos + 1 fase cada una.

**Dependencias:** A + B + D + E.

**Costo estimado:** 5-10 sesiones (después de E).

**Payoff si afirmativa:** **completa el SM en sector materia.** Programa K-033 completo.

**Riesgo si bloquea:** alto, pero terminal — si A-E cierran y solo F bloquea, K-033 ya es éxito mayoritario.

---

## 3. Diagrama de dependencias

```
        [A] Caracterización fermión SCG
            │
            ├─────────────┬───────────────┐
            ↓             ↓               ↓
        [B] 3 gen     [C] Higgs/VEV    (insumos para D)
            │             │
            └──────┬──────┘
                   ↓
        [D] y_top concreto
                   │
                   ↓
        [E] jerarquía m_top/m_e
                   │
                   ↓
        [F] CKM/PMNS
```

**Nota crítica:** A es **bloqueante para todo el programa**. B y C son paralelizables (después de A). D requiere A+B+C. E requiere D. F requiere E.

**Camino crítico:** A → C → D → E → F. ~17-29 sesiones totales. Compatible con la estimación "10+ sesiones" que el snapshot v2.2 menciona, considerando que algunas pueden bloquearse antes.

---

## 4. Selección de la primera sub-tarea

### 4.1 Criterios de selección

(En orden de importancia para una primera sesión exploratoria.)

1. **Bloqueo upstream:** ¿es necesaria para todo lo demás? Si sí, hay que hacerla primero.
2. **Tractabilidad técnica:** ¿tenemos los ladrillos? ¿cuánto trabajo nuevo requiere?
3. **Payoff diagnóstico:** ¿el resultado nos dirá si vale la pena seguir? ¿podemos abortar el programa pronto si bloquea?
4. **Costo:** ¿es realista en 1-3 sesiones?

### 4.2 Aplicación a A-F

| Sub-tarea | Bloqueo upstream | Tractabilidad | Payoff diagnóstico | Costo |
|---|---|---|---|---|
| A | **Sí (todo)** | Alta (ladrillos en H-003 + D-010) | Alto (define el ladrillo cero) | 2-3 sesiones |
| B | Solo de B-F | Media-alta (K-020 ya esbozado) | Alto (cierra K-020) | 2-4 sesiones |
| C | De C-F | Media (Higgs en SCG no atacado) | Alto (escala) | 3-5 sesiones |
| D | De D-F | Baja (sin A+B+C) | Muy alto | 4-6 sesiones |
| E | De E-F | Baja (sin D) | Muy alto | 3-5 sesiones |
| F | De F | Baja (sin A-E) | Alto | 5-10 sesiones |

**Conclusión metodológica:** **A es la primera sub-tarea por necesidad lógica.**

### 4.3 Sub-tarea seleccionada para sesión 42 — A

**Enunciado preciso (refinado para sesión 42):**

> Determinar la correspondencia uno-a-uno (o uno-a-N con N pequeño) entre:
> - **(i)** los objetos físicos del lattice SCG: defectos topológicos, anyones del modelo Walker-Wang sobre `Spin(10)_1`, configuraciones de bordes de la fase modular invertible;
> - **(ii)** los objetos abstractos del MTC `Spin(10)_1`: 1 (vacío), v (10, vectorial), s (16, spinor), c (16̄, spinor conjugado).
>
> En particular: **identificar qué configuración SCG corresponde al objeto s** (la 16-spinor que contiene una generación SM completa).

**Por qué es tractable:**
1. **Ladrillos disponibles:** H-003 ya postula partículas como defectos. D-010 da el espectro MTC. Wen 2003 y Walker-Wang 2011 dan recetas explícitas para identificar anyones en lattice 3+1D.
2. **Caveat estándar:** la identificación es esencialmente un ejercicio de "diccionario topológico" — reproducir lo que ya hizo Wen 2003 (constructivo en su modelo) en el contexto SCG con MTC `Spin(10)_1`.
3. **Producto final esperado:** una tabla con 4 entradas {1, v, s, c} y la configuración SCG asociada a cada una.

**Por qué tiene payoff diagnóstico claro:**
- Si **se cierra limpiamente:** A se convierte en D-013 (derivación estructural) → habilita B y C → K-033 sigue tractable.
- Si **se obstruye:** identificamos exactamente *dónde* (lo más probable: la rep 16 requiere defecto compuesto que excede la trivalencia básica) → caveat honesto + decisión de pivotar a B o abandonar.

**Estimación:** sub-tarea A puede cerrarse en **2 sesiones técnicas (sesión 42-43)**, conservadoramente.

---

## 5. Veredicto sobre viabilidad inicial de K-033

### 5.1 Posición

**Veredicto:** K-033 es **viable como programa exploratorio**, con probabilidad de éxito parcial (al menos hasta sub-tarea D, y_top concreto) **estimada en 40-60%**.

### 5.2 Argumentos a favor (por qué no es prematuro abrirlo)

1. **Andamios sólidos.** D-010 establece el marco; D-011 da la lección metodológica para retreats honestos (K-032.M); H-003 ya postula partículas como defectos.
2. **Análogo metodológico funcional.** El mismo patrón "ataque + retreat estructural con caveat" (Q-043 → D-010, K-032 → D-011) puede operar aquí.
3. **Sub-tareas tractables.** Sub-tarea A es pequeña y tiene ladrillos completos. Permite diagnóstico temprano sin compromiso.
4. **K-005 aplicada.** No estamos inventando mecanismos nuevos; estamos identificando si los conocidos (WW, Wen 2003, Wang-Wen 2018) producen el SM concreto cuando aterrizan en SCG.

### 5.3 Argumentos en contra (caveats honestos)

1. **Bloqueo en C (Higgs/VEV) es serio.** Sin VEV físico definido, Yukawas son adimensionales. Y la condensación de anyones (K-021) está por demostrar como mecanismo de Higgs concreto.
2. **Cálculo de F-symbols `Spin(10)_1`** (necesario para D) es **técnicamente exigente**. Existen en literatura (Di Francesco-Mathieu-Sénéchal 1997 + Kac 1990) pero no fácilmente accesibles.
3. **Dependencia con K-020 especulativa.** Si Z₃_dual no funciona, B se obstruye y D pierde el factor de 3.
4. **Riesgo de "ya hecho en otros marcos":** trabajos como Bilson-Thompson (preons), Finkelstein, Loll-Reuter pueden haber cubierto sub-conjuntos de A-F. Hay que revisar literatura.
5. **Nada en SCG aún garantiza la jerarquía exponencial m_top/m_e.** Es un problema sin solución en ningún programa BSM. Sub-tarea E es más ambiciosa de lo que parece.

### 5.4 Decisión

**Aprobar la apertura del programa K-033 con la siguiente disciplina:**

- **Hard cap inicial:** **3 sesiones técnicas** dedicadas a sub-tarea A (sesiones 42-44).
- **Decisión de continuación:** después de cada una de esas 3 sesiones, evaluar:
  - ¿A está cerrada o muy cerca?
  - ¿Han aparecido obstrucciones inesperadas?
  - ¿Sigue teniendo sentido aspirar a B-F?
- **Criterio de aborto temprano:** si después de 2 sesiones técnicas no hay correspondencia identificable entre defectos SCG y objetos del MTC, **detener K-033** y pivotar a (b) K-036 promoción o (d) Q-045 residual o (c) Q-044 ontology.
- **Criterio de avance:** si A cierra al menos parcialmente (≥ 3 de 4 objetos identificados), proceder a sub-tarea B en sesión 45.

---

## 6. Plan sesiones 42-44 (provisional)

### Sesión 42 — Sub-tarea A, Fase 1: identificación del vacío y la rep vectorial

**Objetivo:** identificar concretamente las configuraciones SCG correspondientes a 1 (vacío) y v (10, vectorial). Verificar que la fusión 1 × x = x se cumple trivialmente y que v × v = 1 + s + c (regla de fusión Z_4 estándar).

**Notas:** son los objetos más simples (no espinoriales). Permite calibrar el "diccionario" sin entrar todavía en la 16.

### Sesión 43 — Sub-tarea A, Fase 2: identificación de las reps espinoriales s y c

**Objetivo:** identificar la configuración SCG correspondiente a s (16-spinor) y c (16̄). Crítico: el espinor de Spin(10) requiere estructura "doble cobertura" — verificar si esto se realiza naturalmente en SCG (probablemente vía orientación de aristas + estructura ESPÍN del lattice).

**Notas:** este es el paso clave. Si bloquea, K-033 está en problemas.

### Sesión 44 — Sub-tarea A, Fase 3: cierre + chequeo de fusión

**Objetivo:** verificar que las identificaciones de las sesiones 42-43 satisfacen la **fusión Z_4 cíclica completa** (s·s = v, s·v = c, etc.). Si todas las fusiones se cumplen, escribir D-013 (síntesis sub-tarea A).

**Notas:** chequeo cruzado fundamental. Si fallan algunas fusiones, hay que ajustar las identificaciones.

### Sesión 45 — Decisión: avanzar a sub-tarea B o pausar

**Si A cerrada:** abrir sub-tarea B (3 generaciones / Z₃_dual + K-020).
**Si A parcial:** documentar caveat estructural (análogo K-032.M) y decidir.
**Si A bloqueada:** cierre honesto (análogo Q-039 con resultado negativo), aborto K-033, pivotar.

---

## 7. Caveats epistémicos del programa K-033 completo

(Para mantener honestidad ante el yo-futuro.)

1. **Esto no es K-032.** K-032 cerró con caveat cuantitativo después de 5 sesiones porque la forma funcional era derivable analíticamente. K-033 requiere construcción concreta de objetos en MTC con cálculos no-perturbativos. **Probabilidad de cierre limpio significativamente menor.**

2. **El "primer Yukawa SM desde lattice GUT" no existe en literatura.** Wang-Wen 2018-2019 demuestra **definibilidad**, no calcula Yukawas. Si SCG logra hacerlo, **es contribución original incluso al programa GUT no-perturbativo**. Pero esto significa que no hay un "manual" claro a seguir.

3. **Riesgo de circularidad.** El SM ya nos dice las masas (medidas). La tentación de "ajustar" SCG para reproducirlas es alta. **Disciplina:** todos los inputs deben venir del lado SCG (parámetros: γ_Immirzi, ℓ_P, eventualmente Λ). El output es comparable con el SM.

4. **K-005 master rule.** Si SCG no produce las masas correctas, **NO añadir mecanismos exóticos**. Aceptar que el marco es incompleto. La Regla 5 ("nunca confundir 'no refutado' con 'confirmado'") y la Regla 9 ("preferir destruir un resultado propio") son las defensas contra el wishful thinking.

5. **Tres generaciones es la barrera dura.** Sin un mecanismo claro de 3 copias, K-033 produce a lo más "1 generación SM". Eso ya es valioso, pero no cierra el programa.

---

## 8. Conexiones con preguntas abiertas

K-033 toca naturalmente varias Q abiertas:

- **Q-004 — ¿Por qué 3 generaciones?** Sub-tarea B la ataca directamente.
- **Q-005 — ¿Qué selecciona las constantes fundamentales?** Sub-tarea D produce parámetros (Yukawas) en términos de γ_Immirzi → si predice valor, parcialmente cierra Q-005.
- **Q-014 — ¿N grados de libertad gravitacionales?** Sub-tarea A los identifica concretamente como objetos MTC.
- **Q-027 — niveles CS k.** Confirmado en D-010 que k=1 para Spin(10)_1; K-033 hereda.
- **Q-028 — Higgs = fase de red SCG?** Sub-tarea C la ataca.
- **Q-035 — defectos de A reproducen fermiones SM?** Sub-tarea A es esencialmente esto, aunque con framing más formal (MTC en vez de "defecto de A").
- **Q-044 — origen de magnitudes físicas.** Si K-033 cierra parcialmente, Q-044 gana contenido (masa, Yukawa son magnitudes físicas concretas).

---

## 9. Conclusión de la sesión 41

**Resultado:**
1. ✅ Mapa del programa K-033 trazado (6 sub-tareas A-F con dependencias).
2. ✅ Sub-tarea A seleccionada como primer ataque (necesaria + tractable + diagnóstica).
3. ✅ Plan provisional sesiones 42-44 definido.
4. ✅ Veredicto: **K-033 viable como programa exploratorio con probabilidad estimada de éxito parcial 40-60%.**
5. ✅ Hard cap inicial: 3 sesiones técnicas dedicadas a A; criterios de avance/aborto explicitados.

**Sin trabajo técnico nuevo.** Sesión exploratoria pura. Todos los resultados son metodológicos.

**Próxima sesión (42):** ataque a sub-tarea A, Fase 1 (identificación de 1 y v en lattice SCG).

**Estado:** K-033 abierto formalmente como programa de investigación con disciplina y plan.
