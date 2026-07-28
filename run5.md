# Run 5

## 1. Objective

We are given a reported and symbolically verified polynomial map

\[
F:\mathbb C^3\to\mathbb C^3,\qquad F(x,y,z)=(P,Q,S),
\]

with constant nonzero Jacobian determinant and a nontrivial fiber of size three. The goal is to discover a **2D polynomial counterexample**:

\[
G:\mathbb C^2\to\mathbb C^2
\]

such that

\[
\det JG \in \mathbb C^\times
\]

is constant and \(G\) is not injective, preferably with an explicit collision of two or three distinct points.

Despite many structured searches, no 2D counterexample has yet been found. The 2D Jacobian conjecture remains open, and a 3D counterexample does **not** automatically imply a 2D one. However, the special algebraic structure of this 3D map gives several nontrivial routes that are still worth exploring.

---

## 2. The Verified 3D Map

The map is

\[
\begin{aligned}
P &= (1+xy)^3z + y^2(1+xy)(4+3xy),\\
Q &= y + 3x(1+xy)^2z + 3xy^2(4+3xy),\\
S &= 2x - 3x^2y - x^3z.
\end{aligned}
\]

Define

\[
a = 1+xy,\qquad b = 4+3xy,
\]

and the crucial auxiliary quantity

\[
M = a^2 z + y^2 b.
\]

Then the map can be written compactly as

\[
P = aM,
\]

\[
Q = y + 3xM,
\]

and

\[
a^2S = x(2+xy)-x^3M.
\]

This \(M\)-formulation is one of the most useful algebraic handles on the map.

---

## 3. Exact Verification

SymPy verifies:

\[
\det JF = -2.
\]

The three distinct points

\[
p_0=\left(0,0,-\frac14\right),
\]

\[
p_1=\left(1,-\frac32,\frac{13}{2}\right),
\]

\[
p_2=\left(-1,\frac32,\frac{13}{2}\right)
\]

all map to

\[
q=\left(-\frac14,0,0\right).
\]

So, inside exact symbolic computation, this is a genuine 3D Keller map with a nontrivial fiber.

---

## 4. Basic Geometry of the Fiber

The three points satisfy

\[
3x+2y=0,
\]

so they lie in the affine plane

\[
y=-\frac32x.
\]

In coordinates \((x,z)\) on this plane, the three points become

\[
(x,z)=\left(0,-\frac14\right),\quad
\left(1,\frac{13}{2}\right),\quad
\left(-1,\frac{13}{2}\right).
\]

There is also an order-two symmetry

\[
\sigma(x,y,z)=(-x,-y,z).
\]

One checks

\[
P\circ\sigma=P,
\]

\[
Q\circ\sigma=-Q,
\]

\[
S\circ\sigma=-S.
\]

Thus the target involution is

\[
\tau(P,Q,S)=(P,-Q,-S).
\]

The points \(p_1,p_2\) are exchanged by \(\sigma\), while \(p_0\) is fixed.

---

## 5. Major Algebraic Discovery: The Cubic Relation

A central discovery is that the source coordinate \(x\) satisfies a cubic equation over the target field \(\mathbb C(P,Q,S)\).

Define the target invariant

\[
K(P,Q,S)=27P^2S^2-18PQS+16P+Q^3S-Q^2.
\]

Then \(x\) satisfies

\[
K(P,Q,S)x^3 + (4-3QS)x - 2S = 0.
\]

Equivalently, if

\[
B = 4-3QS,
\]

\[
C = -2S,
\]

then

\[
Kx^3+Bx+C=0.
\]

This shows that the generic fiber degree is exactly \(3\), because once \(x\) is known, \(y,z\) can be recovered rationally.

At the special target point

\[
q=\left(-\frac14,0,0\right),
\]

one has

\[
K(q)=-4,\qquad B(q)=4,\qquad C(q)=0,
\]

so the cubic becomes

\[
-4x^3+4x=0,
\]

with roots

\[
x=0,\quad x=1,\quad x=-1,
\]

which are exactly the \(x\)-coordinates of the three known preimages.

---

