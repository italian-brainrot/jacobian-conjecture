import sympy as sp

def search_keller_high(max_deg):
    print("================================================================================")
    print(f"   Exhaustive Search for Keller Pairs on S = 0 up to degree {max_deg}          ")
    print("================================================================================")

    s, t = sp.symbols('s t')
    X = s
    Y = (s**3 / 2) * t
    Q = 4 * Y + 6 / X
    P = Y**2 + 3 * Y / X + 2 / X**2

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
    print(f"Number of negative-power-of-s monomials: {len(all_neg_monomials)}")

    M_rows = []
    for a, b in all_neg_monomials:
        row = []
        for exp in expanded_terms_st:
            coeff_expr = exp.coeff(s, a).coeff(t, b)
            row.append(coeff_expr)
        M_rows.append(row)

    A = sp.Matrix(M_rows)
    ns = A.nullspace()
    print(f"Nullspace dimension (number of independent polynomials in s, t): {len(ns)}")

    if len(ns) > 0:
        basis_st = []
        for idx, vec in enumerate(ns):
            check_expr = 0
            for term_st, coeff in zip(terms_st, vec):
                if coeff != 0:
                    check_expr += coeff * term_st
            check_expr_val = sp.expand(sp.cancel(check_expr))
            basis_st.append(check_expr_val)

        # Search for F, G
        a_vars = sp.symbols(f'a_0:{len(basis_st)}')
        b_vars = sp.symbols(f'b_0:{len(basis_st)}')

        F = sum(a_vars[i] * basis_st[i] for i in range(len(basis_st)))
        G = sum(b_vars[i] * basis_st[i] for i in range(len(basis_st)))

        print("Computing Jacobian...")
        J = sp.expand(sp.cancel(F.diff(s) * G.diff(t) - F.diff(t) * G.diff(s)))
        print("Extracting Poly equations...")
        poly_J = sp.Poly(J - 1, s, t)
        eqs = poly_J.coeffs()
        print(f"Number of equations: {len(eqs)}")
        print("Solving linear/quadratic system for coefficients...")
        sol = sp.solve(eqs, list(a_vars) + list(b_vars))
        print("Solutions:", sol)

if __name__ == "__main__":
    search_keller_high(6)
    search_keller_high(8)
