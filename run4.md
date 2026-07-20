# Run 4

## 1. Mission

We are trying to discover a **two-dimensional polynomial counterexample** to the Jacobian conjecture over `C`:

A polynomial map

```text
G : C^2 -> C^2
G(x,y) = (P(x,y), Q(x,y))
```

such that:

1. The Jacobian determinant

```text
J = P_x Q_y - P_y Q_x
```

is a nonzero constant, e.g. `1` or `-2`.

2. The map is not injective. Ideally we want an explicit collision of two or three distinct points, e.g.

```text
G(0,0) = G(1,0)
```

or

```text
G(-1,0) = G(0,0) = G(1,0).
```

The motivation is that a **3D polynomial Keller map with a nontrivial fiber** has been symbolically verified. We are trying to use its structure to find a 2D counterexample.

No 2D counterexample has yet been found. The 2D Jacobian conjecture is extremely hard, and a 3D counterexample does not automatically imply an easy 2D one.

---

## 2. The Verified 3D Map

The verified 3D map is

```text
F(x,y,z) = (P,Q,S)
```

where

```text
P = (1 + x y)^3 z + y^2 (1 + x y)(4 + 3 x y)

Q = y + 3 x (1 + x y)^2 z + 3 x y^2 (4 + 3 x y)

S = 2 x - 3 x^2 y - x^3 z
```

It is useful to define

```text
a = 1 + x y
b = 4 + 3 x y
M = a^2 z + y^2 b
```

Then

```text
P = a M
Q = y + 3 x M
a^2 S = x(2 + x y) - x^3 M
```

Exact SymPy verification gives:

```text
det Jac(F) = -2
```

and the three distinct points

```text
p0 = (0, 0, -1/4)
p1 = (1, -3/2, 13/2)
p2 = (-1, 3/2, 13/2)
```

all map to

```text
q = (-1/4, 0, 0).
```

So this is a genuine 3D polynomial Keller map with a triple fiber, at least symbolically.

---

## 3. Geometry and Symmetry of the 3D Fiber

The three preimages satisfy

```text
3 x + 2 y = 0,
```

so they lie in the affine plane

```text
y = -3 x / 2.
```

In that plane, using coordinates `(x,z)`, the points are

```text
(x,z) = (0, -1/4), (1, 13/2), (-1, 13/2).
```

There is also a source symmetry

```text
σ(x,y,z) = (-x,-y,z)
```

with target action

```text
τ(P,Q,S) = (P,-Q,-S).
```

Under this symmetry:

```text
P ∘ σ = P
Q ∘ σ = -Q
S ∘ σ = -S
```

The points `p1` and `p2` are exchanged by `σ`; `p0` is fixed.

---

## 4. Major Algebraic Discoveries

### 4.1 Generic fiber cubic

Define the target polynomial

```text
K(P,Q,S) =
    27 P^2 S^2
  - 18 P Q S
  + 16 P
  + Q^3 S
  - Q^2.
```

Then the source coordinate `x` satisfies the cubic equation

```text
K x^3 + (4 - 3 Q S) x - 2 S = 0.
```

Equivalently, with

```text
B = 4 - 3 Q S
C = -2 S
```

the generic fiber is described by the depressed cubic

```text
K x^3 + B x + C = 0.
```

At the special target point `q = (-1/4,0,0)`:

```text
K = -4
B = 4
C = 0
```

so

```text
-4 x^3 + 4 x = 0
```

with roots

```text
x = -1, 0, 1.
```

This matches the three preimages.

This strongly suggests that the generic fiber degree of the 3D map is exactly `3`.

---

### 4.2 Discriminant square and the cusp structure `u^2 - v^3`

The discriminant of the cubic is highly structured. One has the exact identity

```text
27 K C^2 + 4 B^3 = 4 (27 P S^2 - 9 Q S + 8)^2.
```

Using

```text
u = 27 P S^2 - 9 Q S + 8
v = 4 - 3 Q S
```

this becomes

```text
27 S^2 K = u^2 - v^3.
```

So the 3D map is algebraically organized around the cusp-type relation

```text
u^2 = v^3
```

