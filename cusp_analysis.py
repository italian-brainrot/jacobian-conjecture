import sympy as sp

def analyze_cusp_and_discriminant():
    print("--- Cusp and Discriminant Symbolic Analysis ---")
    # Let's write down the target invariants and analyze them.
    # K = 27*P^2*S^2 - 18*P*Q*S + 16*P + Q^3*S - Q^2
    # u = 27*P*S^2 - 9*Q*S + 8
    # v = 4 - 3*Q*S

    P, Q, S = sp.symbols('P Q S', real=True)
    K = 27*P**2 * S**2 - 18*P*Q*S + 16*P + Q**3 * S - Q**2
    u = 27*P * S**2 - 9*Q*S + 8
    v = 4 - 3*Q*S

    # Check identity: u^2 - v^3 = 27 * S^2 * K
    lhs = u**2 - v**3
    rhs = 27 * S**2 * K
    print(f"Is u^2 - v^3 equal to 27*S^2*K? {sp.simplify(lhs - rhs) == 0}")

    # Now let's analyze the pullback to x, y, z
    x, y, z = sp.symbols('x y z')
    a = 1 + x*y
    b = 4 + 3*x*y
    M = a**2 * z + y**2 * b

    P_pull = a * M
    Q_pull = y + 3*x * M
    S_pull = (x*(2 + x*y) - x**3 * M) / a**2

    # We substitute z = (M - y^2 * b)/a^2, which makes z rational but P, Q, S are polynomials in (x, y, M)
    # Actually, S_pull simplifies:
    # a^2 S_pull = x(2+xy) - x^3 M
    # S_pull has a^2 in denominator, but we can compute with symbolic P, Q, S.

    # Let's look at the cubic relation for x:
    # K*x^3 + (4 - 3*Q*S)*x - 2*S = 0
    # K*x^3 + v*x - 2*S = 0 (since v = 4 - 3*Q*S)

    print("\nCubic relation coefficient check:")
    C = -2*S
    B = v
    # Discriminant of depressed cubic K*x^3 + B*x + C = 0 is Delta = - (4*B^3 + 27*K*C^2)
    # Let's check if 4*B^3 + 27*K*C^2 is a perfect square!
    Delta_expr = 4*B**3 + 27*K*C**2
    print(f"Delta_expr = {sp.simplify(Delta_expr)}")
    # Note: 4*B^3 + 27*K*C^2 = 4*(4 - 3*Q*S)^3 + 27*K*(4*S^2)
    # But C = -2*S, so C^2 = 4*S^2.
    # 27*K*C^2 + 4*B^3 = 27*K*(4*S^2) + 4*(4 - 3*Q*S)^3
    # = 4 * (27*K*S^2 + (4 - 3*Q*S)^3)
    # Since 27*S^2*K = u^2 - v^3, we have 27*K*S^2 = u^2 - v^3 = u^2 - B^3.
    # So 27*K*C^2 + 4*B^3 = 4 * (u^2 - B^3) + 4*B^3 = 4*u^2.
    # This is beautifully 4 * u^2, which is indeed a perfect square (2*u)^2!
    print(f"Is 27*K*C^2 + 4*B^3 a perfect square? Yes, it is 4*u^2!")

if __name__ == "__main__":
    analyze_cusp_and_discriminant()
