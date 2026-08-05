import sympy as sp

def search_keller_with_h():
    print("================================================================================")
    print("   Searching for Keller Pairs on S = 0 slice with general h(s)                 ")
    print("================================================================================")

    s, t, h0 = sp.symbols('s t h0')

    X = s
    # Let's try h(s) = h0 * s, so k(s) = h0 * s^2
    Y = (s**3 / 2) * t + h0 * s**2

    Q = 4 * Y + 6 / X
    P = Y**2 + 3 * Y / X + 2 / X**2

    # We want to find polynomial F(P, Q) and G(P, Q) in s, t
    # and check if we can get Jac_{s, t}(F, G) = 1.
    # Let's search up to max_PQ_deg = 4 first.
    max_PQ_deg = 4
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

    M_rows = []
    for a, b in all_neg_monomials:
        row = []
        for exp in expanded_terms_st:
            coeff_expr = exp.coeff(s, a).coeff(t, b)
            row.append(coeff_expr)
        M_rows.append(row)

    A = sp.Matrix(M_rows)
    for h0_val in [0, 1, -1, 2]:
        A_val = A.subs(h0, h0_val)
        ns = A_val.nullspace()
        print(f"For h0 = {h0_val}: Nullspace dimension = {len(ns)}")

        if len(ns) > 0:
            basis_st = []
            for vec in ns:
                check_expr = 0
                for term_st, coeff in zip(terms_st, vec):
                    if coeff != 0:
                        check_expr += coeff * term_st
                check_expr_val = sp.expand(sp.cancel(check_expr.subs(h0, h0_val)))
                basis_st.append(check_expr_val)

            # Search for F, G
            a_vars = sp.symbols(f'a_0:{len(basis_st)}')
            b_vars = sp.symbols(f'b_0:{len(basis_st)}')

            F = sum(a_vars[i] * basis_st[i] for i in range(len(basis_st)))
            G = sum(b_vars[i] * basis_st[i] for i in range(len(basis_st)))

            J = sp.expand(sp.cancel(F.diff(s) * G.diff(t) - F.diff(t) * G.diff(s)))
            poly_J = sp.Poly(J - 1, s, t)
            eqs = poly_J.coeffs()
            sol = sp.solve(eqs, list(a_vars) + list(b_vars))
            if sol:
                print(f"  FOUND SOLUTION for h0 = {h0_val}:")
                print("  Sol:", sol)
                return
            else:
                print(f"  No solution for h0 = {h0_val}")

if __name__ == "__main__":
    search_keller_with_h()
