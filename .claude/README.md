# `.claude/` — Configuración del proyecto SCG/H-004

Configuración local de Claude Code para el proyecto de investigación de Teoría del Todo alternativa.

**Creado:** 2026-05-01 (sesión 83, nota meta-organizativa).

---

## Estructura

```
.claude/
├── README.md                      # Este archivo
├── settings.local.json            # Settings locales (no compartido)
├── agents/                        # Agentes especializados
│   ├── theory-auditor.md          # Auditor imparcial de derivaciones
│   ├── consistency-checker.md     # Verificador de consistencia inter-archivo
│   └── literature-scout.md        # Buscador de referencias técnicas
└── skills/                        # Skills slash-comando
    ├── start-session/SKILL.md     # /start-session — protocolo de inicio
    ├── close-subtask/SKILL.md     # /close-subtask — protocolo de cierre
    ├── audit/SKILL.md             # /audit — invoca theory-auditor
    └── snapshot/SKILL.md          # /snapshot — genera snapshot v2.X
```

---

## Agentes — cuándo usar

### `theory-auditor`
**Invocar tras cualquier derivación nueva**, especialmente:
- Cierre de sub-tarea técnica del programa H-004 (β, γ, δ, ε, ζ).
- Promoción de K candidato a confirmado.
- Adopción de A-005 como axioma operativo.

**Función:** aplica D1-D5 + Regla 1 con imparcialidad. Detecta argumentos apelativos disfrazados de derivaciones.

### `consistency-checker`
**Invocar cada 5-10 sesiones del programa H-004** o tras cambios mayores.

**Función:** detecta drift entre archivos del repo (axioms.md, ontology.md, key_insights.md, snapshots, MEMORY_INDEX, current_focus, open_questions). Evita inconsistencias acumuladas.

### `literature-scout`
**Invocar cuando se necesita verificar referencias o buscar precedentes**, especialmente:
- Camino C exploration (Wolfram, Connes, Lurie, Voevodsky).
- Camino B technical references (Bais-Slingerland, Kong, Etingof-Nikshych-Ostrik, Walker-Wang).
- Verificar novedad de propuesta antes de promover K.

**Función:** busca en arXiv, Google Scholar, INSPIRE-HEP, MathSciNet.

---

## Skills — invocación slash

| Skill | Comando | Cuándo |
|---|---|---|
| `start-session` | `/start-session` | Inicio de cada sesión |
| `close-subtask` | `/close-subtask` | Tras cerrar sub-tarea técnica |
| `audit` | `/audit` | Tras escribir derivación nueva |
| `snapshot` | `/snapshot` | Tras hito mayor (programa cerrado, reducción axiomática, hallazgo conceptual mayor) |

---

## Plan de revisión periódica

Disciplina meta del proyecto: **K-005 a meta-escala** — no inflar herramientas si las existentes bastan.

**Cadencia:** cada 5 sesiones del programa H-004, evaluar:
1. ¿Los agentes/skills siguen siendo útiles? (¿Se usaron en las últimas 5 sesiones?)
2. ¿Emergió tarea recurrente nueva que merezca agente/skill propio?
3. ¿Algún agente/skill no se usa? (Considerar deprecar.)
4. ¿Optimización de prompts necesaria?

**Próxima revisión programada:** sesión 88 (post-cierre sub-tarea δ).

---

## Cómo se invocan (validado en S84)

**Importante:** los agentes custom en `.claude/agents/` **NO son invocables programáticamente por Claude principal** vía herramienta Agent con `subagent_type`. Sólo el usuario los invoca desde el chat. Existen dos patrones de uso complementarios:

### Patrón A — Usuario invoca desde chat (preferido para imparcialidad)

```
@"theory-auditor" audita notes/H-004_sesion84_subtarea_delta_*.md
@"consistency-checker" verifica drift entre archivos
@"literature-scout" busca papers sobre Bais-Slingerland condensation
```

O en lenguaje natural: "audita esta derivación con el theory-auditor" — el sistema lo descubre automáticamente.

**Ventaja:** imparcialidad real (el agente custom es un proceso separado del Claude principal que escribió la derivación).

### Patrón B — Claude principal invoca general-purpose + prompt (workaround)

Cuando el usuario quiere que Claude audite algo sin escribir explícitamente, Claude principal usa:

```
Agent(
  subagent_type: "general-purpose",
  description: "Auditoría imparcial sub-tarea X",
  prompt: "<copiar el rol y task del agente custom + contexto específico>"
)
```

**Ventaja:** funciona sin requerir intervención del usuario.
**Desventaja:** menor imparcialidad (mismo motor LLM que escribió la derivación).

**Validación S84:** este patrón funcionó ejemplarmente en la auditoría de la sub-tarea δ — el "auditor" identificó debilidades reales que el autor (Claude principal escribiendo δ) había documentado con caveat insuficiente. La auditoría llevó a recalibración honesta de "moderado" a "fuerte" caveat.

### Patrón C — Skills slash

Los skills (`.claude/skills/`) se invocan vía `/skill-name` en el chat por el usuario. Cuando el usuario invoca `/audit`, el sistema (vía el archivo SKILL.md) sabe activar el patrón A o B según contexto.

## Disciplina de uso

- **K-005 a meta-escala:** los agentes/skills son herramientas, no inventario K. No promover ni inflar sin razón.
- **Imparcialidad del `theory-auditor`:**
  - **Si se busca máxima imparcialidad:** usuario invoca patrón A vía chat.
  - **Si Claude principal audita autonomamente:** patrón B (workaround) — útil pero menos imparcial.
- **Consistencia narrativa-técnica:** los reportes R-XX deben mantenerse alineados con cierres técnicos. El `consistency-checker` lo verifica.
- **Honestidad:** si un agent/skill no añade valor, deprecarlo. K-005 simétrico.

---

## Historial

- **2026-05-01 (S83):** creación inicial de la estructura `.claude/agents/` + `.claude/skills/` con 3 agentes + 4 skills prioritarios. Sugerencia del usuario en S83 ("crear agentes especializados, periódicamente revisarlos, igual que skills").
