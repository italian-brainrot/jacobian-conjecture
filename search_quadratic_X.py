import sympy as sp

def search_quadratic_X():
    print("================================================================================")
    print("   Searching for Y of degree 6 satisfying Jac(X, Y) = X^3 / 2 for Quadratic X   ")
    print("================================================================================")

    s, t = sp.symbols('s t')

    # Define a general Y of degree 6
    deg_Y = 6
    Y = 0
    Y_coeffs = []
    idx = 0
    for d in range(deg_Y + 1):
        for i in range(d + 1):
            j = d - i
            c = sp.Symbol(f'y_{idx}')
            Y += c * s**i * t**j
            Y_coeffs.append(c)
            idx += 1

    # We will test several canonical forms of quadratic X
    # Case 1: X = s^2 + c1*s + c2*t + c3
    # Case 2: X = s*t + c1*s + c2*t + c3
    # Case 3: X = s^2 + t^2 + c1*s + c2*t + c3

    c1, c2, c3 = sp.symbols('c1 c2 c3')

    cases = [
        ("X = s^2 + c1*s + c2*t + c3", s**2 + c1*s + c2*t + c3),
        ("X = s*t + c1*s + c2*t + c3", s*t + c1*s + c2*t + c3),
        ("X = s^2 + t^2 + c1*s + c2*t + c3", s**2 + t**2 + c1*s + c2*t + c3)
    ]

    for name, X_expr in cases:
        print(f"\n--- Testing {name} ---")
        # We can try for general c1, c2, c3 or let's try with specific values to see if solutions exist,
        # or we can treat c1, c2, c3 as symbols and solve the linear system in y_i.
        # Let's first try with general c1, c2, c3 as symbols.
        jac = sp.simplify(X_expr.diff(s) * Y.diff(t) - X_expr.diff(t) * Y.diff(s))
        eq = sp.simplify(jac - X_expr**3 / 2)

        # Extract coefficients of eq w.r.t s and t
        poly_eq = sp.Poly(eq, s, t)
        coeffs_eq = poly_eq.coeffs()

        # Solve the linear system for Y_coeffs (treating c1, c2, c3 as parameters)
        sol = sp.solve(coeffs_eq, Y_coeffs)
        if sol:
            print(f"Found solutions for Y (possibly depending on c1, c2, c3):")
            # Substitute solution back into Y
            Y_sol = sp.simplify(Y.subs(sol))
            print(f"  Y = {Y_sol}")
        else:
            print("No polynomial solution for Y exists.")

if __name__ == "__main__":
    search_quadratic_X()
