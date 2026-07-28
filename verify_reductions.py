import sympy as sp

def verify_all_reductions():
    print("================================================================================")
    print("   STEP 1: Symbolic Verification of the 3D Map and its S = c Slice-Reduction   ")
    print("================================================================================")
    x, y, z, c = sp.symbols('x y z c')
    a = 1 + x*y
    b = 4 + 3*x*y

    # Define 3D map components
    P_3d = a**3 * z + y**2 * a * b
    Q_3d = y + 3*x*a**2 * z + 3*x*y**2 * b
    S_3d = 2*x - 3*x**2*y - x**3*z

    # Compute Jacobian of 3D map
    J_3d = sp.Matrix([P_3d, Q_3d, S_3d]).jacobian([x, y, z])
    det_J_3d = sp.simplify(J_3d.det())
    print(f"3D Map Jacobian Determinant: {det_J_3d}")
    assert det_J_3d == -2, "3D map Jacobian determinant must be -2!"

    # Solve S_3d = c for z
    z_sol = sp.solve(S_3d - c, z)[0]
    print(f"z-parameterization on S = c: {z_sol}")

    # Substitute z_sol into P and Q
    P_c = sp.simplify(P_3d.subs(z, z_sol))
    Q_c = sp.simplify(Q_3d.subs(z, z_sol))
    print(f"P(x,y) on S = c:\n{P_c}\n")
    print(f"Q(x,y) on S = c:\n{Q_c}\n")

    # Compute Jacobian determinant of (P_c, Q_c) w.r.t (x, y)
    J_c = sp.simplify(P_c.diff(x) * Q_c.diff(y) - P_c.diff(y) * Q_c.diff(x))
    print(f"Restricted 2D Jacobian w.r.t (x, y): {J_c}")
    assert J_c == 2/x**3, "Jacobian determinant of restricted (P, Q) must be 2/x^3!"

    print("\n================================================================================")
    print("   STEP 2: Verification of Compact Representation via u = y + 1/x   ")
    print("================================================================================")
    u = sp.Symbol('u')
    # Compact representations:
    P_u = -c*u**3 + u**2 + u/x
    Q_u = -3*c*u**2 + 4*u + 2/x

    # Substituting u = y + 1/x
    P_u_subs = sp.expand(P_u.subs(u, y + 1/x))
    Q_u_subs = sp.expand(Q_u.subs(u, y + 1/x))

    assert sp.expand(P_c) == P_u_subs, "P compact representation with u is incorrect!"
    assert sp.expand(Q_c) == Q_u_subs, "Q compact representation with u is incorrect!"
    print("YES! Compact representations w.r.t u = y + 1/x are perfectly verified.")

    print("\n================================================================================")
    print("   STEP 3: Coordinate Change to (s, t) and Pole Cancellations   ")
    print("================================================================================")
    s, t = sp.symbols('s t')
    # Coordinate change: x = s, y = s^3/2 * t
    x_st = s
    y_st = s**3 / 2 * t

    P_st = sp.simplify(P_c.subs({x: x_st, y: y_st}))
    Q_st = sp.simplify(Q_c.subs({x: x_st, y: y_st}))

    # Verify Jacobian w.r.t (s, t) is 1
    J_st = sp.simplify(P_st.diff(s) * Q_st.diff(t) - P_st.diff(t) * Q_st.diff(s))
    print(f"Jacobian(P, Q) w.r.t (s, t): {J_st}")
    assert J_st == 1, "Jacobian w.r.t (s, t) must be exactly 1!"

    print("\n================================================================================")
    print("   STEP 4: Universal Subring Theorem (For c != 0)   ")
    print("================================================================================")
    # Define R = 27*c*P^2 - 18*P*Q + Q^3
    R = 27*c*P_st**2 - 18*P_st*Q_st + Q_st**3
    R_expanded = sp.expand(R)

    # Check for any negative powers of s in R_expanded
    has_neg_powers = False
    for term in R_expanded.as_ordered_terms():
        pow_dict = term.as_powers_dict()
        if pow_dict.get(s, 0) < 0:
            print(f"Warning: term has negative power of s: {term}")
            has_neg_powers = True

    assert not has_neg_powers, "R has negative powers of s!"
    print("YES! R has NO negative powers of s, making it a genuine polynomial in s, t!")

    # Evaluate R at s = 0
    R_s0 = R_expanded.subs(s, 0)
    print(f"R(s=0, t) = {R_s0}")
    assert R_s0 == 9*c*t, "R(0, t) must equal 9*c*t!"
    print("YES! R(0, t) = 9*c*t != 0 for c != 0. Thus, R is not divisible by s.")

    print("\n================================================================================")
    print("   STEP 5: Subring Analysis for S_0 (For c = 0)   ")
    print("================================================================================")
    # For c = 0:
    P_0_st = sp.simplify(P_st.subs(c, 0))
    Q_0_st = sp.simplify(Q_st.subs(c, 0))

    # Verify Q^2 - 16P = 4/s^2
    relation_16 = sp.simplify(Q_0_st**2 - 16*P_0_st)
    print(f"Q^2 - 16P on S_0: {relation_16}")
    assert relation_16 == 4/s**2, "Q^2 - 16P must equal 4/s^2 on S_0!"

    # Verify R_0 = Q^2 - 18P has no poles
    R_0 = sp.simplify(Q_0_st**2 - 18*P_0_st)
    print(f"R_0 = Q^2 - 18P on S_0: {R_0}")
    # Check for negative powers
    has_neg_powers_0 = False
    for term in sp.expand(R_0).as_ordered_terms():
        pow_dict = term.as_powers_dict()
        if pow_dict.get(s, 0) < 0:
            has_neg_powers_0 = True
    assert not has_neg_powers_0, "R_0 has negative powers of s!"
    print("YES! R_0 has NO negative powers of s, making it a genuine polynomial in s, t!")

    print("\nAll symbolic verifications passed successfully!")

if __name__ == "__main__":
    verify_all_reductions()
