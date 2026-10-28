import numpy as np

def repeat_rows(a: np.ndarray, d: int) -> np.ndarray:
    """Stack d copies of 1-D array a as rows."""
    matrix = [a for row in range(d)]
    
    matrix = np.array(matrix)
    return matrix

