import sympy as sp

def search_equivariant_slice():
    print("================================================================================")
    print("   STEP 1: Define equivariant components G1, G2, G3 and check 3D Jacobian      ")
    print("================================================================================")
    a, y, z = sp.symbols('a y z')

    G1 = a - sp.Rational(3, 2)*a**2*y + a**3*z
    G2 = y/2 - 3*a*z + 6*a*y**2 - 6*a**2*y*z + sp.Rational(9, 2)*a**2*y**3 - 3*a**3*y**2*z
    G3 = -2*z + 4*y**2 - 6*a*y*z + 7*a*y**3 - 6*a**2*y**2*z + 3*a**2*y**4 - 2*a**3*y**3*z

    # 3D Jacobian of (G1, G2, G3) w.r.t (a, y, z)
    J_3d = sp.Matrix([G1, G2, G3]).jacobian([a, y, z])
    det_J_3d = sp.simplify(J_3d.det())
    print("Jacobian determinant of (G1, G2, G3) w.r.t (a, y, z):", det_J_3d)

    print("\n================================================================================")
    print("   STEP 2: Restricting Source Coordinate 'a' to a Constant 'c'                ")
    print("================================================================================")
    c_val = sp.Symbol('c')
    # Substitute a = c_val
    G2_ac = sp.simplify(G2.subs(a, c_val))
    G3_ac = sp.simplify(G3.subs(a, c_val))

    print(f"Restricted G2(y, z) on a = c:")
    sp.pprint(G2_ac)
    print(f"\nRestricted G3(y, z) on a = c:")
    sp.pprint(G3_ac)

    # Compute 2D Jacobian w.r.t (y, z)
    J_2d = sp.simplify(G2_ac.diff(y) * G3_ac.diff(z) - G2_ac.diff(z) * G3_ac.diff(y))
    print("\nJacobian determinant of restricted (G2, G3) w.r.t (y, z):")
    sp.pprint(J_2d)

    print("\n================================================================================")
    print("   STEP 3: Check Injectivity and Invertibility of (G2, G3) on a = c           ")
    print("================================================================================")
    # We want to solve G2_ac = u, G3_ac = v for y and z.
    # Let's see if there is a unique solution or multiple solutions.
    u, v = sp.symbols('u v')
    eqs = [G2_ac - u, G3_ac - v]

    # Let's solve the system for (y, z) using sp.solve
    print("Solving G2_ac = u, G3_ac = v for (y, z) with c=1 as a test case:")
    eqs_c1 = [eq.subs(c_val, 1) for eq in eqs]
    sol_c1 = sp.solve(eqs_c1, [y, z])
    print(f"Found {len(sol_c1)} solutions:")
    for idx, sol in enumerate(sol_c1):
        print(f"  Solution {idx + 1}: y = {sol[0]}")

    print("\nLet's analyze if the solution is a polynomial in u, v:")
    for idx, sol in enumerate(sol_c1):
        is_poly_y = sol[0].is_polynomial(u, v)
        print(f"  Solution {idx + 1}: y is polynomial in (u,v)? {is_poly_y}")

    print("\n================================================================================")
    print("   STEP 4: Verify Algebraic Identities from Tao's Blog Digestion                ")
    print("================================================================================")
    # Define B, C, and W:
    B = 1 + a*y
    C = 1 - sp.Rational(3, 2)*a*y + a**2*z
    W = 1 - C*B**2

    # Verify identity 1: a*G2 = 2*B + 3*W - 2
    id1_left = a*G2
    id1_right = 2*B + 3*W - 2
    diff1 = sp.simplify(id1_left - id1_right)
    print("Identity 1 (a*G2 == 2*B + 3*W - 2) diff:", diff1)
    assert diff1 == 0, "Identity 1 failed!"

    # Verify identity 2: a^2*G3 = B*(B + 2*W - 1)
    id2_left = a**2*G3
    id2_right = B*(B + 2*W - 1)
    diff2 = sp.simplify(id2_left - id2_right)
    print("Identity 2 (a^2*G3 == B*(B + 2*W - 1)) diff:", diff2)
    assert diff2 == 0, "Identity 2 failed!"

    print("\nYES! The exact algebraic identities on the variety are fully verified:")
    print("  a * G2 = 2*B + 3*W - 2")
    print("  a^2 * G3 = B * (B + 2*W - 1)")
    print("where B = 1 + a*y, C = 1 - 3/2*a*y + a^2*z, and W = 1 - C*B^2.")

if __name__ == "__main__":
    search_equivariant_slice()