## 6. Major Algebraic Discovery: The Cusp Identity \(u^2-v^3\)

Define two further target polynomials

\[
u = 27PS^2 - 9QS + 8,
\]

\[
v = 4-3QS.
\]

Then one has the identity

\[
27S^2K = u^2 - v^3.
\]

Equivalently,

\[
27K C^2 + 4B^3 = 4u^2.
\]

This is extremely important: the 3D map is algebraically organized around the cusp singularity

\[
u^2=v^3.
\]

The target coordinates \(P,Q,S\) are rational reparametrizations of the cusp-like data \((u,v,S,K)\). In particular,

\[
Q=\frac{4-v}{3S},
\]

and

\[
P=\frac{u+9QS-8}{27S^2}.
\]

This suggests that any 2D analogue should probably be built from a depressed cubic whose discriminant-like expression has a square or cusp structure.

---

## 7. The Level Surface \(K=-4\)

The special fiber lies on the target level surface

\[
K=-4.
\]

On this surface, the cusp identity becomes

\[
u^2 + 108S^2 = v^3.
\]

Over \(\mathbb C\), this surface is closely related to a \(\mu_3\)-quotient. One useful parametrization is obtained by choosing \(\lambda\) with

\[
\lambda^2=-108.
\]

Then set

\[
v = rs,
\]

\[
u = \frac{r^3+s^3}{2},
\]

\[
S = \frac{r^3-s^3}{2\lambda}.
\]

Then

\[
u^2+108S^2=v^3
\]

is automatically satisfied.

On this parametrized surface, the cubic for \(x\) becomes

\[
-4x^3+rs\,x-\frac{r^3-s^3}{\lambda}=0.
\]

Its three roots are linear forms in \(r,s\). More precisely, choose constants \(\alpha,\beta\) such that

\[
\alpha\beta=\frac1{12},
\]

\[
\alpha^3=-\frac1{4\lambda},
\]

\[
\beta^3=\frac1{4\lambda}.
\]

Then the three roots are

\[
x_1=\alpha r+\beta s,
\]

\[
x_2=\omega\alpha r+\omega^2\beta s,
\]

\[
x_3=\omega^2\alpha r+\omega\beta s,
\]

where \(\omega\) is a primitive cube root of unity.

For the concrete choice

\[
\lambda=6i\sqrt3,
\]

one may take

\[
\alpha=-\frac{i}{2\sqrt3},\qquad
\beta=\frac{i}{2\sqrt3}.
\]

Then

\[
x_1=\frac{i}{2\sqrt3}(s-r).
\]

The three known preimages correspond to the \(\mu_3\)-orbit

\[
(r,s)=(2,2),\quad (2\omega,2\omega^2),\quad (2\omega^2,2\omega).
\]

This structure motivated several 2D searches based on the three-point ideal

\[
J=\langle r^3-8,\;rs-4\rangle.
\]

---

## 8. Pullback of \(K\) and the Source Surface \(K=-4\)

Using the cubic relation, one can compute the pullback of \(K\) to the source without expanding the full target expression.

Let

\[
T = 2-3xy-x^2z.
\]

Since \(S=xT\), one obtains

\[
K_{\text{pull}} =
9MT - 2z - 9y^2 - 3xyz,
\]

where

\[
M=(1+xy)^2z+y^2(4+3xy).
\]

Then

\[
K_{\text{pull}}+4
\]

is quadratic in \(z\). Its coefficients are

\[
A=-9x^2(1+xy)^2,
\]

\[
B=-2(27x^3y^3+36x^2y^2-3xy-8),
\]

\[
C=-81x^2y^4-54xy^3+63y^2+4.
\]

The discriminant in \(z\) simplifies beautifully to

\[
\Delta
=
16\left(9x^2(1+xy)^2+12xy+16\right).
\]

Equivalently,

\[
\Delta
=
16\left(9x^4y^2+18x^3y+9x^2+12xy+16\right).
\]

This discriminant is not a square in \(\mathbb C[x,y]\), so the source surface \(K=-4\) is not simply a polynomial graph over the \((x,y)\)-plane. This explains why naive parametrizations of this surface failed.

