import numpy as np

def diag(A: np.ndarray) -> np.ndarray:
    """Return the main diagonal of square matrix A."""
    diagonals = []
    for row in range(len(A)):
        diagonals.append(int(A[row][row]))

    return diagonals