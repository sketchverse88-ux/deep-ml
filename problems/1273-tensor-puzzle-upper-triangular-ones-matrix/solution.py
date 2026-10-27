import numpy as np

def triu_ones(n: int) -> np.ndarray:
    """n x n upper-triangular matrix of ones (including diagonal)."""
    i = n
    j = n
    matrix = []
    for row in range(i):
        hor = []
        for column in range(j):
            if row <= column:
                hor.append(1.0)
            else:
                hor.append(0.0)
    
        matrix.append(hor)

    matrix = np.array(matrix)
    return matrix