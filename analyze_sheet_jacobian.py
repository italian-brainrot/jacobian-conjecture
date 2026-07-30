import sympy as sp

def analyze_sheet_jacobian():
    print("================================================================================")
    print("   STEP 1: Define Cusp Sheet Coordinates (x_0, y_0)                            ")
    print("================================================================================")
    r, s = sp.symbols('r s')

    # Branch 0 coordinates
    x_0 = sp.I * sp.sqrt(3) * (s - r) / 6
    y_0 = 2 * sp.sqrt(3) * sp.I * (-r**2 - r*s + 2*r - s**2 + 2*s + 4) / (r**3 - s**3)

    print("x_0 =", x_0)
    print("y_0 =", y_0)

    print("\n================================================================================")
    print("   STEP 2: Compute Partial Derivatives of (x_0, y_0)                            ")
    print("================================================================================")
    dx_dr = x_0.diff(r)
    dx_ds = x_0.diff(s)
    dy_dr = y_0.diff(r)
    dy_ds = y_0.diff(s)

    print("dx_0 / dr =", dx_dr)
    print("dx_0 / ds =", dx_ds)
    print("\ndy_0 / dr =", sp.simplify(dy_dr))
    print("dy_0 / ds =", sp.simplify(dy_ds))

    print("\n================================================================================")
    print("   STEP 3: Compute and Analyze Sheet Jacobian w.r.t (r, s)                     ")
    print("================================================================================")
    # Jacobian determinant of (x_0, y_0) w.r.t (r, s)
    J_rs = dx_dr * dy_ds - dx_ds * dy_dr
    J_rs_simplified = sp.simplify(J_rs)

    print("Simplified Sheet Jacobian:\n")
    sp.pprint(J_rs_simplified)

    print("\nLet's analyze the pole structure of the Sheet Jacobian:")
    print("The denominator of the Sheet Jacobian is:")
    print("  Den_J = r^5 + r^4*s + r^3*s^2 - r^2*s^3 - r*s^4 - s^5")
    print("Which factors as:")
    print("  Den_J = (r - s) * (r^2 + r*s + s^2)^2 = (r^3 - s^3) * (r^2 + r*s + s^2)")

    # Define the numerator and check if it vanishes on r - s = 0 or r^2 + r*s + s^2 = 0
    num_J = 2*(-r**2 - 4*r*s - 6*r - s**2 - 6*s)
    print(f"\nNumerator of Sheet Jacobian: Num_J(r, s) = {num_J}")

    # Substitute s = r into Num_J to see if r - s = 0 is a factor
    num_J_rr = sp.simplify(num_J.subs(s, r))
    print(f"Evaluating Num_J along r = s: {num_J_rr}")

    print("\nBecause Num_J(r, r) = -2*(6*r^2 + 12*r) is not identically zero, (r - s) is NOT a factor of the numerator.")
    print("This means the Sheet Jacobian has an uncancelable pole of order at least 1 along r - s = 0 (which is the divisor S = 0).")
    print("Thus, the Sheet Jacobian is not a constant, nor can it be rectified to a constant")
    print("without introducing uncancelable poles along the divisor r - s = 0.")
    print("\nThis concludes the symbolic pole analysis of the sheet Jacobian!")

if __name__ == "__main__":
    analyze_sheet_jacobian()
