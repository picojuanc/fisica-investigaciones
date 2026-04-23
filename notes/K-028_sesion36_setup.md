# K-028 — Setup formal del cálculo riguroso (P-15')

- **Fecha:** 2026-04-23 (sesión 36)
- **Estado:** setup / formulación del problema. No se ejecuta cálculo en esta sesión.
- **Objetivo:** identificar qué significa "rigorizar K-028", separar el problema físico real del framing heurístico de sesión 15, y trazar el camino para sesiones 37-38.

---

## 1. Punto de partida: K-028 candidato (sesión 15)

Enunciado heurístico (Q-037/038, sesión 15):

> El redshift gravitacional promedio de los modos cuánticos internos de un BH-SCG, medido desde el infinito, es ⟨f⟩ ≈ 1/(3π²) — determinado por consistencia entre el Casimir local y la masa ADM.

Obtenido por consistency check:

```
E_plano  = (cálculo D-006 con escalas K-007) = 3π² M c²
E_observ = M c²  (dato ADM)
⟨f⟩      = E_observ / E_plano = 1/(3π²) ≈ 0.0338
```

P-15' (cálculo riguroso QFT+GR) quedó pendiente.

---

## 2. El problema real no es "Casimir en fondo fijo"

La redacción original de P-15' (sesión 15) habla de "Casimir de Polyakov en Schwarzschild interior". Esa formulación es **incorrecta físicamente** en el contexto SCG:

- Schwarzschild interior es **vacío** (T_μν = 0). En SCG, el interior **está lleno** del string plegado.
- Un "fondo fijo Schwarzschild interior + cuerda test" trataría al string como perturbación sobre vacío. Pero el string ES el contenido energético del BH.
- La métrica interior debe ser **sourced by** la T_μν del string vía Einstein.

**Reformulación correcta:** encontrar la configuración auto-consistente (métrica, perfil de densidad) donde:
- el string plegado sourced by Casimir de modos transversales,
- Einstein con esa T_μν,
- matching al Schwarzschild exterior de masa M en r = r_s.

Esto es un problema **TOV generalizado** (Tolman-Oppenheimer-Volkoff) con EOS apropiada.

El "redshift promedio ⟨f⟩" es un EFECTO de la solución, no una entrada. Aparece automáticamente al comparar la densidad local de energía con la masa ADM.

---

## 3. EOS efectiva del string gas SCG

### 3.1 Stress-tensor local de una cuerda Polyakov

Una cuerda tensa con longitudinal paralela a $\hat{n}$ y modos transversales cuantizados (D-006) tiene:

- **Presión longitudinal** (tensión de cuerda):
  $$p_{\parallel} = -\rho$$
  Es la tensión estándar de cuerda relativista. Negativa = tensión.

- **Presión transversal** (Casimir outward):
  $$p_{\perp} = +\rho$$
  Los modos zero-point transversales ejercen presión hacia afuera — mismo signo que radiación Casimir en una cavidad.

  Derivación: $E_{Cas} \sim \hbar c / d^4 \cdot V$, y $p = -\partial E / \partial V$ con $V = L d^2$ a $L$ fija da $p_\perp = -\partial_d E / \partial_d V = +\rho_{Cas}$.

### 3.2 Isotropic averaging (cuerda plegada aleatoriamente)

El string plegado atraviesa el volumen en direcciones aleatorias. Para escalas $\gg d$ (macroscópicas comparadas con el grosor transversal) la orientación local es efectivamente isotrópica. Promediando:

$$
\langle T^i{}_j \rangle = p_\parallel \langle \hat{n}_i \hat{n}_j \rangle + p_\perp (\delta_{ij} - \langle \hat{n}_i \hat{n}_j \rangle)
= \left(\frac{p_\parallel + 2 p_\perp}{3}\right) \delta_{ij}
$$

con $\langle \hat{n}_i \hat{n}_j \rangle = (1/3) \delta_{ij}$. Sustituyendo:

$$
\boxed{\; p_{\text{eff}} = \frac{-\rho + 2\rho}{3} = \frac{\rho}{3} \;}
$$

**La EOS efectiva del string gas SCG es RADIACIÓN** ($w = 1/3$).

