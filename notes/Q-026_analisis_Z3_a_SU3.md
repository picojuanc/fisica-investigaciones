# Análisis de Q-026: de Z₃ a SU(3) completo

**Fecha:** 2026-04-17 (sesión 8)
**Resultado:** resolución conceptual por 5 argumentos convergentes. El más fuerte: Z₃ + quiralidad gravitacional → SU(3)₁ por unicidad matemática.

---

## 1. Replanteamiento del problema

D-004 derivó Z₃ de la trivalencia del vértice SCG. La pregunta Q-026 es: ¿cómo pasa Z₃ → SU(3)?

La respuesta NO es "extender Z₃ a SU(3)" algebraicamente. Es reconocer que **Z₃ con la estructura de trenzado correcta YA ES SU(3)₁** — la teoría de Chern-Simons SU(3) en su nivel mínimo.

---

## 2. Hecho matemático: SU(3) Chern-Simons a nivel k=1

### Representaciones integrables
Para SU(3) a nivel k=1, las representaciones permitidas son aquellas con λ₁+λ₂ ≤ 1:
- **(0,0):** trivial (vacío) → trialidad 0
- **(1,0):** fundamental **3** → trialidad 1
- **(0,1):** anti-fundamental **3̄** → trialidad 2

**Solo 3 anyones.** Exactamente como Z₃.

### Reglas de fusión
```
3 × 3 = 3̄
3 × 3̄ = 1
3̄ × 3̄ = 3
```
Isomorfas a la adición en Z₃. **Fusión abeliana.**

### Espines topológicos (quiralidad)
Los pesos conformes (de la teoría WZW asociada) son:
```
h(1) = 0           → θ(1) = 1
h(3) = 1/3         → θ(3) = e^{2πi/3}
h(3̄) = 1/3         → θ(3̄) = e^{2πi/3}
```

La carga central quiral es **c₋ = 2**. La teoría es **quiral** (no invariante bajo reversión temporal).

### Diferencia con Z₃ Dijkgraaf-Witten
- Z₃ DW (no quiral): **9 anyones** (cargas + flujos), c₋ = 0
- SU(3)₁ (quiral): **3 anyones** (solo cargas), c₋ = 2

**No son la misma teoría.** Tienen las mismas reglas de fusión pero distinto trenzado y distinta quiralidad.

---

## 3. Clasificación de órdenes topológicos con fusión Z₃

Las formas cuadráticas sobre Z₃ clasifican los órdenes topológicos abelianos con fusión Z₃:

| Forma | h(1) | h(2) | c₋ mod 8 | Identificación |
|---|---|---|---|---|
| q(a) = a²/3 | 1/3 | 1/3 | 2 | **SU(3)₁** |
| q(a) = 2a²/3 | 2/3 | 2/3 | -2 | **SU(3)₁*** (conjugado temporal) |
| q = 0 (trivial) | 0 | 0 | 0 | Z₃ DW (no quiral) |

**Resultado:** existen exactamente **2 órdenes topológicos quirales** con fusión Z₃. Son SU(3)₁ y su conjugado, relacionados por inversión temporal (paridad).

La elección entre ellos la determina la **orientación del espacio-tiempo** (signo del término de Chern-Simons).

---

## 4. El argumento central: quiralidad gravitacional → SU(3)₁

### Paso 1: La red SCG tiene un término de Chern-Simons gravitacional

En la formulación de Ashtekar de GR en 3+1D, la conexión gravitacional es SU(2). En una rebanada espacial, el estado cuántico tiene contribución del término de Chern-Simons:
```
S_CS^{grav} = (k/4π) ∫ Tr(A ∧ dA + 2/3 A ∧ A ∧ A)
```

Este término es **quiral**: cambia de signo bajo paridad. La teoría espacial resultante es un orden topológico quiral.

### Paso 2: La Z₃ del vértice vive en un fondo quiral

La Z₃ derivada de la trivalencia (D-004) no vive en el vacío — vive **dentro** de una red SCG que tiene estructura gravitacional quiral (Chern-Simons). El orden topológico del sector Z₃ hereda la quiralidad del fondo gravitacional.

### Paso 3: Z₃ quiral = SU(3)₁ (unicidad)

Por la clasificación de §3, solo hay 2 órdenes topológicos quirales con fusión Z₃: SU(3)₁ y su conjugado. La elección la fija la orientación.

**Conclusión:**
```
Z₃ (de trivalencia, D-004) + quiralidad (de Ashtekar/CS gravitacional)
    → SU(3)₁ por unicidad matemática
```

### Nivel de confianza
- Z₃ de trivalencia: **DERIVADO** (D-004)
- Quiralidad de la teoría gravitacional: **MOTIVADO** (Ashtekar/LQG, no derivado de A-003)
- Z₃ quiral = SU(3)₁: **TEOREMA** (clasificación de órdenes topológicos abelianos)

---

## 5. De SU(3)₁ a SU(3) completo: el flujo de nivel

### El problema
SU(3)₁ tiene solo 3 anyones (abelianos). El QCD del SM tiene representaciones no-abelianas (adjunta 8, etc.) que requieren k ≥ 2.

### La solución: desplazamiento del nivel por integración de modos masivos

En 3+1D, integrar un fermión de Dirac masivo en la representación fundamental de SU(N) desplaza el nivel de CS:
```
Δk = ±½  (por fermión de Dirac fundamental, normalización estándar)
```

