# Ontología SCG

> ¿Qué existe según nuestra teoría? ¿Cuáles son las entidades básicas? ¿Qué se deriva de qué?

Este archivo responde a la pregunta: **"¿De qué está hecho el mundo en SCG?"**.

**Estado:** llenado en S78 (2026-04-30) tras Q-044 abordada por articulación. Refleja el estado del marco post-snapshot v2.4 (S74) + post-pausa estratégica formal (S77).

---

## 1. Jerarquía ontológica

```
NIVEL 0 (fundamental, régimen I — UV / pre-geométrica)
   ├── Escala fundamental: ℓ_P  (única escala continua)                  [A-001]
   └── Red Walker-Wang 3+1D modular sobre UBFC `Spin(10)_1`              [D-010]
            │
            └── Cargas topológicas: rep(SO(10)) + SU(2)_L gravitacional
                                     (~6 cargas independientes)

NIVEL 1 (emergente, régimen II — semiclásico Planck)
   ├── Geometría: métrica curva fluctuante, Ashtekar-Barbero-Immirzi β real
   ├── Cuerda gravitacional estabilizada (interior BH no-singular,
   │      4 zonas, Q-045 cerrada al ~99.98%)                              [H-001 v1.2, K-035]
   ├── Vértice trivalente Z₃ (origen geométrico de SU(3) y Q∈ℤ/3)         [D-004, K-015]
   └── Acoplamientos gauge α_gauge ∝ γ_Immirzi/(4π) ~ 0.02                [K-032.M, K-023]

NIVEL 2 (espacio-tiempo macroscópico, transición II → IV)
   ├── Punto fijo dimensional único (1, 3, 1) en ℤ³_{>0}                 [D-012, K-036]
   ├── Signatura (3+1) Lorentziana                                       [D-005, K-022]
   └── Foliación temporal asintóticamente Killing (régimen IV)

NIVEL 3 (observable, régimen IV — IR / SM)
   ├── Partículas SM como excitaciones topológicas defectuosas:
   │      ├── leptones, quarks (16 spinores SO(10))                       [H-003, K-039]
   │      ├── carga electrica Q ∈ ℤ/3 (doble derivación)                  [K-014, K-015, K-034]
   │      ├── espín ∈ ½ℤ (codimensión 2)                                  [K-011]
   │      └── color ∈ {1, 3, 3̄} (Z₃ → SU(3)_1)                            [K-016, K-017]
   ├── Higgs efectivo = loop-`v` cerrado de la UBFC `Spin(10)_1`          [K-037, K-040]
   ├── Yukawas y CKM Cabibbo cuantitativo (3 predicciones finas)          [K-041, K-042, K-043]
   └── Gravedad clásica + electromagnetismo + interacciones SM
```

**Lectura vertical:** los niveles superiores **emergen** de los inferiores. La emergencia no es metafórica — es estructural y, donde se ha trabajado, derivada (Polyakov → A-003 en D-006; Z₃ trivalente → SU(3)_1 en K-017; UBFC `Spin(10)_1` → SM en programa K-033).

---

## 2. Entidades fundamentales (nivel 0)

### 2.1 Escala fundamental ℓ_P

**Una sola escala continua** define la estructura UV:
$$
\ell_P = \sqrt{\hbar G/c^3} \approx 1.616 \times 10^{-35}\,\text{m}.
$$

En sistema natural Planck ($\hbar = c = G = 1$), todas las magnitudes "continuas" (M, L, T, E, …) son adimensionales. Lo que llamamos `n` dimensiones independientes (M·L·T·…) en análisis dimensional es **artefacto de unidades base IR convencionales**, no rango fundamental del marco.

**Por A-001:** la geometría continua deja de ser válida por debajo de $\ell_P$. Toda cantidad que dependa de subestructura sub-Planckiana debe ser tratada con corte UV.

### 2.2 Red Walker-Wang 3+1D modular

La estructura discreta del nivel 0 es una **red Walker-Wang** sobre la UBFC modular `Spin(10)_1`:
- **Vértices trivalentes** (D-004) con simetría Z₃ geométrica.
- **Aristas** etiquetadas con objetos simples del MTC: $\{1, v(10), s(16), c(\overline{16})\}$ (D-013).
- **Fusión cíclica $\mathbb{Z}_4$** (D-013, K-038).
- **Frontera quiral:** edge modes en (2+1)D dan los fermiones SM.

**Por D-010:** la elección `Spin(10)_1` es estructuralmente **única** como UBFC modular compatible con 16 espinores Weyl SM + cancelación 't Hooft por cobordismo (Wang-Wen 2018-2019; Q-043 ✅ CERRADA estructuralmente).

### 2.3 Cargas topológicas conservadas (nivel 0)

