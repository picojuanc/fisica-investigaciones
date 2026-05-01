---
name: close-subtask
description: Ejecuta el protocolo de cierre de una sub-tarea técnica del programa H-004 (β, γ, δ, ε, ζ) o cualquier hito mayor. Incluye auditorías D1-D5, documento técnico, actualización de memoria, framework/axioms.md, y consideración de R-XX narrativo. Use this skill when closing any sub-task to ensure full discipline.
---

# /close-subtask — Protocolo de cierre de sub-tarea

Ejecuta el cierre completo de una sub-tarea con **disciplina máxima** de las disciplinas D1-D5 + Reglas 1, 5, 7, 9.

## Argumentos esperados

El usuario debe especificar:
- **Sub-tarea cerrada** (ej: "β", "γ", "δ", o tema específico).
- **Resultado preliminar** (cierre limpio / estructural con caveat / parcial / retreat).

Si no especifica, preguntar.

## Pasos

### 1. Verificar disciplinas D1-D5 honestamente

Antes de declarar cierre, ejecutar (o invocar `theory-auditor` agent):

- **D1 anti-vacuidad:** ¿la derivación es matemáticamente rigurosa o apelativa?
- **D2 correspondencia IR:** ¿reproduce lo confirmado fenomenológicamente?
- **D3 extensiones justificadas:** ¿hay matemática nueva? ¿Justificada?
- **D4 falsabilidad:** ¿hay predicciones cuantitativas falsables?
- **D5 auditoría periódica:** ¿pasa los criterios anteriores?

### 2. Decidir nivel epistémico de cierre

Niveles disponibles (de framework/epistemology.md):
- **Cierre limpio:** todos los criterios ✅ sin caveats.
- **Cierre estructural con caveat cuantitativo** (análogo K-032.M): forma funcional rigurosa, valor numérico pendiente.
- **Cierre con caveat moderado:** estructural ✅ + caveat específico documentado.
- **Cierre con caveat fuerte:** estructural con limitaciones mayores explícitas.
- **Cierre parcial:** algunos componentes ✅, otros pendientes.
- **Retreat ordenado (Regla 9):** documentar honestamente y abandonar.

### 3. Escribir documento técnico

Crear `notes/H-004_sesion[NN]_subtarea_[X]_[tema].md` con estructura estándar:
1. Setup técnico
2. Argumento riguroso paso a paso
3. Aplicación a caso prueba (`Spin(10)_1` cuando aplique)
4. Auditorías D1 + D2 + D3 + D4
5. Decisión de cierre
6. Implicaciones para premisa operativa
7. Lo que sigue
8. Conclusión

### 4. Actualizar archivos críticos

- **`framework/axioms.md`** — si se reduce un axioma a derivado, añadir sección "Estado v2.X".
- **`framework/ontology.md`** — si emerge contenido ontológico nuevo.
- **`memory/session_log.md`** — entrada completa de la sesión.
- **`memory/current_focus.md`** — estado post-cierre + próxima sub-tarea.
- **`memory/MEMORY_INDEX.md`** — actualizar inventario actual + entrada de sesión.
- **`memory/open_questions.md`** — si Q-XXX afectada.
- **`memory/key_insights.md`** — solo si K nuevo (raro: K-005 disciplina).

### 5. Considerar R-XX narrativo

Si el cierre marca:
- Hito mayor (programa cerrado, retreat ordenado, hallazgo conceptual mayor) → **escribir R-XX**.
- Cierre técnico de sub-tarea sin hito mayor → R-XX **no necesario** automáticamente; usuario decide.

### 6. Considerar snapshot consolidado

Si el cierre marca cambio mayor en estado (reducción axiomática, nueva premisa operativa, fase mayor cerrada) → **considerar snapshot v2.X+1**.

### 7. Verificar disciplina K-005

¿Se postuló algún K nuevo? Si no, **registrar K-005 ejemplar [N+1]ma vez consecutiva**.

## Output esperado

Resumen al usuario de:
1. Veredicto del cierre (nivel epistémico).
2. Archivos creados/actualizados.
3. Logros + caveats principales.
4. Próximo paso sugerido.

## Disciplinas

- **Honestidad antes que ambición:** un cierre estructural con caveat declarado vale más que un "cierre limpio" inflado.
- **K-005:** ningún K nuevo sin mecanismo derivado.
- **Regla 1:** auditoría honesta — buscar el error ANTES de declarar éxito.
- **Regla 9:** retreat ordenado preferible a defensa por inercia.
