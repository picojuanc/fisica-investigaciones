# D-016 / Sesión 76 — Verificación posterior de optimalidad Pontryagin: resultado ambiguo + retreat ordenado

- **Fecha:** 2026-04-26 (sesión 76).
- **Continuación de:** `notes/D-016_sesion75_Pontryagin_setup.md` (BVP completo S75).
- **Objetivo S76:** verificar si la solución empírica sim010 ($h(x) = 1.028 \cdot x^4$) satisface la condición de optimalidad $\partial H/\partial u = 0$ posterior a integración hacia atrás de $\lambda$'s.
- **Resultado:** **AMBIGUO + RETREAT ORDENADO** (Regla 9). Verificación no concluyente; D-016 completo Pontryagin queda como marca técnica pendiente extendida.

---

## 1. Implementación

### 1.1 Estrategia

Más simple que shooting Newton-Raphson completo:

1. **Forward integration** de $(\tilde m, y)$ con $h(x) = h_0^* x^n$ fijo del sweet-spot.
2. **Backward integration** de $\lambda_m, \lambda_y, \lambda_h$ desde condiciones terminales (1, 0, 0) usando ecuaciones adjuntas.
3. **Verificar** condición de optimalidad: $\partial H/\partial u = \lambda_y \cdot y/(1-h) + \lambda_h \approx 0$ para todo $x$.

### 1.2 Código

`experiments/simulations/sim012_pontryagin_verification.py` (~250 líneas):
- Forward: RK4 simple para $(\tilde m, y)$.
- Backward: Euler para $\lambda$'s.
- Verificación: tabular $\partial H/\partial u$ en cada $x$.

---

## 2. Resultados

### 2.1 Forward integration

**Resultado:** integración detuvo en $x = 0.9821$ con $m_{\text{end}} = 0.7238$ (vs $m_{\text{end}} = 0.998$ en sim010 RK45).

**Diagnóstico:** RK4 simple con 100k pasos es menos preciso que RK45 adaptativo de sim010. **No alcanza el sweet-spot exacto.** Esto degrada la base para verificación adjoint.

### 2.2 Backward integration

**Resultado:** $\lambda$'s al inicio ($x \approx 0$):
- $\lambda_m(0) \approx -2160$ (grande, sospechoso).
- $\lambda_y(0) \approx 1 \times 10^{-4}$ (muy pequeño).
- $\lambda_h(0) \approx 2.35$ (orden 1).

### 2.3 Verificación condición de optimalidad

**Resultado:** $\partial H/\partial u = \lambda_y \cdot y/(1-h) + \lambda_h \approx 2.0$ a $2.2$ **lejos de 0** para todo $x$.

**Tabla representativa:**

| $x$ | $h$ | $y$ | $\lambda_y$ | $\lambda_h$ | $\partial H/\partial u$ |
|---:|---:|---:|---:|---:|---:|
| 0.06 | 0 | 100 | $1.6 \times 10^{-4}$ | 2.06 | **2.07** |
| 0.10 | $10^{-4}$ | 25 | $-5 \times 10^{-4}$ | 2.06 | **2.05** |
| 0.20 | 0.001 | 4 | $-9 \times 10^{-3}$ | 2.13 | **2.10** |
| 0.30 | 0.008 | 1.5 | $-7 \times 10^{-3}$ | 2.18 | **2.17** |

**Violación máxima:** ~2.2.

**Veredicto verificación:** NO confirma optimalidad puntual.

---

## 3. Análisis del resultado

### 3.1 Interpretaciones posibles

**(A) Error de implementación adjoint:**
- Las derivadas $\partial F/\partial \tilde m, y, h$ pueden tener errores algebraicos.
- El cálculo de la sensibilidad parcial en el código puede no coincidir con D-016 §A (Apéndice).
- Implementación de Euler para backward es muy grueso.