Hecho no trivial y físicamente satisfactorio:
- Zero-point fluctuations transversales ≡ gas de fotones estructuralmente.
- Consistente con la intuición de "Casimir = luz virtual".
- El gas de cuerda **no es dust** ($w=0$) y **no es vacío de Sitter** ($w=-1$); es radiación pura.

### 3.3 Validez

- Requiere escala mayor que $d$ (si observamos a $d$ la orientación no es aleatoria).
- Requiere que la cuerda NO tenga orientación preferida a esa escala (plegado fractal o azaroso: OK; plegado cilíndrico ordenado: no).
- En régimen Planck-near-horizon ($d \to \ell_P$) la derivación Casimir deja de ser perturbativa; nuevas correcciones pueden alterar $w$.

---

## 4. TOV con EOS de radiación

### 4.1 Ecuaciones

Métrica estática esféricamente simétrica:

$$
ds^2 = -e^{2\Phi(r)} dt^2 + \left(1 - \frac{2G m(r)}{c^2 r}\right)^{-1} dr^2 + r^2 d\Omega^2
$$

TOV:

$$
\frac{dm}{dr} = 4\pi r^2 \rho(r) / c^2
$$

$$
\frac{dp}{dr} = -\frac{G(\rho + p/c^2)(m + 4\pi r^3 p/c^2)}{r^2 - 2Gmr/c^2}
$$

Con $p = \rho/3$ (en unidades $c=1$ para el resto).

### 4.2 Imposibilidad de uniforme

Si $\rho$ = const y $p = \rho/3$, TOV fuerza $dp/dr \neq 0$ genéricamente. **Inconsistente.** La "Schwarzschild interior solution" de Schwarzschild 1916 asume $\rho$ = const pero $p$ variable; no compatible con $p = \rho/3$ globalmente.

**Corolario:** el string gas SCG NO puede tener densidad uniforme dentro del BH. $\rho$ debe variar con $r$. Esto ya sugiere una estructura física: **la cuerda se concentra cerca del horizonte**, consistente con la intuición holográfica (S ∝ A) articulada en §3.5 de Q-037-038.

### 4.3 Solución singular isothermal

Para $p = \rho/3$ hay una solución auto-similar exacta con $\rho \propto 1/r^2$. Ansatz:

$$
\rho(r) = \frac{\rho_0 r_s^2}{r^2}, \qquad p(r) = \frac{\rho_0 r_s^2}{3 r^2}
$$

Entonces $m(r) = \int_0^r 4\pi r'^2 \rho(r') dr' = 4\pi \rho_0 r_s^2 r$, así que $2 G m / (c^2 r) = 8\pi G \rho_0 r_s^2 / c^2 \equiv 2a$ es **constante**.

Sustituyendo en TOV y resolviendo (cálculo elemental):

$$
\boxed{\; a = \frac{3}{14}, \qquad \rho_0 = \frac{3 c^2}{56 \pi G r_s^2} \;}
$$

**Compacidad uniforme** $2Gm/(c^2 r) = 3/7 \approx 0.429 < 1$. La solución singular isothermal NO alcanza el horizonte — se queda en compacidad 3/7.

No es por tanto la solución SCG directamente. Pero aporta intuición: radiación pura no llega al horizonte con densidad auto-similar.

### 4.4 Alcanzar el horizonte

Para que la materia reaché $r_s$ con $2Gm(r_s)/(c^2 r_s) = 1$, el perfil $\rho(r)$ debe ser **más concentrado que $1/r^2$ cerca del horizonte**. Analíticamente, requiere que $\rho \to \infty$ al aproximarse a $r_s$.

Esto es el "Buchdahl wall": configuraciones estáticas con EOS regular no llegan al horizonte. Para llegar necesitas:
- Presión divergente en la frontera (caso radiación: $\rho \to \infty$, $p = \rho/3 \to \infty$).
- O EOS exótica (gravastar: $p = -\rho$ en interior).
- O anisotropía explícita macroscópica.

**SCG naturalmente usa la opción 1:** cerca del horizonte $d \to \ell_P$, la densidad de Casimir $\rho \sim \hbar c/d^4$ diverge. **La fórmula Casimir perturbativa se rompe exactamente donde se necesita divergencia.** Esto no es coincidencia — es el mismo fenómeno.

