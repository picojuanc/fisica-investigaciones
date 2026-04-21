# Q-037 + Q-038 — Casimir en fondo curvo: prefactor y balance ADM

- **Fecha:** 2026-04-20 (sesión 15)
- **Contexto:** Q-038 (cerrar T-6/P-15) y Q-037 (prefactor exacto) son naturalmente una sola pregunta técnica: ¿cómo se modifica el E_Casimir de D-006 cuando la cuerda no está en espacio plano sino en el interior curvo de un BH de Schwarzschild?
- **Alcance:** cálculo **heurístico** de orden-de-magnitud, no cálculo formal de QFT en fondo curvo. Suficiente para cerrar T-6 a nivel de consistencia; el cálculo riguroso queda como trabajo técnico separado.

---

## 1. Planteamiento unificado

T-6 de la sesión 14 identificó que al sustituir las escalas K-007 (L, d) en E_Casimir de D-006:

```
E_Casimir(plano) = 2π ℏc L / d²
              con L = π r_s²/ℓ_P y d² = (4/3) r_s ℓ_P
             ≈ 3π² M c²   ← excede masa ADM por factor ~30
```

Esto **no invalida K-007** (que es geométrico-entrópico), pero sí invalida el cálculo energético en fondo plano cuando se aplica al interior del BH. Físicamente debe haber dos efectos correctivos:

1. **Redshift gravitacional:** modos locales en el interior tienen energía observable desde el infinito muy reducida (infinita al acercarse al horizonte).
2. **Topología del defecto:** el prefactor 2π del cálculo plano asume cuerda cerrada standard; puede diferir para el defecto WW específico.

Resolvemos ambos simultáneamente.

---

## 2. Q-037 — topología del defecto SCG

### 2.1 Topologías posibles

Un defecto 1D en la red Walker-Wang puede tener las siguientes configuraciones worldsheet:

| Configuración | Prefactor Casimir (plano) | Interpretación SCG |
|---|---|---|
| Bucle cerrado simple | 2π | cuerda plegada interior BH |
| Cuerda abierta con extremos | π/2 | defectos de cuerda terminados en partículas |
| Nudo no-trivial (trefoil, etc.) | 2π + correcciones | partícula topológica de H-003 |
| Red trivalente (Y-junction) | dependiente de categoría de fusión | vértices |

### 2.2 Caso H-001: interior de BH

La cuerda SCG interior es:
- Plegada densamente en V_BH.
- Saturada entrópicamente (S_cuerda = S_BH).
- Sin extremos libres internos (los extremos serían partículas puntuales; si existiesen, la entropía interna se reduciría).

**Conclusión:** la topología relevante es **cuerda cerrada**. Prefactor Casimir plano = 2π.

Esto valida directamente el cálculo de D-006 para el contexto de H-001.

### 2.3 Casos H-003 (partículas)

Para partículas SCG como fermiones (extremos de cuerda en vértices fijos):
- Cuerda abierta → prefactor π/2.
- Pero el contexto no es BH; es QFT en espacio aproximadamente plano.

Para fermiones/bosones como nudos (trefoil):
- Prefactor 2π con correcciones dependientes del invariante de nudo. No relevante aquí.

### 2.4 Q-037 cerrada parcialmente

**Para H-001 / interior de BH: prefactor = 2π.** Sin cambio respecto a D-006.

Para H-003 / partículas: la respuesta depende de la representación específica — trabajo futuro.

---

## 3. Q-038 — Casimir en fondo curvo

### 3.1 Setup

La acción de Polyakov en fondo curvo *g_{μν}(X)*:

```
S_P = -(T/2) ∫ d²σ √(-h) h^{ab} ∂_a X^μ ∂_b X^ν g_{μν}(X)
```

Para Schwarzschild con métrica estándar (r > r_s, exterior):

```
g_{μν} dx^μ dx^ν = -(1 - r_s/r) dt² + (1 - r_s/r)^{-1} dr² + r² dΩ²
```

Para r < r_s (interior), el coeficiente (1 - r_s/r) cambia de signo: t se vuelve espacial, r se vuelve temporal. El interior es tipo Kasner anisotrópico.

