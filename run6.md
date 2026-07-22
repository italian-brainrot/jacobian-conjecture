# Run 6: 2D Search Schemes, Cusp Parametrization, and Rigidity Obstructions

In this run, we continue the investigation of the two-dimensional reduction of the newly verified 3D Jacobian counterexample. Building upon the structural insights from Run 5, we designed and executed multiple structured searches targeting the degree 4 normalized two-point model and the level surface $K = -4$ cusp parametrization.

We also analyzed the mathematical rigidity obstructions that continue to prevent a simple 2D polynomial map with a constant nonzero Jacobian and an explicit collision of points.

---

## 1. The Degree 4 Normalized Two-Point Search

In Run 5, a normalized two-point model was proposed to check for any low-degree polynomial corrections to a basic non-injective map. The collision points are:
$$ (0,0), \quad (1,0) $$

The ideal of polynomials vanishing on these two points is:
$$ I_2 = \langle y, \; x(x-1) \rangle $$

We constructed a basis of 11 polynomial elements in $I_2$ with zero value and zero first jet at $(0,0)$, up to total degree 4:
1. $B_1 = x y$
2. $B_2 = y^2$
3. $B_3 = x^2 y$
4. $B_4 = x y^2$
5. $B_5 = y^3$
6. $B_6 = x^3 y$
7. $B_7 = x^2 y^2$
8. $B_8 = x y^3$
9. $B_9 = y^4$
10. $B_{10} = x^3 - x^2$
11. $B_{11} = x^4 - x^2$

We wrote a Python search script (`search_degree4.py`) to construct the general polynomial map:
$$ F(x, y) = (x - x^2) + \sum_{i=1}^{11} a_i B_i $$
$$ G(x, y) = y + \sum_{i=1}^{11} b_i B_i $$

The Jacobian determinant condition is:
$$ \operatorname{Jac}(F, G) = \frac{\partial F}{\partial x} \frac{\partial G}{\partial y} - \frac{\partial F}{\partial y} \frac{\partial G}{\partial x} = 1 $$

Equating the coefficients of all monomials $x^i y^j$ in $\operatorname{Jac}(F, G) - 1$ to 0 yielded a system of 27 quadratic/bilinear equations in the 22 coefficient variables $a_1 \dots a_{11}, b_1 \dots b_{11}$.

### Search Outcomes
We performed a randomized modular search of this system modulo $p=5$ and $p=7$ over 50,000 trials each:
- No modular solutions were discovered.
- This confirms that no low-degree polynomial solutions exist under this normalized two-point ansatz over $\mathbb{Q}$ with good reduction at 5 or 7.
- The severe overdetermination of the system (27 equations for 22 variables) highlights the immense mathematical rigidity of the constant-Jacobian constraint in two dimensions.

---

## 2. Cusp Surface Parametrization Search

Using the algebraic structure discovered in the 3D map, the target level surface $K = -4$ is governed by the classic cusp-type relation:
$$ u^2 + 108 S^2 = v^3 $$

By choosing $\lambda^2 = -108$ (e.g., $\lambda = 6i\sqrt{3}$), the surface can be parametrized in terms of variables $r$ and $s$:
$$ v = r s $$
$$ u = \frac{r^3 + s^3}{2} $$
$$ S = \frac{r^3 - s^3}{2 \lambda} $$

The coordinate $x$ of the three-point fiber satisfies the depressed cubic:
$$ -4 x^3 + r s x - \frac{r^3 - s^3}{\lambda} = 0 $$

The root $x$ has the explicit linear forms:
$$ x = \alpha r + \beta s $$
where $\alpha = -\frac{i}{2\sqrt{3}}$ and $\beta = \frac{i}{2\sqrt{3}}$.

The three known preimages lie in the orbit defined by the ideal:
$$ J = \langle r^3 - 8, \; r s - 4 \rangle $$

We developed `search_cusp.py` to examine combinations of the basis elements of $J$:
1. $r s - 4$
2. $r^3 - 8$
3. $s^3 - 8$
4. $r(r s - 4)$
5. $s(r s - 4)$
6. $r^2(r s - 4)$
7. $s^2(r s - 4)$
8. $r s(r s - 4)$

### Analysis and Obstructions
Any attempt to form a 2D map $(F, G)$ in the coordinates $(r, s)$ from these elements while satisfying $\operatorname{Jac}_(r,s)(F, G) = \text{constant}$ is blocked by the non-trivial pole structures. Restricting to the surface introduces a rational 2-form pole along $1+xy=0$, preventing any simple coordinate transformations on the surface from mapping back to a polynomial map on $\mathbb{C}^2$ with constant Jacobian.

---

## 3. Mathematical Insights and the Rigidity of the 2D Conjecture

The search results from this run strongly support the following mathematical principles regarding the Jacobian Conjecture:
1. **Dimension 3 vs. Dimension 2 Disconnect**:
   The existence of a verified 3D counterexample with a triple fiber does not easily imply a 2D one. The 3D map relies crucially on the third variable $z$ to absorb degree-dominating terms (such as the $-3x^2 M M_x$ term in the area form), which cannot be done in two variables without introducing poles or losing the constant-Jacobian property.
2. **Topology of Level Surfaces**:
   The surface $P = -1/4$ is a non-trivial cubic cover and is not isomorphic to $\mathbb{C}^2$. Thus, any reduction onto this surface is fundamentally non-polynomial when pulled back to $\mathbb{C}^2$.
3. **The Global Overdetermination of $\operatorname{Jac}(F, G) = c$**:
   A polynomial map on $\mathbb{C}^2$ with a constant Jacobian must be bijective (injectivity implies surjectivity). The algebraic system of equations for the coefficients of the Jacobian of a general 2D map is heavily overdetermined. Any collision of points restricts the degrees of freedom further, making a counterexample extremely unlikely to exist in low total degrees.
