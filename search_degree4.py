import sympy as sp
import random
import sys

def setup_system():
    x, y = sp.symbols('x y')
    basis = [
        x*y,          # 1
        y**2,         # 2
        x**2*y,       # 3
        x*y**2,       # 4
        y**3,         # 5
        x**3*y,       # 6
        x**2*y**2,     # 7
        x*y**3,       # 8
        y**4,         # 9
        x**3 - x**2,  # 10
        x**4 - x**2   # 11
    ]

    a = sp.symbols('a1:12')
    b = sp.symbols('b1:12')

    F0 = x - x**2
    G0 = y

    F = F0 + sum(ai * basis_elem for ai, basis_elem in zip(a, basis))
    G = G0 + sum(bi * basis_elem for bi, basis_elem in zip(b, basis))

    Fx = sp.diff(F, x)
    Fy = sp.diff(F, y)
    Gx = sp.diff(G, x)
    Gy = sp.diff(G, y)

    Jac = Fx * Gy - Fy * Gx
    expr = sp.expand(Jac - 1)

    poly = sp.Poly(expr, x, y)
    coeff_dict = poly.as_dict()
    eqs = [sp.expand(eq) for eq in coeff_dict.values() if eq != 0]

    return a, b, eqs

def search_modular(a_syms, b_syms, eqs, p=5, max_trials=10000):
    """
    Search for a solution modulo p.
    We can solve the system by linear/quadratic reduction.
    Let's analyze the equations first.
    We have 22 variables: a1..a11, b1..b11.
    Some equations are simple. Let's find simple linear relations or substitutions.
    """
    # Let's map equations to SymPy Poly or expressions modulo p
    # To find any solution, we can randomly assign some variables and solve for the rest,
    # or perform a backtrack/DFS on the variables.
    # Since we want to find any modular solution, let's write a simple backtracking solver.
    print(f"Starting modular search modulo {p}...")

    # We can simplify the system by finding a Gröbner basis modulo p,
    # or by substituting known linear relationships first.
    # From Run 4:
    # Eq 1: a1 + 2*b2 = 0 => a1 = -2*b2 mod p
    # Eq 7: -2*a10 - 2*a11 + b1 - 2 = 0 => b1 = 2*a10 + 2*a11 + 2 mod p
    # Let's write a simple solver that propagates these linear equations.

    # We can do a random search first as a quick check:
    all_syms = list(a_syms) + list(b_syms)
    # Let's evaluate equations for a random assignment
    for trial in range(max_trials):
        assignment = {sym: random.randint(0, p-1) for sym in all_syms}
        # Check if all equations are 0 mod p
        success = True
        for eq in eqs:
            val = eq.subs(assignment)
            if val % p != 0:
                success = False
                break
        if success:
            print(f"FOUND MODULAR SOLUTION modulo {p} on trial {trial}:")
            print(assignment)
            return assignment

    print(f"No modular solution found modulo {p} after {max_trials} trials.")
    return None

if __name__ == "__main__":
    a_syms, b_syms, eqs = setup_system()
    print(f"Loaded {len(eqs)} equations.")

    # Run modular searches
    search_modular(a_syms, b_syms, eqs, p=5, max_trials=50000)
    search_modular(a_syms, b_syms, eqs, p=7, max_trials=50000)