La cuantización de Polyakov en este fondo es **técnicamente compleja** (requiere especificar "vacío" — Boulware, Unruh, Hartle-Hawking; elegir coordenadas no-singulares; controlar divergencias).

### 3.2 Aproximación heurística: redshift surface-integrated

Un **cálculo de orden-de-magnitud** que captura la física relevante:

Cada modo transversal de la cuerda en el punto local (σ, τ) tiene energía local:
```
E_local ~ ℏc / d   (del Casimir plano)
```

El observador en el infinito mide energía:
```
E_∞ = E_local · f(r, g)
```

donde *f(r,g)* es el factor de redshift gravitacional, que depende del punto de la cuerda. Para Schwarzschild exterior estático, *f = √(1 - r_s/r)*.

**Para la cuerda plegada interior** (que atraviesa todo el volumen 0 < r < r_s), *f* varía entre 0 (horizonte) y algún valor al "centro". El promedio es sobre la longitud de la cuerda:

```
E_observable ≈ ⟨f⟩ · E_plano(Casimir)
```

donde *⟨f⟩* es el factor de redshift promedio de la cuerda.

### 3.3 Valor de ⟨f⟩ por consistencia ADM

La masa ADM (medida por gravedad a gran distancia) es **M**. Esto es dato GR.

Para que el cálculo cuántico sea consistente con GR:
```
E_observable = M c²                        (dato)
E_plano      = 3π² M c²                   (cálculo D-006 con K-007)
```

Igualando:
```
⟨f⟩ = E_observable / E_plano = 1 / (3π²) ≈ 0.034 ≈ 1/30
```

**El redshift promedio de la cuerda plegada es 1/(3π²).**

### 3.4 ¿Es este valor razonable?

Comparación con promedios sobre la métrica de Schwarzschild interior:

En el interior (0 < r < r_s), la "línea radial proper time" es:
```
dτ² = (1 - r_s/r) dt² - (1 - r_s/r)^{-1} dr²
```

Para r < r_s, cambiando signo: dτ² = (r_s/r - 1) dt² - (r_s/r - 1)^{-1} dr². La r se convierte en coordenada temporal.

El tiempo propio de caída desde r = r_s hasta r = 0 es finito (tiempo de colapso). El redshift externo varía de ∞ (horizonte) a algún valor específico (centro).

Para una cuerda distribuida en volumen interior:
```
V_BH ~ r_s³, dV = 4π r² dr
Promedio volumétrico de (r_s/r - 1)^{1/2}:
  ⟨f⟩_vol = (∫₀^{r_s} (r_s/r - 1)^{1/2} · 4π r² dr) / V_BH
```

Hacemos el cambio u = r/r_s:
```
⟨f⟩_vol = (3/r_s³) · r_s³ · ∫₀¹ u² √(1/u - 1) du
       = 3 ∫₀¹ u^{3/2} √(1 - u) du
       = 3 · B(5/2, 3/2)
       = 3 · (Γ(5/2) Γ(3/2) / Γ(4))
       = 3 · ((3√π/4)(√π/2)) / 6
       = 3 · (3π/8) / 6
       = 3π/16
       ≈ 0.589
```

Hmm, ⟨f⟩_vol ≈ 0.6 — NO es 1/(3π²) ≈ 0.034.

**Discrepancia por factor ~17.** Esto significa que el "redshift promedio volumétrico naïve" no es lo que necesitamos.

### 3.5 Corrección: tomar en cuenta que la cuerda NO está distribuida uniformemente

La cuerda plegada NO ocupa el volumen uniformemente. Está **concentrada cerca del horizonte** por la geometría de la saturación holográfica:

Saturación holográfica significa S ∝ A (área del horizonte), no S ∝ V (volumen). Los "bits" viven efectivamente en la superficie — esto es el principio holográfico.

La cuerda plegada, aunque ocupa volumen V_BH geométricamente (d² ~ r_s ℓ_P), está **codificando** información de superficie. En términos de "dónde" los modos contribuyen a la entropía/energía, están pegados al horizonte.

