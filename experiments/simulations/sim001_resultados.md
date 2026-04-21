# Resultados de sim001_cuerda_basica.js

- **Fecha:** 2026-04-15
- **Hipótesis puesta a prueba:** H-001 (versión toy del modelo D-001)

## Configuración

- n = 20 nodos en línea, bordes fijos.
- dt = 0.001, amortiguamiento = 0.02 (para estabilidad numérica).
- 20 000 pasos.
- Espaciamiento inicial ≈ 1, con perturbación aleatoria pequeña.

## Resultados

| Caso | G | k | λ | E final | Espaciamiento final | Comportamiento |
|---|---|---|---|---|---|---|
| A | 0.5 | 0.1 | 1.5 | ~4.3 | ~1.00 | ✅ estable |
| B | 1.5 | 0.1 | 0.5 | ~10⁸ (diverge) | ~1.00* | 💥 colapso |
| C | 1.0 | 0.1 | 1.0 | ~-32 | ~1.00 | ➖ marginal, estable |
| D | 0.5 | 2.0 | 1.5 | ~40 | ~1.00 | ✅ estable (rígida) |

*en B el colapso hace que pares de nodos se fundan y las fuerzas 1/d² explotan numéricamente.

## Conclusiones parciales

1. **Se observa la transición cualitativa de fase propuesta por H-001**:
   - Con λ > G → sistema estable (fase cuerda)
   - Con λ < G → colapso catastrófico (fase BH)
2. **La transición no es suave** al menos en este modelo toy — en λ ≈ G hay una divergencia aparente que con disipación queda "congelada".
3. **El espaciamiento de equilibrio NO es d*** en este setup (con bordes fijos). El sistema se asienta en el espaciamiento impuesto por las condiciones de frontera. Para ver d* se necesita:
   - bordes libres con confinamiento (p. ej., condiciones periódicas), o
   - masa total distribuida con simetría adecuada.

## Limitaciones reconocidas

- No conserva energía (amortiguamiento explícito).
- Boundary conditions artificiales.
- Solo 1D; no hay espacio ambiente.
- λ, G, k son adimensionales; no calibrados con constantes físicas.

## Próximos pasos con esta simulación

1. Añadir condiciones periódicas para observar d* emergente.
2. Versión conservativa (sin amortiguamiento) para verificar estabilidad verdadera.
3. Barrido de parámetros (λ/G) para mapear la frontera de fases.
4. Añadir temperatura (sim002).
5. Añadir ruptura y reconexión (sim003).

## Interpretación honesta (no sobrevender)

Esta simulación **NO prueba** H-001. Solo muestra que **el modelo toy es internamente consistente** y reproduce la intuición cualitativa de dos fases. Es el primer ladrillo, y sus limitaciones son severas (P-6 en `debilidades_H-001.md`).