---

## 9. A Two-Dimensional Shadow from \((s,W)\)

Another useful reduction comes from the variables

\[
s=xy,
\]

\[
M=(1+xy)^2z+y^2(4+3xy),
\]

\[
W=x^2M.
\]

The target cusp invariants \(u,v\) depend only on \((s,W)\). Define

\[
N = 2+s-W,
\]

\[
A = s+3W.
\]

After clearing denominators, one obtains a natural polynomial near-miss map

\[
F_*(N,A)=N\left(3N(N-2)+A(A-2)\right),
\]

\[
G_*(N,A)=AN.
\]

The two relevant points are

\[
(N,A)=(2,0)
\]

corresponding to \(p_0\), and

\[
(N,A)=(0,0)
\]

corresponding to the \(\sigma\)-orbit \(\{p_1,p_2\}\).

Both map to \((0,0)\). The Jacobian is

\[
\operatorname{Jac}(F_*,G_*)=
N(9N^2-12N-A^2).
\]

This is nonconstant and degenerates at \(N=0\), but it motivated a normalized two-point search.

After translating

\[
N=x+1,
\]

the two points become

\[
(x,A)=(-1,0),\quad (1,0),
\]

and after another affine normalization one obtains the ideal

\[
I_2=\langle y,\;x(x-1)\rangle
\]

with collision points

\[
(0,0),\quad (1,0).
\]

---

## 10. Previously Attempted Strategies and Negative Results

The following strategies were tried and failed to produce a 2D counterexample.

### 10.1 Graph Slices \(z=h(x,y)\), Projecting to \((P,Q)\)

Polynomial height functions \(h(x,y)\) were chosen to satisfy

\[
h(0,0)=-\frac14,
\]

\[
h\left(1,-\frac32\right)=\frac{13}{2},
\]

\[
h\left(-1,\frac32\right)=\frac{13}{2}.
\]

Then one considers

\[
G(x,y)=\left(P(x,y,h(x,y)),\;Q(x,y,h(x,y))\right).
\]

Many quadratic and low-degree choices were tested. All produced nonconstant Jacobians.

A structural obstruction exists: writing

\[
M=a^2h(x,y)+y^2b,
\]

the projected map is

\[
G(x,y)=(aM,\;y+3xM),
\]

and its Jacobian contains a dominant term

\[
-3x^2MM_x,
\]

which prevents constant Jacobian for nontrivial polynomial \(M\).

---

### 10.2 Special Plane \(y=-3x/2\)

Restricting the 3D map to the plane containing the three fiber points and projecting to

\[
(P,Q),\quad (P,S),\quad (Q,S)
\]

preserves the collision but gives nonconstant Jacobians.

Constant linear combinations of the three \(2\times2\) minors were also tested. None were constant.

---

### 10.3 Affine Planes Through Pairs of Preimages

Since a 2D counterexample only needs two colliding points, many affine planes through pairs among

\[
p_0,p_1,p_2
\]

were searched, together with linear target recombinations. No constant-minor combination was found.

---

### 10.4 Nonlinear Target-Polynomial Recombinations on the Special Plane

On the special plane define

\[
A=P+\frac14,\qquad B=Q,\qquad C=S.
\]

At the three preimages,

\[
(A,B,C)=(0,0,0).
\]

Many polynomial pairs

\[
(f(A,B,C),g(A,B,C))
\]

without constant term were tested, including parity-respecting even/odd pairs. No constant-Jacobian pair was found.

---

### 10.5 The \(S=0\) Reduction

On the target plane \(S=0\), using

\[
t=\frac1x,\qquad r=2xy+3,
\]

one obtains the reduced map

\[
P=\frac{t^2(r^2-1)}4,
\]

\[
Q=2tr.
\]

After shifting \(P\) by \(1/4\),

\[
P_0=\frac{t^2(r^2-1)}4+\frac14,
\]

\[
Q_0=2tr.
\]

The two points

\[
(t,r)=(1,0),\quad (-1,0)
\]

map to \((0,0)\), but