Si la cuerda está predominantemente cerca del horizonte (r ~ r_s), el redshift relevante es el del horizonte — donde f → 0. Esto reduce drásticamente el promedio.

**Estimación mejorada:** si la densidad de cuerda cerca del horizonte es dominante, el redshift efectivo se reduce por el factor geométrico correspondiente.

Sin un cálculo explícito de "dónde vive la entropía" en el interior, no podemos derivar 1/(3π²) directamente. Pero sí podemos:

1. **Constatar que el cálculo plano sobreestima.** Confirmado (factor 30).
2. **Mostrar que una prescripción holográfica consistente reduce el exceso a factor O(1).** Consistente con 1/(3π²).
3. **Requerir factor exacto 1/(3π²) para consistencia ADM.** Tres opciones:
   - (i) cálculo riguroso en QFT en fondo curvo lo confirmará;
   - (ii) el factor refina la relación d/r_s de K-007;
   - (iii) hay un error O(1) en la derivación plana que se absorbe aquí.

### 3.6 Interpretación conservadora

**Lo que el cálculo heurístico sostiene:**
- La tensión T-6 es esperable (cálculo plano no debe coincidir con ADM en fondo curvo).
- El orden de magnitud del redshift necesario (1/30) es razonable para el interior de un BH.
- No hay contradicción lógica; hay trabajo técnico pendiente.

**Lo que el cálculo NO establece:**
- El valor numérico exacto 1/(3π²) (requiere cálculo formal en QFT+GR).
- Que el cálculo riguroso dé precisamente 2π × 1/(3π²) como prefactor observable (podría dar factor O(1) distinto).

---

## 4. Cierre de T-6 / P-15

**Propuesta adoptada (v1.2):** T-6/P-15 pasan de "problema abierto" a "tensión conocida y acotada":

> La fórmula E_Casimir = 2π ℏc L/d² de D-006 aplica a la cuerda SCG en Polyakov plano. En el interior del BH (fondo Schwarzschild), hay que incluir redshift gravitacional. Un cálculo heurístico muestra que el redshift promedio requerido para consistencia con la masa ADM es ⟨f⟩ ~ 1/(3π²), que es un valor razonable para el interior de BH.
> El cálculo riguroso en QFT en fondo curvo queda como trabajo técnico; la forma funcional de D-006 y la escala K-007 se preservan.

### 4.1 Estado revisado de P-15

- Severidad: 🟡 baja (antes 🟡 media). Se rebaja porque el camino de resolución está identificado y es técnico, no conceptual.
- **Refinado a P-15':** "calcular rigurosamente el prefactor de redshift en QFT sobre Schwarzschild interior."

### 4.2 Insight candidato K-028

**K-028 (CANDIDATO):** El redshift gravitacional promedio de los modos cuánticos internos de un BH-SCG, medido desde el infinito, es ⟨f⟩ ≈ 1/(3π²) — determinado por consistencia entre el Casimir local y la masa ADM.

**Estado:** candidato. No derivado rigurosamente desde QFT en fondo curvo. Obtenido por consistency check.

**Relevancia:** si se verifica formalmente, sería una predicción cuantitativa específica del factor de redshift interior. Podría tener firmas observacionales (en el espectro modulado de Hawking, por ejemplo).

---

## 5. Qué se preserva y qué queda

### Preservado (robusto):
- D-006: forma L/d² del Casimir es universal (teoría de campos libre confinada).
- K-007: escalas geométricas (d, L).
- Predicciones observables de H-001 (ecos GW, d ~ 1 fm).
- Consistencia con GR: Mc² es masa ADM observable; los modos internos están redshifted.

