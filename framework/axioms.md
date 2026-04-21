# Axiomas del marco teórico

> Los axiomas son postulados de los que todo lo demás se deduce. Deben ser pocos, claros, y mutuamente compatibles. Cada uno lleva una **justificación** (por qué lo adoptamos) y una **alternativa rechazada** (qué otro axioma podríamos haber tomado y por qué no).

**Estado actual:** tres axiomas tentativos. Aún no son la base completa; pueden ser reemplazados.

---

## A-001 — Escala Planckiana como corte de validez geométrica

**Enunciado:** existe una escala característica ℓ_P = √(ℏG/c³) ≈ 1.6×10⁻³⁵ m a partir de la cual la descripción continua del espacio-tiempo deja de ser físicamente válida.

**Justificación:** es consenso en gravedad cuántica. No se conoce el mecanismo exacto, pero todos los programas serios (LQG, cuerdas, causal sets) coinciden en que ℓ_P marca un corte.

**Alternativas rechazadas:** continuo sin corte → lleva a divergencias en toda cuantización de la gravedad.

**Consecuencias inmediatas:** toda cantidad que dependa de subestructura por debajo de ℓ_P debe ser tratada con corte UV o reinterpretada.

**Depende de:** —

---

## A-002 — Transición de fase gravitacional

**Enunciado:** cuando la densidad de energía local ρ alcanza una densidad crítica ρ_c comparable a la densidad de Planck ρ_P = c⁵/(ℏG²), la descripción efectiva de la materia/energía sufre una **transición de fase cualitativa**: la configuración de mínima energía deja de ser esférica (BH clásico) y pasa a ser 1D extendida (cuerda gravitacional).

**Justificación:** motivada por E-003 (inestabilidad de horizontes deformados lleva a sistemas que, por cuantización, pueden encontrar configuraciones no-geométricas) y por la correspondencia BH–cuerda ya conocida (Horowitz–Polchinski).

**Alternativas rechazadas:**
- "Toda materia a densidad Planckiana es un BH esférico estándar" → no explica por qué Horowitz–Polchinski funciona, no evita singularidad.
- "La transición es suave" → va contra la evidencia de muchos sistemas físicos donde las transiciones de fase son abruptas.

**Consecuencias inmediatas:** existencia de al menos dos fases gravitacionales de la energía concentrada; existencia de una frontera de fase.

**Depende de:** A-001.

**Problema abierto:** derivar ρ_c desde primeros principios.

---

## A-003 — Presión de degeneración de los grados de libertad gravitacionales

> **Reformulado el 2026-04-16.** La versión anterior ("coste energético de la información cuántica / presión de entrelazamiento") se reemplaza por una formulación más simple, derivable y menos arbitraria. Detalle del razonamiento: `notes/P-1_analisis.md`.

**Enunciado:** los grados de libertad del espacio-tiempo a escala Planck manifiestan una **presión cinética cuántica** (consecuencia del principio de incertidumbre de Heisenberg) que se opone al colapso gravitacional, en analogía directa con las presiones de degeneración que estabilizan enanas blancas (electrones) y estrellas de neutrones (neutrones).

**Forma:** para un grado de libertad confinado en una región de tamaño d:
- no relativista: E ≥ ℏ²/(2m d²) (escala 1/d²)
- relativista / sin masa: E ≥ ℏc/d (escala 1/d)

Para el término E_info del modelo D-001 se adopta la segunda forma: `E_info ≈ N · ℏc / d` donde N es el número de modos por celda.

**Justificación:**
- Es mecánica cuántica + relatividad especial estándar aplicadas al régimen Planck. **No es un postulado nuevo**, es un cálculo.
- Consistente con el principio holográfico (la presión acota la densidad de información local).
- Analogía cuantitativa con objetos astrofísicos conocidos (ver E-005).
- Compatible con LQG (cuantización del área/volumen) y con fuzzballs (microestructura interior del BH).

**Alternativas consideradas y descartadas:**
- "Coste energético de la información cuántica" (formulación vieja): palabra bonita, sin derivación. Superseded.
- Energía de Casimir: típicamente atractiva, iría al revés.
- Complejidad computacional: demasiado abstracta para aterrizar en un término local.

**Consecuencias inmediatas:**
- El término estabilizador de H-001 tiene origen físico claro.
- Existe un análogo del límite de Chandrasekhar para configuraciones gravitacionales a escala Planck.
- No requiere postular "entidades informacionales" nuevas.

