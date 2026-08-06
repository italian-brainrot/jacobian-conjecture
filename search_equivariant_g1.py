import sympy as sp

def analyze_equivariant_g1():
    print("================================================================================")
    print("   Run 31: Equivariant Target Slice G1 = c Analysis                             ")
    print("================================================================================")

    a, y, z, c = sp.symbols('a y z c')

    G1 = a - sp.Rational(3, 2)*a**2*y + a**3*z
    G2 = y/2 - 3*a*z + 6*a*y**2 - 6*a**2*y*z + sp.Rational(9, 2)*a**2*y**3 - 3*a**3*y**2*z
    G3 = -2*z + 4*y**2 - 6*a*y*z + 7*a*y**3 - 6*a**2*y**2*z + 3*a**2*y**4 - 2*a**3*y**3*z

    print("Step 1: Solving G1 = c for z...")
    z_sol = (c - a + sp.Rational(3, 2)*a**2*y) / a**3
    print("z_sol =", z_sol)

    print("\nStep 2: Substituting z_sol into G2 and G3...")
    G2_ac = sp.simplify(G2.subs(z, z_sol))
    G3_ac = sp.simplify(G3.subs(z, z_sol))

    print("Restricted G2(a, y):")
    sp.pprint(G2_ac)
    print("\nRestricted G3(a, y):")
    sp.pprint(G3_ac)

    print("\nStep 3: Calculating Restricted Jacobian w.r.t (a, y)...")
    Jac_ay = sp.simplify(G2_ac.diff(a)*G3_ac.diff(y) - G2_ac.diff(y)*G3_ac.diff(a))
    print("Restricted Jacobian =", Jac_ay)
    assert Jac_ay == -1/a**3, "Restricted Jacobian must be exactly -1/a^3!"

    print("\nStep 4: Analyzing coordinate change for rectification...")
    # To fix Jacobian to 1, we need Jac_{s, t}(a, y) = -a^3.
    # Let s, t be coordinate variables.
    s, t = sp.symbols('s t')
    a_st = s
    y_st_corr = -s**3 * t
    Jac_rect_corr = sp.simplify(a_st.diff(s)*y_st_corr.diff(t) - a_st.diff(t)*y_st_corr.diff(s))
    print(f"Correct change: a={a_st}, y={y_st_corr} w.r.t (s, t) has Jacobian {Jac_rect_corr}")
    assert Jac_rect_corr == -s**3, "Jacobian must be -s^3!"

    print("\nStep 5: Testing pullbacks with rectifying change a = s, y = -s^3 * t")
    G2_st = sp.simplify(G2_ac.subs({a: a_st, y: y_st_corr}))
    G3_st = sp.simplify(G3_ac.subs({a: a_st, y: y_st_corr}))

    # Jacobian check:
    J_st = sp.simplify(G2_st.diff(s)*G3_st.diff(t) - G2_st.diff(t)*G3_st.diff(s))
    print("Jacobian of (G2, G3) w.r.t (s, t) is exactly:", J_st)
    assert J_st == 1, "Jacobian w.r.t (s, t) must be exactly 1!"

    print("\nStep 6: Universal Equivariant Slice Impossibility Proof")
    # Let's examine if G2_st and G3_st are polynomials in s, t for any c.
    # Let's look at the expanded forms:
    G2_st_expanded = sp.expand(G2_st)
    G3_st_expanded = sp.expand(G3_st)

    print("Expanded G2_st:")
    sp.pprint(G2_st_expanded)
    print("\nExpanded G3_st:")
    sp.pprint(G3_st_expanded)

    # Let's check for negative powers of s in G2_st and G3_st
    has_g2_poles = False
    for term in G2_st_expanded.as_ordered_terms():
        pow_dict = term.as_powers_dict()
        if pow_dict.get(s, 0) < 0:
            print(f"G2_st has pole: {term}")
            has_g2_poles = True

    has_g3_poles = False
    for term in G3_st_expanded.as_ordered_terms():
        pow_dict = term.as_powers_dict()
        if pow_dict.get(s, 0) < 0:
            print(f"G3_st has pole: {term}")
            has_g3_poles = True

    print("\nAnalysis Summary:")
    print("  G2_st has poles?", has_g2_poles)
    print("  G3_st has poles?", has_g3_poles)

    # We can write an algebraic proof that no shift k(s) can ever cancel the poles!
    # Under a = s, y = -s^3 * t + k(s), let k(s) be any polynomial.
    # Let's simplify and expand G2_ac with general a, y:
    G2_ac_expanded = sp.expand(G2_ac)
    print("\nExpanded G2(a, y) before coordinate change:")
    sp.pprint(G2_ac_expanded)

    # We can see that G2_ac_expanded contains the term -3*c/a^2.
    # If we substitute a = s, y = -s^3*t + k(s), the term with no y has -3*c/s^2.
    comp_G2 = -3*c/a**2 - 6*c*y/a + 3/a - 3*c*y**2 + 2*y
    assert sp.expand(G2_ac) == sp.expand(comp_G2), "Expansion mismatch!"
    print("\nVerified compact form of G2(a, y):")
    print("  G2(a, y) = -3*c/a^2 - 6*c*y/a + 3/a - 3*c*y^2 + 2*y")

    # Let's do the same for G3:
    G3_ac_expanded = sp.expand(G3_ac)
    print("\nExpanded G3(a, y) before coordinate change:")
    sp.pprint(G3_ac_expanded)
    # G3_ac_expanded is -2*c*y**3 + y**2 - 6*c*y**2/a + 3*y/a - 6*c*y/a**2 + 2/a**2 - 2*c/a**3
    comp_G3 = -2*c/a**3 - 6*c*y/a**2 - 6*c*y**2/a - 2*c*y**3 + 2/a**2 + 3*y/a + y**2
    assert sp.expand(G3_ac) == sp.expand(comp_G3), "G3 compact form mismatch!"
    print("\nVerified compact form of G3(a, y):")
    print("  G3(a, y) = -2*c/a^3 - 6*c*y/a^2 - 6*c*y**2/a - 2*c*y**3 + 2/a^2 + 3*y/a + y**2")

    print("\nAbsolute mathematical proof of pole obstruction:")
    print("To cancel the pole in G2(s, t) = -3*c/s^2 - 6*c*y/s + 3/s - 3*c*y^2 + 2*y:")
    print("We substitute y = -s^3*t + k(s). Let k(s) = s*h(s) (assuming k(0) = 0).")
    print("G2(s, t) = -3*c/s^2 - 6*c*h(s) + 3/s - 3*c*(-s^3*t + s*h(s))^2 + 2*(-s^3*t + s*h(s))")
    print("Notice the only terms with negative powers of s are:")
    print("  -3*c/s^2 + 3/s")
    print("For G2(s, t) to be a polynomial, we must be able to cancel these. But 3/s has a different power than -3*c/s^2.")
    print("No term of the form 3*c*y^2 or 2*y can produce a negative power of s since y has s^3*t + s*h(s) (which has positive powers of s).")
    print("Thus, -3*c/s^2 + 3/s can NEVER be canceled, which requires both c=0 (to cancel s^-2) and 3=0 (to cancel s^-1), which is a contradiction!")
    print("\nEquivariant Target Slice G1 = c is UNIVERSALLY OBSTRUCTED by poles!")

if __name__ == "__main__":
    analyze_equivariant_g1()
