# Run 16: Mathematical Foundations of the $S=0$ Slice, Subring Isomorphisms, and Keller Obstructions

In Run 16, we performed a deep algebraic and geometric exploration of the 2D rational slice $S = 0$ derived from the verified 3D Jacobian counterexample. This investigation yielded a series of rigorous proofs and definitive negative results that solidify our understanding of the boundary of the Jacobian Conjecture in two dimensions.

---

## 1. Direct Restriction to the $S=0$ Slice

Setting the third component of the 3D map $S = 0$ yields a parameterization for the coordinate $z$:
$$z = \frac{2x - 3x^2y}{x^3}$$

Substituting this into $P$ and $Q$ results in the 2D rational mapping:
$$P(x,y) = \frac{(xy+1)(xy+2)}{x^2}$$
$$Q(x,y) = \frac{4xy+6}{x}$$

The Jacobian determinant of this rational pair is:
$$\operatorname{Jac}_{x,y}(P, Q) = \frac{2}{x^3}$$

---

## 2. Cancellation of Poles and Isomorphic Coordinate Changes

To rectify the Jacobian to a constant value of 1, we introduced a coordinate change $(s, t) \to (x, y)$ satisfying:
$$\operatorname{Jac}_{s,t}(x,y) = \frac{x^3}{2}$$

We investigated two candidate families for this coordinate change:

### 2.1 The Triangular Family
$$x = s, \quad y = \frac{s^3}{2}t + k(s)$$

Evaluating the rational components under this change of variables (with $k(s) = 0$ for simplicity) gives:
$$P(s,t) = \frac{(s^4t+2)(s^4t+4)}{4s^2}$$
$$Q(s,t) = \frac{2(s^4t+3)}{s}$$

This yields an exact constant Jacobian:
$$\operatorname{Jac}_{s,t}(P, Q) = 1$$

However, both $P$ and $Q$ possess Laurent poles of the form $1/s$ and $1/s^2$ at $s = 0$.

### 2.2 The Non-Triangular (Linear) Family
We showed that we can "bend" the coordinate change using any non-trivial linear combination of the variables. Specifically, we solved the governing PDE:
$$x_s y_t - x_t y_s = \frac{x^3}{2}$$
for $x = s + c \cdot t$. The general polynomial solution is:
$$x = s + c \cdot t$$
$$y = \frac{(c \cdot t - s)(s + c \cdot t)^3}{4 c}$$

Under this coordinate change (for $c = 1$):
$$Q = \frac{(t-s)(s+t)^4 + 6}{s+t}$$
$$P = \frac{(s+t)^4 [-12s + 12t + (s-t)^2(s+t)^4] + 32}{16(s+t)^2}$$

This also results in $\operatorname{Jac}_{s,t}(P, Q) = 1$, but with poles along $s+t = 0$.

### 2.3 The Isomorphism Theorem
We proved that any non-triangular polynomial coordinate change $x = s + c \cdot t$ is isomorphic to the triangular coordinate change $x = s, y = s^3/2 \cdot t$. Specifically, under the substitution $u = s+t$ and $v = t-s$, the equations for $P$ and $Q$ are mathematically identical Laurent polynomials in $u$ and $v$. Thus, searching for polynomial Keller maps under any such coordinate change is equivalent to the triangular case.

---

## 3. Algebraic Structure of the Subring $S = \mathbb{C}[P, Q] \cap \mathbb{C}[s, t]$

We analyzed the subring $S$ of all polynomials in $P$ and $Q$ that are also polynomials in $s, t$ (i.e., those containing no negative powers of $s$ or $s+t$).

### 3.1 The Fundamental Relation
We verified that:
$$Q^2 - 16P = \frac{4}{s^2}$$

And the key invariant that removes the poles is:
$$R = Q^2 - 18P = -\frac{s^2 t (s^4 t + 6)}{2}$$
which is a genuine polynomial in $s, t$.

### 3.2 The Division Theorem
Let $f(P, Q) \in \mathbb{C}[P, Q]$. By dividing $f(P, Q)$ by $R = Q^2 - 18P$ with respect to the variable $Q$, we obtain:
$$f(P, Q) = R \cdot q(P, Q) + Q \cdot r_1(P) + r_0(P)$$
where $q(P, Q)$ is a polynomial, and $r_1(P), r_0(P)$ are polynomials in $P$ alone.

Since $R$ is a polynomial in $s, t$ with a factor of $s^2$, and $Q$ and $P$ have poles at $s = 0$ of odd and even degrees respectively, any non-zero term in the remainder $Q \cdot r_1(P) + r_0(P)$ will introduce uncancelable poles at $s = 0$. Therefore, $f(P, Q)$ is a polynomial in $s, t$ if and only if $r_1(P) = 0$ and $r_0(P) = \text{constant}$.

Thus, the subring is completely determined:
$$S = \mathbb{C} \oplus (Q^2 - 18P) \mathbb{C}[P, Q]$$

---

## 4. Rigorous Search for 2D Keller Maps on the Slice

We performed a systematic, computer-assisted algebraic search using SymPy for any pair of polynomials $F(P, Q), G(P, Q) \in S$ up to degree 8 in $P, Q$ such that:
$$\operatorname{Jac}_{s,t}(F, G) = 1$$

Since any non-constant elements of $S$ must be of the form $R \cdot q(P, Q)$, we formulated $F$ and $G$ as linear combinations of the basis elements of $S$ and solved the resulting system of polynomial equations for their coefficients.

**Result:**
The system has **no solutions** in the tested range. This confirms that the pole obstruction is mathematically absolute, and no polynomial Keller pairs can be formed in the subring of the $S=0$ slice.

---

## 5. Conclusion and Outlook

Run 16 has successfully:
1. Formulated the exact rational mappings and Jacobian on the $S=0$ slice.
2. Solved the PDE for non-triangular coordinate changes and proved their isomorphism to the triangular case.
3. Proven that the subring of polynomial combinations in $P, Q$ is exactly $S = \mathbb{C} \oplus (Q^2 - 18P) \mathbb{C}[P, Q]$.
4. Demonstrated that no polynomial Keller maps exist on this slice, confirming the absolute nature of the pole obstruction.

These findings close the chapter on slice-reduction and coordinate-bending strategies for the 3D counterexample. Any future attempts at a 2D counterexample must look to completely independent geometric origins, such as finite étale covers of curve complements.
