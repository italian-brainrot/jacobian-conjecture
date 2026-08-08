import sympy as sp

def analyze_Q_slice():
    print("================================================================================")
    print("   Analyzing target slice Q = c                                                ")
    print("================================================================================")
    x, y, c = sp.symbols('x y c')
    a = 1 + x*y
    b = 4 + 3*x*y

    # Q = y + 3*x*a**2 * z + 3*x*y**2 * b = c
    # Solve for z:
    # z = (c - y - 3*x*y**2 * b) / (3*x*a**2)
    z = (c - y - 3*x*y**2 * b) / (3*x*a**2)

    # Substitute z into P and S
    P = a**3 * z + y**2 * a * b
    S = 2*x - 3*x**2 * y - x**3 * z

    P_simp = sp.simplify(P)
    S_simp = sp.simplify(S)

    print("Restricted P(x, y) on Q = c:")
    sp.pprint(P_simp)
    print("\nRestricted S(x, y) on Q = c:")
    sp.pprint(S_simp)

    # Compute 2D Jacobian determinant w.r.t (x, y)
    J = sp.simplify(P_simp.diff(x) * S_simp.diff(y) - P_simp.diff(y) * S_simp.diff(x))
    print("\nJacobian determinant of restricted (P, S) w.r.t (x, y):")
    sp.pprint(J)

if __name__ == "__main__":
    analyze_Q_slice()