deformed by the factor `27 S^2 K`.

This is one of the most important structural clues.

---

### 4.3 The `S = 0` near-miss

On the target plane `S = 0`, there is a component with `x ≠ 0`. Using

```text
t = 1/x
r = 2 x y + 3
```

the map reduces to

```text
P0 = t^2 (r^2 - 1)/4 + 1/4
Q0 = 2 t r
```

The two points

```text
(t,r) = (1,0), (-1,0)
```

both map to `(0,0)`.

But the Jacobian is

```text
Jac(P0,Q0) = -t^2.
```

So this has the desired collision but the Jacobian vanishes at `t = 0`. This is a very suggestive near-miss: the obstruction is extending polynomially across `t = 0` without destroying the collision.

Many even/odd deformation searches were performed on this ansatz, with no success.

---

### 4.4 The `P = -1/4` surface

The target level surface

```text
P = -1/4
```

contains the full triple fiber.

On this surface, with `a = 1 + x y`, one obtains rational expressions

```text
Q = y - 3 x / (4 a)

S = x(2 + x y)/a^2 + x^3/(4 a^3).
```

Clearing denominators gives polynomial building blocks

```text
Q0 = y + x y^2 - 3 x / 4

S0 = x(2 + x y)(1 + x y) + x^3 / 4.
```

Both vanish at the projected fiber points

```text
(0,0), (1,-3/2), (-1,3/2).
```

However, the rational map `(Q0,S0)` has Jacobian

```text
Jac(Q,S) = -2 / (1 + x y)^3.
```

Thus the surface carries a rational 2-form with a pole along

```text
1 + x y = 0.
```

This explains why simple polynomial pairs built from `Q0`, `S0`, and powers of `a` failed. The surface is likely not isomorphic to `C^2`; it behaves more like a Danielewski-type or cubic-cover surface.

---

### 4.5 The `Q = 0` surface

The surface

```text
Q = 0
```

also contains the full fiber.

A useful parametrization uses variables `(x,M)`, where

```text
M = a^2 z + y^2 b.
```

On `Q = 0`, one has

```text
y = -3 x M
a = 1 - 3 x^2 M.
```

Then

```text
P = a M
S = 2 x (1 - 2 x^2 M) / a^2.
```

The shifted target coordinate

```text
A = P + 1/4
```

and the cleared denominator quantity

```text
N = a^2 S = 2 x (1 - 2 x^2 M)
```

become polynomial in `(x,M)`:

```text
A = M - 3 x^2 M^2 + 1/4
N = 2 x (1 - 2 x^2 M).
```

The three fiber points become

```text
(x,M) = (0,-1/4), (1,1/2), (-1,1/2).
```

This gave a natural even/odd coordinate system:

```text
U(x,M) = F(x^2, M)
V(x,M) = x H(x^2, M)
```

with Jacobian condition

```text
2 X F_X H_M - F_M H - 2 X F_M H_X = constant,
X = x^2.
```

Many searches in this coordinate system failed, both in the subring generated by `(A,a,N)` and in the full polynomial ring in `(X,M)`.

---

## 5. Main Classes of Attempts and Their Outcomes

### 5.1 Graph slices `z = h(x,y)`

We tried polynomial height functions `h(x,y)` interpolating the three fiber `z`-values, then projected to `(P,Q)`.

Examples included quadratic heights such as

```text
h = -1/4 - 4/3 x - 8/9 y - 9/2 x y
h = -1/4 - 4/3 x - 8/9 y + 27/4 x^2
h = -1/4 + 27/4 x^2
```

All preserved the collision but produced nonconstant Jacobians.

A structural degree argument shows that for

```text
G(x,y) = (a M, y + 3 x M)
```

with

```text
M = a^2 h(x,y) + y^2 b,
```

the term

```text
-3 x^2 M M_x
```

obstructs constant Jacobian for nonconstant polynomial `M`.

---

### 5.2 Special plane `y = -3 x / 2`

We restricted to the plane containing the three preimages and tested projections

```text
(P,Q), (P,S), (Q,S)
```

in coordinates `(x,z)`.

All projections preserved the collision but had nonconstant Jacobians.

