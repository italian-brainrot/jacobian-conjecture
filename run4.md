# Run 4

## 1. Goal and Current Status

### Goal
Given a reported and symbolically verified 3D polynomial counterexample to the Jacobian conjecture, attempt to discover a **2D polynomial counterexample**:

A polynomial map

\[
G:\mathbb C^2\to\mathbb C^2
\]

such that:

1. Its Jacobian determinant is a nonzero constant.
2. It is not injective, preferably with an explicit collision of two or three distinct points.

### Current Status
- The **3D map passes exact symbolic verification**:
  - Jacobian determinant is constantly `-2`.
  - Three distinct points map to the same image.
- **No 2D counterexample was found** despite many structured searches.
- The searches ruled out a large number of natural reductions, slices, projections, target recombinations, and low-/medium-degree ansätze.
- The problem remains open in our hands; the 2D Jacobian conjecture is historically extremely hard, and a 3D counterexample does not automatically give an easy 2D one.

---

## 2. The Verified 3D Map

The 3D map is:

\[
F(x,y,z) = (P,Q,S)
\]

where

```python
P = (1 + x*y)**3 * z + y**2 * (1 + x*y) * (4 + 3*x*y)
Q = y + 3*x*(1 + x*y)**2 * z + 3*x*y**2 * (4 + 3*x*y)
S = 2*x - 3*x**2*y - x**3*z
```

Equivalently, define

\[
a = 1+xy,\qquad b = 4+3xy.
\]

Then

\[
P = a^3 z + y^2 a b,
\]

\[
Q = y + 3x a^2 z + 3x y^2 b,
\]

\[
S = 2x - 3x^2y - x^3z.
\]

A very useful auxiliary quantity is

\[
M = a^2 z + y^2 b.
\]

Then

\[
P = aM,
\]

\[
Q = y + 3xM,
\]

and one can derive

\[
a^2 S = x(2+xy) - x^3 M.
\]

This `M` formulation was used repeatedly.

---

## 3. Verified 3D Fiber

The three distinct points are:

\[
p_0 = \left(0,0,-\frac14\right),
\]

\[
p_1 = \left(1,-\frac32,\frac{13}{2}\right),
\]

\[
p_2 = \left(-1,\frac32,\frac{13}{2}\right).
\]

They all map to

\[
q = \left(-\frac14,0,0\right).
\]

Exact SymPy verification produced:

```text
Jacobian determinant: -2
Constant nonzero Jacobian? True

Point {x: 0, y: 0, z: -1/4} -> (-1/4, 0, 0)
Point {x: 1, y: -3/2, z: 13/2} -> (-1/4, 0, 0)
Point {x: -1, y: 3/2, z: 13/2} -> (-1/4, 0, 0)

All listed points have the same image? True
```

So, within exact symbolic computation, this is a genuine 3D Keller map with a nontrivial fiber.

---

## 4. Geometry of the Three Preimages

The three points satisfy the linear relation

\[
3x+2y=0.
\]

Thus they lie in the affine plane

\[
y = -\frac32 x.
\]

In that plane, using coordinates `(x,z)`, the points become:

\[
(x,z) = \left(0,-\frac14\right),\quad
\left(1,\frac{13}{2}\right),\quad
\left(-1,\frac{13}{2}\right).
\]

This plane was the first natural 2D slice attempted.

There is also a symmetry:

\[
\sigma(x,y,z)=(-x,-y,z).
\]

One checks:

\[
P\circ\sigma = P,
\]

\[
Q\circ\sigma = -Q,
\]

\[
S\circ\sigma = -S.
\]

So the target involution is

\[
\tau(P,Q,S) = (P,-Q,-S).
\]

The points `p1` and `p2` are exchanged by `σ`; `p0` is fixed.

---

## 5. Attempted Strategy 1: Graph Slices `z = h(x,y)` and Project to `(P,Q)`

### Idea
Choose a polynomial height function `h(x,y)` passing through the three required `z`-values:

\[
h(0,0)=-\frac14,
\]

\[
h\left(1,-\frac32\right)=\frac{13}{2},
\]

\[
h\left(-1,\frac32\right)=\frac{13}{2}.
\]

Then define a 2D map

\[
G(x,y) = \bigl(P(x,y,h(x,y)),\; Q(x,y,h(x,y))\bigr).
\]

The collision is automatic. The question is whether the 2D Jacobian can be constant.

### Quadratic Height Family
A general quadratic height satisfying the interpolation constraints can be written as

\[
h(x,y)
=
-\frac14
+\frac32 Bx
+By
+\left(\frac{27}{4}+\frac32D-\frac94E\right)x^2
+Dxy
+Ey^2.
\]

Several choices were tested, including:

```text
h1 = -1/4 - 4/3 x - 8/9 y - 9/2 xy
h2 = -1/4 - 4/3 x - 8/9 y + 27/4 x^2
h3 = -1/4 - 4/3 x - 8/9 y + 3 y^2
h4 = -1/4 + 27/4 x^2
```

All preserved the collision, but all produced nonconstant Jacobians.

### Structural Observation for `(P,Q)` Graph Slices
Using

\[
M = a^2h(x,y)+y^2b,
\]

the projected map becomes

\[
G(x,y) = (aM,\; y+3xM).
\]

Its Jacobian is

\[
J_G
=
(y-3x)M
+
(a-3x^2M)M_x
-
3MM_y.
\]

A degree argument strongly suggests that no nonconstant polynomial `M` can make this a nonzero constant. In particular, if `deg M = d > 0`, the term

\[
-3x^2MM_x
\]

has degree `2d+1` unless the top homogeneous part of `M` is independent of `x`; then other top-degree terms force contradiction. This explains why many graph-slice attempts using `(P,Q)` failed.

---

## 6. Attempted Strategy 2: The Special Plane `y = -3x/2`

### Idea
Restrict the 3D map to the plane containing all three preimages:

\[
y = -\frac32 x.
\]

Then test projections:

\[
(P,Q),\quad (P,S),\quad (Q,S)
\]

as maps in variables `(x,z)`.

### Result
All three projections preserved the collision but had nonconstant Jacobians.

For example, the projection `(P,Q)` produced a Jacobian of the form:

```text
-729*x**10*z/32 + ... - 3*z + 3/2
```

not constant.

The projections `(P,S)` and `(Q,S)` also failed.

---

## 7. Attempted Strategy 3: Constant Linear Recombination of Minors

### Idea
Given a restricted map

\[
\Phi(u,v) = (F_1,F_2,F_3):\mathbb C^2\to\mathbb C^3,
\]

compute its three 2×2 minors:

\[
M_{12} = \frac{\partial(F_1,F_2)}{\partial(u,v)},
\]

\[
M_{13} = \frac{\partial(F_1,F_3)}{\partial(u,v)},
\]

\[
M_{23} = \frac{\partial(F_2,F_3)}{\partial(u,v)}.
\]

If constants `λ1, λ2, λ3` exist such that

\[
\lambda_1 M_{12}+\lambda_2 M_{13}+\lambda_3 M_{23}=c\neq 0,
\]

then those constants define two linear combinations of `F1,F2,F3` whose 2D Jacobian is constant.

This was tested on:

- the special plane `y=-3x/2`;
- several graph slices `z=h(x,y)`;
- later, many affine planes through pairs of preimages.

### Result
No nonzero constant linear combination of minors was found in the tested families.

For the special plane, this failure can be understood partly: the restricted components are linear in `z`, and their `z`-coefficient functions are essentially independent, forcing any constant-Jacobian linear projection to degenerate.

---

## 8. Attempted Strategy 4: Affine Planes Through Pairs of Preimages

### Idea
A 2D counterexample only needs two colliding points, not all three. So we searched affine planes through pairs:

- `p0` and `p1`;
- `p0` and `p2`;
- `p1` and `p2`.

A plane was parametrized as

\[
X(u,v)=p+u(q-p)+vs,
\]

where `s` is a direction vector.

For each plane, we searched for constants `λ1,λ2,λ3` such that the corresponding minor combination is constant.

### Search Range
The user ran at least:

```python
max_per_pair = 12
direction_limit = 2
```

and also:

```python
max_per_pair = 24
direction_limit = 3
```

### Result
No passing affine-plane candidate was found.

This rules out many simple linear sections through two fiber points with linear target projections.

---

## 9. Attempted Strategy 5: Nonlinear Target-Polynomial Recombinations on the Special Plane

### Idea
On the special plane, define shifted target functions

\[
A = P+\frac14,\qquad B=Q,\qquad C=S.
\]

At the three preimages,

\[
(A,B,C)=(0,0,0).
\]

Any polynomial `f(A,B,C)` and `g(A,B,C)` without constant term automatically preserves the collision.

We searched for pairs

\[
G(x,z)=\bigl(f(A,B,C),g(A,B,C)\bigr)
\]

with constant Jacobian.

### Direct Degree-2 Candidates
Examples tested:

```text
(A + B^2, B + C^2)
(A + C^2, B + A*C)
(A + B*C, B + C^2)
(A + B^2 + C^2, B + A*C)
(A + B^2, C + A*B)
```

All failed.

### Linear-Fixed Search
We also fixed `f` to be linear-plus-quadratic, for example:

```text
f = A + B^2
f = A + C^2
f = A + B*C
f = A + B^2 + C^2
f = A + A^2
f = A + A^2 + B*C
```

and solved linearly for `g` of degree ≤ 2.

No solution was found.

---

## 10. Attempted Strategy 6: Parity-Respecting Target Polynomials

### Observation
On the plane `y=-3x/2`, under `x -> -x`:

- `A = P+1/4` is even;
- `B = Q` is odd;
- `C = S` is odd.

A constant Jacobian is even. Therefore a natural candidate should have one even component and one odd component.

### Search
We searched maps where:

\[
f(A,B,C) \text{ is even},
\]

\[
g(A,B,C) \text{ is odd}.
\]

The odd basis up to degree 3 was:

```text
B, C,
A B, A C,
A^2 B, A^2 C,
B^3, B^2 C, B C^2, C^3
```

Fixed even `f` candidates included:

```text
A + B^2
A + C^2
A + B*C
A + B^2 + C^2
A + B^2 - C^2
A + 2*B*C
A + A^2
A + A^2 + B*C
A + A*B*C
```

No passing candidate was found.

---

## 11. Attempted Strategy 7: Reduction from the Surface `S=0`

This was one of the most promising structural reductions.

### Derivation
On the target plane `S=0`, the preimage has a component with `x ≠ 0`.

Use variables

\[
t = \frac1x,\qquad s=xy,\qquad r = 2s+3.
\]

On the `S=0` component, the target coordinates `(P,Q)` become:

\[
P = \frac{t^2(r^2-1)}{4},
\]

\[
Q = 2tr.
\]

After shifting `P` by `1/4`, define

\[
P_0 = \frac{t^2(r^2-1)}{4}+\frac14,
\]

\[
Q_0 = 2tr.
\]

Then the two points

\[
(t,r)=(1,0),\quad (-1,0)
\]

both map to `(0,0)`.

The Jacobian is

\[
\operatorname{Jac}(P_0,Q_0) = -t^2.
\]

So this map already has the desired collision, but its Jacobian is not constant; it vanishes at `t=0`.

### Even/Odd Deformation Ansatz
Because the map is even/odd under `t -> -t`, we searched maps of the form

\[
G(t,r)=\bigl(F(t^2,r),\; tH(t^2,r)\bigr).
\]

Let

\[
X=t^2.
\]

The Jacobian condition is

\[
2X F_X H_r - F_r H - 2X F_r H_X = c.
\]

