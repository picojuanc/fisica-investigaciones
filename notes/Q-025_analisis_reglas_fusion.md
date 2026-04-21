# Análisis de Q-025: reglas de fusión de la red SCG

**Fecha:** 2026-04-17 (sesión 8)
**Resultado:** derivación parcial en D-004. U(1) derivado, Z₃ derivado, SU(2) motivado, SU(3) abierto.

---

## Resumen ejecutivo

La pregunta Q-025 se atacó razonando desde primeros principios sobre la geometría de un vértice trivalente de cuerdas SCG en D=3. Los resultados:

### Derivado
1. **U(1)** emerge de la conservación del momento angular transversal (2 modos en D=3, simetría SO(2))
2. **Z₃** emerge de la ruptura SO(2) → Z₃ por la trivalencia del vértice en D=3
3. La **cuantización de la carga en 1/3** es consecuencia directa de Z₃

### Motivado (no derivado, pero con precedente fuerte)
4. **SU(2)** como grupo gauge gravitacional, vía la formulación de Ashtekar de GR (= estructura de redes de espín en LQG)

### Abierto
5. **SU(3) completo** — solo tenemos su centro Z₃. La extensión continua es Q-026.

---

## ¿Por qué es significativo el resultado Z₃?

La cuantización de la carga eléctrica en unidades de 1/3 es uno de los hechos empíricos más básicos del Modelo Estándar, y **no tiene explicación dentro del SM**. El SM simplemente postula las cargas de quarks y leptones.

En el marco SCG, la cuantización en 1/3 **se deriva**:
```
D = 3 (H-002)
    → vértices genéricos son trivalentes
        → SO(2)_transversal se rompe a Z₃
            → cargas se clasifican mod 3
                → Q = 0, ±1/3, ±2/3, ±1
```

Cada paso es geometría + mecánica cuántica. No hay postulados nuevos.

### Analogía iluminadora

Es como la cuantización del momento angular en QM: L_z = mℏ con m ∈ ℤ. Nadie "postula" que m es entero — emerge de la condición de periodicidad ψ(φ+2π) = ψ(φ). Del mismo modo, la cuantización en 1/3 emerge de la periodicidad Z₃ del vértice trivalente.

---

## Ruta hacia SU(3): tres posibilidades abiertas

### Ruta A: extensión de Z₃ por deformaciones continuas del vértice
Los 3 "canales" del vértice definen 3 estados cuánticos. Las rotaciones entre ellos formarían U(3). Con conservación de número total → SU(3) × U(1). El U(1) extra sería el número bariónico.
- **Problema:** Schur's lemma bloquea si SO(3) actúa irreduciblemente.
- **Posible escape:** si los 3 canales NO son equivalentes bajo SO(3) (por ejemplo, si tienen distintos espines j), la representación se descompone y deja espacio para SU(3).

### Ruta B: de Z₃ discreta a SU(3) por condensación de enlaces
En una red densa de cuerdas SCG, los enlaces (Borromean-type) de 3 cuerdas podrían condensar, generando una simetría continua emergente. Análogo: en un cristal, las simetrías discretas del retículo dan lugar a fonones que tienen simetría continua emergente (Goldstone).
- **Atractivo:** no requiere nuevo axioma — es un fenómeno de fase.
- **Problema:** requiere modelar la dinámica de la red SCG (más allá de un solo vértice).

### Ruta C: SU(3) como sector no-perturbativo
Quizás SU(3) no emerge del análisis perturbativo de un solo vértice, sino de la topología global de la red (instantones, configuraciones topológicas de la red). Análogo: la masa del protón viene mayormente de efectos no-perturbativos de QCD.
- **Problema:** extremadamente difícil de calcular.

---

## El cuadro completo comparado con el Modelo Estándar

| Factor SM | Significado | Origen en SCG | Estado |
|---|---|---|---|
| SU(3)_c | Color (quarks) | Z₃ derivado; SU(3) abierto | Parcial |
| SU(2)_L | Isospín débil | Conexión gravitacional (Ashtekar) | Motivado |
| U(1)_Y | Hipercarga | Momento angular transversal | Derivado |
| Higgs | Ruptura electrodébil | ¿Condensado de la red SCG? | Sin explorar |
| 3 generaciones | Repetición de familias | Sin mecanismo convincente | Abierto |
| Masas de fermiones | Jerarquía de Yukawa | Sin mecanismo | Abierto |

### Lo que explica (nuevo respecto al SM):
- **Por qué carga en 1/3:** D=3 → trivalencia → Z₃
- **Por qué existe simetría gauge:** defectos topológicos en la red SCG (Levin-Wen)
- **Por qué violación de paridad:** Chern-Simons inherentemente viola P
- **Por qué gravedad + gauge coexisten:** ambas son aspectos de la misma red SCG

### Lo que NO explica (aún):
- El grupo SU(3) completo (solo Z₃)
- El mecanismo de Higgs
- Las 3 generaciones
- Los valores numéricos de masas y acoplamientos
- Los niveles de Chern-Simons k

---

## Nuevos insights y preguntas

### Insights
- **K-014:** U(1) gauge emerge del momento angular transversal de cuerdas SCG en D=3
- **K-015:** La cuantización de la carga en 1/3 emerge de la trivalencia de vértices en D=3 (ruptura SO(2) → Z₃)
- **K-016:** 2 de 3 factores del grupo gauge del SM (U(1) y SU(2)) emergen de la geometría SCG; el tercero (SU(3)) tiene su centro Z₃ derivado

### Preguntas nuevas
- **Q-026:** ¿Cómo se extiende Z₃ a SU(3) completo? (Rutas A, B, C arriba)
- **Q-027:** ¿Cuáles son los niveles de Chern-Simons k para cada factor?
- **Q-028:** ¿La ruptura de simetría electrodébil (Higgs) corresponde a un cambio de fase de la red SCG?
