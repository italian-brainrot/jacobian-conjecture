import sympy as sp

# Let's verify the change of variables: s, t
# We want X(s, t), Y(s, t) such that Jac_{s, t}(X, Y) = X^3 / 2
# Let's check with X = s, Y = s^3/2 * t
s, t = sp.symbols('s t')
X = s
Y = s**3 / 2 * t

J_XY = X.diff(s)*Y.diff(t) - X.diff(t)*Y.diff(s)
print("Jacobian(X, Y) =", sp.simplify(J_XY))
print("X^3 / 2 =", sp.simplify(X**3 / 2))

# Now let's substitute X for x, and Y for y in P_restricted, Q_restricted:
P_subs = P_restricted = (X*Y + 1)*(X*Y + 2)/X**2
Q_subs = 4*Y + 6/X

print("P in s, t =", sp.simplify(P_subs))
print("Q in s, t =", sp.simplify(Q_subs))

# Check Jacobian of (P_subs, Q_subs) w.r.t (s, t)
J_PQ_st = P_subs.diff(s) * Q_subs.diff(t) - P_subs.diff(t) * Q_subs.diff(s)
print("Jacobian(P, Q) w.r.t (s, t) =", sp.simplify(J_PQ_st))