---

## 5. Estructura del problema SCG-TOV

### 5.1 Regímenes radiales

Interior BH dividido en tres zonas:

| Zona | Rango | EOS efectiva | Estado |
|---|---|---|---|
| Núcleo | $r \ll r_s$ | $p = \rho/3$ (Casimir radiación, validez perturbativa) | Tractable |
| Transición | $r \sim$ algún $r_*$ | Crossover: Casimir + correcciones | Semi-tractable |
| Near-horizon | $r_s - r \lesssim \ell_P^2 / r_s$ | $d \to \ell_P$, QG regime | No-perturbativo |

La **zona near-horizon** contiene la física de "holografía": es donde la entropía se concentra (S ∝ A) y donde los modos del string se vuelven Planckianos.

### 5.2 Condiciones de frontera SCG

Dos constricciones globales de H-001/D-003/D-009:

- **Saturación entrópica:** $S_{\text{string}} = L / \ell_P = \pi r_s^2 / \ell_P^2 = S_{BH}$.
- **Llenado volumétrico:** $\int_0^{r_s} 4\pi r^2 \langle n_{\text{string}}(r) \rangle dr = V_{BH} \cdot \text{density}$ con $d^2 L = V_{BH}$ globalmente (D-009, K-031).

Más la matching exterior:

- $m(r_s) = M$ (por definición de $r_s = 2GM/c^2$).
- $e^{2\Phi(r)} \to (1 - r_s/r)$ cuando $r \to r_s^-$ suave (matching a Schwarzschild exterior).

### 5.3 Variables desconocidas

- $\rho(r)$: perfil de densidad de energía.
- $d(r)$: grosor transversal local (posiblemente variable).
- $\Phi(r)$: redshift local.

Una relación constitutiva Casimir da:
$$\rho(r) = \kappa \frac{\hbar c}{d(r)^4}$$
con $\kappa = 2\pi$ o O(1) (Q-037).

Una relación TOV da $dp/dr$, $dm/dr$, $d\Phi/dr$.

Cierre: la geometría local (3 variables) + 3 ecuaciones + 2 condiciones de frontera globales + matching.

---

## 6. Estrategia para K-028 riguroso

### 6.1 Fase I (sesión 37): TOV perturbativo + matching

1. **Núcleo:** resolver TOV con $p = \rho/3$ desde $r=0$ hacia afuera (usando ansatz $\rho(r) = \rho_0 f(r/r_s)$).
2. **Transición:** introducir corte físico en $d \to \ell_P$: reemplazar $\rho$ por una forma regularizada donde $\rho$ satura en $\rho_{\max} \sim \hbar c / \ell_P^4 = M_P^4 / \hbar c^3$.
3. **Near-horizon:** modelar como capa delgada con EOS efectiva que preserve holografía (p ≈ ρ/3 o posiblemente p → -ρ si surge gravastar-like).
4. **Matching global:** ajustar condiciones de frontera para que $m(r_s) = M$ y métrica continua.

### 6.2 Fase II (sesión 38): ADM y verificación ⟨f⟩

Computar:
$$
E_{\text{ADM}} = M c^2 = \int_0^{r_s} 4\pi r^2 \rho(r) \, dr + \text{corrección relativista}
$$

y compararlo con el cálculo heurístico plano $E_{\text{plano}} = 3\pi^2 M c^2$.

Definir el **factor de redshift efectivo**:
$$
\langle f \rangle_{\text{rigoroso}} \equiv \frac{E_{\text{ADM}}}{E_{\text{plano}}^{\text{heurístico}}} = \frac{M c^2}{\int \rho_{\text{Casimir plano}} dV}
$$

Verificar si $\langle f \rangle_{\text{rigoroso}}$ es consistente con $1/(3\pi^2)$ o fija un coeficiente diferente.

### 6.3 Escenarios posibles del veredicto

