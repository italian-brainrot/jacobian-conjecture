import sympy as sp

def analyze_q0_rectification():
    print("================================================================================")
    print("   STEP 1: Analyzing the Q = 0 Rational Rectification PDE                      ")
    print("================================================================================")
    x, w = sp.symbols('x w')

    # Define G(x, w) on Q = 0
    G = 2*x*(1 + x**2*w)*(1 + 3*x**2*w)

    # Compute the derivatives of G
    G_x = sp.simplify(G.diff(x))
    G_w = sp.simplify(G.diff(w))

    print("G(x, w) =", G)
    print("G_x =", G_x)
    print("G_w =", G_w)

    print("\nThe Jacobian PDE Jac(R, G) = R_x * G_w - R_w * G_x = -2 simplifies to:")
    # We want to show that under weight(x) = 1, weight(w) = -2, the PDE is homogeneous.
    # If R = w * phi(u) with u = x^2 * w:
    u = sp.Symbol('u')
    phi = sp.Function('phi')(u)

    # Let's define u_expr = x**2 * w
    u_expr = x**2 * w

    # Let's represent phi_u and its derivative phi_u_prime
    phi_u = sp.Function('phi')(u_expr)
    phi_u_prime = sp.Derivative(sp.Function('phi')(u), u).subs(u, u_expr)

    # Compute R_x and R_w for R = w * phi(x^2*w) using chain rule:
    # R_x = w * phi_u_prime * (2*x*w) = 2*x*w^2 * phi_u_prime
    # R_w = phi_u + w * phi_u_prime * x^2 = phi_u + x^2 * w * phi_u_prime
    R_x = 2*x*w**2 * phi_u_prime
    R_w = phi_u + x**2*w * phi_u_prime

    pde_lhs = R_x * G_w - R_w * G_x
    pde_lhs_simplified = sp.simplify(pde_lhs)

    print("\nProposed ODE for phi(u) where R = w * phi(u) and u = x^2 * w:")
    print("  u*(1+u)*(1+3*u)*phi'(u) + (1 + 12*u + 15*u**2)*phi(u) = 1")

    # Let's verify this by substituting R_x and R_w into the PDE and checking if it simplifies to the ODE.
    print("\n--- STEP 2: SymPy Verification of the ODE reduction ---")
    expected_pde_lhs = -2 * (u_expr * (1 + u_expr) * (1 + 3*u_expr) * phi_u_prime + (1 + 12*u_expr + 15*u_expr**2) * phi_u)
    print("Is the PDE LHS exactly equal to -2 * (ODE LHS + 1)?")
    pde_match = sp.simplify(pde_lhs_simplified - expected_pde_lhs) == 0
    print("  PDE Match Check:", pde_match)
    assert pde_match, "The PDE does not reduce to the proposed ODE!"

    print("\n--- STEP 3: Analytical Proof of No Polynomial Solution ---")
    # Let's find the integrating factor and the general solution
    # P(u) = (1 + 12*u + 15*u^2) / (u*(1+u)*(1+3*u))
    # Integrating factor: I(u) = u * (1+u)^2 * (1+3*u)^2
    # I(u) * phi(u) = \int (1+u)*(1+3*u) du = u + 2*u^2 + u^3 + C
    # phi(u) = (u + 2*u^2 + u^3 + C) / (u * (1+u)^2 * (1+3*u)^2)

    C = sp.Symbol('C')
    phi_general = (u + 2*u**2 + u**3 + C) / (u * (1+u)**2 * (1+3*u)**2)
    print("The general analytical solution for phi(u) is:")
    sp.pprint(phi_general)

    # Let's verify that this satisfies the ODE
    phi_general_prime = phi_general.diff(u)
    ode_test = sp.simplify(u * (1 + u) * (1 + 3*u) * phi_general_prime + (1 + 12*u + 15*u**2) * phi_general)
    print("\nSubstituting the general solution back into the ODE LHS yields:", ode_test)
    assert ode_test == 1, "The general analytical solution is incorrect!"
    print("YES! The general analytical solution is perfectly verified.")

    # Proof of pole presence:
    # Since the denominator of phi(u) is u * (1+u)^2 * (1+3*u)^2 which has degree 5,
    # and the numerator (u + 2*u^2 + u^3 + C) has degree at most 3,
    # any non-zero solution phi(u) is a rational function with degree <= 3 - 5 = -2 at infinity.
    # Therefore, phi(u) MUST have poles and can never be a polynomial in u.
    # Consequently, R(x, w) = w * phi(x^2*w) always possesses uncancelable poles in C^2.
    print("\nSince the denominator of phi(u) has degree 5 and the numerator has degree <= 3,")
    print("any non-zero solution phi(u) has negative degree at infinity, forcing the presence of poles.")
    print("This rigorously proves that NO polynomial partner R(x, w) can exist!")
    print("The Q = 0 rational slice rectification is mathematically and definitively obstructed!")

if __name__ == "__main__":
    analyze_q0_rectification()