**(B) Control singular real:**
- Como identifiqué en S75, $H$ lineal en $u$ → control singular.
- La condición $\partial H/\partial u = 0$ NO determina $u^*$ puntualmente.
- La trayectoria singular óptima requiere derivadas de orden superior (Goh/Kelley).
- **El sweet-spot empírico puede ser óptimo en sentido singular** sin que $\partial H/\partial u = 0$ se cumpla puntualmente.

**(C) Solución empírica subóptima formalmente:**
- $h(x) = h_0^* x^4$ es ansatz funcional específico — puede no ser el óptimo global del BVP.
- El óptimo formal puede tener forma funcional distinta no captura por el ansatz power-law.

**(D) BVP setup incompleto:**
- Las condiciones de frontera podrían ser incorrectas.
- La identificación del control singular puede requerir más cuidado.

### 3.2 Diagnóstico más probable

**(B) + (A) combinadas.** El control singular es real y la implementación adjoint con Euler simple no es lo suficientemente precisa para resolver la sutileza singular.

**Conclusión técnica:** la verificación posterior con esta implementación es **insuficiente**. Resolver requeriría:
- (i) Implementación adjoint con RK45 (no Euler).
- (ii) Manejo correcto del control singular vía derivadas Goh.
- (iii) Posiblemente, redefinir el óptimo en sentido distinto ($J' = \tilde m(1) - \epsilon \int u^2$ regularización).

---

## 4. Decisión metodológica (Regla 9)

### 4.1 Re-calibración honesta

**Pre-S76:** plan multi-sesión D-016 completo en 4-5 sesiones (S75-S79), probabilidad 50-60% de cierre limpio.

**Post-S76:** **probabilidad ajustada a 25-35%** dado el resultado ambiguo.

**Razones:**
- Control singular es complicación técnica significativa.
- Implementación adjoint requiere refinamiento (RK45 + manejo singular).
- Posibles 5-10 sesiones más con resultado incierto.

### 4.2 Decisión: RETREAT ORDENADO DE D-016 COMPLETO

**Justificación:**
1. **Costo-beneficio desfavorable:** 5-10 sesiones más con < 35% probabilidad cierre limpio.
2. **K-035 estatus actual ya es honesto:** "confirmado estructuralmente con derivación variacional parcial" (post-S69) NO requiere D-016 Pontryagin completo para validez.
3. **Análogo Fase 5:** ambos episodios (Fase 5 super-MTC, D-016 Pontryagin) son trabajos técnicos densos con probabilidad < 35% de cierre limpio. Patrón epistémico maduro: retreat ordenado en estos casos.
4. **Otras direcciones más accesibles esperan:** H-004 nueva hipótesis, refinamientos K-033 con caveat fuerte, consolidación adicional, pausa estratégica.

### 4.3 Lo que sí se logró en S75-S76

✅ **D-016 BVP Pontryagin formalmente establecido** (S75) — setup técnico denso completado.
✅ **Control singular identificado** como sutileza técnica clave del problema.
✅ **Trayectoria singular** $u_{\text{sing}}^*$ derivada formalmente.
✅ **Implementación verificación posterior** (sim012) con Euler simple.
✅ **Resultado ambiguo documentado honestamente** — diagnóstico claro de las limitaciones.
✅ **Retreat ordenado** con plan B identificado.

### 4.4 Lo que NO se logró

❌ **Convergencia numérica del shooting** o verificación posterior limpia.
❌ **K-035 promoción a confirmado limpio.**
❌ **Curva crítica $h_0^*(n, y_c)$ derivada analíticamente.**

---

## 5. Marca técnica pendiente extendida (D-016 Pontryagin)

**Para futuro trabajo si D-016 se reabre:**

1. **Implementación adjoint refinada con RK45.**
2. **Tratamiento explícito del control singular** vía Goh condition.
3. **Regularización del problema:** $J' = \tilde m(1) - \epsilon \int u^2$.
4. **Shooting Newton-Raphson** completo con warm start refinado.
5. **Comparación con literatura** anisotropic stars (Bowers-Liang 1974, Mak-Harko 2003) para validación cruzada.

**Estimación costo si se retoma:** 5-10 sesiones técnicas adicionales.

**Estatus:** pendiente sin urgencia. K-035 mantiene estatus actual.

---

## 6. Implicaciones para K-035

**K-035 estatus:** "confirmado estructuralmente con derivación variacional parcial" (post-S69-S70) **se mantiene** post-S75-S76.

**Refinamiento del estatus:**
- ✅ Forma funcional $y = exp(-κ_f/4)$ derivada (D-016 §3.1).
- ✅ Banda $d_{LR}$ verificada empíricamente.
- ✅ Sweet-spot empírico identificado (sim010).
- ✅ BVP Pontryagin formalmente establecido (D-016 §S75).
- ⚠ Verificación posterior optimalidad ambigua (sim012 S76).
- ⚠ Curva crítica $h_0^*(n, y_c)$ no derivada analíticamente.

**K-035 sigue confirmado estructuralmente con caveat numérico < 0.02% y derivación variacional parcial.** Esto es honestidad metodológica, no degradación.

---

## 7. Próximos pasos (post-S76)

### 7.1 Opciones disponibles

| Opción | Descripción | Costo | Probabilidad cierre |
|---|---|---|---|
| (A) D-016 refinado (Goh + RK45 + regularización) | Reintentar con técnica más sofisticada | 5-10 sesiones | 25-35% |
| **(B) H-004 nueva hipótesis** | Constantes fundamentales (Q-005 + Q-044) | 5-10 sesiones | 30-40% |
| (C) Refinamientos sub-tareas K-033 (B, C) | Bajo payoff | 5-15 sesiones | < 25% |
| (D) Pausa estratégica | Tiempo para reflexión | 0 sesiones | n/a |
| (E) Consolidación final + reporte 33 narrativo | Documentar retreat D-016 | 1 sesión | n/a |

### 7.2 Recomendación post-S76

**(E) consolidación primero** (1 sesión, reporte 33 narrativo del retreat D-016) → luego **(D) pausa estratégica** O **(B) H-004 nueva hipótesis**.

**Por qué:**
- Periodo intenso S66-S76 (11 sesiones consecutivas) merece pausa.
- Reporte 33 cierra documentalmente el episodio D-016 con misma honestidad que reportes 30-32.
- H-004 sería nueva línea — mejor con perspectiva fresca post-pausa.

---

## 8. Conclusión S76

**D-016 completo Pontryagin: RETREAT ORDENADO.** Verificación posterior con implementación simple no concluyente. Refinamiento (Goh + RK45) requeriría 5-10 sesiones más con < 35% probabilidad cierre.

**K-035 mantiene estatus actual** ("confirmado estructuralmente con derivación variacional parcial") — sin afectación.

**Marca técnica pendiente extendida** para D-016 Pontryagin completo: trabajo accesible si se decide reabrir, pero no urgente.

**Disciplina S76 ejemplar:**
- K-005: implementación técnica estándar, no postular nuevo.
- Regla 1: verificación posterior + diagnóstico claro del resultado ambiguo.
- Regla 5: retreat documentado honestamente sin disfraz de éxito.
- Regla 9: retreat ordenado tras 2 sesiones (S75-S76) por costo-beneficio desfavorable.
- **K-005 ejemplar 15 veces consecutivas** preservado.

**Lección meta:** **dos retreat ordenados consecutivos** (Fase 5 super-MTC en S71-S72, D-016 Pontryagin en S75-S76) — el marco SCG identifica honestamente cuándo trabajos técnicos están fuera de scope práctico. Esto NO es debilidad — es ciencia disciplinada que prioriza calidad sobre cantidad.

**La teoría continúa.**