\[
\operatorname{Jac}(P_0,Q_0)=-t^2.
\]

This is a beautiful near-miss. Extensive even/odd deformation searches of the form

\[
G(t,r)=\left(F(t^2,r),\;tH(t^2,r)\right)
\]

were performed up to degree \(20\). No polynomial correction made the Jacobian constant.

---

### 10.6 Direct 2D Fixed-First-Component Searches

Many direct 2D searches were performed for maps

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

For fixed \(P\), this is a linear PDE for \(Q\). Many Danielewski-type first components were tested, for example

\[
P=x^2y+x(x-1),
\]

with \(Q\)-degree up to \(20\). No polynomial solution was found.

A typical obstruction is that the local solution behaves like

\[
Q=\frac1x+\phi(P),
\]

which is not polynomial.

---

### 10.7 The Level Surface \(P=-1/4\)

The target level surface

\[
P=-\frac14
\]

contains the full fiber. On this surface one obtains rational expressions

\[
Q=y-\frac{3x}{4a},
\]

\[
S=\frac{x(2+xy)}{a^2}+\frac{x^3}{4a^3},
\]

where \(a=1+xy\).

Clearing denominators gives polynomial building blocks

\[
Q_0=aQ=y+xy^2-\frac34x,
\]

\[
S_0=a^3S=x(2+xy)(1+xy)+\frac14x^3.
\]

Both vanish at the three projected preimages.

Many scaled pairs

\[
(Q_0a^i,\;S_0a^j)
\]

and linear-span variants were tested. None produced constant Jacobian.

The rational Jacobian of the natural map \((Q_0,S_0)\) is

\[
-\frac{2}{(1+xy)^3},
\]

showing that this surface has a nontrivial pole structure and is not obviously isomorphic to \(\mathbb C^2\).

---

## 11. New Searches Performed in the Most Recent Phase

The following newer searches were also performed and produced no counterexample.

---

### 11.1 Six-Point Cusp Ideal Search

The cusp parametrization naturally introduced the variables \(r,s\) and the six-point ideal

\[
I=\langle r^3-s^3,\;rs-4\rangle.
\]

This ideal vanishes on both orbits

\[
r^3=s^3=8
\]

and

\[
r^3=s^3=-8.
\]

A simple base map is

\[
U=r^3-s^3,
\]

\[
V=4-rs.
\]

It has

\[
\operatorname{Jac}(U,V)=-3(r^3+s^3).
\]

Searches were performed for

\[
F,G\in I
\]

with

\[
\operatorname{Jac}(F,G)=1.
\]

Degrees up to \(5\), and a small degree-\(6\) probe, were tested using fixed-\(F\) linear solves and modular random searches. No candidate was found.

---

### 11.2 Three-Point Ideal Search

The actual triple fiber corresponds to the three-point ideal

\[
J=\langle r^3-8,\;rs-4\rangle.
\]

Useful degree-two elements of \(J\) are

\[
u=r-\frac{s^2}{2},
\]

\[
v=s-\frac{r^2}{2}.
\]

They vanish on the three points

\[
(2,2),\quad (2\omega,2\omega^2),\quad (2\omega^2,2\omega).
\]

Their Jacobian is

\[
\operatorname{Jac}(u,v)=1-rs.
\]

On the collision orbit \(rs=4\), this is \(-3\), so the map is nondegenerate there, but the Jacobian is not constant.

Searches for corrections

\[
F=u+f,\qquad G=v+g,
\]

with \(f,g\in J\), were performed up to degree \(5\) and partially degree \(6\). No constant-Jacobian pair was found.

---

### 11.3 Normalized Two-Point Model

Using the \((s,W)\)-shadow, the problem was reduced to a normalized two-point model.

Let the collision points be

\[
(0,0),\quad (1,0).
\]

The vanishing ideal is

\[
I_2=\langle y,\;x(x-1)\rangle.
\]

A normalized skeleton is

\[
F_0=x-x^2,
\]

\[
G_0=y.
\]

Then

\[
F_0(0,0)=F_0(1,0)=0,
\]

