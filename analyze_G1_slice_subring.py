import sympy as sp

def analyze_G1_slice_subring(c_val):
    print(f"================================================================================")
    print(f"   Analyzing the G1 = {c_val} Slice Subring                                     ")
    print(f"================================================================================")
    s, t = sp.symbols('s t')
    a = s
    y = s**3 * t

    # G1 = c_val. We substitute a = s, y = s**3 * t into the restricted G2, G3:
    # G2 = -3*c*y**2 + 2*y - 6*c*y/a + 3/a - 3*c/a**2
    # G3 = -2*c*y**3 + y**2 - 6*c*y**2/a + 3*y/a - 6*c*y/a**2 + 2/a**2 - 2*c/a**3
    c = c_val
    G2 = -3*c*y**2 + 2*y - 6*c*y/a + 3/a - 3*c/a**2
    G3 = -2*c*y**3 + y**2 - 6*c*y**2/a + 3*y/a - 6*c*y/a**2 + 2/a**2 - 2*c/a**3

    G2 = sp.expand(G2)
    G3 = sp.expand(G3)

    print(f"G2(s, t) for c = {c_val}:")
    sp.pprint(G2)
    print(f"\nG3(s, t) for c = {c_val}:")
    sp.pprint(G3)

    # We want to find polynomial combinations of G2, G3 up to some degree that have no poles (i.e. no negative powers of s).
    max_deg = 4
    terms_G23 = []
    terms_st = []
    for d in range(1, max_deg + 1):
        for i in range(d + 1):
            j = d - i
            terms_G23.append(sp.Symbol('G2')**i * sp.Symbol('G3')**j)
            terms_st.append(sp.simplify(G2**i * G3**j))

    # Find all negative-power monomials of s
    all_neg_monomials = set()
    expanded_terms_st = []
    for expr in terms_st:
        exp = sp.expand(expr)
        expanded_terms_st.append(exp)
        coeff_dict = exp.as_coefficients_dict()
        for mono in coeff_dict.keys():
            pow_dict = mono.as_powers_dict()
            a_pow = pow_dict.get(s, 0)
            b_pow = pow_dict.get(t, 0)
            if a_pow < 0:
                all_neg_monomials.add((a_pow, b_pow))

    all_neg_monomials = sorted(list(all_neg_monomials))
    print(f"\nNumber of negative-power-of-s monomials: {len(all_neg_monomials)}")

    # Construct the coefficient matrix
    M_rows = []
    for a_pow, b_pow in all_neg_monomials:
        row = []
        for exp in expanded_terms_st:
            coeff_dict = exp.as_coefficients_dict()
            val = 0
            for mono, coeff in coeff_dict.items():
                pow_dict = mono.as_powers_dict()
                if pow_dict.get(s, 0) == a_pow and pow_dict.get(t, 0) == b_pow:
                    val = coeff
                    break
            row.append(val)
        M_rows.append(row)

    A = sp.Matrix(M_rows)
    ns = A.nullspace()
    print(f"Nullspace dimension (independent regular polynomials in s, t): {len(ns)}")

    if len(ns) > 0:
        basis_G23 = []
        basis_st = []
        for idx, vec in enumerate(ns):
            poly_expr = 0
            check_expr = 0
            for term_G23, term_st, coeff in zip(terms_G23, terms_st, vec):
                if coeff != 0:
                    poly_expr += coeff * term_G23
                    check_expr += coeff * term_st
            basis_G23.append(poly_expr)
            basis_st.append(sp.simplify(check_expr))
            print(f"Basis {idx}: {poly_expr}")
            print(f"  expanded in s, t: {sp.simplify(check_expr)}")

        # Search for Keller Pairs
        print("\nSearching for Keller pairs F, G in the subring...")
        a_vars = sp.symbols(f'a_0:{len(basis_st)}')
        b_vars = sp.symbols(f'b_0:{len(basis_st)}')
        F = sum(a_vars[i] * basis_st[i] for i in range(len(basis_st)))
        G = sum(b_vars[i] * basis_st[i] for i in range(len(basis_st)))

        J = sp.simplify(F.diff(s) * G.diff(t) - F.diff(t) * G.diff(s))
        poly_J = sp.Poly(J - 1, s, t)
        eqs = poly_J.coeffs()
        print(f"Number of equations to solve: {len(eqs)}")
        sol = sp.solve(eqs, list(a_vars) + list(b_vars))
        print("Solutions:", sol)

if __name__ == "__main__":
    analyze_G1_slice_subring(0)
    analyze_G1_slice_subring(1)
