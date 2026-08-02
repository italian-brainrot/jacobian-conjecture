import sympy as sp

def search():
    print("================================================================================")
    print("   Searching for Polynomial Solutions to the Jacobian PDE:                     ")
    print("   X_s * Y_t - X_t * Y_s = 1/2 * X^3                                           ")
    print("================================================================================")
    s, t = sp.symbols('s t')

    # Case 1: X is quadratic, i.e., degree 2
    # Let's write a general quadratic X(s, t)
    # We can use affine transformations to simplify X.
    # Since X is quadratic, can we find Y such that Jac(X, Y) = 1/2 * X^3?
    # Let's write down a general polynomial for Y of degree up to 6.

    # We want to check if any non-degenerate solutions exist where X is not a power of a linear form.
    # Let's test a simple quadratic X = s^2 + t.
    X1 = s**2 + t
    # We want to solve for Y: X1_s * Y_t - X1_t * Y_s = 1/2 * X1^3
    # 2*s * Y_t - Y_s = 1/2 * (s^2 + t)^3
    # This is a linear first order PDE for Y. Let's find its general solution using Method of Characteristics.
    # The characteristic equations are:
    # ds / (-1) = dt / (2*s) = dY / (1/2 * (s^2 + t)^3)
    # ds / (-1) = dt / (2*s) => 2*s*ds + dt = 0 => s^2 + t = C1 (constant of characteristic)
    # Then along the characteristic curve:
    # dY / ds = -1/2 * C1^3
    # Y = -1/2 * C1^3 * s + C2 = -1/2 * (s^2 + t)^3 * s + f(s^2 + t)
    # Since any solution Y must be of the form -1/2 * s * (s^2 + t)^3 + f(s^2 + t) for some function f,
    # let's check if this can be a polynomial.
    # Yes! If f is any polynomial, then Y is a polynomial!
    # Let's verify this solution.
    Y1 = -sp.Rational(1, 2) * s * (s**2 + t)**3
    J1 = sp.simplify(X1.diff(s) * Y1.diff(t) - X1.diff(t) * Y1.diff(s))
    print(f"For X = s^2 + t and Y = {Y1}:")
    print(f"  Jacobian(X, Y) = {J1}")
    print(f"  Is Jacobian equal to 1/2 * X^3? {J1 == sp.simplify(sp.Rational(1, 2) * X1**3)}")

    # Wow, that is beautiful! This is a completely new non-triangular coordinate change!
    # Let's analyze if we plug this new coordinate change into P and Q on the S = 0 rational slice.
    # Recall on S = 0:
    # P(x, y) = (x*y + 1)*(x*y + 2) / x^2
    # Q(x, y) = 4*y + 6/x
    # Under our new coordinate change (X1, Y1):
    # P = (X1*Y1 + 1)*(X1*Y1 + 2) / X1^2
    # Q = 4*Y1 + 6/X1
    # Let's check their expressions:
    P_new = (X1 * Y1 + 1) * (X1 * Y1 + 2) / X1**2
    Q_new = 4 * Y1 + 6 / X1
    print("\nUnder new coordinate change:")
    print("  P =", sp.simplify(P_new))
    print("  Q =", sp.simplify(Q_new))

    # Are there negative powers of (s^2 + t) in P and Q?
    # Yes, both will have (s^2 + t) in the denominator!
    # Specifically, Q_new has 6 / (s^2 + t), and P_new has (s^2+t)^2 in the denominator.
    # Can we find a polynomial combination of P_new and Q_new that cancels the poles?
    # Let's check R_new = Q_new^2 - 18 * P_new:
    R_new = Q_new**2 - 18 * P_new
    print("\nCheck R = Q^2 - 18*P:")
    print("  R =", sp.simplify(R_new))

if __name__ == "__main__":
    search()
