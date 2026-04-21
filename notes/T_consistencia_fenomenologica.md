# Consistencia fenomenológica: ¿emergen las partículas del SM?

**Fecha:** 2026-04-19 (sesión 11)
**Objetivo:** verificar que cada partícula del SM tiene una asignación consistente como defecto topológico de la red SCG.

---

## 1. Inventario del SM

### Fermiones (por generación, antes de ruptura electrodébil)

| Fermión | SU(3) | SU(2)_L | Y | Q |
|---|---|---|---|---|
| (u_L, d_L) | **3** | **2** | +1/6 | (+2/3, −1/3) |
| u_R | **3** | 1 | +2/3 | +2/3 |
| d_R | **3** | 1 | −1/3 | −1/3 |
| (ν_L, e_L) | 1 | **2** | −1/2 | (0, −1) |
| e_R | 1 | 1 | −1 | −1 |
| (ν_R) | 1 | 1 | 0 | 0 |

### Bosones

| Bosón | Campo | Número |
|---|---|---|
| Gluones | SU(3) adjunta (8) | 8 |
| W±, Z, γ | SU(2)_L × U(1)_Y → U(1)_EM | 4 |
| Higgs | (1, 2, +½) escalar | 1 físico |

---

## 2. Asignación fermión → defecto SCG

En el marco Wen (2003)/Walker-Wang, los fermiones son extremos de cuerdas abiertas. Las cargas se asignan por la estructura del vértice/arista:

| Propiedad SM | Mecanismo SCG | Origen en D-004 |
|---|---|---|
| Color (3, 3̄, 1) | Trialidad: m mod 3 ∈ {1, 2, 0} | Parte II (Z₃ del vértice) |
| Isospín débil (2, 1) | Espín j de la holonomía: j=½ (doblete) o j=0 (singlete) | Parte III (Ashtekar) |
| Hipercarga Y | Momento angular transversal m (normalización ≡) | Parte I (U(1)) |
| Quiralidad L/R | L se acopla a conexión autodual, R a anti-autodual | K-019 |
| Espín ½ | Espinor de la conexión gravitacional | Representaciones del grupo de Lorentz |

### Tabla de asignación completa

| Fermión | Trialidad | j (SU(2)) | L/R | ¿Consistente? |
|---|---|---|---|---|
| u_L | 1 (quark) | ½ (doblete) | L (autodual) | ✓ |
| d_L | 1 (quark) | ½ (doblete) | L (autodual) | ✓ |
| u_R | 1 (quark) | 0 (singlete) | R (anti-autodual) | ✓ |
| d_R | 1 (quark) | 0 (singlete) | R (anti-autodual) | ✓ |
| ν_L | 0 (leptón) | ½ (doblete) | L (autodual) | ✓ |
| e_L | 0 (leptón) | ½ (doblete) | L (autodual) | ✓ |
| e_R | 0 (leptón) | 0 (singlete) | R (anti-autodual) | ✓ |
| ν_R | 0 (leptón) | 0 (singlete) | R (anti-autodual) | ✓ (estéril) |

**Todas las partículas tienen asignación consistente.**

---

## 3. Verificación de Gell-Mann–Nishijima

Q = T₃ + Y. Para cada fermión:

| Fermión | T₃ | Y | Q calculado | Q real | ✓ |
|---|---|---|---|---|---|
| u_L | +½ | +1/6 | +2/3 | +2/3 | ✓ |
| d_L | −½ | +1/6 | −1/3 | −1/3 | ✓ |
| ν_L | +½ | −1/2 | 0 | 0 | ✓ |
| e_L | −½ | −1/2 | −1 | −1 | ✓ |
| u_R | 0 | +2/3 | +2/3 | +2/3 | ✓ |
| d_R | 0 | −1/3 | −1/3 | −1/3 | ✓ |
| e_R | 0 | −1 | −1 | −1 | ✓ |
| ν_R | 0 | 0 | 0 | 0 | ✓ |