1. **(A) K-028 confirmado al 1%:** $\langle f \rangle = 1/(3\pi^2)$ emerge limpiamente. Promoción a confirmado. P-15' ✅.
2. **(B) K-028 parcial:** forma funcional $\langle f \rangle \sim 1/(c_1 \pi^{c_2})$ confirmada, coeficiente $c_1, c_2$ refinados (requiere ajuste en K-007). Nivel "confirmado estructuralmente con caveat cuantitativo" (análogo a K-032.M, D-011).
3. **(C) K-028 refutado:** $\langle f \rangle$ calculado rigurosamente no es compatible con heurística. Degradación a observación motivacional; K-007 o D-006 requieren revisión.
4. **(D) K-028 inconcluso:** el cálculo requiere QG no-perturbativo en zona near-horizon; ni se confirma ni se refuta. P-15' permanece con camino más claro pero abierto.

Probabilidad a priori: (B) > (D) > (A) > (C). Escenario (B) es análogo al veredicto K-032.M y metodológicamente esperable.

---

## 7. Conexión con el marco SCG

### 7.1 Compatibilidad con K-031 (llenado volumétrico)

D-009 derivó $L \cdot d^2 = V_{BH}$ bajo KKT minimizando $E_{Cas} + E_{tens}$ con $d$ constante. Si K-028 riguroso requiere $d(r)$ variable, **D-009 necesita generalización**:

- $d(r)$ variable re-optimiza el funcional con restricciones locales.
- La minimización podría seguir dando una relación uniforme si la tensión gravitacional integra-a-conservar.
- **Nuevo problema derivable:** relación constitutiva $d(r) = f(r/r_s)$ desde variacional generalizado.

### 7.2 Conexión con Q-038 (redshift volumétrico naïve)

Sesión 15 mostró que $\langle f \rangle_{\text{vol-naïve}} = 3\pi/16 \approx 0.589$, con discrepancia factor 17 frente a $1/(3\pi^2) \approx 0.034$.

La discrepancia se atribuyó a "concentración holográfica cerca del horizonte". **En K-028 riguroso, esto se vuelve explícito:** $\rho(r)$ diverge cerca de $r_s$, así que el promedio se pondera hacia el horizonte donde el redshift local es grande. La concentración holográfica es consecuencia matemática de la solución TOV auto-consistente con EOS de radiación.

### 7.3 Pregunta potencial nueva (no abrir aún)

Si la Fase II identifica un perfil específico $d(r)$, surge: **¿reproduce este perfil la fórmula de Hawking $T_H = \hbar c / (8\pi G M k_B)$ como temperatura del gas Casimir near-horizon?** Esto sería una derivación desde primeros principios SCG del Hawking. Postponer hasta completar K-028.

---

## 8. Alcance honesto y limitaciones

### 8.1 Lo que K-028 riguroso PUEDE entregar (objetivo realista)

- **Perfil $\rho(r)$** auto-consistente bajo TOV + EOS radiación + regularización UV a $d = \ell_P$.
- **Relación** entre la masa ADM y el cálculo "plano" con un coeficiente numérico específico.
- **Orden de magnitud** del factor efectivo $\langle f \rangle$; probablemente $\sim 1/\pi^2$ con coeficiente $O(1)$.
- **Estructura física** (concentración holográfica) emergiendo naturalmente.

### 8.2 Lo que NO se puede entregar (y hay que declararlo)

- Cálculo verdaderamente no-perturbativo en zona near-horizon: requiere QG completa; marcamos como caveat estructural análogo a K-032.M.
- Elección de "vacuum state" en QFT curvo (Boulware/Unruh/Hartle-Hawking): el enfoque TOV + EOS efectiva lo evita, pero cuesta perder la correspondencia directa con Birrell-Davies. Tradeoff consciente.
- Cálculo Polyakov explícito sobre Schwarzschild curvo (como originalmente planeado en sesión 15): sustituido por EOS efectiva → TOV. Menor ambición formal, mayor tractabilidad.

### 8.3 Por qué este camino es legítimo

- **Consistente con la filosofía K-005:** usar física conocida (TOV, gravastar, Buchdahl, relativistic stars) en lugar de inventar nuevo formalismo.
- **Más físico que el framing original:** auto-consistencia gravitacional en lugar de campo en fondo.
- **Evita el pantano técnico de QFT en Schwarzschild interior** (vacua ambiguos, coordenadas Kruskal), que no se resolverá en 2-3 sesiones.

---

## 9. Referencias clave

