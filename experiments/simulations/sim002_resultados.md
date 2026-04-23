# sim002_resultados — TOV con EOS de radiación (p = ρ/3)

- **Fecha:** 2026-04-23 (sesión 37).
- **Script:** `sim002_tov_radiacion.py`.
- **Contexto:** K-028 / P-15'. Resolución del interior BH-SCG bajo EOS derivada en sesión 36 (isotropic averaging del string gas).

---

## 1. Objetivo de la simulación

Verificar numéricamente la hipótesis de trabajo:

> El interior BH-SCG con EOS radiación $p = \rho/3$ admite una solución estática, esféricamente simétrica, que alcanza el horizonte ($2Gm(r_s)/c^2 r_s = 1$) como superficie de la estrella.

Si la hipótesis es correcta, existe un $y_c$ crítico (densidad central en unidades de $\rho_* = 3M/(4\pi r_s^3)$) que da una configuración self-consistent.

---

## 2. Sistema ODE integrado

Variables adimensionales:

- $x = r/r_s$
- $\tilde{m}(x) = m(r)/M$
- $y(x) = \rho(r)/\rho_*$ con $\rho_* = 3M/(4\pi r_s^3)$.

ODEs (derivadas en `notes/K-028_sesion36_setup.md`):

$$
\frac{d\tilde{m}}{dx} = 3 x^2 y, \qquad
\frac{dy}{dx} = -\frac{2 y (\tilde{m} + y x^3)}{x(x - \tilde{m})}, \qquad
\frac{d\Phi}{dx} = \frac{\tilde{m} + y x^3}{x(x - \tilde{m})}
$$

Condiciones iniciales en $x_0 = 10^{-5}$ (expansión regular):
$\tilde{m}(x_0) = y_c x_0^3$, $y(x_0) = y_c (1 - 2 y_c x_0^2)$, $\Phi(x_0) = 0$.

Integrador: RK4 manual (sin dependencias externas, scipy no disponible en el sistema).

---

## 3. Identidad geométrica analítica (sin TOV)

Antes de cualquier integración:

$$
\frac{E_{\text{plano}}}{Mc^2} = \frac{\rho_{K007} \cdot V_{BH}}{Mc^2} = 3\pi^2 \approx 29.608813
$$

$$
\langle f \rangle_{\text{heurístico}} = \frac{Mc^2}{E_{\text{plano}}} = \frac{1}{3\pi^2} \approx 0.033774
$$

Esto es una identidad geométrica pura, no requiere QFT+GR ni TOV. Sigue directamente del coeficiente 4/3 de K-007, la fórmula Casimir $\rho = 2\pi \hbar c / d^4$, y la definición de $V_{BH}$.

**Implicación:** la interpretación de sesión 15 (⟨f⟩ como factor de redshift) era operacionalmente equivalente a decir "ρ uniforme K-007 sobre-estima la masa ADM por factor 3π²". No es una medida física dinámica.

---

## 4. Resultados numéricos TOV

### 4.1 Exploración de $y_c$

Integración desde $x_0 = 10^{-5}$ hasta $x_{\max} = 0.99999$ para diversos valores de $y_c$:

| $y_c$ | $x_{\text{end}}$ | $\tilde{m}_{\text{end}}$ | $y_{\text{end}}$ | compactness | status |
|---:|---:|---:|---:|---:|---|
| 0.1 | 1.000 | 0.0890 | 8.24e-02 | **0.0890** | x_max |
| 0.3 | 1.000 | 0.2163 | 1.74e-01 | **0.2163** | x_max |
| 1.0 | 1.000 | 0.4083 | 2.26e-01 | **0.4083** | x_max |
| 3.0 | 1.000 | 0.4910 | 1.75e-01 | **0.4910** | x_max |
| 10.0 | 1.000 | 0.4688 | 1.32e-01 | **0.4689** | x_max |
| 30.0 | 1.000 | 0.4311 | 1.25e-01 | **0.4311** | x_max |
| 100.0 | 1.000 | 0.4118 | 1.34e-01 | **0.4118** | x_max |
| 300.0 | 1.000 | 0.4147 | 1.44e-01 | **0.4147** | x_max |
| 1000.0 | 1.000 | 0.4259 | 1.48e-01 | **0.4259** | x_max |
| 10000.0 | 0.9999 | 0.4323 | 1.43e-01 | **0.4323** | x_max |

