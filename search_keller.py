import sympy as sp

s, t = sp.symbols('s t')
X = s
Y = (s**3 / 2) * t
Q = 4 * Y + 6 / X
P = Y**2 + 3 * Y / X + 2 / X**2

# Let's perform a correct search using sp.Poly to get the equations in terms of the coefficients.
max_PQ_deg = 8
terms_PQ = []
terms_st = []
for d in range(1, max_PQ_deg + 1):
    for i in range(d + 1):
        j = d - i
        terms_PQ.append(sp.Symbol('P')**i * sp.Symbol('Q')**j)
        terms_st.append(sp.simplify(P**i * Q**j))

# Find all negative-power monomials of s in any of the terms_st
all_neg_monomials = set()
expanded_terms_st = []
for expr in terms_st:
    exp = sp.expand(expr)
    expanded_terms_st.append(exp)
    coeff_dict = exp.as_coefficients_dict()
    for mono in coeff_dict.keys():
        pow_dict = mono.as_powers_dict()
        a = pow_dict.get(s, 0)
        b = pow_dict.get(t, 0)
        if a < 0:
            all_neg_monomials.add((a, b))

all_neg_monomials = sorted(list(all_neg_monomials))
print(f"Number of negative-power-of-s monomials: {len(all_neg_monomials)}")

# Construct the matrix of coefficients of these negative-power monomials
M_rows = []
for a, b in all_neg_monomials:
    row = []
    for exp in expanded_terms_st:
        coeff_dict = exp.as_coefficients_dict()
        val = 0
        for mono, coeff in coeff_dict.items():
            pow_dict = mono.as_powers_dict()
            if pow_dict.get(s, 0) == a and pow_dict.get(t, 0) == b:
                val = coeff
                break
        row.append(val)
    M_rows.append(row)

A = sp.Matrix(M_rows)
null_space = A.nullspace()
print(f"Nullspace dimension (number of independent polynomials in s, t): {len(null_space)}")

basis_PQ = []
basis_st = []
for idx, vec in enumerate(null_space):
    poly_expr = 0
    check_expr = 0
    for term_PQ, term_st, coeff in zip(terms_PQ, terms_st, vec):
        if coeff != 0:
            poly_expr += coeff * term_PQ
            check_expr += coeff * term_st
    basis_PQ.append(poly_expr)
    basis_st.append(sp.simplify(check_expr))

# Now, we want to find if there exist F, G as linear combinations of these basis elements:
# F = sum a_k basis_st[k]
# G = sum b_k basis_st[k]
# such that Jac_{s, t}(F, G) = 1.
# Let's set up the variables and equations.
print("\nSearching for F, G such that Jac_{s, t}(F, G) = 1...")
a = sp.symbols(f'a_0:{len(basis_st)}')
b = sp.symbols(f'b_0:{len(basis_st)}')

F = sum(a[i] * basis_st[i] for i in range(len(basis_st)))
G = sum(b[i] * basis_st[i] for i in range(len(basis_st)))

J = sp.simplify(F.diff(s) * G.diff(t) - F.diff(t) * G.diff(s))

# Using sp.Poly to correctly extract the coefficients of s and t:
poly_J = sp.Poly(J - 1, s, t)
eqs = poly_J.coeffs()

print(f"Number of equations to solve: {len(eqs)}")
sol = sp.solve(eqs, list(a) + list(b))
print("Solutions:", sol)
