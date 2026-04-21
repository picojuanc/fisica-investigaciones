// sim001_cuerda_basica.js
// Simulación mínima (sin temperatura) del modelo D-001.
// Objetivo: comprobar si existe un equilibrio de cuerda cuando λ > G,
// y si el colapso ocurre cuando λ < G.
//
// Uso:   node sim001_cuerda_basica.js
//
// Salida: posiciones finales + distancia promedio entre nodos + energía total.
//
// NOTA IMPORTANTE: este es un modelo toy. Los resultados son cualitativos.

"use strict";

class CuerdaGravitacional {
  constructor({ n = 20, G = 0.5, k = 0.1, lambda = 1.0 } = {}) {
    this.n = n;
    this.G = G;
    this.k = k;
    this.lambda = lambda;
    // posiciones iniciales espaciadas con pequeña perturbación
    this.x = Array.from({ length: n }, (_, i) => i + 0.05 * (Math.random() - 0.5));
    this.v = Array.from({ length: n }, () => 0);
  }

  energiaTotal() {
    let Eg = 0, Et = 0, Ei = 0;
    for (let i = 0; i < this.n; i++) {
      for (let j = i + 1; j < this.n; j++) {
        const d = Math.abs(this.x[j] - this.x[i]);
        if (d > 1e-9) Eg -= this.G / d;
      }
    }
    for (let i = 0; i < this.n - 1; i++) {
      const d = this.x[i + 1] - this.x[i];
      Et += this.k * d * d;
      if (d > 1e-9) Ei += this.lambda / d;
    }
    return { Eg, Et, Ei, total: Eg + Et + Ei };
  }

  // Fuerza sobre nodo i (sin temperatura)
  fuerza(i) {
    let F = 0;
    // gravedad (contribución de todos los demás nodos)
    for (let j = 0; j < this.n; j++) {
      if (j === i) continue;
      const dx = this.x[j] - this.x[i];
      const d = Math.abs(dx);
      if (d < 1e-9) continue;
      // F_grav sobre i por parte de j: atractiva hacia j, magnitud G/d^2
      F += Math.sign(dx) * this.G / (d * d);
    }
    // tensión (vecinos)
    if (i > 0) {
      const d1 = this.x[i] - this.x[i - 1];
      F += -2 * this.k * d1;  // equilibrio a d1 = 0? no, recordar que queremos d = d*
    }
    if (i < this.n - 1) {
      const d2 = this.x[i + 1] - this.x[i];
      F += 2 * this.k * d2;
    }
    // info (repulsión corta de vecinos)
    // F_i^info = +λ/d1² (empuja a i lejos de i-1, es decir hacia +x)
    //          -λ/d2² (empuja a i lejos de i+1, es decir hacia -x)
    if (i > 0) {
      const d1 = this.x[i] - this.x[i - 1];
      if (d1 > 1e-9) F += +this.lambda / (d1 * d1);
    }
    if (i < this.n - 1) {
      const d2 = this.x[i + 1] - this.x[i];
      if (d2 > 1e-9) F += -this.lambda / (d2 * d2);
    }
    return F;
  }

  paso(dt = 0.001, amortig = 0.02) {
    const F = this.x.map((_, i) => this.fuerza(i));
    // bordes fijos para evitar deriva global (no físico pero útil)
    for (let i = 1; i < this.n - 1; i++) {
      this.v[i] += F[i] * dt;
      this.v[i] *= (1 - amortig);
      this.x[i] += this.v[i] * dt;
    }
  }

  espaciamientoMedio() {
    let s = 0;
    for (let i = 0; i < this.n - 1; i++) s += this.x[i + 1] - this.x[i];
    return s / (this.n - 1);
  }

  distEquilibrioEstimada() {
    // d* = [ (λ - G) / (2k) ]^(1/3) según D-001
    const num = this.lambda - this.G;
    if (num <= 0) return null;
    return Math.cbrt(num / (2 * this.k));
  }
}

function correr({ nombre, params, pasos = 20000 }) {
  const sim = new CuerdaGravitacional(params);
  const E0 = sim.energiaTotal();
  for (let t = 0; t < pasos; t++) sim.paso();
  const E1 = sim.energiaTotal();
  const dMedio = sim.espaciamientoMedio();
  const dStar = sim.distEquilibrioEstimada();
  console.log(`\n--- ${nombre} ---`);
  console.log(`parámetros: ${JSON.stringify(params)}`);
  console.log(`E inicial : total=${E0.total.toFixed(3)} (g=${E0.Eg.toFixed(2)} t=${E0.Et.toFixed(2)} i=${E0.Ei.toFixed(2)})`);
  console.log(`E final   : total=${E1.total.toFixed(3)} (g=${E1.Eg.toFixed(2)} t=${E1.Et.toFixed(2)} i=${E1.Ei.toFixed(2)})`);
  console.log(`espaciamiento medio final: ${dMedio.toFixed(4)}`);
  console.log(`d* predicho por D-001    : ${dStar === null ? 'colapso (λ ≤ G)' : dStar.toFixed(4)}`);
}

// --- Experimentos ---

// Caso A: equilibrio esperado (λ > G)
correr({
  nombre: "A: λ > G  (predice equilibrio de cuerda)",
  params: { n: 20, G: 0.5, k: 0.1, lambda: 1.5 }
});

// Caso B: colapso esperado (λ < G)
correr({
  nombre: "B: λ < G  (predice colapso tipo BH)",
  params: { n: 20, G: 1.5, k: 0.1, lambda: 0.5 }
});

// Caso C: cerca del umbral
correr({
  nombre: "C: λ ≈ G  (transición)",
  params: { n: 20, G: 1.0, k: 0.1, lambda: 1.0 }
});

// Caso D: tensión dominante
correr({
  nombre: "D: k grande  (cuerda muy rígida)",
  params: { n: 20, G: 0.5, k: 2.0, lambda: 1.5 }
});
