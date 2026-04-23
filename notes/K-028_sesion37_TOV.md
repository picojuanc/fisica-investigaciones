# K-028 sesión 37 — TOV auto-consistente + verdicto preliminar

- **Fecha:** 2026-04-23 (sesión 37).
- **Estado:** veredicto preliminar sobre K-028 tras integración numérica.
- **Continuación de:** `notes/K-028_sesion36_setup.md` (setup formal, EOS derivada).
- **Artefactos:** `experiments/simulations/sim002_tov_radiacion.py`, `experiments/simulations/sim002_resultados.md`, `experiments/simulations/sim002_profile.dat`.

---

## 1. Síntesis ejecutiva

La sesión 37 ejecutó la **Fase I** del plan K-028: resolver TOV con EOS de radiación ($p = \rho/3$, derivada en sesión 36) + regularización UV, para encontrar el perfil auto-consistente del interior BH-SCG.

**Resultado principal (doble):**

1. **La interpretación heurística de K-028 como "factor de redshift" es incorrecta.** El valor $1/(3\pi^2) \approx 0.0338$ es una **identidad geométrica pura** derivable sin QFT+GR, directamente del coeficiente 4/3 de K-007 y la definición de $V_{BH}$.

2. **La hipótesis de trabajo (radiación pura auto-consistente) se REFUTA numéricamente.** Para cualquier densidad central $y_c$, la TOV con $p = \rho/3$ satura en compactness $= 3/7$ en el radio de Schwarzschild, nunca alcanzando $1$. La materia de radiación pura solo puede cargar **3/7 de la masa ADM total** en $r < r_s$.

Ambos resultados combinan para dar:

> **Veredicto preliminar K-028:** escenario (C) — refutación de la lectura heurística (redshift) + identificación de un problema estructural mayor: la EOS del string gas SCG no puede ser isotropic-average puro; el interior requiere anisotropy, shell exótica, o transición de fase near-horizon.

Esto es progreso científico positivo aunque negativo en apariencia: identifica un defecto conceptual en el marco heurístico de sesión 15 y señala una dirección concreta de refinamiento.

---

## 2. Identidad geométrica $1/(3\pi^2)$

### 2.1 Derivación directa (sin TOV)

Partiendo de:
- $d^2 = (4/3) r_s \ell_P$ (K-007).
- $\rho_{K007} = 2\pi \hbar c / d^4$ (D-006 aplicado a K-007).
- $V_{BH} = (4\pi/3) r_s^3$.
- $M = r_s c^2/(2G)$, $\ell_P^2 = \hbar G/c^3$.

En unidades Planck ($\hbar = c = G = \ell_P = M_P = 1$), con $r_s = 2M$:

$$
d^2 = \frac{8M}{3}, \qquad \rho_{K007} = \frac{2\pi}{(8M/3)^2} = \frac{9\pi}{32 M^2}
$$

$$
V_{BH} = \frac{4\pi}{3}(2M)^3 = \frac{32\pi M^3}{3}, \qquad E_{\text{plano}} = \rho_{K007} \cdot V_{BH} = \frac{9\pi}{32 M^2} \cdot \frac{32\pi M^3}{3} = 3\pi^2 M
$$

$$
\boxed{\; \frac{E_{\text{plano}}}{M c^2} = 3\pi^2, \qquad \langle f \rangle_{\text{heurístico}} = \frac{M c^2}{E_{\text{plano}}} = \frac{1}{3\pi^2} \approx 0.0338 \;}
$$

La identidad es **exacta, geométrica, y no requiere física curva**. Sigue del coeficiente $4/3$ de K-007 (obtenido en D-003 / D-009 por análisis variacional) combinado con $V_{BH}$ y $\rho_{K007}$.

### 2.2 Lectura correcta de la identidad

Leída correctamente, la identidad dice:

> **La densidad uniforme que K-007 implica ($\rho_{K007}$) sobre-estima la densidad necesaria para dar masa ADM $M$ por factor $3\pi^2$.**

Equivalentemente: si llenáramos $V_{BH}$ con densidad uniforme $\rho_{K007}$, la masa total sería $3\pi^2 M$, no $M$. Para que la masa sea $M$, la densidad uniforme debe ser $\rho_{K007}/(3\pi^2) = 3M/(4\pi r_s^3) = \langle \rho \rangle_V$.

### 2.3 Por qué la interpretación "redshift" era errónea