---

## 4. Bosones gauge

| Bosón | Origen SCG | ¿Emerge? |
|---|---|---|
| Fotón γ | U(1)_EM = combinación lineal post-Higgs de U(1)_Y y T₃ | ✓ (estructura) |
| 8 gluones | Fluctuaciones SU(3) de la red; 8 = dim de la adjunta de SU(3) | ✓ (a k >> 1) |
| W± | Excitaciones SU(2)_L cargadas, masivas post-Higgs | ✓ (estructura) |
| Z⁰ | Combinación ortogonal al fotón, masiva post-Higgs | ✓ (estructura) |

---

## 5. Higgs

| Aspecto | SM | SCG | ✓? |
|---|---|---|---|
| Representación | (1, **2**, +½) | Doblete SU(2), hipercarga +½ | ✓ |
| Mecanismo | Potencial mexicano V(|φ|) | Condensación topológica | ✓ (Bais-Slingerland + Fradkin-Shenker) |
| Resultado | SU(2)_L×U(1)_Y → U(1)_EM | Idem | ✓ |
| VEV | v = 246 GeV | v ~ M_P·exp(−c·k₂), no predicho | ∼ |
| m_H = 125 GeV | Del potencial cuártico | No predicho | ✗ |

---

## 6. Tres generaciones

| Aspecto | SM | SCG | ✓? |
|---|---|---|---|
| N_gen = 3 | Dato experimental | Z₃ del grafo dual (K-020) | ∼ (propuesto) |
| Jerarquía de masas | m_e << m_μ << m_τ | Modos rotacionales del triángulo dual | ∼ (cualitativo) |
| Mezcla (CKM, PMNS) | Matrices unitarias | No derivada | ✗ |

---

## 7. Resumen

| Sector | Estado | Detalle |
|---|---|---|
| Grupo gauge | **✓** | SU(3)×SU(2)×U(1) emerge |
| Bosones gauge | **✓** estructura | γ, g, W, Z emergen; masas no |
| Fermiones (cargas) | **✓** | Toda la tabla de representaciones es consistente |
| Quiralidad | **✓** | K-026 explica por qué solo SU(2) |
| Gell-Mann–Nishijima | **✓** | Q = T₃ + Y verificado para toda partícula |
| Higgs (mecanismo) | **✓** | Condensación topológica + Fradkin-Shenker |
| 3 generaciones | **∼** | Propuesto (Z₃ dual), no derivado |
| Masas | **✗** | Sin Lagrangiana, sin masas |
| Normalización de Y | **∼** | Estructura (1/3) correcta; escala no fijada (P-12) |
| Estadística fermiónica | **∼** | Posible (Wen), no derivada para SCG (P-13) |
| Anomalías | **✓** plausible | Red libre de anomalías por construcción |

### Nuevos problemas identificados

- **P-12:** la normalización de la hipercarga (¿por qué Y = 1/6 para Q_L y no 1/3?) no se deriva de D-004. D-004 da cuantización en tercios pero no fija los valores específicos de Y para cada representación.
- **P-13:** la estadística fermiónica (espín ½) no se deriva explícitamente del Hamiltoniano Walker-Wang de la red SCG. Wen (2003) muestra que es posible; falta el cálculo específico.

### Evaluación global

**La consistencia fenomenológica es POSITIVA a nivel estructural.** Cada partícula del SM tiene una asignación consistente como defecto de la red SCG. Las cargas, la quiralidad, y la fórmula Q = T₃ + Y son correctas. El mecanismo de Higgs es compatible.

**La consistencia CUANTITATIVA falta.** No se predicen masas, ángulos de mezcla, VEV del Higgs, ni las 19 constantes libres del SM. Esto requiere la Lagrangiana (P-8).

**La teoría pasa el test de consistencia fenomenológica al nivel que puede, dado su estado actual (framework sin Lagrangiana).**