Las "magnitudes discretas" del marco (Q, espín, color, sabor) son **cargas topológicas** asociadas a la estructura de la red Walker-Wang. Toman valores en representaciones de:

$$
G_{\text{topológico}} = \text{Spin}(10)_1 \times \text{SU}(2)_L^{\text{gravitacional}}
$$

con rango total ≈ 6 (5 Cartans SO(10) + 1 SU(2)_L gravitacional).

**Estas cargas son fundamentales en régimen I** — no son emergentes. Lo emergente es la **geometría** que aparece en régimen II.

---

## 3. Lo que NO existe en SCG

| Entidad | Razón |
|---|---|
| Singularidades clásicas | H-001 cuerda plegada interior BH no-singular, Q-045 cerrada al ~99.98% |
| Espacio-tiempo continuo bajo $\ell_P$ | A-001 corte UV |
| Anyones macroscópicos en (3+1)D | Topológicos sólo en frontera (2+1)D quiral |
| Compactificaciones extra-dimensionales | K-036: punto fijo (1, 3, 1) único en ℤ³_{>0} |
| Vacío "vacío" sin estructura | Lattice WW activa en cualquier región |
| Fermiones puntuales | H-003: defectos topológicos extendidos |
| SUSY | No parte del marco; no necesaria |
| Tiempo absoluto | D-005, K-022: tiempo emerge en régimen II |
| Energía absoluta a nivel fundamental | Régimen I conserva sólo cargas topológicas, no energía |

---

## 4. El espacio de magnitudes físicas

> **Resultado de Q-044 (S78):** las magnitudes físicas en SCG forman un catálogo cerrado: 1 escala continua + cargas topológicas discretas en representaciones de $G_{\text{topológico}}$.

### 4.1 Tabla completa de magnitudes

| Magnitud | Origen estructural | Tipo | Tabla periódica |
|---|---|---|---|
| **L** (longitud) | $\ell_P$ corte UV | Escala continua primitiva | $\mathbb{R}_{>0}$, regularizada $\geq \ell_P$ |
| **T** (tiempo) | Factorización quiral única + foliación | Derivada de L vía c | $\mathbb{R}$ |
| **E, M** | Polyakov (Casimir) + relatividad | Derivada | $\mathbb{R}_{>0}$ |
| **S** (acción) | $\hbar$ cuanto fundamental | Escala primitiva cuántica | $\mathbb{R}$ (cuantificada) |
| **Q** (carga eléctrica) | Z₃ trivalencia + ruptura SU(5) | Carga topológica | $\frac{1}{3}\mathbb{Z}$ |
| **Espín** | Codimensión 2 nudos D=3 | Carga topológica | $\frac{1}{2}\mathbb{Z}$ |
| **Color** | Z₃ + quiralidad → SU(3)_1 | Carga topológica | $\{1, 3, \overline{3}\}$ |
| **Sabor** | UBFC `Spin(10)_1` rep `s` | Carga topológica | $\text{rep}(\text{Spin}(10))$, dim 16 |
| **Generación** | Z₃_dual conjetural | Carga topológica conjetural | $\mathbb{Z}/3$ (caveat fuerte K-039) |

### 4.2 Reducción dimensional

En unidades naturales ($\hbar = c = 1$):
$$
[E] = [M] = [L]^{-1} = [T]^{-1} = \ell_P^{-1}.
$$

La separación M·L·T del análisis dimensional convencional ($\mathbb{Z}^3$) **se colapsa a $\mathbb{Z}^1$** generado por $\ell_P$. La elección de unidades base (MKS, MKSC, Planck) no afecta la estructura — sólo etiqueta los IR proxies.

### 4.3 ¿Cuántas dimensiones físicas hay realmente?

> **Respuesta SCG (Q-044):**
> - **1 dimensión continua:** $\ell_P$ (equivalentemente $\hbar c$).
> - **6 cargas topológicas discretas:** rango($G_{\text{topológico}}$).
> - **Total:** 7 grados de libertad estructurales independientes para etiquetar magnitudes físicas.

La separación M, L, T, Q, espín, color, sabor en uso ingenieril es **convencional**, no una lectura del rango fundamental.

---

## 5. Conservaciones y simetrías

### 5.1 Conservaciones fundamentales (nivel 0, régimen I)

**Cargas topológicas** del UBFC `Spin(10)_1` son **conservadas exactamente** por construcción de la red Walker-Wang modular. Las fusiones $a \otimes b = \bigoplus_c N^c_{ab} c$ preservan los números cuánticos.