We also searched constant linear combinations of the three minors of the restricted map

```text
Φ(x,z) = (A,B,C) = (P+1/4, Q, S).
```

No constant nonzero minor combination was found.

---

### 5.3 Affine planes through pairs of preimages

Since a 2D counterexample only needs two colliding points, we searched affine planes through pairs:

```text
p0,p1
p0,p2
p1,p2
```

with many direction vectors, and looked for constant linear combinations of minors.

No candidate passed.

---

### 5.4 Nonlinear target-polynomial recombinations

On the special plane, with

```text
A = P + 1/4
B = Q
C = S
```

we searched for polynomial pairs

```text
G(x,z) = (f(A,B,C), g(A,B,C))
```

with constant Jacobian.

Tested families included:

```text
(A + B^2, B + C^2)
(A + C^2, B + A C)
(A + B C, B + C^2)
(A + B^2 + C^2, B + A C)
(A + B^2, C + A B)
```

and many linear-fixed searches where `f` was fixed and `g` solved linearly.

No solution was found.

---

### 5.5 Parity-respecting target polynomials

Under `x -> -x` on the special plane:

```text
A is even
B is odd
C is odd
```

A constant Jacobian is even, so we searched maps with one even and one odd component.

Odd basis up to degree 3 included:

```text
B, C,
A B, A C,
A^2 B, A^2 C,
B^3, B^2 C, B C^2, C^3.
```

No passing candidate was found.

---

### 5.6 `S = 0` even/odd deformations

The `S=0` reduced map

```text
P0 = t^2(r^2 - 1)/4 + 1/4
Q0 = 2 t r
```

has Jacobian `-t^2`.

We searched maps of the form

```text
G(t,r) = (F(t^2,r), t H(t^2,r))
```

with

```text
X = t^2
```

and Jacobian condition

```text
2 X F_X H_r - F_r H - 2 X F_r H_X = constant.
```

Collision conditions:

```text
F(1,0) = 0
H(1,0) = 0
H(0,0) ≠ 0.
```

Many fixed-`H` searches were performed, including degrees up to `20` for `F`. No polynomial solution was found.

---

### 5.7 Direct 2D fixed-`P` searches

We searched directly for maps

```text
G(x,y) = (P(x,y), Q(x,y))
```

with collisions and

```text
P_x Q_y - P_y Q_x = 1.
```

For fixed `P`, this is a linear PDE for `Q`.

Tested `P` families included Danielewski-type polynomials:

```text
P = x^2 y + x(x-1)
P = x^2 y + x(x-1) + y^2
P = x^2 y + x(x-1) - y^2
P = x^2 y + x(x-1) + x y^2
```

and many deformations.

No polynomial `Q` was found up to degree `20`.

For example, for

```text
P = x^2 y + x(x-1),
```

the local solution behaves like

```text
Q = 1/x + φ(P),
```

which is not polynomial.

---

### 5.8 Target-polynomial graph coordinates

We searched for a polynomial

```text
H(A,B,C)
```

in shifted target coordinates

```text
A = P + 1/4
B = Q
C = S
```

such that after pullback by the 3D map,

```text
∂H/∂z = 1.
```

If such an `H` exists, then `H = 0` defines a polynomial graph `z = h(x,y)`.

Degree `≤ 2` search found nothing.

A targeted degree-3 search using the cusp generator

```text
B^3 + 27 A^2 C
```

plus quadratics and linears also found nothing.

---

### 5.9 Factoring `K + 4`

Because the fiber has `K = -4`, we examined

```text
K_pullback + 4.
```

Using the simplified pullback

```text
K_pull =
  -9 x^2 (1 + x y)^2 z^2
  + (16 + 6 x y - 18 x^2 y^2 (4 + 3 x y)) z
  + y^2 (63 - 54 x y - 81 x^2 y^2),
```

we factored

```text
K_pull + 4
```

and tested whether any factor defines a polynomial graph through at least two fiber points.

The polynomial was irreducible in the relevant sense, and no useful graph factor was found.

---

### 5.10 Modular and finite-field searches

We performed many modular searches for direct 2D maps with collisions.