Sesión 15 (Q-037/038) razonó:
- Modos Casimir locales tienen energía $\sim \hbar c / d$ con $d = $ K-007.
- Observados desde infinito: $E_\infty = f(r) \cdot E_{\text{local}}$.
- Consistencia ADM: $\int f(r) \cdot \rho_{K007} dV = M c^2$.
- Valor promedio: $\langle f \rangle = 1/(3\pi^2)$.

El error: **la premisa "$\rho = \rho_{K007}$ uniforme" no es una descripción física del interior SCG**. Es una hipótesis geométrica sobre la escala típica. Confundir "escala característica" con "densidad uniforme" llevó a la interpretación de redshift.

El marco auto-consistente (TOV + EOS) **reemplaza** la uniformidad por un perfil variable. En ese marco, $\rho(r)$ no es uniforme y el "redshift" no aparece como factor multiplicativo.

### 2.4 Estatus revisado de K-028

K-028 como candidato original **se refuta** en su lectura heurística.

K-028.R (reinterpretación, sesión 37):

> **K-028.R:** El factor $1/(3\pi^2)$ es la razón geométrica entre la densidad uniforme ADM-consistente $\langle \rho \rangle_V = 3M/(4\pi r_s^3)$ y la densidad Casimir implícita en K-007 $\rho_{K007} = 2\pi \hbar c/d_{K007}^4$. Es una identidad exacta que refleja el coeficiente específico $4/3$ de K-007, no una medición física.

K-028.R es una identidad, **no** un insight físico. No debe contar como un K confirmado; degradar a observación matemática o nota técnica.

---

## 3. Integración numérica TOV (Fase I)

### 3.1 Setup

ODEs adimensionales (sesión 36, §4):

$$
\frac{d\tilde{m}}{dx} = 3 x^2 y, \qquad
\frac{dy}{dx} = -\frac{2 y (\tilde{m} + y x^3)}{x(x - \tilde{m})}
$$

Método: RK4 manual con paso adaptativo. $x \in [10^{-5}, 0.99999]$. Expansión regular en el centro.

### 3.2 Exploración sobre $y_c$

Barrido logarítmico $y_c \in [0.1, 10^4]$. Ver tabla en `sim002_resultados.md` §4.1.

**Patrón numérico universal:**

- **Compactness $\tilde{m}(x)/x$ satura en $\approx 3/7 = 0.4286$** en $x = 1$, para todo $y_c \gtrsim 3$.
- Independientemente de la densidad central (desde Planck-near hasta subcrítica), el perfil converge al **singular isothermal** $y_{\text{iso}}(x) = 1/(7 x^2)$ en el bulk.
- La "superficie de la estrella" (donde $y \to 0$) NO se alcanza en ningún punto $x < \infty$.

### 3.3 Validación con solución singular isothermal analítica

La solución exacta auto-similar $y_{\text{iso}}(x) = 1/(7 x^2)$ con $\tilde{m}(x) = 3x/7$, compactness constante $3/7$, satisface TOV exactamente (verificación analítica en `notes/K-028_sesion36_setup.md` §4.3).

El perfil numérico (y_c = 10^4) coincide con $y_{\text{iso}}$ al < 2% en el rango $0.1 \leq x \leq 0.999$:

| $x$ | $y_{\text{num}}$ | $y_{\text{iso}} = 1/(7x^2)$ | diff |
|---:|---:|---:|---:|
| 0.2 | 3.62 | 3.571 | 1.4% |
| 0.5 | 0.584 | 0.571 | 2.3% |
| 0.7 | 0.295 | 0.2915 | 1.2% |
| 0.9 | 0.177 | 0.1763 | 0.4% |
| 0.99 | 0.146 | 0.1459 | 0.1% |

**El bulk SCG es singular isothermal.** Confirmación numérica.

### 3.4 Comportamiento near-center y near-horizon

- **Near-center** ($x \leq 10^{-3}$): $y(x) \approx y_c$, casi constante. Densidad alta, Casimir cerca del corte UV si $y_c \to y_{\max}$. En este régimen la fórmula Casimir perturbativa se rompe (física Planck-scale).

- **Near-horizon** ($0.9 < x < 1$): SIN cambio cualitativo. Compactness permanece en $3/7$. No hay aceleración hacia 1. **El horizonte NO emerge.**

### 3.5 Implicación estructural

$$
\boxed{\; \text{TOV con } p = \rho/3 \implies \tilde{m}(1) \leq \frac{3}{7}, \text{ nunca } 1 \;}
$$

Traducción: un gas isotrópico de cuerdas Casimir solo puede acumular $3/7 \approx 43\%$ de la masa ADM dentro de $r_s$. El otro **57% ($4/7$)** necesita otra descripción.

---