\[
G_0(0,0)=G_0(1,0)=0,
\]

and

\[
d(F_0,G_0)_{(0,0)}=
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix}.
\]

However,

\[
\operatorname{Jac}(F_0,G_0)=1-2x.
\]

The search problem becomes: find corrections

\[
f,g\in I_2
\]

with zero value and zero first jet at \((0,0)\), such that

\[
\operatorname{Jac}(F_0+f,\;G_0+g)=1.
\]

For degree \(3\), the correction space has dimension \(6\). An exhaustive search over all \(F\)-coefficients in \(\mathbb F_5\) was performed:

\[
5^6=15625
\]

candidates. For each \(F\), the equation for \(G\) is linear. No modular solution was found.

For degree \(4\), the correction space has dimension \(11\). A randomized search over \(\mathbb F_5\) with \(20000\) trials was performed. No modular solution was found.

This is strong evidence that no low-degree normalized two-point solution exists over \(\mathbb Q\) with good reduction at \(5\).

---

### 11.4 Symmetry-Quotient Invariant Search

Using the involution

\[
\sigma(x,y,z)=(-x,-y,z),
\]

the special plane was quotiented by \(x\mapsto -x\). Set

\[
u=x^2,
\]

\[
v=z+\frac14-\frac{27}{4}u.
\]

The quotient fiber points become

\[
(u,v)=(0,0),\quad (1,0).
\]

Invariant target generators are

\[
A=P+\frac14,
\]

\[
U=Q^2,
\]

\[
V=S^2,
\]

\[
W=QS.
\]

All vanish at both quotient fiber points.

Searches were performed for polynomial pairs

\[
F,G\in \mathbb C[A,U,V,W]
\]

without constant term, satisfying

\[
\operatorname{Jac}_{u,v}(F,G)=1.
\]

The truncated spans turned out to be very small: degree-filtered generator spans had dimensions only \(3\) and \(5\). No candidate was found.

---

### 11.5 Generalized Non-Affine Surface Search

A broader surface search was performed over all three graph orientations:

\[
y=h(x,z),
\]

\[
x=h(y,z),
\]

\[
z=h(x,y).
\]

For each orientation, polynomial height functions \(h\) of degree \(2\) and \(3\) were constructed through the three fiber points. For each surface, the three minors

\[
M_{PQ},\quad M_{PS},\quad M_{QS}
\]

were computed with respect to the surface coordinates, and a modular search was performed for constants

\[
\lambda_{PQ},\lambda_{PS},\lambda_{QS}
\]

such that

\[
\lambda_{PQ}M_{PQ}
+
\lambda_{PS}M_{PS}
+
\lambda_{QS}M_{QS}
=1.
\]

No quadratic or cubic surface in this family produced a constant-minor combination.

---

## 12. Mathematical Lessons Learned

### 12.1 Collision Is Easy; Constant Jacobian Is Extremely Restrictive

It is easy to build polynomial maps that identify the desired points. The hard part is making the Jacobian determinant a nonzero constant. This is a severe global PDE condition.

---

### 12.2 Linear-in-One-Variable Components Are Obstructed

If a component has the form

\[
F_1(x,z)=A(x)z+B(x)
\]

with nonconstant \(A(x)\), then there is generally no polynomial \(G(x,z)\) such that

\[
\{F_1,G\}=1.
\]

A coefficient argument in powers of \(z\) forces divisibility by \(A(x)\), preventing a nonzero constant bracket.

This explains many failed projections from surfaces where one target component remains linear in a coordinate.

---

### 12.3 Coordinate-Like Components Tend to Force Injectivity

If one component is a genuine coordinate, for example with derivative \(1\) in one variable, then a constant-Jacobian partner often becomes triangular in that coordinate, preventing collisions.

For example, if \(U_z=1\), then in coordinates \((x,U)\), a constant-Jacobian partner often has the form

\[
V=-cx+\phi(U),
\]

which is injective in \(x\).

---

### 12.4 The \(S=0\) and \(P=-1/4\) Surfaces Are Not Naively \(\mathbb C^2\)