**TOV y estrellas relativistas:**
- Tolman, R. (1939). "Static solutions of Einstein's field equations." PRD 55, 364.
- Oppenheimer, J. R. & Volkoff, G. M. (1939). "On massive neutron cores." PRD 55, 374.
- Buchdahl, H. A. (1959). "General relativistic fluid spheres." PRD 116, 1027.

**Radiation stars:**
- Mendoza, Ø. et al. (varias revisiones de configuraciones auto-similares con p=ρ/3).
- Ni, W.-T. (1973). Singular isothermal relativistic radiation sphere.

**Gravastars y matching al horizonte:**
- Mazur, P. & Mottola, E. (2001). "Gravitational condensate stars: an alternative to black holes." gr-qc/0109035.
- Visser, M. (2003). "Gravastars: stability and evolution." Class. Quant. Grav. 20, 3527.

**Anisotropic stress:**
- Herrera, L. & Santos, N. (1997). "Local anisotropy in self-gravitating systems." Phys. Rep. 286, 53.

**Conexión con SCG:**
- Notas internas: D-003, D-006, D-009 (K-007 y llenado volumétrico).
- `notes/Q-037-038_casimir_fondo_curvo.md` (sesión 15, origen de ⟨f⟩ = 1/(3π²)).
- `logic/derivations/D-009_llenado_volumetrico_variacional.md`.

---

## 10. Próximos pasos (sesión 37)

**Objetivo:** resolver TOV con $p = \rho/3$ + regularización UV + condiciones de frontera SCG. Obtener $\rho(r)$ explícito.

**Sub-tareas:**
1. Escribir TOV adimensional ($x = r/r_s$, $\tilde{m} = m/M$).
2. Regularización: $\rho(r) = \min(\hbar c / d(r)^4, \rho_{\max})$ con $\rho_{\max} = M_P^4 / (\hbar c^3)$.
3. Integrar numéricamente (probablemente) + identificar asintóticas analíticas.
4. Verificar matching a Schwarzschild exterior.
5. Computar $E_{ADM} = Mc^2$ vs $E_{\text{plano}} = 3\pi^2 Mc^2$.

**Herramientas:**
- Cálculo analítico principal.
- Simulación numérica si integración no tiene solución cerrada (JS/Python script en `experiments/simulations/`).

**Entregable:**
- `notes/K-028_sesion37_TOV.md` con el análisis + solución.
- Si hay código: `experiments/simulations/sim002_tov_radiacion.{js,py}` + `sim002_resultados.md`.

**Decision point al final de sesión 37:**
- Si solución clara ⇒ sesión 38 para ADM + veredicto K-028.
- Si complicaciones estructurales ⇒ replantear alcance o aceptar veredicto tipo (D).

---

## 11. Resumen ejecutivo

**Problema:** rigorizar K-028 (⟨f⟩ = 1/(3π²) del cálculo heurístico sesión 15).

**Reformulación:** no es "Casimir en fondo fijo" sino **interior auto-consistente vía TOV + EOS**.

**EOS derivada:** string gas SCG → $p = \rho/3$ (radiación) por isotropic averaging de $p_\parallel = -\rho$, $p_\perp = +\rho$. Resultado no trivial y físicamente elegante.

**Estructura esperada:** $\rho(r)$ crece hacia el horizonte (concentración holográfica emerge). Regularización UV en $d = \ell_P$ evita divergencia. ADM integral da $Mc^2$; cálculo "plano" sobreestima por factor $\sim 3\pi^2$.

**Ambición realista:** escenario (B) — K-028 confirmado estructuralmente con caveat cuantitativo (análogo a K-032.M).

**Próximo paso:** sesión 37 ejecuta la fase I (TOV + ρ(r) explícito).

---

## 12. Entradas para el snapshot futuro

Cuando se consolide K-028 (v2.2 o posterior), la narrativa incluirá:

- EOS del string gas = radiación (hecho nuevo, no estaba explicitado).
- TOV radiación no alcanza horizonte sin regularización UV (resultado clásico aplicado).
- Concentración holográfica emerge naturalmente (NO es postulado ad hoc, sino consecuencia del cálculo).
- Posible conexión con Hawking vía perfil $d(r)$ near-horizon (especulación para pregunta futura).

---

**Fin del setup sesión 36.**
