def poly_term_derivative(c: float, x: float, n: float) -> float:

    ce = n * c
    new_n = n - 1

    derivative = ce * x ** new_n

    return derivative
    