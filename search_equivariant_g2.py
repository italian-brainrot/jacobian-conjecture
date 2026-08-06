import sympy as sp

def analyze_equivariant_g2():
    print("================================================================================")
    print("   Run 32: Equivariant Target Slice G2 = c and Denominator Obstructions         ")
    print("================================================================================")

    a, y, z, c = sp.symbols('a y z c')

    G1 = a - sp.Rational(3, 2)*a**2*y + a**3*z
    G2 = y/2 - 3*a*z + 6*a*y**2 - 6*a**2*y*z + sp.Rational(9, 2)*a**2*y**3 - 3*a**3*y**2*z
    G3 = -2*z + 4*y**2 - 6*a*y*z + 7*a*y**3 - 6*a**2*y**2*z + 3*a**2*y**4 - 2*a**3*y**3*z

    print("Step 1: Solving G2 = c for z...")
    # Group z terms in G2: -3*a*z - 6*a**2*y*z - 3*a**3*y**2*z = -3*a*z*(1 + a*y)**2
    # G2 = y/2 + 6*a*y**2 + 9/2 * a**2*y**3 - 3*a*z*(1 + a*y)**2 = c
    z_sol = (y/2 + 6*a*y**2 + sp.Rational(9, 2)*a**2*y**3 - c) / (3*a*(1 + a*y)**2)
    print("z_sol =", z_sol)

    print("\nStep 2: Substituting z_sol into G1 and G3...")
    G1_ac = sp.simplify(G1.subs(z, z_sol))
    G3_ac = sp.simplify(G3.subs(z, z_sol))

    print("Restricted G1(a, y):")
    sp.pprint(G1_ac)
    print("\nRestricted G3(a, y):")
    sp.pprint(G3_ac)

    print("\nStep 3: Calculating Restricted Jacobian w.r.t (a, y)...")
    Jac_ay = sp.simplify(G1_ac.diff(a)*G3_ac.diff(y) - G1_ac.diff(y)*G3_ac.diff(a))
    print("Restricted Jacobian =", Jac_ay)

    expected_Jac = -1 / (3*a*(1 + a*y)**2)
    diff_Jac = sp.simplify(Jac_ay - expected_Jac)
    print("Difference from expected Jacobian (-1 / (3*a*(1 + a*y)^2)):", diff_Jac)
    assert diff_Jac == 0, "Restricted Jacobian does not match theoretical expectation!"

    print("\nStep 4: Analyzing the Jacobian Rectification PDE...")
    print("To rectify the Jacobian to 1, we need a polynomial coordinate change a = A(s, t), y = Y(s, t) satisfying:")
    print("  Jac_{s, t}(A, Y) = -3 * A * (1 + A * Y)**2")

    # Let's perform a symbolic search to see if any low-degree polynomial coordinate change can satisfy this.
    # Let's write a general A and Y of degree <= 2 and see if they can satisfy the PDE:
    s, t = sp.symbols('s t')
    A_coeffs = sp.symbols('a_0:6')
    Y_coeffs = sp.symbols('y_0:6')

    A_expr = A_coeffs[0] + A_coeffs[1]*s + A_coeffs[2]*t + A_coeffs[3]*s**2 + A_coeffs[4]*s*t + A_coeffs[5]*t**2
    Y_expr = Y_coeffs[0] + Y_coeffs[1]*s + Y_coeffs[2]*t + Y_coeffs[3]*s**2 + Y_coeffs[4]*s*t + Y_coeffs[5]*t**2

    Jac_comp = A_expr.diff(s)*Y_expr.diff(t) - A_expr.diff(t)*Y_expr.diff(s)
    target = -3 * A_expr * (1 + A_expr * Y_expr)**2

    # We want to check if Jac_comp = target for some coefficients.
    # Since A_expr and Y_expr have degree 2, 1 + A*Y has degree up to 5, and A*(1 + A*Y)^2 has degree up to 12.
    # But Jac_comp has degree up to 2.
    # Thus, for the degrees to match, the higher-degree terms of the target must vanish.
    # Let's examine this carefully.
    print("\nDegrees of terms in the rectification equation:")
    print("  deg(Jac_comp) <=", sp.total_degree(Jac_comp, s, t))
    print("  deg(target) up to:", sp.total_degree(target, s, t))

    print("\nThis degree mismatch immediately proves that if A and Y are non-constant polynomials,")
    print("the degree of the right hand side, deg(-3 * A * (1 + A * Y)^2), is always strictly greater")
    print("than the degree of the Jacobian, deg(Jac(A, Y)), unless A * Y is constant or some trivial case.")
    print("Let's prove this rigorously:")
    print("  If deg(A) = d_A >= 1 and deg(Y) = d_Y >= 1:")
    print("  deg(Jac(A, Y)) <= d_A + d_Y - 2")
    print("  deg(-3 * A * (1 + A * Y)^2) = d_A + 2 * (d_A + d_Y) = 3 * d_A + 2 * d_Y")
    print("  Since d_A >= 1 and d_Y >= 1, we have:")
    print("    3 * d_A + 2 * d_Y >= 5")
    print("    d_A + d_Y - 2 < d_A + d_Y < 3 * d_A + 2 * d_Y")
    print("  Thus, the degree of the target is ALWAYS strictly larger than the degree of the Jacobian!")
    print("  Therefore, no non-constant polynomial coordinate change of any degree can ever satisfy the PDE!")

    print("\nConclusion:")
    print("  Equivariant Target Slice G2 = c is UNIVERSALLY OBSTRUCTED by the Jacobian rectification degree mismatch!")

if __name__ == "__main__":
    analyze_equivariant_g2()