Collision conditions:

\[
F(1,0)=0,
\]

\[
H(1,0)=0.
\]

To avoid Jacobian degeneracy at `t=0`, one also wants

\[
H(0,0)\neq 0.
\]

### Fixed-`H` Search
Many families of `H` were tried, for example:

```text
H = 1 - X + m X r
H = 1 - X + m X r^2
H = 1 - X + m r^2
H = 1 - X + m (X-1) r
H = 1 - X + m (X^2 - X)
```

with many rational values of `m`.

The user even tried:

```python
F_DEGREE = 20
MAX_H = 100
```

No polynomial `F` was found for any tested `H`.

### Interpretation
The `S=0` reduction gives a very simple map from something like \(\mathbb C^*\times\mathbb C\) with Jacobian `-t^2`. The obstruction is extending it polynomially across `t=0` while keeping the Jacobian nonzero and preserving the collision. The attempted even/odd polynomial extensions did not exist in the searched families.

---

## 12. Attempted Strategy 8: Direct 2D Search with a Fixed First Component `P(x,y)`

### Idea
Forget the 3D map for a moment and search directly for a 2D map

\[
G(x,y)=(P(x,y),Q(x,y))
\]

with

\[
P(0,0)=P(1,0)=0,
\]

\[
Q(0,0)=Q(1,0)=0,
\]

and

\[
P_xQ_y-P_yQ_x=1.
\]

For a fixed `P`, this is a linear PDE for `Q`.

### Tested `P` Families
Examples included Danielewski-type polynomials:

```text
P = x^2 y + x(x-1)
P = x^2 y + x(x-1) + y^2
P = x^2 y + x(x-1) - y^2
P = x^2 y + x(x-1) + x y^2
```

and many deformations:

```text
P = x(x-1) + y(1 + a x + b y)
P = x(x-1) + y(1 + a x + b y + c x y)
```

Also:

```text
P = (x^2+1)^2 y + x(x-1)
```

### Search Degree
The user ran:

```python
Q_DEGREE = 20
MAX_P = 100
```

No polynomial `Q` was found.

### Example Obstruction
For

\[
P=x^2y+x(x-1),
\]

the PDE

\[
P_xQ_y-P_yQ_x=1
\]

has characteristic equations leading locally to

\[
Q = \frac1x + \phi(P),
\]

which is not polynomial. This explains the failure for that family.

---

## 13. Attempted Strategy 9: Level Surface `P = -1/4`

This was the last major reduction attempted.

### Idea
Use the target level surface

\[
P=-\frac14,
\]

which contains the whole triple fiber.

On this surface, solve for `z` rationally and express `Q` and `S` in terms of `x,y`.

Let

\[
a=1+xy.
\]

On `P=-1/4`, one obtains:

\[
Q = y - \frac{3x}{4a},
\]

\[
S = \frac{x(2+xy)}{a^2}+\frac{x^3}{4a^3}.
\]

Clearing denominators gives polynomial building blocks:

\[
Q_0 = aQ = y+xy^2-\frac34x,
\]

\[
S_0 = a^3S = x(2+xy)(1+xy)+\frac14x^3.
\]

Both vanish at the three projected preimages:

\[
(0,0),\quad (1,-3/2),\quad (-1,3/2).
\]

### Tested Maps
We tested simple scaled pairs:

\[
G_{i,j}(x,y)=\bigl(Q_0a^i,\;S_0a^j\bigr)
\]

for `0 ≤ i,j ≤ 4`.

All failed.

We also searched linear spans:

\[
U = Q_0a^i,
\]

\[
V = S_0(c_0+c_1a+\cdots+c_da^d),
\]

and the reverse:

\[
V = S_0a^j,
\]

\[
U = Q_0(c_0+c_1a+\cdots+c_da^d).
\]

No solution was found in the tested ranges.

---

## 14. Summary of Negative Results

The following classes were searched and produced **no 2D counterexample**:

1. Polynomial graph slices `z=h(x,y)` projecting to `(P,Q)`.
2. The special plane `y=-3x/2` with projections `(P,Q)`, `(P,S)`, `(Q,S)`.
3. Constant linear combinations of minors on those slices.
4. Affine planes through pairs of preimages, with many direction vectors, and linear target projections.
5. Degree-2 polynomial recombinations of target components `(A,B,C)=(P+1/4,Q,S)`.
6. Linear-fixed target-polynomial searches with `f` linear-plus-quadratic and `g` degree ≤ 2.
7. Parity-respecting even/odd target-polynomial searches with odd `g` up to degree 3.
8. The `S=0` reduced map and extensive even/odd deformation searches, including `F_DEGREE=20`.
9. Direct 2D searches solving `P_xQ_y-P_yQ_x=1` for many Danielewski-type `P`, with `Q_DEGREE=20`.
10. The `P=-1/4` level-surface building blocks `Q0,S0`, scaled pairs, and linear span searches.

---

## 15. Important Mathematical Lessons Learned

### 15.1 Collision Is Easy; Constant Jacobian Is Extremely Restrictive
Many maps can be forced to collide at the desired points by interpolation or by using target polynomials vanishing at the common fiber. But making the Jacobian constant is a severe global PDE condition.

### 15.2 Linear-in-`z` First Components Are Obstructed
If a 2D first component has the form

\[
F_1(x,z)=A(x)z+B(x)
\]

with nonconstant `A(x)`, then there is generally no polynomial `H(x,z)` such that

\[
\{F_1,H\}=1.
\]

A coefficient argument using expansion in powers of `z` shows that the constant term of the bracket is divisible by `A(x)`, preventing a nonzero constant.

This explains many failures involving projections that remain linear in one variable.

### 15.3 If a Component Is a Coordinate, the Map Is Usually Triangular/Automorphic
If one can make a component with `∂/∂z = 1`, then it is often a coordinate, and any constant-Jacobian partner tends to force a triangular automorphism, preventing collisions.

For example, on the plane slice we constructed a Bezout combination `U` with `U_z=1`. The map `(U,2x)` had constant Jacobian `-2`, but the points did not collide. More generally, if `U_z=1`, then in coordinates `(x,U)`, a constant-Jacobian partner must be of the form

\[
V = -cx+\phi(U),
\]

which is injective in `x`.

### 15.4 The `S=0` Reduction Produces a Near-Miss
The reduced map

\[
(P,Q)=\left(\frac{t^2(r^2-1)}4+\frac14,\;2tr\right)
\]

has the collision but Jacobian `-t^2`.

The obstruction is the vanishing at `t=0`, which corresponds to a boundary/component at infinity. Polynomially extending across `t=0` without losing the collision appears nontrivial or impossible in the searched ansätze.

### 15.5 The `P=-1/4` Surface Is Still Worth Investigating
The level surface

\[
P=-\frac14
\]

contains the full fiber and gives simple rational expressions for `Q` and `S`. Clearing denominators produced polynomial building blocks, but the simple scaled pairs and linear spans failed.

However, this surface may still have a nontrivial polynomial parametrization or a more sophisticated pair of polynomial functions with constant Jacobian.

---

## 16. Key Formulas for Future Work

### 16.1 3D Map
```python
P = (1 + x*y)**3 * z + y**2 * (1 + x*y) * (4 + 3*x*y)
Q = y + 3*x*(1 + x*y)**2 * z + 3*x*y**2 * (4 + 3*x*y)
S = 2*x - 3*x**2*y - x**3*z
```

### 16.2 Useful Auxiliary `M`
\[
M=(1+xy)^2z+y^2(4+3xy).
\]

Then:

\[
P=(1+xy)M,
\]

\[
Q=y+3xM,
\]

\[
(1+xy)^2S=x(2+xy)-x^3M.
\]

### 16.3 Special Plane
\[
y=-\frac32x.
\]