## 4. Diagnóstico: por qué la radiación pura no basta

### 4.1 Obstrucción matemática

Para radiación pura con densidad decreciente monotónica (por regularidad TOV), la compactness máxima accesible es:

$$
\left(\frac{2 G m(r)}{c^2 r}\right)_{\max} = \frac{3}{7} \quad (\text{singular isothermal})
$$

Éste es un resultado bien conocido en la literatura relativistic-stars. Se debe a la rigidez de la EOS $p = \rho/3$: el gas no puede soportar configuraciones más compactas sin colapsar al singular isothermal.

### 4.2 Física del déficit

El string gas SCG fue derivado por isotropic averaging (sesión 36, §3.2). Pero este promedio asume que la orientación del string plegado es completamente aleatoria a todas las escalas. Esta asunción es demasiado fuerte:

- **Near-horizon**, razones holográficas (entropía ∝ área, no volumen) sugieren que el string se **estira tangencialmente a la superficie horizontal**. La orientación deja de ser aleatoria; hay una dirección preferente (radial suppressed, tangencial enhanced).

- **Near-center**, hay tensiones no capturadas por isotropic averaging (¿cuerda termina? ¿nudos concentrados?).

Por tanto la EOS efectiva DEBE ser anisotrópica en regiones específicas:

$$
p_r(r) \neq p_t(r)
$$

con posiblemente $p_r < p_t$ near-horizon (string tangencialmente alineado).

### 4.3 Precedentes en la literatura

- **Gravastars** (Mazur-Mottola 2001): interior $p = -\rho$ (de Sitter), shell delgada con EOS $p = \rho$ (ultra-stiff), matching al Schwarzschild exterior. Compactness 1 alcanzable.
- **Boson stars / strange stars**: anisotropy evade Buchdahl.
- **Estrellas con pressure anisotropic** (Herrera-Santos 1997): compactness arbitrariamente cerca de 1.

Las variantes de SCG que responden al 4/7 probablemente habitan este espacio de soluciones.

---

## 5. Veredicto K-028

### 5.1 Enunciado

El candidato K-028 original (sesión 15):

> ⟨f⟩_redshift = 1/(3π²) es el factor de redshift gravitacional promedio del interior BH-SCG.

**se refuta por dos motivos:**

1. El valor $1/(3\pi^2)$ es una identidad geométrica (razón entre densidades uniformes hipotéticas), no una cantidad física de redshift.
2. El marco "uniforme con redshift" es GR-inconsistente: EOS radiación + TOV no produce interior uniforme reaching horizon.

### 5.2 Estatus epistémico

- **K-028 (versión original):** degradado de candidato a **observación matemática**. Mantener referencia histórica (como K-001, K-002); no contar en inventario de insights físicos.
- **K-028.R (reinterpretación):** formulada, pero no se promueve — es una identidad, no un insight.
- **P-15' (cálculo riguroso):** cerrado con resultado negativo (no había una cantidad física $\langle f \rangle$ rigurosa que calcular).
- **Nueva pregunta:** ¿qué mecanismo SCG carga el 4/7 restante de masa? (Q-045, abajo.)

### 5.3 Consistencia con el resto del marco

- **H-001:** la estructura general (cuerda plegada + saturación entrópica) **sigue intacta**. Solo se refina: el interior NO es uniforme; es singular isothermal + estructura adicional near-horizon.
- **K-007 (d ~ √(r_s ℓ_P)):** sigue válida como **escala característica** (en $x \sim 1/(√{42}\pi) \approx 0.05$ del singular isothermal, $\rho_{\text{iso}} = \rho_{K007}$). Pero NO es una densidad uniforme; es una densidad puntual.
- **D-003 (entropía plegada):** sigue válida si reinterpretamos "$d$ uniforme" como "$d$ promedio".
- **D-009 (llenado volumétrico variacional):** **requiere generalización** para $d(r)$ variable. El 4/7 no cabe en la minimización tal como se hizo.

### 5.4 Alerta meta (Regla 9)

Este es un caso ejemplar de **Regla 9 aplicada** (preferir destruir un resultado propio a defenderlo por inercia):

- El "success" K-028 de sesión 15 era atractivo pero heurístico.
- El análisis honesto lo refuta.
- Se celebra: se identificó un error conceptual que habría propagado a v2.2+.
- K-005 también aplica: la teoría es más modesta de lo que la coincidencia numérica prometía.

---

## 6. Nueva pregunta abierta (Q-045)

**Q-045 (nueva, sesión 37, prioridad alta):**

