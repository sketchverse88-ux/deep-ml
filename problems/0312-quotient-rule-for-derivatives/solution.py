import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    #Creates polynomials
    g = np.poly1d(g_coeffs)
    h = np.poly1d(h_coeffs)

    #Gets the derivatives
    g_d = g.deriv()
    h_d = h.deriv()
    
    #Derivative of f(x) = f'(x) 
    f_x = (h(x) * g_d(x)) - (g(x) * h_d(x))
    fx =  h(x) ** 2
    
    return f_x / fx
