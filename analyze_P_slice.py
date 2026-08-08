import sympy as sp

def analyze_P_slice():
    print("================================================================================")
    print("   Analyzing target slice P = c                                                ")
    print("================================================================================")
    x, y, c = sp.symbols('x y c')
    a = 1 + x*y
    b = 4 + 3*x*y

    # Solve P = a^3 * z + y^2 * a * b = c for z
    # z = (c - y**2 * a * b) / a**3
    z = (c - y**2 * a * b) / a**3

    # Substitute z into Q and S
    Q = y + 3*x*a**2 * z + 3*x*y**2 * b
    S = 2*x - 3*x**2 * y - x**3 * z

    Q_simp = sp.simplify(Q)
    S_simp = sp.simplify(S)

    print("Restricted Q(x, y) on P = c:")
    sp.pprint(Q_simp)
    print("\nRestricted S(x, y) on P = c:")
    sp.pprint(S_simp)

    # Compute 2D Jacobian determinant w.r.t (x, y)
    J = sp.simplify(Q_simp.diff(x) * S_simp.diff(y) - Q_simp.diff(y) * S_simp.diff(x))
    print("\nJacobian determinant of restricted (Q, S) w.r.t (x, y):")
    sp.pprint(J)

if __name__ == "__main__":
    analyze_P_slice()
