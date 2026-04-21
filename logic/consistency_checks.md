# Chequeos de consistencia entre hipótesis

Matriz de compatibilidad entre hipótesis activas y confirmadas. Debe actualizarse cada vez que se añade, confirma o refuta una hipótesis.

## Matriz (actualizada sesión 10)

### H-001 vs H-002: **COMPATIBLE**
- H-001 establece que los objetos fundamentales son cuerdas 1D (D-002). H-002 usa p=1 para derivar D=3. Son complementarias: H-001 da la dimensionalidad interna, H-002 da la dimensionalidad espacial.
- No hay tensión lógica.

### H-001 vs H-003: **COMPATIBLE, con pregunta abierta**
- H-001 describe la fase SCG como estructura del interior de BHs (red densa). H-003 describe las partículas como excitaciones topológicas de la red SCG (red ordenada, vacío).
- **Pregunta:** ¿cómo se conectan la "red densa" (BH) y la "red diluida" (vacío)? ¿Hay una transición de fase? No hay incompatibilidad lógica, pero la conexión no está formalizada.

### H-002 vs H-003: **COMPATIBLE, dependencia directa**
- H-003 depende de H-002 (D=3 es necesario para nudos estables, trivalencia, y toda la cadena de D-004).
- Sin H-002, H-003 colapsa. La dependencia es unidireccional.

### D-004 vs axiomas: **COMPATIBLE, con decisión forzada**
- D-004 requiere la conexión autodual de Ashtekar (compleja) para el eslabón SU(2)_L. Esto no contradice A-001 a A-004, pero impone un requisito adicional sobre la formulación de GR que se usa.
- La decisión autodual separa SCG de la LQG mainstream (que usa Barbero-Immirzi). No es una incompatibilidad con nuestros axiomas, pero sí una restricción que debe documentarse.
- **Actualización sesión 11:** Ashtekar autodual identificado como premisa fuerte (P-11). La conexión Ashtekar → Crane-Yetter → Walker-Wang es históricamente natural (Crane-Yetter 1993 fue motivada por Ashtekar).

### H-003 vs framework dimensional: **COMPATIBLE, corregido en sesión 11**
- H-003 originalmente citaba Levin-Wen (2+1D) y Chern-Simons como framework. La red SCG es 3+1D.
- **Corrección (sesión 11):** el framework correcto es Walker-Wang (2011) / Crane-Yetter (1993) para 3+1D. Los eslabones [4] y [5] de H-003 han sido reformulados. CS es la teoría de frontera, no del bulk. Las reglas de fusión de D-004 se transfieren (son geométricas). Wen (2003 PRD) demostró constructivamente U(1)×SU(2)×SU(3) en red 3+1D.
- K-026 (patrón de quiralidad) confirma consistencia: solo SU(2) es quiral porque es el único factor gravitacional.

### Consistencia fenomenológica: **VERIFICADA a nivel estructural (sesión 11)**
- Cada partícula del SM (8 fermiones/generación + bosones gauge + Higgs) tiene asignación consistente como defecto de la red SCG.
- Gell-Mann–Nishijima Q = T₃ + Y verificado para todas las partículas.
- Masas y constantes numéricas no predichas (requiere Lagrangiana, P-8).
- Ver: `notes/T_consistencia_fenomenologica.md`.

## Procedimiento

1. Cuando se propone una nueva hipótesis H-nueva:
   - Comparar contra cada hipótesis activa/confirmada.
   - Para cada par, escribir: ¿pueden ser ambas verdaderas? ¿por qué?
2. Si se detecta incompatibilidad:
   - Crear un archivo `R-XXX` en `logic/refutations/` con el análisis formal.
   - Decidir cuál hipótesis se descarta, modifica, o si se debe reformular ambas.
3. Una inconsistencia no resuelta bloquea el avance hasta resolverse.
