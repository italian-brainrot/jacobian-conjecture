import sympy as sp

def parameterize():
    print("================================================================================")
    print("   STEP 1: Define S, Q, P in terms of Cusp Parameters r, s on K = -4           ")
    print("================================================================================")
    r, s = sp.symbols('r s')

    lam = 6 * sp.I * sp.sqrt(3)
    alpha = -sp.I / (2 * sp.sqrt(3))
    beta = sp.I / (2 * sp.sqrt(3))

    # 1. Define S, Q, P in terms of r, s
    S_val = (r**3 - s**3) / (2 * lam)
    v_val = r * s
    u_val = (r**3 + s**3) / 2
    Q_val = (4 - v_val) / (3 * S_val)
    P_val = (u_val + 3*(4 - v_val) - 8) / (27 * S_val**2)

    print("S =", sp.simplify(S_val))
    print("Q =", sp.simplify(Q_val))
    print("P =", sp.simplify(P_val))

    print("\n================================================================================")
    print("   STEP 2: Define Branch 0 Pullback (x_0, y_0, z_0)                            ")
    print("================================================================================")
    x_0 = sp.I * sp.sqrt(3) * (s - r) / 6
    y_0 = 2 * sp.sqrt(3) * sp.I * (-r**2 - r*s + 2*r - s**2 + 2*s + 4) / (r**3 - s**3)

    print("x_0 =", x_0)
    print("y_0 =", y_0)

    # Recover z_0 from M = (Q - y)/(3*x), z = (M - y^2*b)/a^2
    a = 1 + x_0 * y_0
    b = 4 + 3 * x_0 * y_0
    M = (Q_val - y_0) / (3 * x_0)
    z_0 = (M - y_0**2 * b) / a**2

    # 3D map equations verification
    P_calc = sp.simplify(a * M)
    Q_calc = sp.simplify(y_0 + 3 * x_0 * M)
    S_calc = sp.simplify((x_0 * (2 + x_0 * y_0) - x_0**3 * M) / a**2)

    P_diff = sp.simplify(P_calc - P_val)
    Q_diff = sp.simplify(Q_calc - Q_val)
    S_diff = sp.simplify(S_calc - S_val)

    print(f"\nVerifying Branch 0 Pullback:")
    print(f"  P difference: {P_diff}")
    print(f"  Q difference: {Q_diff}")
    print(f"  S difference: {S_diff}")

    assert P_diff == 0 and Q_diff == 0 and S_diff == 0, "Branch 0 verification failed!"
    print("YES! Branch 0 Pullback is perfectly verified!")

    print("\n================================================================================")
    print("   STEP 3: Verify Invariance of Target Components Under Cyclic mu_3 Action    ")
    print("================================================================================")
    # Target components S, Q, P are invariant because they only depend on r^3, s^3 and r*s
    # Under cyclic action (r, s) -> (w*r, w^2*s):
    # (w*r)^3 = r^3, (w^2*s)^3 = s^3, (w*r)*(w^2*s) = r*s
    print("Since target components are rational functions of S, u, and v which depend only on r^3, s^3, and r*s,")
    print("they are algebraically invariant under (r, s) -> (w*r, w^2*s) where w^3 = 1.")
    print("This guarantees that Branch 1 and Branch 2 obtained by cyclic action are also valid pullbacks!")

    print("\n================================================================================")
    print("   STEP 4: Compute Sheet Jacobian w.r.t (r, s)                                  ")
    print("================================================================================")
    dx_dr = x_0.diff(r)
    dx_ds = x_0.diff(s)
    dy_dr = y_0.diff(r)
    dy_ds = y_0.diff(s)

    J_xy_rs = dx_dr * dy_ds - dx_ds * dy_dr
    print("Jacobian(x, y) w.r.t (r, s) =")
    sp.pprint(sp.simplify(J_xy_rs))

if __name__ == "__main__":
    parameterize()
