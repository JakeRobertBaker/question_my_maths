from sympy import Matrix, symbols


def symbolic_matrix_power(n: int, m: int) -> str:
    X = Matrix(symbols(f"x:{n}:{n}")).reshape(n, n)
    return str(X**m)