The \(S=0\) reduction gives a beautiful near-miss with Jacobian \(-t^2\), but polynomial extension across \(t=0\) appears obstructed.

The \(P=-1/4\) surface gives rational building blocks with a pole along \(1+xy=0\). Its natural rational Jacobian is

\[
-\frac{2}{(1+xy)^3}.
\]

This suggests that the surface is not polynomially isomorphic to \(\mathbb C^2\) in any simple way.

---

### 12.5 The Cusp Structure Is Real but Not Yet Sufficient

The identity

\[
27S^2K=u^2-v^3
\]

is a major structural clue. It shows that the 3D map is organized around the cusp \(u^2=v^3\) and a degree-three cover.

However, directly turning this into a 2D polynomial Keller map has not yet succeeded.

---

## 13. What Has Likely Been Ruled Out

Unless a much larger computational method is used, the following are probably not worth repeating:

1. Simple graph slices \(z=h(x,y)\) projecting to \((P,Q)\) with low-degree \(h\).
2. The special plane \(y=-3x/2\) with simple projections \((P,Q)\), \((P,S)\), \((Q,S)\).
3. Constant linear minor combinations on the special plane.
4. Low-degree target-polynomial pairs in \((A,B,C)=(P+1/4,Q,S)\) of degree \(\le 2\).
5. Parity-respecting even/odd target-polynomial searches with odd degree \(\le 3\).
6. The specific \(S=0\) even/odd fixed-\(H\) families already tested up to degree \(20\).
7. Direct fixed-\(P\) linear PDE searches for the listed Danielewski-type \(P\) families up to \(Q\)-degree \(20\).
8. Simple scaled pairs \((Q_0a^i,S_0a^j)\) from the \(P=-1/4\) surface for small \(i,j\).
9. Low-degree searches in the six-point ideal \(\langle r^3-s^3,rs-4\rangle\) up to degree \(5\) or \(6\).
10. Low-degree searches in the three-point ideal \(\langle r^3-8,rs-4\rangle\) up to degree \(5\) or \(6\).
11. Normalized two-point degree-\(3\) searches over \(\mathbb F_5\); these were exhaustive.
12. Normalized two-point degree-\(4\) random searches over \(\mathbb F_5\); no hits were found.
13. Quadratic and cubic graph-surface searches in all three orientations \(y=h(x,z)\), \(x=h(y,z)\), \(z=h(x,y)\) using constant minor combinations.

These are not logically impossible in full generality, but they have been heavily explored and appear unpromising without a new structural insight.

---

## 14. Most Promising Remaining Directions

### 14.1 Full Nonlinear Algebraic-Geometry Solve in Degree 4 or 5

The normalized two-point model gives a clean polynomial system.

Let

\[
F_0=x-x^2,\qquad G_0=y.
\]

Let \(B_1,\dots,B_n\) be a basis of polynomials in

\[
I_2=\langle y,x(x-1)\rangle
\]

with zero value and zero first jet at \((0,0)\).

For degree \(3\), \(n=6\).
For degree \(4\), \(n=11\).

Write

\[
F=F_0+\sum_{i=1}^n a_iB_i,
\]

\[
G=G_0+\sum_{i=1}^n b_iB_i.
\]

Then impose

\[
\operatorname{Jac}(F,G)=1.
\]

This gives a quadratic coefficient system.

For degree \(3\):

- variables: \(12\);
- nonconstant Jacobian coefficient equations: about \(14\).

An exhaustive modular search over \(F\) in \(\mathbb F_5\) found no solution. A full complex homotopy or Gröbner solve could still be useful to rule out algebraic solutions with bad reduction or solutions over extensions.

For degree \(4\):

- variables: \(22\);
- nonconstant Jacobian coefficient equations: about \(27\).

This is large but potentially approachable with:

- HomotopyContinuation.jl;
- Bertini;
- PHCpack;
- Singular/Sage Gröbner methods over finite fields;
- sparse polynomial system techniques.

This is probably the strongest direct next step.

---

### 14.2 Search Over Algebraic Coefficients or Finite-Field Extensions

