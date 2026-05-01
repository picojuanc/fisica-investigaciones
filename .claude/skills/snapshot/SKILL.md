---
name: snapshot
description: Genera snapshot consolidado del marco SCG/H-004 en formato v2.X. Use this skill when major fase has closed (programa cerrado, varias sub-tareas cerradas, reducción axiomática mayor, hallazgo conceptual mayor). Documents complete current state in self-contained file.
---

# /snapshot — Generar snapshot consolidado

Genera un snapshot consolidado autocontenido del marco SCG/H-004 en formato `journal/YYYY-MM-DD_snapshot_v[X.Y].md`.

## Cuándo usar

Activar este skill cuando:
- Una fase importante de hipótesis cerró (todas debilidades críticas rebajadas).
- Reformulación mayor de axiomas o hipótesis adoptada.
- Hallazgo conceptual mayor (ej: unificación A-002 ↔ Higgs categorial).
- Trabajo acumulado suficiente para que lectura secuencial del repositorio sea incómoda.
- Cada 3-4 sub-tareas cerradas del programa H-004.

## Argumentos esperados

- **Versión** (ej: "v2.6", "v3.0"). Si no se especifica, incrementar la última.
- **Foco** del snapshot (ej: "post-cierre δ", "post-unificación-Higgs"). Opcional.

## Pasos

### 1. Verificar estado del marco

Leer `memory/MEMORY_INDEX.md` + `memory/current_focus.md` + último snapshot existente para identificar:
- Inventario actual (Ks, derivaciones, hipótesis, axiomas).
- Sub-tareas cerradas / pendientes.
- Premisa operativa actual.
- Cambios desde último snapshot.

### 2. Verificar consistencia (recomendado)

Invocar `consistency-checker` agent para detectar drift antes de fijar el snapshot.

### 3. Estructura del snapshot

```markdown
# Snapshot v[X.Y] — [Foco]

**Fecha:** YYYY-MM-DD (sesión SNN)
**Sesiones cubiertas:** 0-NN
**Estado:** [PREMISA OPERATIVA: SCG / SCG+H-004 / H-004]
**Análogo histórico:** [snapshot previo de magnitud comparable]

## 0. Resumen ejecutivo

| Aspecto | Estado |
|---|---|
| Marco SCG operativo | ... |
| Programa H-004 | ... |
| Inventario K | ... |
| Hipótesis activas | ... |
| Axiomas activos | ... |
| Derivaciones | ... |
| Snapshots | ... |
| Reportes narrativos | ... |
| Eslabones rojos | ... |
| K-005 ejemplar | ... |

## 1. Cuadro post-S[NN]

[Síntesis ontológica, estado por sectores SCG / H-004.]

## 2. Cambio de eje epistémico (si aplica)

## 3. Programa H-004 — plan multi-sesión

[Sub-tareas, cronograma, mapas, triggers.]

## 4. Inventario detallado

## 5. Lo que cambia respecto a v[X.Y-1]

## 6. Caveats honestos del estado v[X.Y]

## 7. Próximos hitos esperados

## 8. Disciplinas activas

## 9. Conclusión del snapshot
```

### 4. Generar archivo

Path: `journal/YYYY-MM-DD_snapshot_v[X.Y].md`.

### 5. Actualizar MEMORY_INDEX

Añadir entrada en sección "Snapshots consolidados" con descripción comprehensiva.

### 6. Verificar inclusión narrativa

Si hay R-XX recientes que aún no están reflejados en snapshots previos, mencionarlos en sección "Reportes narrativos" del snapshot.

## Disciplinas

- **Auto-contenido:** el snapshot debe ser leíble sin abrir otros archivos.
- **Honesto:** caveats explícitos en sección 6.
- **K-005:** no inflar inventario en snapshot — sólo lo confirmado.
- **Regla 7:** snapshot consolida fase, no marca empezar fase nueva.

## Output esperado

Resumen al usuario de:
1. Path del snapshot generado.
2. Líneas totales / contenido principal.
3. Cambios principales documentados (vs último snapshot).
4. Recomendación de actualizar MEMORY_INDEX.