Points:

\[
(x,z)=\left(0,-\frac14\right),\quad
\left(1,\frac{13}{2}\right),\quad
\left(-1,\frac{13}{2}\right).
\]

### 16.4 `S=0` Reduced Map
Let

\[
t=1/x,\qquad r=2xy+3.
\]

Then on the `S=0`, `x≠0` component:

\[
P=\frac{t^2(r^2-1)}4,
\]

\[
Q=2tr.
\]

Shifted:

\[
P_0=\frac{t^2(r^2-1)}4+\frac14,
\]

\[
Q_0=2tr.
\]

Jacobian:

\[
\operatorname{Jac}(P_0,Q_0)=-t^2.
\]

Collision:

\[
(1,0),\;(-1,0)\mapsto (0,0).
\]

### 16.5 Even/Odd Deformation PDE
For

\[
G(t,r)=\bigl(F(t^2,r),tH(t^2,r)\bigr),
\]

with `X=t^2`, the Jacobian is

\[
2X F_XH_r-F_rH-2XF_rH_X.
\]

We want this to be a nonzero constant.

### 16.6 `P=-1/4` Surface Building Blocks
Let

\[
a=1+xy.
\]

On `P=-1/4`:

\[
Q = y-\frac{3x}{4a},
\]

\[
S = \frac{x(2+xy)}{a^2}+\frac{x^3}{4a^3}.
\]

Polynomial building blocks:

\[
Q_0 = y+xy^2-\frac34x,
\]

\[
S_0 = x(2+xy)(1+xy)+\frac14x^3.
\]

Both vanish at:

\[
(0,0),\quad (1,-3/2),\quad (-1,3/2).
\]

---

## 17. Suggested Next Directions for a Fresh Agent

### 17.1 Independently Verify the 3D Map
Before investing further in 2D reduction, verify the 3D map using another CAS if possible:

- SymPy already verifies it.
- Try Singular, Magma, Sage, or Mathematica.
- Check not only the determinant and the three points, but also:
  - distinctness of the points;
  - generic fiber degree;
  - whether the map is dominant/finite/generically étale;
  - possible hidden rational inverse branches.

### 17.2 Compute the Generic Degree and Monodromy
The map has at least three preimages over `q`. Determine:

- Is the generic fiber degree 3?
- Are there more preimages generically?
- What is the Galois/monodromy group?
- Is there a deck transformation or correspondence permuting branches?

This may reveal a quotient or lower-dimensional construction.

### 17.3 Use Resultants to Eliminate Variables
Try eliminating `y,z` to get a minimal polynomial for `x` over the target field:

\[
\mathbb C(P,Q,S).
\]

Similarly for `M`, `xy`, or other symmetric combinations.

A cubic relation with explicit coefficients may suggest a 2D map.

### 17.4 Investigate the Surface `P=-1/4` More Deeply
The surface

\[
P=-\frac14
\]

contains the full fiber. Important questions:

1. Is this surface isomorphic to \(\mathbb C^2\)?
2. Can it be polynomially parametrized?
3. If so, what are the pulled-back functions `Q` and `S` in those coordinates?
4. Does some polynomial pair on that surface have constant Jacobian?

The simple `(x,y)` parametrization with rational `z` produced `Q0,S0`, but perhaps a different polynomial coordinate system on the surface works.

### 17.5 Search Non-Affine Surfaces Through the Fiber
Previous surface searches used:

- affine planes;
- graph slices `z=h(x,y)`;
- target level surfaces `S=0`, `Q=0`, `P=-1/4`.

A more general approach:

\[
\phi(u,v) = p_0 + u(p_1-p_0)+v(p_2-p_0)+\text{higher-degree terms}
\]

and search for polynomial surfaces plus target recombinations such that the pulled-back 2-form is constant.

This is a PDE/constraint system but may be tractable with low-degree ansätze and Gröbner bases.