**Patrón crítico:**

- Ningún $y_c$ produce $\tilde{m}(1)/1 = 1$ (compactness = 1 en el horizonte).
- Para $y_c \gtrsim 3$: compactness en $x=1$ satura en **~3/7 = 0.4286**.
- Para $y_c \to \infty$: compactness → 3/7 exactamente, i.e., el singular isothermal.
- La "superficie de la estrella" (donde $y \to 0$) NO se alcanza para ningún $y_c$ en el rango probado.

### 4.2 Perfil de $y_c = 10^4$ (aprox. máximo probado)

| $x$ | $\tilde{m}$ | $y$ | $\tilde{m}/x$ | $\Phi$ |
|---:|---:|---:|---:|---:|
| 0.0001 | ~0 | 10000 | ~0 | 0.0001 |
| 0.001 | 1.0e-5 | 9800 | 0.010 | 0.010 |
| 0.01 | 4.1e-3 | 2251 | 0.409 | 0.746 |
| 0.05 | 0.022 | 49.5 | 0.436 | 2.654 |
| 0.10 | 0.041 | 13.3 | 0.412 | 3.312 |
| 0.20 | 0.084 | 3.62 | 0.417 | 3.962 |
| 0.30 | 0.128 | 1.64 | 0.425 | 4.359 |
| 0.50 | 0.216 | 0.584 | 0.432 | 4.874 |
| 0.70 | 0.303 | 0.295 | 0.433 | 5.216 |
| 0.80 | 0.346 | 0.225 | 0.433 | 5.352 |
| 0.90 | 0.390 | 0.177 | 0.433 | 5.472 |
| 0.99 | 0.428 | 0.146 | 0.432 | 5.568 |

**Observaciones:**

1. **Núcleo** ($x \lesssim 10^{-3}$): densidad cercana a $y_c$; se comporta como "gas caliente" en región Casimir fuerte. Φ crece rápidamente (lapse decrece fuerte). **Este es el régimen donde la fórmula Casimir perturbativa debería romperse** (ρ → ρ_max si $y_c$ fuera aún mayor).

2. **Transición** ($10^{-3} \lesssim x \lesssim 0.05$): $y$ cae como potencia, compactness crece rápido hasta saturar en 3/7.

3. **Bulk** ($x \gtrsim 0.1$): el perfil sigue exactamente la **solución singular isothermal** analítica $y(x) \approx (1/7)/x^2$. Compactness constante en 3/7.

4. **Near-"horizon"** ($0.9 < x < 1$): SIN cambio cualitativo. Compactness permanece en 3/7, sin acelerar hacia 1. **El horizonte NO se forma.**

5. $\Phi$ al final ≈ 5.57, valor específico del singular isothermal. Finito, no divergente.

### 4.3 Comparación con singular isothermal analítico

La solución singular isothermal exacta: $y_{\text{iso}}(x) = 1/(7x^2)$, compactness constante $= 3/7$.

El perfil numérico en $x = 0.5$ da $y \approx 0.584$. Comparación: $y_{\text{iso}}(0.5) = 1/(7 \cdot 0.25) = 0.571$. **Diferencia 2%.**

Para $x = 0.9$: $y \approx 0.177$. $y_{\text{iso}}(0.9) = 1/(7 \cdot 0.81) = 0.176$. **Diferencia < 1%.**

**La solución numérica converge al singular isothermal en el bulk, como se predijo analíticamente.**

---

## 5. Resultado estructural mayor

### 5.1 La hipótesis de trabajo es FALSA

Para cualquier densidad central $y_c$:

- La compactness $\tilde{m}(x)/x$ satura en **3/7 < 1**.
- El horizonte **nunca** se forma como superficie de la estrella con materia radiación.
- La materia TOV-radiación se extiende indefinidamente (hacia $x > 1$), asintóticamente singular isothermal.

Es decir: **TOV con p = ρ/3 NO puede describir el interior self-consistent de un BH-SCG de masa M. La materia solo puede acumular 3/7 de la masa total en $r < r_s$; el remanente 4/7 ~ 57% no tiene cabida dentro de la radiación pura.**

### 5.2 Significado físico