For triple collision at

```text
(-1,0), (0,0), (1,0)
```

the ideal is

```text
(y, x^3 - x).
```

For two-point collision at

```text
(0,0), (1,0)
```

the ideal is

```text
(y, x(x-1)).
```

Some characteristic-3 modular hits appeared, for example

```text
P = 2 x^3 y + 2 x^3 - 2 x + 2 y^3
Q = y
```

modulo `3`.

This works modulo `3` because

```text
d(x^3)/dx = 0 mod 3.
```

These are Frobenius-type artifacts and did not lift to characteristic zero.

---

### 5.11 The quotient block `L4`

From the `P = -1/4` quotient invariants, one obtains a two-point building block. After a linear change placing the projected points at

```text
(0,0), (1,0),
```

and clearing denominators, one gets

```text
L4 = 9 x^2 - 12 x y - 9 x + 4 y^2 + 4 y.
```

This polynomial vanishes at `(0,0)` and `(1,0)`.

It is the strongest modular signal found.

For fixed

```text
P = L4,
```

we searched for `Q` in the ideal

```text
(y, x(x-1))
```

such that

```text
P_x Q_y - P_y Q_x = 1.
```

Results:

```text
deg Q <= 5: modular solution mod 5 only
deg Q <= 6: modular solution mod 5 only
deg Q <= 7: modular solutions mod 5 and mod 7
deg Q <= 8: modular solutions mod 5 and mod 7
```

No modular solution was found modulo `11` or `13` in the tested degrees.

No rational `QQ` solution was found for degrees `≤ 7`.

Hensel lifting attempts modulo `5` and `7` for degrees `7` and `8` failed with the implemented solver.

Small deterministic deformations of `L4` mostly destroyed even the modular solutions, except for some modulo `5` solutions when changing the `y` coefficient. Those also failed to lift.

---

### 5.12 Numerical degree-3 direct search

We set up a full nonlinear degree-3 ansatz for two-point collision.

Let

```text
f = x(x-1).
```

Write

```text
P = y * (degree ≤ 2 polynomial) + f * (degree ≤ 1 polynomial)
Q = y * (degree ≤ 2 polynomial) + f * (degree ≤ 1 polynomial)
```

This gives `18` coefficients. After normalizing three local derivative coefficients, one obtains `15` unknowns and `15` Jacobian coefficient equations.

SymPy `nsolve` repeatedly failed with:

```text
matrix is numerically singular
```

This suggests either no isolated low-degree solution exists in that normalization, or the system is badly conditioned / has no solution near the random starts. A proper homotopy-continuation implementation is still worth trying.

---

## 6. Important Mathematical Obstructions Learned

### 6.1 Collision is easy; constant Jacobian is extremely restrictive

It is easy to build polynomial maps that vanish at two or three desired points. The hard part is making the Jacobian determinant a nonzero constant everywhere.

---

### 6.2 Linear-in-one-variable first components are obstructed

If a component has the form

```text
F1(x,z) = A(x) z + B(x)
```

with nonconstant `A(x)`, then there is generally no polynomial partner `F2(x,z)` such that

```text
{F1,F2} = constant.
```

A coefficient argument in powers of `z` forces divisibility by `A(x)`, preventing a nonzero constant.

This explains many failed projections from slices.

---

### 6.3 If a component is too coordinate-like, the map becomes injective

If one can construct a component `U` with

```text
U_z = 1,
```

then `U` is essentially a coordinate. A constant-Jacobian partner often becomes triangular:

```text
V = -c x + φ(U),
```

which is injective in `x`. Thus the collision is lost.

---

### 6.4 The `S=0` reduction has a boundary obstruction

The reduced map

```text
(P0,Q0) = (t^2(r^2-1)/4 + 1/4, 2 t r)
```

has collision but Jacobian

```text
-t^2.
```

The zero at `t = 0` corresponds to a boundary/component at infinity. Polynomially extending across this point while preserving collision and nonzero constant Jacobian appears highly nontrivial.

---

### 6.5 The `P=-1/4` surface has a rational 2-form pole

On `P=-1/4`, the natural rational map has Jacobian

