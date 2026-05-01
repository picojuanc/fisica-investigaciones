---
name: audit
description: Invoca el agent theory-auditor sobre un archivo o sub-tarea específica del marco SCG/H-004. Apply rigurously D1-D5 + Regla 1 with imparcialidad. Use after writing any new derivation, especially before declaring sub-task closure. Returns audit report.
---

# /audit — Auditoría imparcial vía theory-auditor

Invoca el agente `theory-auditor` para auditar imparcialmente un archivo o sub-tarea específica.

## Argumentos esperados

El usuario especifica:
- **Archivo a auditar** (ej: `notes/H-004_sesion84_subtarea_delta_*.md`), o
- **Sub-tarea a auditar** (ej: "sub-tarea δ").

Si no especifica, preguntar.

## Acción

1. Identificar archivo(s) relevantes.
2. Invocar el agent `theory-auditor` con prompt:
   - Path al archivo a auditar.
   - Contexto: ¿qué sub-tarea? ¿qué pretende cerrar?
   - Pedir informe estructurado D1-D5 + Regla 1 + K-005.
3. Devolver el informe al usuario.

## Importante

- **NO modificar archivos** durante la auditoría — sólo recibir informe.
- Si el agent encuentra debilidad mayor, **escalar** al usuario para decisión:
  - Reformular derivación.
  - Aceptar caveat más fuerte.
  - Retreat ordenado (Regla 9).
- Si la auditoría es **APROBADA LIMPIA**, considerar invocar `consistency-checker` para verificar drift inter-archivo.

## Cadencia recomendada

- **Tras cada cierre de sub-tarea** (β, γ, δ, ε, ζ del programa H-004).
- **Antes de promover K candidato** a confirmado.
- **Antes de adoptar A-005** como axioma operativo (cierre completo H-004).
