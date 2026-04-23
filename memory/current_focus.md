# Foco actual de investigación

**Actualizado:** 2026-04-23 (cierre de sesión 37 — K-028 REFUTADO heurísticamente; Q-045 nueva; SCG v2.1.1)

## Estado

**Sesión 37 CERRADA. K-028 heurístico refutado.** Fase I del plan TOV ejecutada: radiación pura ($p = \rho/3$) satura en compactness $3/7$, no alcanza el horizonte. El factor $1/(3\pi^2)$ identificado como **identidad geométrica pura**, no redshift. Obstrucción estructural mayor: **4/7 de la masa ADM** no cabe en EOS radiación isotrópica. **Q-045 abierta**: mecanismo para los 4/7 restantes.

### Logros consolidados de sesión 37

1. **Identidad geométrica $1/(3\pi^2)$ derivada analíticamente** sin QFT+GR. Sigue del coeficiente 4/3 de K-007 + definición $V_{BH}$.
2. **`sim002_tov_radiacion.py`** ejecutado exitosamente (RK4 manual, sin scipy). Barrido $y_c \in [0.1, 10^4]$.
3. **Patrón universal confirmado numéricamente:** compactness satura en $3/7$ para todo $y_c$; singular isothermal es atractor global del bulk.
4. **K-028 HEURÍSTICO REFUTADO:** interpretación como redshift y framing "interior uniforme" ambos GR-inconsistentes.
5. **K-028 degradado** de candidato a observación matemática; no cuenta en inventario.
6. **Q-045 abierta** (reemplaza P-15' efectivamente): mecanismo para los 4/7 de masa ADM no cubiertos por radiación pura.
7. **K-007 aclarado:** escala característica válida ($\rho_{K007} = \rho_{\text{iso}}(r)$ en $r \approx r_s/20$), NO densidad uniforme.
8. **Documentos creados:**
   - `experiments/simulations/sim002_tov_radiacion.py` (~330 líneas, RK4 manual)
   - `experiments/simulations/sim002_profile.dat` (2082 puntos del perfil crítico)
   - `experiments/simulations/sim002_resultados.md` (~180 líneas)
   - `notes/K-028_sesion37_TOV.md` (~340 líneas, análisis completo + veredicto)

### Inventario v2.1.1 (post-sesión 37)

- **30 insights confirmados** (30 limpios/estructurales + 1 con caveat cuantitativo: K-032). K-028 removido.
- **1 candidato:** K-034.
- **11 derivaciones** (D-001 a D-011). Sin cambio.
- **3 hipótesis activas** (H-001 interior con caveat "no uniforme", H-002, H-003).
- **26 reportes narrativos.** Sin cambio.
- **11 snapshots.** (No se crea v2.1.1 snapshot; la refutación no amerita snapshot nuevo.)
- **2 axiomas activos.**
- **Preguntas abiertas:** +1 (Q-045 nueva; P-15' cerrada con resultado negativo).
- **Repo público:** https://github.com/picojuanc/fisica-investigaciones

### Cambios documentales (v2.1 → v2.1.1, parche)

- K-028 marcado como observación matemática (no insight físico).
- Q-045 documentada.
- H-001 requiere caveat "interior no uniforme" (pendiente escritura en archivo de H-001).
- D-009 marca de "generalizar a $d(r)$ variable" (pendiente).
- K-007 aclarado en documentación: escala característica, no densidad uniforme.

## Siguientes pasos (sesión 38)

**Opciones principales:**

### Opción A (recomendada, primer intento) — TOV anisotrópica

- **Objetivo:** derivar TOV con $p_r(r) \neq p_t(r)$ para string gas SCG con orientación preferente near-horizon.
- **Modelo SCG propuesto:** interpolación entre radiación isotrópica bulk ($p_r = p_t = \rho/3$) y orientación tangencial near-horizon ($p_r \to 0$ o negativo, $p_t$ enhanced).
- **Técnica:** TOV anisotrópica estándar (Herrera-Santos 1997, Mak-Harko 2003).
- **Criterio de éxito:** compactness $\to 1$ accesible; perfil $d(r)$ consistente con K-007 como escala promedio.
- **Techo:** 1 sesión; si no cierra, ir a Opción C.
- **Entregables:** `notes/Q-045_sesion38_anisotropic_TOV.md`, posible `sim003_tov_anisotrop.py`.

### Opción B — Shell gravastar-invertido

- **Objetivo:** modelar bulk singular isothermal + shell delgada near-$r_s$ con EOS exótica.
- **Técnica:** Israel junction conditions + Mazur-Mottola 2001.
- **Criterio:** matching estable + 4/7 de masa en shell.
- **Contra:** requiere postular EOS exótica específica; menos natural que Opción A.

### Opción C (conservadora) — Consolidación + giro a otra prioridad

- **Objetivo:** aceptar el resultado negativo, documentar Q-045 como programa largo, girar a K-033, Q-030, o super-modular.
- **Por qué:** si dos sesiones más no cierran Q-045, es momento de cambiar foco y volver cuando haya insights externos.

### Recomendación

**Opción A primero** (sesión 38), con techo de 1 sesión. Evaluar al final: si avance claro, sesión 39 continúa. Si obstruido, Opción C (pasar a K-033 o Q-030).

## Debilidades activas post-sesión 37

| # | Problema | Severidad | Cambio |
|---|---|---|---|
| **P-15'** | **Redshift interior BH riguroso** | ✅ **CERRADO con resultado negativo** (sesión 37) | **No había cantidad física a calcular; interpretación heurística refutada. Sustituida por Q-045.** |
| P-8 | Lagrangiana (bosquejo) | ✅ cerrado con caveat (sesión 35) | Sin cambio |
| P-11 | Ashtekar autodual | ✅ resuelto estructuralmente | Sin cambio |
| P-14 | Polyakov 4D no-crítica | 🟡 media | Sin cambio |
| P-10 | WW dimensional | 🟡 media | Sin cambio |
| P-12, P-13 | Hipercarga, estadística | 🟡 media | Sin cambio |

**Sin eslabones rojos.** Q-045 nueva es una debilidad estructural identificada, no un eslabón roto.

## Para el yo futuro en sesión 38

**Archivos imprescindibles en orden de lectura:**

1. `memory/MEMORY_INDEX.md`.
2. **`notes/K-028_sesion37_TOV.md`** (veredicto completo sesión 37 — PRIMERA LECTURA).
3. **`experiments/simulations/sim002_resultados.md`** (numérico del TOV radiación).
4. `notes/K-028_sesion36_setup.md` (setup; EOS derivation sigue válida).
5. Este archivo (`current_focus.md`).
6. `memory/open_questions.md` (Q-045 nueva).
7. `memory/session_log.md` (última entrada: sesión 37).

**Primera acción recomendada sesión 38:**

- Leer `notes/K-028_sesion37_TOV.md` completo (veredicto y plan).
- Decidir: Opción A, B, o C.
- **Si A:** derivar TOV anisotrópica (Herrera-Santos 1997 como referencia), proponer modelo SCG del perfil $(p_r, p_t)(r)$, implementar extensión a `sim002_tov_radiacion.py` o crear `sim003`.
- **Si B:** leer Mazur-Mottola 2001 (y/o Visser 2003), plantear matching con shell.
- **Si C:** documentar estado consolidado, girar a K-033 o Q-030.

**Estado documental al cierre sesión 37:**
- `open_questions.md` actualizado (Q-045).
- `notes/K-028_sesion37_TOV.md` + `sim002_*` creados.
- `memory/session_log.md` actualizado.
- `memory/current_focus.md` (este archivo) actualizado.
- `memory/MEMORY_INDEX.md` pendiente actualización sesión 37.
- `memory/key_insights.md` pendiente marcar K-028 como degradado.
- `logic/refutations/debilidades_H-001.md` pendiente marcar P-15' cerrado.
- `hypotheses/active/H-001...md` pendiente caveat "interior no uniforme" en próxima revisión sustantiva.

**Observación meta (sesión 37):**
- **Regla 9 aplicada ejemplarmente.** Un "success" heurístico antiguo (K-028 sesión 15) no resistió análisis riguroso; se refuta con honestidad.
- **K-005 aplicada:** no se inventó redshift exótico ni EOS ad hoc. TOV + radiación + numérico dice lo que dice.
- **Resultado disfrazado:** refinamiento positivo (nueva pregunta Q-045 concreta; K-007 aclarado como escala) vestido de refutación. Patrón común en teoría madura.
- **Calibración:** escenario (B) predicho sesión 36 resultó ser escenario (C). La calibración sube la desconfianza futura en coincidencias numéricas atractivas (K-033 Yukawas, K-034 Q=1/3, etc., eventualmente requerirán el mismo filtro).

La teoría continúa.
