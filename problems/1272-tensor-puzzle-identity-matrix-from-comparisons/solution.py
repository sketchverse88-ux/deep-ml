import numpy as np

def eye(n: int) -> np.ndarray:
    """n x n identity matrix without np.eye."""
    matrix = []
    for num in range(n):
        row = []
        for num2 in range(n):
            if num == num2:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    #matrix = np.ndarray(matrix)
    return matrix 