> ¿Qué mecanismo SCG carga los $4/7 \approx 57\%$ de la masa ADM que la EOS radiación pura no acomoda? Tres candidatos principales:
>
> - **(a) Anisotropic stress macroscópica:** orientación preferente del string plegado near-horizon (holográfica).
> - **(b) Shell delgada cerca de $r_s$:** capa con EOS exótica (posible $p = -\rho$ de Sitter local).
> - **(c) Transición de fase de la EOS near-horizon:** Casimir → nueva física cuando $d \to \ell_P$.

Relacionada con: P-15', H-001 (interior), D-009 (llenado variacional), K-007 (escala característica), K-031 (llenado volumétrico).

---

## 7. Plan sesión 38

### 7.1 Opción A (recomendada): TOV anisotrópica

1. Derivar TOV anisotrópica general con $p_r(r), p_t(r)$ independientes.
2. Proponer modelo SCG: $p_r = \alpha \rho$, $p_t = \beta \rho$ con $\alpha, \beta$ dependientes de $r$. Motivación holográfica: $\alpha \to 1$ bulk, $\alpha \to -1$ near-horizon.
3. Integrar numéricamente. Verificar si compactness → 1 accesible.
4. Extraer perfil $d(r)$ efectivo.
5. Comparar con K-007 como escala promedio.

### 7.2 Opción B: Modelo shell tipo gravastar-invertido

1. Bulk: singular isothermal para $r < r_{\text{shell}}$.
2. Shell: capa delgada en $r_{\text{shell}} \lesssim r < r_s$ con EOS exótica.
3. Matching: Israel junction conditions para masa + tensión de shell.
4. Compatibilidad con SCG.

### 7.3 Opción C (conservadora): consolidar y documentar

1. Actualizar H-001 con caveat "interior no uniforme".
2. Generalizar D-009 a $d(r)$ variable.
3. Abrir Q-045 formalmente.
4. **Dejar el 4/7 como misterio estructural abierto** y pasar a otro tema (K-033, Q-030).

### 7.4 Recomendación de cierre

**Opción A para sesión 38**, pero con techo de esfuerzo: si en 1 sesión no se cierra, ir a Opción C.

La disciplina K-005: no inventemos física exótica; usemos herramienta estándar (TOV anisotrópica, tratable).

---

## 8. Entregables producidos

- `experiments/simulations/sim002_tov_radiacion.py` — RK4 manual + bisección.
- `experiments/simulations/sim002_profile.dat` — 2082 puntos del perfil.
- `experiments/simulations/sim002_resultados.md` — resumen numérico.
- `notes/K-028_sesion37_TOV.md` (este archivo).

---

## 9. Recapitulación meta

**Lo que cambia en v2.1 → v2.1.1 (snapshot no requerido, parche documental):**

- K-028 **degradado** de candidato a observación matemática; no cuenta en inventario.
- Identidad geométrica $1/(3\pi^2)$ documentada en este note.
- Q-045 abierta (reemplaza a P-15' efectivamente).
- H-001 interior necesita caveat "no uniforme".
- D-009 marca de "generalizar a $d(r)$ variable".

**Lo que NO cambia:**

- H-001 fase SCG sigue válida en términos generales.
- H-002, H-003 intactas.
- Grupo gauge + Ashtekar + Walker-Wang (v2.0/v2.1) sin tocar.
- Bosquejo Lagrangiana 5/5 cerrado sigue válido (K-028 era P-15' residual, no una sub-tarea de la Lagrangiana).
- Inventario de K confirmados: 31 pre-sesión 37 ⇒ **30** post-sesión 37 (K-028 removido como candidato).

**Regla 5 aplicada disciplinadamente:** no se refuta K-007 ni D-009 globalmente; solo la extensión operacional "K-007 ≡ densidad uniforme" que nunca fue derivada.

---

## 10. Observación final

El resultado de sesión 37 es un **refinamiento positivo disfrazado de resultado negativo**. La teoría pierde una predicción heurística (⟨f⟩ = 1/(3π²) como redshift) pero:

- Identifica una inconsistencia estructural previamente invisible.
- Abre una pregunta concreta y tratable (Q-045).
- Aclara que K-007 es una **escala** (correcta), no una **densidad uniforme** (incorrecta).
- Revela que el interior SCG tiene estructura dual: bulk singular isothermal + algo near-horizon.

**Es exactamente el tipo de resultado que una teoría madura debe producir:** refinar honestamente a medida que se somete al escrutinio cuantitativo.

**Próximo paso:** decidir entre Opciones A, B, C para sesión 38. Mi recomendación: **A** con techo de esfuerzo.