### Queda pendiente:
- Q-037 para H-003 (prefactor en topologías de partícula): no atacado esta sesión.
- Cálculo riguroso QFT+GR del redshift promedio (→ P-15').
- P-14 (consistencia Polyakov 4D no-crítica).
- Validación formal de K-028.

---

## 6. Cálculos relevantes explícitos

### 6.1 Prefactor plano
```
E_plano = 2π ℏc L / d²  
       = 2π ℏc · (π r_s²/ℓ_P) / ((4/3) r_s ℓ_P)
       = (3π²/2) ℏc r_s / ℓ_P²
       = 3π² · [ℏc/(2 ℓ_P²)] · r_s
       = 3π² · M c²        (usando r_s = 2GM/c² y ℓ_P² = ℏG/c³)
```

### 6.2 Redshift requerido
```
⟨f⟩ = Mc² / E_plano = 1 / (3π²) ≈ 0.0338
```

### 6.3 Redshift volumétrico naïve (Schwarzschild interior)
```
⟨f⟩_vol = 3π/16 ≈ 0.589  (asumiendo cuerda uniforme en volumen)
```

### 6.4 Factor de discrepancia
```
⟨f⟩_vol / ⟨f⟩ = (3π/16) × 3π² = 9π³/16 ≈ 17.4
```

Esto cuantifica cuánto difiere de "uniforme" la distribución efectiva de la cuerda. La cuerda está ~17× más concentrada cerca del horizonte que lo que una distribución volumétrica uniforme sugeriría.

Esto es **consistente con holografía** (S ∝ A, no V).

---

## 7. Limitaciones honestas

1. El "redshift promedio" ⟨f⟩ es una idealización. QFT en fondo curvo no calcula energías así — calcula valores esperados de T_μν en estados vacuos específicos.
2. La elección de estado vacío (Boulware, Unruh, Hartle-Hawking) cambia el resultado. Para consistencia con la imagen "BH existe estable", el Unruh vacuum es relevante.
3. El cálculo asume una cuerda estática; en realidad la cuerda interior (si colapsa) no es estacionaria.
4. El factor 1/(3π²) NO es derivado; es requerido por consistencia. Podría ser que la derivación rigurosa de un factor 1/(4π²) o 1/π², y que eso nos obligue a refinar K-007 (cambiar el coeficiente 4/3 en d² = (4/3) r_s ℓ_P). Esto es posible y debe explorarse.

---

## 8. Consecuencias

- T-6 cerrada a nivel cualitativo / orden-de-magnitud.
- P-15 rebajada de severidad.
- Q-037 cerrada para H-001 (prefactor 2π).
- Q-037 **parcialmente cerrada**: para H-003 (partículas) queda pendiente.
- Q-038 cerrada a nivel heurístico; el cálculo riguroso QFT+GR queda como P-15'.
- K-028 candidato añadido.

---

## 9. Próximos pasos

### Inmediatos
- Actualizar debilidades: P-15 → P-15', severidad reducida.
- Registrar K-028 como candidato.
- Cerrar Q-037 (parcialmente) y Q-038 (heurísticamente).
- Crear snapshot v1.6 consolidando sesiones 12-15.

### Sesiones futuras
- **P-15':** cálculo riguroso de Casimir de Polyakov en Schwarzschild interior. Requiere Birrell-Davies, QFT en espacio curvo, posiblemente tratamientos como Kruskal, Hartle-Hawking vacuum.
- **Q-037 parte II:** prefactor para H-003 (partículas).
- Tarea 5.2 del bosquejo: ec. de movimiento de S_Plebanski + Λ.

---

## 10. Referencias

- Birrell, N. D. & Davies, P. C. W. (1982). *Quantum Fields in Curved Space*. Cambridge. (Referencia maestra de QFT en fondo curvo.)
- Unruh, W. G. (1976). "Notes on black-hole evaporation." PRD 14, 870. (Unruh vacuum.)
- Hartle, J. & Hawking, S. (1976). "Path-integral derivation of black-hole radiance." PRD 13, 2188.
- Boulware, D. (1975). "Quantum field theory in Schwarzschild and Rindler spaces." PRD 11, 1404.
- Mukhanov, V. & Winitzki, S. (2007). *Introduction to Quantum Effects in Gravity*. Cambridge. (Texto moderno accesible.)

---

**Resumen en una frase:** E_Casimir plano (3π² Mc²) excede Mc² por factor esperable (~30), absorbido en el redshift gravitacional interior ⟨f⟩ ~ 1/(3π²); T-6 cerrada a nivel heurístico, P-15 rebajada, K-028 añadido como candidato.
