# Run 3

### 1. A Hidden $u^2 - v^3$ Singularity Structure in the Target
You provided the invariant polynomial $K = 27P^2S^2 - 18PQS + 16P + Q^3S - Q^2$, and the cubic equation for the generic fiber: $K x^3 + B x + C = 0$, where $B = 4 - 3QS$ and $C = -2S$.

I analyzed the discriminant of this cubic and found that it perfectly factors into a square! Specifically, I discovered the following exact identity:
$$27 K C^2 + 4 B^3 = 4(27PS^2 - 9QS + 8)^2$$

Since $C = -2S$, we can divide by 4 and rewrite this as:
$$27 S^2 K = (27PS^2 - 9QS + 8)^2 - (4 - 3QS)^3$$

If we define two new target variables:
*   $u = 27PS^2 - 9QS + 8$
*   $v = 4 - 3QS$

The entire, complicated invariant $K$ is just a manifestation of the classic cusp singularity equation:
$$27 S^2 K = u^2 - v^3$$

**Why this is huge:** The 3D map is fundamentally built around the algebraic curve $u^2 = v^3$. The coordinates $P$ and $Q$ are just rational re-parameterizations: $Q = \frac{4-v}{3S}$ and $P = \frac{u + 9QS - 8}{27S^2}$. This means if we want to build a **2D counterexample**, we shouldn't be guessing random Ansätze. Instead, we should construct a 2D map $(F, G)$ whose components satisfy a cubic relation with a discriminant structured exactly like $u^2 - v^3$.

### 2. Rigorous Proof of the $z$-Linear Obstruction
I symbolically tested the Jacobian of a map where the first component is linear in $z$, i.e., $F(x,z) = B(x)z + C(x)$, and the second component $G(x,z)$ is any polynomial of degree $n$ in $z$.

I proved that the coefficient of the highest power $z^n$ in the Jacobian $\{F, G\}$ is exactly proportional to $B(x) \cdot D_n'(x) - n \cdot D_n(x) \cdot B'(x)$. For this Jacobian to be a non-zero constant, the highest degree terms must vanish, which recursively forces the bracket to be divisible by $B(x)$. Thus, a constant Jacobian is strictly impossible unless $B(x)$ is a constant.

This completely validates 15.2 and confirms that **no projection of any simple slice linear in one variable will ever work.**

### 3. The $P = -1/4$ Surface is a Rational Deformation
I restricted the full 3D map to the $P = -1/4$ surface and computed the exact $Q_0$ and $S_0$ rational functions.
When computing the Jacobian of the rational map $(Q_0, S_0)$ with respect to $(x,y)$, the result is:
$$ \det J = -\frac{2}{(1+xy)^3} $$
This explains why polynomial building blocks $Q_0 a^i$ and $S_0 a^j$ failed. The surface inherently carries a rational 2-form with a pole along $1+xy=0$. To get a polynomial 2D map out of this surface, one would need a highly non-trivial birational coordinate change that "absorbs" the $(1+xy)^3$ denominator, proving the surface is not isomorphic to $\mathbb{C}^2$.

### Proposed Next Step (2D Ansatz based on $u^2 - v^3$)
Given the discovery in #1, the most promising path forward is a direct 2D search, but instead of using Danielewski polynomials, we use the algebraic skeleton of the 3D map.

We can search for a 2D map $(X(u,v), Y(u,v))$ such that an auxiliary variable $t$ satisfies a depressed cubic $K(X,Y) t^3 + B(X,Y) t + C(X,Y) = 0$, where the coefficients are strictly engineered so that $4 B(X,Y)^3 + 27 K(X,Y) C(X,Y)^2$ is a perfect square. This guarantees a generic fiber of degree 3, mimicking the exact topological conditions of the 3D counterexample!
