import sympy as sp

def run_verification():
    print("--- STEP 1: Verify P and Q on the general slice S = c ---")
    x, y, c = sp.symbols('x y c')

    # On S = 2*x - 3*x**2*y - x**3*z = c, we solve for z:
    z = (2*x - 3*x**2*y - c) / x**3

    # 3D map P, Q components with z substituted:
    a = 1 + x*y
    P = a**3 * z + y**2 * a * (4 + 3*x*y)
    Q = y + 3*x*a**2 * z + 3*x*y**2 * (4 + 3*x*y)

    P_simplified = sp.simplify(P)
    Q_simplified = sp.simplify(Q)

    print("Simplified P(x, y) on S = c:")
    sp.pprint(P_simplified)
    print("\nSimplified Q(x, y) on S = c:")
    sp.pprint(Q_simplified)

    # Check the Jacobian w.r.t (x, y)
    J = sp.simplify(P_simplified.diff(x) * Q_simplified.diff(y) - P_simplified.diff(y) * Q_simplified.diff(x))
    print("\nJacobian determinant of (P, Q) w.r.t (x, y):", J)
    assert J == 2/x**3, "Jacobian determinant of restricted (P, Q) must be 2/x^3!"

    print("\n--- STEP 2: Verify representation using u = y + 1/x ---")
    u = sp.Symbol('u')
    # Let's check if our proposed u-representations match the expanded P and Q:
    P_u = -c*u**3 + u**2 + u/x
    Q_u = -3*c*u**2 + 4*u + 2/x

    # Substitute u = y + 1/x
    P_u_subs = sp.expand(P_u.subs(u, y + 1/x))
    Q_u_subs = sp.expand(Q_u.subs(u, y + 1/x))

    assert sp.expand(P_simplified) == P_u_subs, "P representation with u is incorrect!"
    assert sp.expand(Q_simplified) == Q_u_subs, "Q representation with u is incorrect!"
    print("YES! P and Q are perfectly represented by u = y + 1/x:")
    print("  P(x, y) = -c*u^3 + u^2 + u/x")
    print("  Q(x, y) = -3*c*u^2 + 4*u + 2/x")

    print("\n--- STEP 3: Verify Laurent series pole cancellation in R ---")
    s, t = sp.symbols('s t')
    # Coordinate change: x = s, y = s^3/2 * t
    x_st = s
    y_st = s**3 / 2 * t

    P_st = P_simplified.subs({x: x_st, y: y_st})
    Q_st = Q_simplified.subs({x: x_st, y: y_st})

    # Check Jacobian w.r.t (s, t)
    # Since Jac_{s, t}(x, y) = s^3/2, the Jacobian of P, Q w.r.t (s, t) should be (2/s^3) * (s^3/2) = 1
    J_st = sp.simplify(P_st.diff(s) * Q_st.diff(t) - P_st.diff(t) * Q_st.diff(s))
    print("Jacobian determinant of (P, Q) w.r.t (s, t):", J_st)
    assert J_st == 1, "Jacobian w.r.t (s, t) must be exactly 1!"

    # We define R = 27*c*P^2 - 18*P*Q + Q^3
    R = 27*c*P_st**2 - 18*P_st*Q_st + Q_st**3
    R_expanded = sp.expand(R)

    # Let's check for any negative powers of s in R_expanded
    has_neg_powers = False
    for term in R_expanded.as_ordered_terms():
        pow_dict = term.as_powers_dict()
        if pow_dict.get(s, 0) < 0:
            print(f"Warning: term has negative power of s: {term}")
            has_neg_powers = True

    if not has_neg_powers:
        print("YES! R = 27*c*P^2 - 18*P*Q + Q^3 has NO negative powers of s!")
        print("R is a genuine polynomial in s, t for any constant c!")
        print("\nSimplified R(s, t) / t:")
        sp.pprint(sp.simplify(R / t))
    else:
        raise ValueError("R has negative powers of s!")

if __name__ == "__main__":
    run_verification()