Esto incluye, post-ruptura:
- Carga eléctrica $Q$ (subgrupo $U(1)_{em}$).
- Color (subgrupo $SU(3)_c$).
- Hipercarga $Y$, isospín $T_3$ (subgrupos $U(1)_Y$, $SU(2)_L$).
- Número leptónico/bariónico hasta efectos no-perturbativos (instanton 't Hooft, SO(10) → permite $B-L$ violación a escala SO(10)).

### 5.2 Conservaciones emergentes (nivel 1+, régimen II)

**Energía** es Noether sobre $\partial_t$, pero $\partial_t$ está bien definido sólo asintóticamente:
- **Régimen IV (SM observable):** Killing temporal asintótico → energía ADM bien definida y conservada exactamente.
- **Régimen II (Planck / cerca de horizontes):** conservación global ADM, no local. Compatible con BH evaporación unitaria (cuerda interior + radiación Hawking).
- **Régimen I (UV):** energía no es generador de evolución temporal — concepto no aplica. Reemplazada por conservación de cargas topológicas.

### 5.3 Predicción estructural

Para procesos a energía $E$ con escala geométrica $\ell$:
$$
\text{Corrección no-conservación local} \sim O(E/M_P) \quad \text{o} \quad O(\ell_P/\ell).
$$

A energías LHC ($E \sim$ TeV): $\sim 10^{-15}$. Inobservable directamente. Marca técnica menor (sin urgencia, S78).

---

## 6. Comparación con candidatos pre-SCG

| Candidato (snapshot v0) | SCG actual |
|---|---|
| Información pura como base | Parcialmente: cargas topológicas son "información" en sentido UBFC |
| Relaciones (relacionalismo) | Parcialmente: lattice WW = nodos + aristas etiquetadas |
| Procesos (Whitehead) | No adoptado; SCG es estructural |
| Estructura matemática (Tegmark) | Compatible pero no adoptado fuertemente |
| Campo único | Parcialmente: el "campo" es la red WW; los modos son variados |
| Red causal | Parcialmente: red WW lleva orientación (quiralidad) |

**SCG combina lattice WW + escala $\ell_P$ + UBFC `Spin(10)_1`** — más específico que cualquiera de los candidatos pre-SCG, pero compatible con elementos de varios.

---

## 7. Premisa operativa v2.4 (S74)

(Replicada de framework/axioms.md con extensiones post-Q-045.)

- **Sector gravitacional:** Ashtekar-Barbero-Immirzi con β real (γ_Immirzi ≈ 0.2375), formulación Plebanski-autodual + Λ (D-007), Kodama normalizable vía Randono 2006.
- **Sector topológico SM:** Walker-Wang modular sobre UBFC `Spin(10)_1` MTC (D-010). Ruptura SO(10) → SU(5) → SM provee contenido SM (Wang-Wen 2018-2019).
- **Desacople estructural** entre sectores (D-010, O5).
- **Interior BH:** estructura 4 zonas (bulk + transición + cruce $h=1$ + near-horizon, K-035 promovido) — Q-045 cerrada al ~99.98% (sim010).
- **Sector materia SM:** programa K-033 ✅ COMPLETO (S41-S66, 6/6 sub-tareas + síntesis D-015): 1 generación + Higgs + Yukawa cuantitativo + CKM Cabibbo cuantitativo. **3 predicciones cuantitativas finas unificadas** ($m_t$ al 0.6%, banda $d_{LR}$, $\theta_{12}^{CKM}$ al 2%).

---

## 8. Niveles epistémicos del marco (apéndice consolidado)

(Replicado de snapshot v2.4 §7.3 para auto-contención.)

| Nivel | Definición | Total post-S78 |
|---|---|---|
| 1. Confirmado limpio | Derivación rigurosa + literatura validante + sin caveat | 31 K |
| 2. Candidato limpio | Estructura derivada, valor numérico no calibrado | 5 (K-027, K-029, K-031, K-037, K-038) |
| 3. Candidato caveat moderado | Forma funcional ✓, factor numérico abierto | 4 (K-036, K-041, K-042, K-043) |
| 4. Candidato caveat fuerte | Estructura conjetural, mecanismo no aterrizado | 3 (K-034, K-039, K-040) |

**Total: 31 + 9 = 40 K en inventario.** Sin eslabones rojos.

---

## 9. Pendiente

- **H-004:** nueva hipótesis posible (constantes fundamentales / Q-005). Decidir tras Q-044 cierre.
- **Q-001:** "espacio-tiempo emergente" — ya tocada parcialmente por D-005, K-022, D-012, K-036. Articulación complementaria a Q-044 pendiente.
- **Q-005:** valores numéricos $\hbar, c, G$ — puntos abiertos del marco. Naturalmente vinculados con H-004.
- **Marca técnica menor:** corrección cuantitativa $O(E/M_P)$ en conservación local régimen II (sin urgencia).

---

## Historial

- **2026-04-15:** archivo creado como esqueleto.
- **2026-04-30 (S78):** llenado en respuesta a Q-044 abordada por articulación. Refleja estado SCG post-snapshot v2.4 (S74) + pausa estratégica S77.

---

**Fin de la ontología SCG (estado S78).**