Many searches were over \(\mathbb Q\) or \(\mathbb F_5\). The cusp/\(\mu_3\) structure suggests that \(\sqrt{-3}\) or cube roots of unity may be essential.

Possible experiments:

1. Search the normalized two-point system over \(\mathbb Q(\sqrt{-3})\).
2. Search modulo primes \(p\equiv 1\pmod 3\), where \(\mathbb F_p\) contains cube roots of unity.
3. Search over extension fields \(\mathbb F_{p^2}\) or \(\mathbb F_{p^3}\).
4. Use Hensel lifting if modular solutions appear but do not lift over \(\mathbb Q\).

---

### 14.3 Compute Monodromy and Possible Deck Correspondences

The generic fiber degree is \(3\). A crucial unknown is the monodromy group of the cover

\[
F:\mathbb C^3\to\mathbb C^3.
\]

Questions:

1. Is the monodromy group \(S_3\) or \(A_3\)?
2. Is there a rational correspondence permuting the three branches?
3. Does there exist a rational deck transformation on a finite cover?
4. Can the Galois closure be parametrized explicitly?
5. Does the field extension \(\mathbb C(x,y,z)/\mathbb C(P,Q,S)\) contain an intermediate transcendence-degree-two subfield that could give a 2D map?

If a rational branch-permuting correspondence exists, it may produce a quotient or invariant map in dimension two.

---

### 14.4 Analyze the Source Surface \(K=-4\) More Deeply

The source surface

\[
K_{\text{pull}}+4=0
\]

is quadratic in \(z\), with discriminant

\[
16\left(9x^2(1+xy)^2+12xy+16\right).
\]

It is not a simple polynomial graph. However, it may still be rational or unirational.

Important questions:

1. Is this surface rational?
2. Is it isomorphic to a Danielewski-type surface?
3. Does it admit an \(\mathbb A^1\)-fibration?
4. Can it be parametrized by two rational parameters?
5. If so, what is the induced map to the target surface \(K=-4\)?
6. Can one choose polynomial coordinates on a normalization so that the induced 2D map has constant Jacobian?

The target surface \(K=-4\) has the cusp parametrization

\[
u^2+108S^2=v^3.
\]

Understanding the relation between the normalization of the target surface and the normalization of the source surface may be the key.

---

### 14.5 Use the Parametrized Cusp Surface to Build a 2D Map Directly

On \(K=-4\), use parameters \(r,s\) with

\[
v=rs,
\]

\[
u=\frac{r^3+s^3}{2},
\]

\[
S=\frac{r^3-s^3}{2\lambda},
\qquad \lambda^2=-108.
\]

For a chosen root

\[
x=\alpha r+\beta s,
\]

one should be able to recover \(y,z\) rationally from the target equations.

A fresh agent could try to:

1. Derive explicit rational formulas for \(y,z\) in terms of \(r,s\) on a chosen sheet.
2. Determine whether the source sheet is polynomially or rationally parametrized by \((r,s)\).
3. Pull back natural target pairs such as \((Q,S)\), \((P,S)\), \((u,v)\), or polynomial combinations.
4. Search for polynomial corrections or coordinate changes making the Jacobian constant.

This route uses the most structural information from the 3D map and has not been exhausted.

---

### 14.6 Check Literature for Dimension-Reduction Theorems

It is worth carefully checking whether any theorem gives a reduction from a 3D Keller map with a fiber of size \(3\) to a 2D counterexample.

Questions:

1. Does a counterexample in dimension \(3\) imply one in dimension \(2\) under any additional hypotheses?
2. Are there results about Keller maps with small generic degree?
3. Are there results about Keller maps with a fiber of cardinality \(3\)?
4. Are there stable-range or Lefschetz-type theorems that could produce plane sections?
5. Is there a known construction of 2D counterexamples from cyclic cubic covers?

If such a theorem exists, it would likely be the fastest path.

---

## 15. Important Exact Formulas for a Fresh Agent

### 15.1 3D Map

\[
P=(1+xy)^3z+y^2(1+xy)(4+3xy),
\]