```text
-2 / (1 + x y)^3.
```

The pole along `1 + x y = 0` prevents simple polynomial coordinate systems from working.

---

### 6.6 Finite étale covers of `A^2` are trivial

Any polynomial map with constant nonzero Jacobian is étale. If it were also finite/proper, then it would be a finite étale cover of `A^2`, hence trivial because `A^2` is simply connected.

Therefore any 2D counterexample must be non-finite/non-proper. In cubic-ansatz language, the leading coefficient of the cubic relation must vanish somewhere, corresponding to roots escaping to infinity.

---

## 7. Current Best Structural Clues

The most important clues are:

1. **The 3D map has generic fiber degree 3.**

   The source coordinate `x` satisfies

   ```text
   K x^3 + (4 - 3 Q S) x - 2 S = 0.
   ```

2. **The cubic discriminant is a square up to `K`.**

   With

   ```text
   u = 27 P S^2 - 9 Q S + 8
   v = 4 - 3 Q S
   ```

   one has

   ```text
   27 S^2 K = u^2 - v^3.
   ```

3. **The `S=0` reduction gives a near-miss with Jacobian `-t^2`.**

4. **The `P=-1/4` surface is a cubic-cover/Danielewski-type surface, not obviously `C^2`.**

5. **The quotient block `L4` has genuine modular solutions modulo `5` and `7`, but no known characteristic-zero lift.**

---

## 8. What Has Been Ruled Out, At Least in Tested Families

The following have been heavily explored and should not be repeated without a substantially new idea or much larger computational method:

1. Simple graph slices `z = h(x,y)` projecting to `(P,Q)` with low-degree `h`.

2. The special plane `y = -3 x / 2` with projections `(P,Q)`, `(P,S)`, `(Q,S)`.

3. Constant linear minor combinations on that plane.

4. Low-degree target-polynomial pairs in `(A,B,C) = (P+1/4,Q,S)` up to degree `2`.

5. Parity-respecting target-polynomial searches with odd degree `≤ 3` and fixed even `f` from the tested lists.

6. The specific `S=0` even/odd fixed-`H` families already tested up to degree `20`.

7. Direct fixed-`P` linear PDE searches for the listed Danielewski-type `P` families up to `Q` degree `20`.

8. Simple scaled pairs

   ```text
   (Q0 a^i, S0 a^j)
   ```

   from the `P=-1/4` surface for small `i,j`.

9. Low-degree target-polynomial graph coordinates `H(A,B,C)` with `H_z = 1` up to degree `2`, and the targeted cusp-degree-3 family.

10. Simple factor searches of `K + 4`.

11. Basic random modular pair searches in low degree without structural guidance.

12. Simple Hensel lifting of the `L4` modular solutions using the current fixed-free-variable solver; this failed for degrees `7` and `8` modulo `5` and `7`.

---

## 9. Promising Directions for a Fresh Agent

### 9.1 Use professional numerical algebraic geometry

The full nonlinear coefficient system for low-degree 2D maps should be attacked with proper homotopy continuation, not SymPy `nsolve`.

Recommended tools:

```text
HomotopyContinuation.jl
Bertini
PHCpack
Sage + PHCpack interface
```

A good starting ansatz is the two-point collision ideal

```text
I = (y, x(x-1)).
```

Let

```text
P = y A(x,y) + x(x-1) B(x,y)
Q = y C(x,y) + x(x-1) D(x,y)
```

with total degrees `3`, `4`, or `5`.

Impose

```text
P_x Q_y - P_y Q_x = 1
```

by equating coefficients.

Use affine source/target normalizations to reduce symmetry. For example, normalize the derivative at `(0,0)` to a convenient invertible matrix.

Then:

1. Solve numerically over `C`.
2. Look for low-height rational solutions.
3. Verify exactly in SymPy/Sage.

The earlier SymPy `nsolve` failure is not conclusive; it only means that naive local Newton methods with random starts were insufficient.

---

### 9.2 Improve the modular/Hensel approach

The `L4` modular signal is still interesting:

```text
P = 9 x^2 - 12 x y - 9 x + 4 y^2 + 4 y.
```