**Problema abierto residual:** ¿qué son *exactamente* los "grados de libertad del espacio-tiempo"? (Ver Q-014.)

**Depende de:** A-001.

---

### Historial del axioma A-003

- **2026-04-15 (v1.0):** introducido como "coste energético de información cuántica" (formulación ad hoc).
- **2026-04-16 (v1.1):** reformulado como presión cinética cuántica de grados de libertad gravitacionales, derivable de QM + GR. Motivado por el análisis de P-1 (ver `logic/refutations/debilidades_H-001.md`).
- **2026-04-20 (v1.2 — DERIVADO, YA NO ES AXIOMA):** A-003 v1.1 se deriva rigurosamente como la *presión de Casimir de los modos transversales de la cuerda* (Polyakov con corte UV en d = ℓ_P). Ver derivación **D-006** (`logic/derivations/D-006_A-003_desde_polyakov.md`) y análisis completo en `notes/Q-032_polyakov_y_A-003.md`. Resuelve Q-032 afirmativamente. Promueve K-027 a insight confirmado estructuralmente.

### Estado v1.2 (2026-04-20)

**A-003 deja de ser axioma independiente.** Se mantiene esta sección como documento histórico y de contexto, pero el contenido matemático de A-003 v1.1 (E_info ≈ N ℏc / d por celda) es ahora **consecuencia** de:
- A-001 (corte Planck → corte UV en d ≥ ℓ_P).
- Cuantización canónica estándar de la acción de Polyakov.

En el esquema v1.2:
- **Axiomas activos:** A-001, A-002.
- **Proposiciones derivadas que antes eran axiomas:** A-003 → D-006.

El coeficiente de la forma E ∝ ℏc L/d² es fijado por la topología worldsheet (cuerda cerrada: 2π; abierta: π/2). No queda como parámetro libre.

**Caveat residual:** consistencia cuántica de Polyakov 4D no-crítica como teoría efectiva (P-14) — ver debilidades_H-001.md.

---

## Relaciones entre axiomas (v1.2 — actualizado 2026-04-20)

```
A-001 (corte Planck)
   │
   ├──→ A-002 (transición de fase gravitacional)
   │
   └──→ [cuantización canónica de Polyakov en sector IR de WW]
            │
            └──→ D-006 (A-003 v1.1: presión de degeneración = Casimir transversal)
                     │
                     └──→ H-001 (fase de cuerda estabilizada)
```

Sólo dos axiomas activos (A-001, A-002). A-003 v1.1 pasa a ser teorema (D-006). H-001 es más modesta axiomáticamente en v1.2.

---

## Candidatos aún no adoptados (del documento inicial)

### Primacía informacional
> *La información es la entidad ontológica básica; materia y espacio-tiempo son patrones de información.*

Relacionado con A-003 pero más fuerte. A-003 afirma que la información tiene coste; la primacía informacional afirma que la información es **todo**. Aún no adoptado — se estudia.

### Finitud computacional
> *Cualquier proceso físico es computable en pasos discretos finitos.*

Consistente con A-001 pero más fuerte. Por adoptar si se demuestra necesario para derivaciones posteriores.

### Autoconsistencia
> *El universo es el único conjunto de leyes que se describe a sí mismo sin contradicción.*

Atractivo pero peligroso (riesgo de circularidad). En pausa.

### Relacionalismo estricto
> *Solo existen relaciones; los "objetos" son nodos de relaciones.*

Posible fundamento metafísico, pero no necesario para H-001. Archivado.

---

## Axioma tentativo asociado a H-002

### A-004 (tentativo) — Principio topológico de emergencia espacial

> La dimensionalidad del espacio macroscópico es aquella en la cual los objetos fundamentales (de dimensión p) poseen topología no trivial persistente. Esto corresponde a codimensión 2: **D = p + 2**.

**Estado:** tentativo. Es un hecho matemático (topología algebraica) reinterpretado como principio físico. Aún no se ha derivado *por qué* la naturaleza selecciona la dimensionalidad topológicamente óptima. Posible ruta: mostrar que configuraciones sin topología robusta son energéticamente inestables (conjetura, ver E-007).

**Consecuencia directa:** con p = 1 (cuerdas SCG, de H-001): D = 3.

**Depende de:** H-001 v1.1 (p = 1).

**Problema abierto:** ¿es A-004 un axioma genuino o una consecuencia derivable de A-001 + A-002 + A-003 + algún principio de estabilidad? Si se puede derivar, no es axioma — es teorema.
