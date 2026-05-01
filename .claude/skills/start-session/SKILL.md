---
name: start-session
description: Ejecuta el protocolo de inicio de sesión del proyecto SCG/H-004. Lee MEMORY_INDEX, snapshot consolidado más reciente, current_focus, open_questions, y resume el estado actual de la investigación en 3-5 líneas. Use this skill at the start of every session to come up to speed quickly.
---

# /start-session — Protocolo de inicio de sesión

Ejecuta el protocolo de inicio definido en `CLAUDE.md` del proyecto SCG/H-004.

## Pasos

1. **Lee `memory/MEMORY_INDEX.md`** — índice maestro de la memoria a largo plazo.
2. **Identifica el snapshot consolidado más reciente** listado en MEMORY_INDEX (sección "Snapshots consolidados") y léelo. Es la forma más rápida de ponerse al día.
3. **Lee `memory/current_focus.md`** — en qué se estaba trabajando la última vez.
4. **Lee las últimas entradas de `memory/session_log.md`** (mínimo las últimas 3 sesiones).
5. **Lee `memory/open_questions.md`** — preguntas abiertas pendientes (cabezal + secciones recientes).
6. **Verifica `hypotheses/active/`** — hipótesis vivas.

## Output esperado

Un resumen de **3-5 líneas** al usuario indicando:
1. Estado general del marco (programa H-004 status, sub-tareas cerradas, K-005 streak).
2. Última sesión cerrada y qué logró.
3. Próximo paso sugerido (sub-tarea próxima, archivo crítico a leer).
4. Cualquier alerta (drift en consistencia, sub-tarea crítica próxima, etc.).

## Disciplinas

- **Económico con tokens:** evita re-leer archivos completos cuando una sección basta. Usa offset/limit en Read.
- **No comenzar trabajo nuevo** sin que el usuario lo pida explícitamente.
- **Reportar honestamente:** si encuentras drift o inconsistencia, mencionarla.

## Ejemplo de output

> **Estado:** Marco H-004 con 3/6 sub-tareas cerradas (α + β + γ). A-005 único axioma propuesto; A-001 y A-002 derivados modulo Q-005. Programa K-033 ✅ COMPLETO heredado. Sin eslabones rojos.
>
> **Última sesión (S83):** sub-tarea γ cerrada estructuralmente — A-002 reducido + hallazgo unificación A-002 ↔ Higgs categorial.
>
> **Próximo:** sub-tarea δ (S84) — punto crítico, re-derivar `Spin(10)_1` específica desde A-005 + criterio (6).