\[
Q=y+3x(1+xy)^2z+3xy^2(4+3xy),
\]

\[
S=2x-3x^2y-x^3z.
\]

### 15.2 Auxiliary \(M\)

\[
M=(1+xy)^2z+y^2(4+3xy).
\]

Then

\[
P=(1+xy)M,
\]

\[
Q=y+3xM,
\]

\[
(1+xy)^2S=x(2+xy)-x^3M.
\]

### 15.3 Target Cubic Invariant

\[
K=27P^2S^2-18PQS+16P+Q^3S-Q^2.
\]

The source coordinate \(x\) satisfies

\[
Kx^3+(4-3QS)x-2S=0.
\]

### 15.4 Cusp Variables

\[
u=27PS^2-9QS+8,
\]

\[
v=4-3QS.
\]

Identity:

\[
27S^2K=u^2-v^3.
\]

### 15.5 Pullback of \(K\)

Let

\[
T=2-3xy-x^2z,
\]

\[
M=(1+xy)^2z+y^2(4+3xy).
\]

Then

\[
K_{\text{pull}}=9MT-2z-9y^2-3xyz.
\]

The equation

\[
K_{\text{pull}}+4=0
\]

is quadratic in \(z\), with discriminant

\[
16\left(9x^2(1+xy)^2+12xy+16\right).
\]

### 15.6 Three-Point Ideal from the Cusp Parametrization

\[
J=\langle r^3-8,\;rs-4\rangle.
\]

Useful elements:

\[
u=r-\frac{s^2}{2},
\]

\[
v=s-\frac{r^2}{2}.
\]

Their Jacobian:

\[
\operatorname{Jac}(u,v)=1-rs.
\]

### 15.7 Normalized Two-Point Model

Collision points:

\[
(0,0),\quad (1,0).
\]

Ideal:

\[
I_2=\langle y,\;x(x-1)\rangle.
\]

Skeleton:

\[
F_0=x-x^2,
\]

\[
G_0=y.
\]

Search for

\[
F=F_0+f,\qquad G=G_0+g,
\]

where \(f,g\in I_2\) have zero first jet at \((0,0)\), and

\[
\operatorname{Jac}(F,G)=1.
\]

---

## 16. Suggested Concrete First Task for a Fresh Agent

A strong first task is to set up the normalized two-point degree-\(4\) system and attack it with a serious nonlinear solver.

Concretely:

1. Work in variables \(x,y\).
2. Build the vector space of polynomials of degree \(\le 4\) in
   \[
   I_2=\langle y,x(x-1)\rangle
   \]
   with zero value and zero first jet at \((0,0)\).
3. Let this basis be \(B_1,\dots,B_{11}\).
4. Introduce variables \(a_1,\dots,a_{11}\) and \(b_1,\dots,b_{11}\).
5. Define
   \[
   F=x-x^2+\sum a_iB_i,
   \]
   \[
   G=y+\sum b_iB_i.
   \]
6. Expand
   \[
   F_xG_y-F_yG_x-1.
   \]
7. Set all coefficients in \(x,y\) equal to zero.
8. Solve the resulting quadratic system using:
   - HomotopyContinuation.jl;
   - Bertini;
   - PHCpack;
   - Singular Gröbner bases over finite fields;
   - or a modular/Hensel lifting strategy.

Degree \(3\) has already been exhaustively searched modulo \(5\) with no solution, so degree \(4\) is the first genuinely open low-degree case.

---

## 17. Overall Assessment

The 3D map is structurally rich:

- it has generic fiber degree \(3\);
- it has an explicit cubic equation for \(x\) over the target;
- its target invariants satisfy a cusp identity \(u^2-v^3\);
- it has a natural \(\mu_3\)-type parametrization on the level surface \(K=-4\);
- it admits several near-miss 2D reductions.

However, every attempted polynomial 2D reduction so far has failed because the constant-Jacobian condition is extremely rigid. The most promising remaining avenues are not more ad hoc ansätze, but deeper algebraic-geometric analysis and serious nonlinear algebraic solvers.

The problem remains open in this experimental pipeline.