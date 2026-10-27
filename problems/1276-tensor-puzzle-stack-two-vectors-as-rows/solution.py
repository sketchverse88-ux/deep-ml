import numpy as np

def vstack(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Stack 1-D arrays a and b as rows of a (2, n) matrix."""
    matrix = []
    matrix.append(a)
    matrix.append(b)
    matrix = np.array(matrix)
    return matrix