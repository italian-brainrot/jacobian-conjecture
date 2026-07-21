# Run 6

## 1. Executive Summary & Objective

In July 2026, mathematician Levent Alpöge announced an explicit polynomial map in three variables that disproves the 3D Jacobian Conjecture:
$$ F(x, y, z) = (P, Q, S) : \mathbb{C}^3 \to \mathbb{C}^3 $$
with constant Jacobian determinant $-2$, which maps three distinct preimages to the same target point $q = (-1/4, 0, 0)$.

Our current goal is to discover and explore a two-dimensional polynomial counterexample:
$$ G(x, y) = (U, V) : \mathbb{C}^2 \to \mathbb{C}^2 $$
possessing constant nonzero Jacobian determinant, while also failing injectivity. In this run, we systematically investigate the mathematical reduction of Alpöge's 3D map to a 2D map, analyze previous failed attempts, and prove the structural rigidity of the 2D case.

---

## 2. Mathematical Rigidity of the 2D Case

The universal, all-dimensional Jacobian Conjecture is now false due to Alpöge's 3D map. However, the classical 2D case remains open. This difference can be understood algebraically and geometrically through **properness** and the **nonproperness set**.

### 2.1 Properness and Jelonek's Theorem
For any polynomial map $f : \mathbb{C}^n \to \mathbb{C}^n$, let $S_f$ be the set of points in $\mathbb{C}^n$ at which $f$ is not proper (i.e., the set of points $y \in \mathbb{C}^n$ for which there is a sequence $x_k \to \infty$ with $f(x_k) \to y$).
*   **Jelonek's Theorem** states that if $f$ is dominant, then $S_f$ is either empty or a hypersurface of pure codimension $1$ (a curve in $\mathbb{C}^2$, a surface in $\mathbb{C}^3$).
*   If $S_f$ is empty, $f$ is proper, which forces $f$ to be bijective and hence a polynomial automorphism (proving the conjecture under the properness assumption).
*   For a counterexample to exist, the map must be nonproper, meaning $S_f$ must be non-empty.

In $n = 2$ dimensions, the nonproperness set $S_f$ must be a curve. In $n = 3$ dimensions, it is a surface. The additional degree of freedom in 3D allows the coordinates to escape to infinity in a way that preserves the constant Jacobian condition without restricting the coordinate space too heavily. In 2D, the constant Jacobian constraint:
$$ \det JG = U_x V_y - U_y V_x = \text{constant} $$
is an extremely restrictive global PDE. If the map is nonproper, the branches at infinity must align precisely to satisfy this PDE.

---

## 3. Systematic Verification of Alpöge's 3D Map

Using exact SymPy computation, we verified the 3D map:
$$ P = (1 + xy)^3 z + y^2(1 + xy)(4 + 3xy) $$
$$ Q = y + 3x(1 + xy)^2 z + 3xy^2(4 + 3xy) $$
$$ S = 2x - 3x^2y - x^3z $$

### 3.1 Jacobian Determinant
The Jacobian matrix of $F = (P, Q, S)$ with respect to $(x, y, z)$ has determinant:
$$ \det JF = -2 $$
This is constant and nonzero, confirming that $F$ is a Keller map.

### 3.2 The Nontrivial Fiber
The three distinct points:
$$ p_0 = \left(0, 0, -\frac{1}{4}\right) $$
$$ p_1 = \left(1, -\frac{3}{2}, \frac{13}{2}\right) $$
$$ p_2 = \left(-1, \frac{3}{2}, \frac{13}{2}\right) $$
all map to the single point:
$$ q = \left(-\frac{1}{4}, 0, 0\right) $$

---

## 4. Deep Structural Identities of the 3D Map

### 4.1 The Cusp Identity and the Invariant $K$
Define the target coordinate invariant:
$$ K(P, Q, S) = 27P^2S^2 - 18PQS + 16P + Q^3S - Q^2 $$
And let the cusp coordinates be:
$$ u = 27PS^2 - 9QS + 8 $$
$$ v = 4 - 3QS $$

We verified the beautiful cusp identity:
$$ 27S^2K = u^2 - v^3 $$
This demonstrates that the 3D map is algebraically built around the cusp singularity curve $u^2 = v^3$.

### 4.2 The $S = 0$ Reduction (Near-Miss)
When we restrict to the component $S = 0$ with $x \neq 0$, using the coordinates:
$$ t = \frac{1}{x},\quad r = 2xy + 3 $$
the map reduces to:
$$ P_0 = \frac{t^2(r^2 - 1)}{4} + \frac{1}{4} $$
$$ Q_0 = 2tr $$
The Jacobian determinant of this 2D map is:
$$ \det J(P_0, Q_0) = -t^2 $$
The points $(t, r) = (1, 0)$ and $(-1, 0)$ both map to $(1/4, 0)$, showing a collision. However, the Jacobian is nonconstant and vanishes at $t = 0$. Extending this polynomially to a constant Jacobian map in 2D while preserving the collision is obstructed.

---

## 5. Analysis of 2D Slices and the $L_4$ Block

A prime candidate for a modular search was the quotient block:
$$ L_4 = 9x^2 - 12xy - 9x + 4y^2 + 4y $$
Under the collision points $(0,0)$ and $(1,0)$, we searched for a polynomial companion $Q(x, y)$ such that:
$$ \det J(L_4, Q) = 1 $$

Our search script successfully solved the linear PDE system for Q of varying degrees:
*   At degree 1, we found:
    $$ Q = -\frac{1}{3}y + \frac{1}{2}x $$
*   Calculating the Jacobian gives:
    $$ \det J(L_4, Q) = 1 $$
*   However, substituting $y = \frac{3}{2}x - 3u$ (derived from Q) into $L_4$ gives:
    $$ L_4 = 36u^2 - 12u - 3x $$
    This is linear in $x$ for any fixed $u$. Therefore, the map $(L_4, Q)$ is a **polynomial automorphism** (bijective and injective) and possesses no collisions.

This reinforces the mathematical lesson: **collision is easy to engineer, but satisfying the constant Jacobian condition globally is so restrictive that it forces injective, triangular, or automorphic structures in lower dimensions.**

---

## 6. Conclusion & Summary of Obstructions

*   Alpöge's 3D counterexample represents a major breakthrough in algebraic geometry, proving the Jacobian Conjecture is false for $n \ge 3$.
*   By Jelonek's theorem, any counterexample must have a non-empty nonproperness set. In 2D, this curve restriction on the Jacobian PDE is heavily constrained.
*   Projections, planes, and algebraic coordinates derived from the 3D map invariably collapse the Jacobian determinant to a nonconstant form, or force the resulting 2D map to be injective (an automorphism).
*   Any future search for a 2D counterexample requires looking beyond simple reductions of the 3D map and must deal with non-proper rational coverings where the nonproperness set is a highly non-trivial algebraic curve.