- El "bulk" del interior SCG es singular isothermal ($\rho \propto 1/r^2$). Matemáticamente sólido.
- El "shell near-horizon" que debe cargar 4/7 de la masa ADM requiere **física adicional** más allá de la fórmula Casimir perturbativa.
- Posibilidades (a explorar en sesión 38):
  - (a) **Anisotropic stress** macroscópica: si el string plegado tiene orientación preferente (por ejemplo radial near-horizon), la EOS isotrópica no aplica; TOV anisotrópica puede exceder la cota Buchdahl-like de 3/7.
  - (b) **Thin shell gravastar-like invertido**: capa delgada cerca de $r_s$ con EOS $p = -\rho$ (de Sitter local) o similar exótica, cargando el 4/7 restante.
  - (c) **Phase transition** near-horizon: la Casimir se rompe cuando $d \to \ell_P$, posible nuevo régimen con EOS diferente.
  - (d) **El problema está mal planteado**: el "BH estático con interior TOV" quizás no es la descripción correcta; habría que usar descripción dinámica o stringy no-local.

### 5.3 Veredicto K-028

**Escenario (C) activado**: K-028 en su interpretación heurística como redshift está **refutado**.

El valor numérico $1/(3\pi^2)$ es una identidad geométrica (no física) que emerge del coeficiente 4/3 de K-007 y el ansatz de densidad uniforme. Pero la uniformidad es **incompatible** con Einstein+TOV para EOS radiación.

La reinterpretación "K-028.R" propuesta:

> **K-028.R (refutado sesión 37):** El factor $1/(3\pi^2)$ no es un factor de redshift gravitacional. Es la razón geométrica $\langle \rho \rangle_V / \rho_{K007}$ entre la densidad ADM-consistente y la densidad Casimir implícita en K-007. La hipótesis operacional que subyace (uniformidad) no resiste análisis TOV auto-consistente con EOS radiación.

Esta reinterpretación **no** descarta K-007 ni H-001 — solo refuta la lectura heurística de ⟨f⟩ como redshift y la idea de interior uniforme. La estructura geométrica de SCG sigue intacta.

---

## 6. Datos crudos

Perfil completo en `sim002_profile.dat` (2082 puntos). Columnas: `x  m_tilde  y  compactness  Phi`.

Para reanálisis futuro (plots externos, comparaciones con gravastar, etc.).

---

## 7. Próximos pasos sugeridos (sesión 38)

**Opción A — Anisotropic TOV (preferida):**
Relajar la isotropic averaging del string gas. Modelo: near-horizon, el string tiende a orientarse tangencialmente (paralelo al horizonte) por razones holográficas, dando:
- $p_r \neq p_t$ localmente.
- Buchdahl-like bound puede evadirse; compactness → 1 posible.
- TOV anisotrópica numérica + interpretación.

**Opción B — Shell gravastar-like invertido:**
Modelar capa delgada en $r \sim r_s$ con EOS $p = -\rho$ u otra exótica. Calcular mass budget; verificar si el 4/7 cabe.

**Opción C — Aceptar resultado negativo, consolidar:**
Formalizar K-028.R como refutación productiva. Actualizar H-001/D-003/D-009 con el caveat: "la asunción de uniformidad interior es GR-inconsistente con EOS radiación pura; el SCG BH requiere estructura más rica (bulk + shell)". Puede llevar al D-009 generalizado.

**Mi recomendación:** Opción A (anisotropic TOV). Razones:
- Físicamente más natural (el string tiene orientación; la isotropic averaging era una idealización).
- Matemáticamente tractable (TOV anisotrópica estándar).
- Probablemente responde a "¿de dónde viene el 4/7?" desde primeros principios.

Si Opción A también refuta: ir a Opción B (gravastar híbrido).

---

## 8. Resumen

- Integración RK4 TOV con $p = \rho/3$, diez valores de $y_c$ barridos.
- **Compactness satura en 3/7, no 1**, para todo $y_c$.
- Perfil numérico converge al singular isothermal analítico en el bulk.
- Identidad geométrica $1/(3\pi^2)$ verificada; es geométrica pura.
- **K-028 heurístico (redshift) refutado por análisis auto-consistente.**
- K-028.R: factor geométrico, no físico. 4/7 de la masa ADM requiere física adicional.
- Sesión 38: Opción A (anisotropic TOV) para resolver el déficit 4/7.
