import sympy as sp

def analyze_equivariant_slices():
    print("================================================================================")
    print("   Analyzing SL_2-Equivariant Slice G1 = c                                      ")
    print("================================================================================")
    a, y, c = sp.symbols('a y c')

    # Solve G1 = c for z:
    # G1 = a - 3/2 * a^2 * y + a^3 * z = c => z = (c - a + 3/2 * a^2 * y) / a^3
    z = (c - a + sp.Rational(3, 2)*a**2*y) / a**3

    G2 = y/2 - 3*a*z + 6*a*y**2 - 6*a**2*y*z + sp.Rational(9, 2)*a**2*y**3 - 3*a**3*y**2*z
    G3 = -2*z + 4*y**2 - 6*a*y*z + 7*a*y**3 - 6*a**2*y**2*z + 3*a**2*y**4 - 2*a**3*y**3*z

    G2_simp = sp.simplify(G2)
    G3_simp = sp.simplify(G3)

    print("Restricted G2(a, y) on G1 = c:")
    sp.pprint(G2_simp)
    print("\nRestricted G3(a, y) on G1 = c:")
    sp.pprint(G3_simp)

    # Compute 2D Jacobian of (G2, G3) w.r.t (a, y)
    J = sp.simplify(G2_simp.diff(a) * G3_simp.diff(y) - G2_simp.diff(y) * G3_simp.diff(a))
    print("\nJacobian determinant of restricted (G2, G3) w.r.t (a, y):")
    sp.pprint(J)

    print("\n================================================================================")
    print("   Analyzing SL_2-Equivariant Slice G3 = c                                      ")
    print("================================================================================")
    # Solve G3 = c for z:
    # G3 = z*(-2 - 6*a*y - 6*a^2*y^2 - 2*a^3*y^3) + 4*y^2 + 7*a*y^3 + 3*a^2*y^4 = c
    # Note that -2 - 6*a*y - 6*a^2*y^2 - 2*a^3*y^3 = -2*(1 + a*y)^3
    # So G3 = -2*(1+a*y)^3 * z + y^2 * (1+a*y) * (4+3*a*y) = c
    # Let B = 1 + a*y. Then G3 = -2*B^3 * z + y^2 * B * (4 + 3*a*y) = c
    # This matches the S component representation from the 3D map under (a, y, z)!
    # Let's solve G3 = c for z:
    # z = (y^2 * (1+a*y) * (4+3*a*y) - c) / (2*(1+a*y)^3)
    B = 1 + a*y
    z_G3 = (y**2 * B * (4 + 3*a*y) - c) / (2 * B**3)

    G1_G3 = a - sp.Rational(3, 2)*a**2*y + a**3*z_G3
    G2_G3 = y/2 - 3*a*z_G3 + 6*a*y**2 - 6*a**2*y*z_G3 + sp.Rational(9, 2)*a**2*y**3 - 3*a**3*y**2*z_G3

    G1_G3_simp = sp.simplify(G1_G3)
    G2_G3_simp = sp.simplify(G2_G3)

    print("Restricted G1(a, y) on G3 = c:")
    sp.pprint(G1_G3_simp)
    print("\nRestricted G2(a, y) on G3 = c:")
    sp.pprint(G2_G3_simp)

    # Compute 2D Jacobian of (G1, G2) w.r.t (a, y)
    J_G3 = sp.simplify(G1_G3_simp.diff(a) * G2_G3_simp.diff(y) - G1_G3_simp.diff(y) * G2_G3_simp.diff(a))
    print("\nJacobian determinant of restricted (G1, G2) w.r.t (a, y):")
    sp.pprint(J_G3)

if __name__ == "__main__":
    analyze_equivariant_slices()