### 17.6 Use Full Nonlinear Low-Degree Solvers
Many searches fixed one component and solved linearly for the other. A fresh agent could try fully nonlinear systems:

- normalized 2D maps with prescribed collisions;
- low total degree, e.g. degree 3, 4, or 5;
- use HomotopyContinuation.jl, Bertini, PHCpack, or numerical algebraic geometry;
- then attempt rational reconstruction.

For example, search directly for

\[
F(x,y)=(P,Q)
\]

with:

\[
F(0,0)=F(1,0)=F(0,1)=(0,0),
\]

and

\[
\det JF=1.
\]

This is a quadratic coefficient system. It may be large but could be approachable with homotopy methods.

### 17.7 Finite-Field and Modular Searches
Search over finite fields for maps with:

- constant nonzero Jacobian modulo `p`;
- prescribed collisions modulo `p`.

Then attempt to lift patterns to characteristic zero.

This is heuristic but may reveal low-degree structures invisible to rational ansätze.

### 17.8 Explore the Symmetry Quotient
The map has symmetry:

\[
(x,y,z)\mapsto(-x,-y,z),
\]

and target symmetry:

\[
(P,Q,S)\mapsto(P,-Q,-S).
\]

The quotient may reduce dimension or reveal invariant polynomial combinations that produce a lower-dimensional étale map.

Invariant source coordinates include:

\[
x^2,\quad xy,\quad y^2,\quad z.
\]

Invariant target coordinates include:

\[
P,\quad Q^2,\quad QS,\quad S^2.
\]

A careful quotient analysis may produce a 2D map on a surface or invariant subvariety.

### 17.9 Check Whether a Theorem Gives 3D ⇒ 2D
Investigate the literature carefully:

- Does a counterexample in dimension 3 imply one in dimension 2?
- Are there known reductions from Keller maps in dimension `n` to dimension `2` under additional fiber assumptions?
- Are there results about maps with small fibers, e.g. degree 3, that force a plane section counterexample?

If such a theorem exists, it may provide a constructive path.

---

## 18. Things Probably Not Worth Repeating

A fresh agent should probably **not** repeat the following unless using a much larger computational method:

1. Simple graph slices `z=h(x,y)` with projection `(P,Q)` and low-degree `h`.
2. Simple plane slice `y=-3x/2` with projections `(P,Q)`, `(P,S)`, `(Q,S)`.
3. Constant linear minor combinations on the special plane.
4. Low-degree target-polynomial pairs in `(A,B,C)=(P+1/4,Q,S)` with degree ≤ 2.
5. Parity-respecting target-polynomial search with odd degree ≤ 3 and fixed even `f` from the tested list.
6. The specific `S=0` even/odd fixed-`H` families already tested up to degree 20.
7. Direct 2D fixed-`P` linear PDE search for the listed Danielewski-type `P` families up to `Q` degree 20.
8. Simple scaled pairs `(Q0*a^i, S0*a^j)` from the `P=-1/4` surface for small `i,j`.

These are not logically impossible in all generality, but they have been heavily explored and appear unpromising without a new structural insight.

---

## 19. Final Conclusion

The 3D map is symbolically verified as a Keller map with a triple fiber. Many natural routes to a 2D counterexample were explored:

- plane slices;
- graph slices;
- affine plane sections;
- linear and nonlinear target recombinations;
- symmetry/parity restrictions;
- reductions from `S=0` and `P=-1/4`;
- direct 2D PDE searches.

None produced a 2D polynomial map with constant nonzero Jacobian and an explicit collision.

The most promising remaining directions are deeper algebraic-geometric analysis of the 3D map:

- compute its generic fiber and monodromy;
- analyze the surface `P=-1/4`;
- search for polynomial parametrizations of relevant surfaces;
- use resultants/minimal polynomials;
- use numerical algebraic geometry or finite-field searches for low-degree 2D maps;
- investigate whether the known 3D counterexample can be formally reduced to dimension 2.

The problem remains open in this experimental pipeline.
