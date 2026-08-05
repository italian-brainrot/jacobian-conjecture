import sympy as sp

def analyze_boundary_equation():
    print("================================================================================")
    print("   Analyzing the Jacobian Boundary Equation at s = 0                           ")
    print("================================================================================")

    s, t = sp.symbols('s t')
    X = s
    Y = (s**3 / 2) * t
    Q = 4 * Y + 6 / X
    P = Y**2 + 3 * Y / X + 2 / X**2

    # Let's compute the first few basis elements and their values at s = 0 and their s-derivatives at s = 0.
    # We want to see the space of pairs (F_0(t), F_1(t)) where:
    # F_0(t) = F(0, t)
    # F_1(t) = F_s(0, t)
    # for F in S_0.

    max_deg = 8
    terms_PQ = []
    terms_st = []
    for d in range(1, max_deg + 1):
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

    M_rows = []
    for a, b in all_neg_monomials:
        row = []
        for exp in expanded_terms_st:
            coeff_expr = exp.coeff(s, a).coeff(t, b)
            row.append(coeff_expr)
        M_rows.append(row)

    A = sp.Matrix(M_rows)
    ns = A.nullspace()
    print(f"Nullspace dimension: {len(ns)}")

    # For each basis element, we compute F_0(t) and F_1(t)
    basis_pairs = []
    for idx, vec in enumerate(ns):
        check_expr = 0
        for term_st, coeff in zip(terms_st, vec):
            if coeff != 0:
                check_expr += coeff * term_st
        F = sp.expand(sp.cancel(check_expr))
        F_0 = F.subs(s, 0)
        F_1 = F.diff(s).subs(s, 0)
        basis_pairs.append((F_0, F_1))
        print(f"Basis {idx}:")
        print(f"  F_0(t) = {F_0}")
        print(f"  F_1(t) = {F_1}")

    # We want to see if we can find linear combinations:
    # F_0 = sum a_k F_0_k, F_1 = sum a_k F_1_k
    # G_0 = sum b_k F_0_k, G_1 = sum b_k F_1_k
    # such that F_1 * G_0' - F_0' * G_1 = 1
    a_vars = sp.symbols(f'a_0:{len(ns)}')
    b_vars = sp.symbols(f'b_0:{len(ns)}')

    F_0_comb = sum(a_vars[i] * basis_pairs[i][0] for i in range(len(ns)))
    F_1_comb = sum(a_vars[i] * basis_pairs[i][1] for i in range(len(ns)))
    G_0_comb = sum(b_vars[i] * basis_pairs[i][0] for i in range(len(ns)))
    G_1_comb = sum(b_vars[i] * basis_pairs[i][1] for i in range(len(ns)))

    eq_boundary = sp.expand(F_1_comb * G_0_comb.diff(t) - F_0_comb.diff(t) * G_1_comb - 1)
    poly_eq = sp.Poly(eq_boundary, t)
    eqs = poly_eq.coeffs()

    print(f"\nNumber of boundary equations: {len(eqs)}")
    sol = sp.solve(eqs, list(a_vars) + list(b_vars))
    print("Solutions to boundary equation:", sol)

if __name__ == "__main__":
    analyze_boundary_equation()
