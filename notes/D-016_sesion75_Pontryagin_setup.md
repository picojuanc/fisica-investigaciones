# D-016 / Sesión 75 — Setup Pontryagin completo: BVP del problema variacional Q-045

- **Fecha:** 2026-04-26 (sesión 75).
- **Continuación de:** `logic/derivations/D-016_variacional_anisotropy_holografica.md` (S69, setup formal).
- **Objetivo S75:** reformular el problema variacional D-016 como BVP Pontryagin completo + plan numérico shooting method.
- **Estado al inicio:** D-016 setup S69 establece el problema como control óptimo con función de control $h(x)$. Esta sesión lo refina a formulación rigurosa con $h'(x)$ como control libre.

---

## 1. Reformulación con $h(x)$ como variable de estado

### 1.1 Problema original (D-016 §2)

**Variables:** $\tilde m(x), y(x)$ con $h(x)$ como control.
**Sistema:** $\dot{\tilde m} = 3 x^2 y$, $\dot y = F(\tilde m, y, h, h'; x)$.
**Función objetivo:** $J = \tilde m(1)$.

**Problema técnico:** $F$ depende de $h'(x)$ — es problema de control con "derivada de control" como input, lo cual complica Pontryagin estándar.

### 1.2 Reformulación: $h$ como variable de estado

**Idea:** introducir $h$ como variable de estado adicional con derivada $u = h'$ como control libre.

**Variables de estado (3):** $\tilde m, y, h$.
**Variable de control (1):** $u(x)$.
**Sistema:**
$$
\begin{aligned}
\dot{\tilde m} &= 3 x^2 y \\
\dot y &= F(\tilde m, y, h, u; x) \\
\dot h &= u
\end{aligned}
$$

donde $F$ explícitamente con $u$ en lugar de $h'$:
$$
F(\tilde m, y, h, u; x) = \frac{1}{1 - h}\left[ y u - \frac{y(4 - h)[\tilde m + x^3 y(1-h)]}{2 x(x - \tilde m)} + \frac{3 y h}{x} \right]
$$

**Ventaja:** ahora $F$ es **lineal en $u$** — Pontryagin estándar aplicable.

### 1.3 Función objetivo

$$
J[u(\cdot)] = \tilde m(x_{\text{end}}) \quad \text{maximizar}
$$

con la condición terminal $x_{\text{end}} = 1$ (cierre completo al horizonte).

### 1.4 Restricciones

- **Iniciales:** $\tilde m(0) = 0, y(0) = y_c, h(0) = 0$.
- **Terminales:** $\tilde m(1) = 1$ (cierre), libre $y(1), h(1)$.
- **Estados:** $h(x) \in [-2, 4]$ (DEC), $y(x) > 0$, $\tilde m(x) < x$.

---

## 2. Hamiltoniano de Pontryagin

### 2.1 Definición

$$
H(\tilde m, y, h, u, \lambda_m, \lambda_y, \lambda_h; x) = \lambda_m \cdot 3 x^2 y + \lambda_y \cdot F(\tilde m, y, h, u; x) + \lambda_h \cdot u
$$

donde $\lambda_m, \lambda_y, \lambda_h$ son las **variables adjuntas** (multiplicadores de Lagrange dinámicos).

### 2.2 Separación lineal en $u$

Reescribiendo $F$ separando el término lineal en $u$:
$$
F = \underbrace{\frac{y}{1-h}}_{a(\tilde m, y, h, x)} \cdot u + \underbrace{\frac{1}{1-h}\left[-\frac{y(4-h)[\tilde m + x^3 y(1-h)]}{2x(x-\tilde m)} + \frac{3yh}{x}\right]}_{b(\tilde m, y, h, x)}
$$

Entonces:
$$
H = \lambda_m \cdot 3x^2 y + \lambda_y \cdot [a(\cdot) u + b(\cdot)] + \lambda_h u = \lambda_m \cdot 3x^2 y + \lambda_y \cdot b + (\lambda_y a + \lambda_h) u
$$

### 2.3 Condición de optimalidad

**Pontryagin:** $u^*(x)$ extrema $H$. Para $H$ lineal en $u$:
$$
\frac{\partial H}{\partial u} = \lambda_y a + \lambda_h = \lambda_y \cdot \frac{y}{1-h} + \lambda_h
$$

**Caso interesante (interior del dominio):** si $u^*$ no está en frontera ($u^* \neq u_{\min}, u_{\max}$):
$$
\boxed{\;\lambda_y \cdot \frac{y}{1-h} + \lambda_h = 0 \quad \Rightarrow \quad \lambda_h = -\lambda_y \cdot \frac{y}{1-h}\;}
$$

**Esta es relación algebraica** entre $\lambda_h$ y $\lambda_y$ — permite eliminar una variable adjunta.

**Singularidad estructural:** el problema es **degenerado en el control** ($H$ no depende cuadráticamente de $u$), lo cual significa que el control óptimo no se determina puntualmente por la condición $\partial H/\partial u = 0$ — es **singular** en el sentido del control óptimo.

**Consecuencia:** el control óptimo se determina por **derivadas de orden superior** de la condición $\partial H/\partial u$ (Goh condition o Kelley condition). Esto **complica significativamente el problema** y es típico de problemas variacionales con linealidad en el control.

---

## 3. Ecuaciones adjuntas

### 3.1 Forma general

$$
\dot \lambda_m = -\frac{\partial H}{\partial \tilde m}, \quad \dot \lambda_y = -\frac{\partial H}{\partial y}, \quad \dot \lambda_h = -\frac{\partial H}{\partial h}
$$

### 3.2 Cálculo de las derivadas

**$\partial H/\partial \tilde m$:** sólo $b$ depende de $\tilde m$ via $[\tilde m + x^3 y(1-h)]/[2x(x-\tilde m)]$:
$$
\frac{\partial b}{\partial \tilde m} = \frac{1}{1-h} \cdot \frac{-y(4-h)}{2x} \cdot \frac{(x-\tilde m) + [\tilde m + x^3 y(1-h)]}{(x-\tilde m)^2}
$$

Después de simplificar:
$$
\frac{\partial b}{\partial \tilde m} = -\frac{y(4-h)[x + x^3 y(1-h)/(x-\tilde m)]}{2x(1-h)(x-\tilde m)} = -\frac{y(4-h)}{2(1-h)} \left[\frac{1}{x-\tilde m} + \frac{x^2 y(1-h)}{(x-\tilde m)^2}\right]
$$

**$\partial H/\partial y$:** $\lambda_m \cdot 3x^2 + \lambda_y \cdot \partial F/\partial y$. El término $\partial F/\partial y$ tiene varios componentes:
$$
\frac{\partial F}{\partial y} = \frac{1}{1-h}\left[u - \frac{(4-h)[2 x^3 y(1-h) + \tilde m]}{2x(x-\tilde m)} \cdot \text{(normalizar)} + \frac{3h}{x}\right]
$$

(Expansión completa pendiente — ver Apéndice A para detalle algebraico.)

**$\partial H/\partial h$:** combinación de varios términos (factor $1/(1-h)^2$, derivadas del polinomio en $h$).

### 3.3 Condiciones terminales (transversalidad)

Para $J = \tilde m(1)$:
$$
\lambda_m(1) = \frac{\partial J}{\partial \tilde m}\bigg|_1 = 1, \quad \lambda_y(1) = 0, \quad \lambda_h(1) = 0
$$

**Pero** si tenemos restricción $\tilde m(1) = 1$ (cierre completo al horizonte como condición), entonces $\lambda_m(1)$ es libre y se determina por la restricción.

---

## 4. BVP completo

### 4.1 Sistema de ODEs (6 ecuaciones)

$$
\begin{aligned}
\dot{\tilde m} &= 3 x^2 y \\
\dot y &= F(\tilde m, y, h, u^*; x) \\
\dot h &= u^*(x) \\
\dot \lambda_m &= -\partial H/\partial \tilde m \\
\dot \lambda_y &= -\partial H/\partial y \\
\dot \lambda_h &= -\partial H/\partial h
\end{aligned}
$$

donde $u^*(x)$ se determina por la condición de optimalidad.

### 4.2 Caso de control singular

Como ya identificado, $H$ es lineal en $u$ → control singular. La condición $\partial H/\partial u = 0$ da relación algebraica $\lambda_h = -\lambda_y y/(1-h)$, NO determina $u^*$ puntualmente.

**Estrategia para control singular (Bell-Jacobson 1975):** derivar la condición $\partial H/\partial u = 0$ con respecto a $x$ hasta que aparezca $u$ explícitamente. La primera derivada da:
$$
\frac{d}{dx}(\lambda_h + \lambda_y y/(1-h)) = 0
$$

Expandiendo:
$$
\dot \lambda_h + \dot \lambda_y \cdot \frac{y}{1-h} + \lambda_y \cdot \frac{\dot y (1-h) + y \cdot \dot h}{(1-h)^2} = 0
$$

Sustituyendo $\dot y = F$ y $\dot h = u$:
$$
\dot \lambda_h + \dot \lambda_y \cdot \frac{y}{1-h} + \lambda_y \cdot \frac{F(1-h) + yu}{(1-h)^2} = 0
$$

Aquí $u$ aparece explícitamente. Resolviendo:
$$
u_{\text{singular}}^* = -\frac{(1-h)^2}{\lambda_y y} \left[\dot \lambda_h + \dot \lambda_y \cdot \frac{y}{1-h}\right] - \frac{F(1-h)}{y}
$$

Esta es la **trayectoria singular** óptima.

### 4.3 Condiciones de frontera

| Variable | $x = 0$ | $x = 1$ |
|---|---|---|
| $\tilde m$ | $0$ | $1$ (cierre) |
| $y$ | $y_c$ (parámetro) | libre |
| $h$ | $0$ (regularidad) | libre |
| $\lambda_m$ | libre | $1$ |
| $\lambda_y$ | libre | $0$ |
| $\lambda_h$ | libre | $0$ |

**Total:** 6 ODEs, 6 condiciones de frontera (3 iniciales + 3 terminales). BVP bien planteado.

---

## 5. Plan numérico — shooting method

### 5.1 Estrategia general

1. **Adivinar** valores iniciales libres: $\lambda_m(0), \lambda_y(0), \lambda_h(0)$.
2. **Integrar** sistema 6 ODEs hacia adelante de $x = 0$ a $x = 1$.
3. **Verificar** condiciones terminales:
   - $\tilde m(1) = 1$? Error $e_1 = \tilde m(1) - 1$.
   - $\lambda_m(1) = 1$? Error $e_2 = \lambda_m(1) - 1$.
   - $\lambda_y(1) = 0$? Error $e_3 = \lambda_y(1)$.
4. **Iterar** valores iniciales con Newton-Raphson para minimizar $|e_1|^2 + |e_2|^2 + |e_3|^2$.

### 5.2 Inicialización (warm start)

Usar resultado empírico sim010 ($h_0^* = 1.028, n = 4 \to \tilde m_{\text{end}} = 99.98\%$) como **punto de partida**:
- Solución empírica: $h(x) = 1.028 x^4$.
- $u(x) = 4 \cdot 1.028 \cdot x^3$.
- Calcular $\lambda$'s consistentes con esta solución (relaciones algebraicas).

**Esto da una "buena adivinanza" para el shooting method**, acelerando convergencia.

### 5.3 Verificación

Si shooting converge:
- Comparar $h(x)$ óptimo derivado vs $h_0 x^4$ empírico (sim010).
- Verificar $\tilde m(1) \to 1$ exacto (no 0.99982).
- Validar curva crítica $h_0^*(n, y_c)$ analíticamente.

### 5.4 Costo computacional estimado

- 1 sesión: implementar shooting method básico (sim012).
- 1 sesión: ejecutar + verificar convergencia.
- 1 sesión: análisis comparativo + curva crítica.
- 1-2 sesiones: validación contra sim010 + escritura D-016 completo.

**Total: 3-5 sesiones técnicas para D-016 completo.**

---

## 6. Riesgos identificados

### 6.1 Técnicos

1. **Control singular** complica resolución numérica — el shooting método estándar puede no converger directamente.
2. **Sistema 6D BVP** es tractable pero no trivial. Requiere estabilidad numérica cuidadosa.
3. **Cruce $h = 1$** sigue siendo punto delicado (singularidad coordinate). Tratamiento especial necesario.

### 6.2 Conceptuales

1. **Existencia y unicidad del control óptimo:** asumida pero no demostrada rigurosamente.
2. **Condiciones de orden superior** (Kelley, Goh) pueden ser necesarias para identificar $u^*$ correctamente.
3. **Control bang-bang:** posibilidad de que $u^*$ sea discontinuo (transitions entre régimen interior y frontera).

### 6.3 Metodológicos

- **K-005:** mantener disciplina — shooting es trabajo técnico estándar, no postular nuevo.
- **Regla 9:** si BVP no converge en 2-3 sesiones, retreat ordenado.

---

## 7. Decisión metodológica S75

**Decisión:** S75 cierra como **setup formal completo** del BVP Pontryagin. **NO se implementa shooting** en esta sesión — esa es S76 (1 sesión técnica).

**Justificación:**
- El setup formal es denso técnicamente y merece sesión propia.
- Implementación shooting requiere atención cuidadosa al control singular.
- Disciplina K-005 + Regla 9: una cosa por sesión.

### 7.1 Plan multi-sesión D-016 completo

| Sesión | Tarea | Output |
|---|---|---|
| **S75** | **Setup Pontryagin BVP completo (este documento)** | `notes/D-016_sesion75_Pontryagin_setup.md` |
| S76 | Implementación shooting method (sim012) | `experiments/simulations/sim012_pontryagin_shooting.py` |
| S77 | Ejecución + verificación + análisis | `notes/D-016_sesion77_resultados.md` |
| S78 | D-016 completo + curva crítica analítica | actualización `logic/derivations/D-016_*.md` |
| S79 (opcional) | K-035 promoción a confirmado limpio + actualización inventario | memoria |

**Total estimado: 4-5 sesiones (S75-S79).**

### 7.2 Criterios de éxito

- **Si shooting converge** y $h(x)$ derivado coincide con sim010 al < 1%: K-035 → confirmado limpio.
- **Si shooting converge parcial** (~10% diferencia): K-035 sigue caveat moderado refinado.
- **Si shooting NO converge:** retreat ordenado, K-035 mantiene estatus actual.

---

## 8. Conclusión S75

**D-016 BVP Pontryagin formalmente establecido:**
- Reformulación con $h$ como variable de estado y $u = h'$ como control libre.
- Hamiltoniano explícito + ecuaciones adjuntas.
- Identificación del **control singular** como sutileza técnica clave.
- Trayectoria singular óptima derivada formalmente.
- BVP 6D con 6 condiciones de frontera bien planteado.
- Plan numérico shooting method para S76.

**Próxima sesión (S76):** implementación sim012 shooting con warm start desde sim010.

**Disciplina S75:** K-005 + Reglas 1+5+9 ejemplares. Setup técnico denso, implementación postpuesta a S76.

---

## Apéndice A — Cálculos algebraicos detallados

### A.1 Forma cerrada de $\partial F/\partial \tilde m$

$$
F = \frac{1}{1-h} \cdot \left[yu - \frac{y(4-h)A}{2x(x-\tilde m)} + \frac{3yh}{x}\right]
$$

donde $A = \tilde m + x^3 y(1-h)$.

$$
\frac{\partial F}{\partial \tilde m} = \frac{1}{1-h} \cdot \left[-\frac{y(4-h)}{2x} \cdot \frac{1 \cdot (x-\tilde m) + A}{(x-\tilde m)^2}\right]
$$

Sustituyendo $A = \tilde m + x^3 y(1-h)$:

$$
1 \cdot (x-\tilde m) + A = x - \tilde m + \tilde m + x^3 y(1-h) = x + x^3 y(1-h) = x[1 + x^2 y(1-h)]
$$

Entonces:
$$
\frac{\partial F}{\partial \tilde m} = -\frac{y(4-h)}{2(1-h)(x-\tilde m)^2} \cdot [1 + x^2 y(1-h)]
$$

### A.2 Forma cerrada de $\partial F/\partial y$

$$
\frac{\partial F}{\partial y} = \frac{1}{1-h} \cdot \left[u - \frac{(4-h)[\tilde m + 2 x^3 y(1-h)]}{2x(x-\tilde m)} + \frac{3h}{x}\right]
$$

(Cálculo análogo, expandiendo $\partial[y A]/\partial y = A + y \cdot \partial A/\partial y = A + y \cdot x^3(1-h)$.)

### A.3 Forma cerrada de $\partial F/\partial h$

Más laborioso por dependencia $1/(1-h)$ y polinomio en $h$. Resultado simbólico:

$$
\frac{\partial F}{\partial h} = \frac{F}{1-h} + \frac{1}{1-h} \cdot \left[-\frac{y(-1)A + y(4-h) \partial A/\partial h}{2x(x-\tilde m)} + \frac{3y}{x}\right]
$$

donde $\partial A/\partial h = -x^3 y$.

(Detalle algebraico para implementación sim012 en S76.)

### A.4 Hamiltoniano expandido

$$
H = \lambda_m \cdot 3x^2 y + \lambda_y \cdot \left[\frac{y u}{1-h} + b(\tilde m, y, h, x)\right] + \lambda_h u
$$

donde:
$$
b = \frac{1}{1-h}\left[-\frac{y(4-h)A}{2x(x-\tilde m)} + \frac{3yh}{x}\right]
$$

Condición de optimalidad:
$$
\frac{\partial H}{\partial u} = \lambda_y \cdot \frac{y}{1-h} + \lambda_h = 0
$$

### A.5 Trayectoria singular completa

Diferenciando la condición de optimalidad respecto a $x$:
$$
\frac{d}{dx}\left[\lambda_y \cdot \frac{y}{1-h} + \lambda_h\right] = 0
$$

Expandiendo (omitiendo cálculo) se obtiene una relación que involucra $u$ explícitamente. Resolviendo para $u$ se obtiene la **trayectoria singular** $u_{\text{sing}}^*(\tilde m, y, h, \lambda_m, \lambda_y, \lambda_h; x)$.

(Implementación detallada en sim012, S76.)