For this `P`, modular `Q` solutions exist modulo `5` and `7` in degrees `7` and `8`.

The implemented Hensel lift failed, but it used a relatively naive treatment of free variables. A stronger approach would:

1. Build the full linear operator

   ```text
   A_P(Q) = P_x Q_y - P_y Q_x.
   ```

2. Work over `Z/p^k Z` using Smith normal form or a proper module solver.

3. Track the full kernel at each lift step, not just one free-variable assignment.

4. Try multiple lift branches.

5. Use rational reconstruction with larger precision.

6. Compare `p=5` and `p=7` lifts via CRT.

7. If a rational solution exists with denominators divisible by `11` or `13`, modular absence modulo those primes is not fatal.

Sage or Magma would be much better than SymPy for this.

---

### 9.3 Search for a polynomial parametrization of a surface through the fiber

Instead of affine planes or simple graphs, search for a polynomial embedding

```text
φ : C^2 -> C^3
φ(u,v) = (X(u,v), Y(u,v), Z(u,v))
```

whose image contains two or three fiber points, and such that the pullback of some target 2-form is constant.

Equivalently, choose two target polynomials `f(P,Q,S)` and `g(P,Q,S)` and require

```text
Jac_{u,v}( f(F(φ(u,v))), g(F(φ(u,v))) ) = constant.
```

This is a PDE/constraint system. Low-degree ansätze could be attacked with Gröbner bases or numerical algebraic geometry.

The symmetry-respecting form

```text
x = u
y = u R(u^2,v)
z = Z(u^2,v)
```

is a natural subclass, but earlier random searches in this class were too sparse. A systematic Gröbner or homotopy approach could be better.

---

### 9.4 Analyze the monodromy/deck transformation of the 3D map

Since the generic fiber is cubic and the discriminant is square-structured, the monodromy may be cyclic of order `3`.

A fresh agent should try to compute explicitly:

1. The three inverse branches `x_i(P,Q,S)`.
2. Rational expressions for `y_i,z_i` once `x_i` is known.
3. A possible deck transformation

   ```text
   τ : C^3 --> C^3
   ```

   permuting the three branches.

If a rational or polynomial deck transformation exists, invariant surfaces or quotient constructions may yield a 2D map.

---

### 9.5 Study the `P=-1/4` surface as an affine surface

The surface

```text
P = -1/4
```

contains the full fiber and appears to be a nontrivial cubic/Danielewski-type surface.

Important questions:

1. Is it isomorphic to `C^2`?
2. Does it admit a polynomial parametrization?
3. What is its Makar-Limanov invariant?
4. Does it have an `A^1`-fibration?
5. Can the rational 2-form with pole `a^{-3}` be absorbed by a nontrivial polynomial coordinate change?

If one can find polynomial coordinates `(u,v)` on this surface, then the pulled-back target functions might produce a 2D Keller map.

---

### 9.6 Build a 2D cubic-cover ansatz using `u^2 - v^3`

The identity

```text
27 S^2 K = u^2 - v^3
```

suggests constructing a 2D map whose auxiliary cubic has discriminant controlled by a cusp-like square.

One possible framework:

Choose polynomials in two source variables `(x,y)`:

```text
K(x,y), B(x,y), C(x,y)
```

such that `x` satisfies

```text
K x^3 + B x + C = 0
```

and

```text
4 B^3 + 27 K C^2 = square.
```

But this alone is not enough. One must also impose the constant-Jacobian condition for the actual target map.

A useful parametrization of the discriminant-square condition is:

```text
B = t^2 + C F
D = 2 t^3 + 3 t C F
K = -F^2 (3 t^2 + 4 C F) / 27
```

which gives

```text
D^2 = 4 B^3 + 27 K C^2.
```

Also, the cubic

```text
K X^3 + B X + C = 0
```

has root

```text
X = 3/F.
```

However, naive polynomial realizations of this skeleton tend to create a critical point at `F = 0` or at the root/parameter origin. A successful ansatz must avoid this global ramification, likely by making the map non-finite in a controlled way.

---

### 9.7 Search finite fields more systematically