La red SCG tiene **muchos modos vibracionales a escala Planck** (de A-003). Cada modo que se "integra" al bajar de energía contribuye al desplazamiento:
```
k_eff(E) = k_bare + Σ_f ½ · sign(m_f) · T(R_f)
```

### El flujo de renormalización
```
E = M_Planck: k_eff = 1     → SU(3)₁ (abeliano, Z₃, fuertemente acoplado)
E ↓:          k_eff crece   → más representaciones permitidas
E = Λ_QCD:    k_eff >> 1    → SU(3) casi clásico (perturbativo)
E → 0:        k_eff → ∞     → SU(3) Yang-Mills clásico
```

### Conexión con la libertad asintótica
La libertad asintótica de QCD (el acoplamiento decrece a altas energías) se reinterpreta:
- **UV (Planck):** g² ~ 1/k = 1 → acoplamiento fuerte, teoría topológica
- **IR (QCD):** g² ~ 1/k → 0 → acoplamiento débil, teoría perturbativa

Y el **confinamiento** en el IR se reinterpreta como el retorno a la estructura Z₃ fundamental:
- **Confinamiento ↔ simetría Z₃ del centro preservada** (resultado establecido en QCD de retículo)
- El parámetro de orden es el **lazo de Polyakov** ⟨L⟩:
  - ⟨L⟩ = 0 → confinamiento → Z₃ preservada
  - ⟨L⟩ ≠ 0 → deconfinamiento → Z₃ rota
- El **origen UV** de esta Z₃ es la trivalencia del vértice SCG

---

## 6. Los 5 argumentos convergentes para SU(3)

| # | Argumento | Tipo | Fuerza |
|---|---|---|---|
| 1 | **Z₃ quiral = SU(3)₁** (unicidad matemática) | Teorema | **Fuerte** |
| 2 | **SU(3) = menor grupo simple con centro Z₃** | Parsimonia (K-005) | Medio |
| 3 | **Desplazamiento de nivel** k=1 → k→∞ recupera SU(3) YM | QFT estándar | **Fuerte** |
| 4 | **Confinamiento ↔ Z₃** (QCD de retículo) | Física establecida | **Fuerte** |
| 5 | **Cancelación de anomalías** puede forzar Z₃ → SU(3) | Investigación activa | Sugerente |

Ningún argumento aislado es una derivación completa. Pero los 5 convergen al mismo punto: **Z₃ (derivada de la geometría SCG en D=3) se completa naturalmente a SU(3).**

---

## 7. Resultado completo: el grupo gauge del SM

Combinando D-004 con la resolución de Q-026:

```
Red SCG en D=3
    │
    ├── Segmentos: 2 modos transversales → SO(2) ≅ U(1)
    │       → campo gauge U(1) emergente ← DERIVADO
    │
    ├── Vértices trivalentes: SO(2) → Z₃
    │       → cuantización de carga en 1/3 ← DERIVADO
    │       + quiralidad gravitacional → SU(3)₁ ← ARGUMENTADO (5 vías)
    │       + flujo de nivel → SU(3) completo ← QFT ESTÁNDAR
    │
    └── Conexión gravitacional (Ashtekar): SU(2)
            → campo gauge SU(2) emergente ← MOTIVADO (LQG)
```

**Grupo gauge emergente: SU(3) × SU(2) × U(1)**

---

## 8. Predicciones nuevas del marco SCG para el sector gauge

### P.7 — Discretización del color a escala Planck
A energías E → M_P, el acoplamiento fuerte α_s → O(1) y el grupo de color se "discretiza" de SU(3) a Z₃. Esto implica:
- No hay gluones propagantes a escala Planck (k=1 → solo 3 anyones, sin adjunta)
- Los quarks en BH tipo SCG portan solo carga Z₃, no color SU(3) completo
- La unificación de acoplamientos a alta energía podría verse modificada

### P.8 — Origen geométrico del confinamiento
El confinamiento de color no es un fenómeno dinámico misterioso — es la **manifestación IR de la trivalencia UV**. La Z₃ fundamental (geometría del vértice) es la raíz del confinamiento. Solo los estados Z₃-singuletes (trialidad 0) propagacan libremente.

---

## 9. Nuevos insights

### K-017 — Z₃ + quiralidad gravitacional = SU(3)₁ por unicidad
Solo existen 2 órdenes topológicos quirales con fusión Z₃ (SU(3)₁ y su conjugado). La quiralidad de la red SCG (del CS gravitacional) selecciona SU(3)₁.

### K-018 — El confinamiento de color tiene origen geométrico UV
La simetría Z₃ del centro de SU(3) — cuya preservación equivale al confinamiento — se origina en la trivalencia del vértice SCG, que a su vez se origina en D=3.

---

## 10. Caveats y limitaciones

1. El argumento de unicidad (§4) depende de que la red SCG realmente tenga quiralidad gravitacional. Esto está motivado por LQG pero no derivado de A-003 solo.
2. El flujo de nivel (§5) es un mecanismo estándar pero los detalles cuantitativos (valor de k_eff a cada escala) no están calculados.
3. No se ha demostrado que el SU(3)₁ de la red SCG se acopla a la materia de la forma correcta para reproducir QCD.
4. Las anomalías (argumento 5) son un área de investigación activa, no un resultado cerrado.
5. E₆ (dim 78) también tiene centro Z₃ y no puede descartarse formalmente por el argumento de unicidad solo.