Positive characteristic has many non-injective Keller maps due to Frobenius phenomena. These usually do not lift, but they can reveal algebraic forms.

A better finite-field strategy:

1. Work over several primes, e.g. `3,5,7,11`.
2. Use Gröbner bases over finite fields for the full nonlinear coefficient system.
3. Search for solutions modulo `p` that survive modulo `p^2`, `p^3`, etc.
4. Use CRT and rational reconstruction.
5. Distinguish Frobenius artifacts from potentially liftable structures.

The char-3 hits already found are almost certainly Frobenius artifacts, but a char-5 or char-7 hit that lifts to `p^2` would be much more interesting.

---

## 10. Reusable Formulas

### 10.1 3D map

```text
P = (1 + x y)^3 z + y^2 (1 + x y)(4 + 3 x y)
Q = y + 3 x (1 + x y)^2 z + 3 x y^2 (4 + 3 x y)
S = 2 x - 3 x^2 y - x^3 z
```

### 10.2 Auxiliary `M`

```text
a = 1 + x y
b = 4 + 3 x y
M = a^2 z + y^2 b

P = a M
Q = y + 3 x M
a^2 S = x(2 + x y) - x^3 M
```

### 10.3 Fiber cubic

```text
K = 27 P^2 S^2 - 18 P Q S + 16 P + Q^3 S - Q^2

K x^3 + (4 - 3 Q S) x - 2 S = 0
```

### 10.4 Discriminant identity

```text
u = 27 P S^2 - 9 Q S + 8
v = 4 - 3 Q S

27 S^2 K = u^2 - v^3
```

### 10.5 `S=0` reduced map

```text
t = 1/x
r = 2 x y + 3

P0 = t^2(r^2 - 1)/4 + 1/4
Q0 = 2 t r

Jac(P0,Q0) = -t^2
```

### 10.6 `P=-1/4` building blocks

```text
a = 1 + x y

Q = y - 3 x/(4 a)
S = x(2 + x y)/a^2 + x^3/(4 a^3)

Q0 = a Q = y + x y^2 - 3 x/4
S0 = a^3 S = x(2 + x y)(1 + x y) + x^3/4
```

### 10.7 `Q=0` building blocks

```text
y = -3 x M
a = 1 - 3 x^2 M

A = P + 1/4 = M - 3 x^2 M^2 + 1/4
N = a^2 S = 2 x (1 - 2 x^2 M)
```

### 10.8 Two-point quotient block `L4`

With collision points

```text
(0,0), (1,0)
```

the polynomial

```text
L4 = 9 x^2 - 12 x y - 9 x + 4 y^2 + 4 y
```

belongs to the ideal

```text
(y, x(x-1))
```

and has modular `Q`-solutions for

```text
L4_x Q_y - L4_y Q_x = 1
```

modulo `5` and `7` in degrees `7` and `8`.

---

## 11. Current Overall Conclusion

The 3D map is symbolically verified as a Keller map with a triple fiber and generic cubic fiber structure. Many natural and semi-natural reductions to two dimensions have been tested and failed.

The most important positive structural facts are:

1. The generic fiber is cubic:

   ```text
   K x^3 + (4 - 3 Q S)x - 2 S = 0.
   ```

2. The discriminant is controlled by a cusp-like identity:

   ```text
   27 S^2 K = u^2 - v^3.
   ```

3. The `S=0` reduction gives a near-miss with Jacobian `-t^2`.

4. The `P=-1/4` surface is a nontrivial cubic-cover-like surface with a rational 2-form pole.

5. The quotient block `L4` gives the strongest modular signal found so far, but no characteristic-zero lift has been obtained.

No 2D counterexample has been found. The problem remains open in this experimental pipeline. A fresh agent should prioritize:

1. Proper numerical algebraic geometry for full nonlinear low-degree 2D systems.
2. Stronger modular/Hensel lifting with full kernel tracking.
3. Deeper algebraic-geometric analysis of the 3D map’s monodromy and the `P=-1/4` surface.
4. Construction of a non-finite cubic-cover 2D ansatz based on the `u^2 - v^3` discriminant structure while avoiding the known ramification-at-origin obstruction.