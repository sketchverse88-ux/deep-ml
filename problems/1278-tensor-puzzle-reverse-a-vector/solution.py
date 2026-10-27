import numpy as np

def flip(a: np.ndarray) -> np.ndarray:
    """Reverse 1-D array a without slicing a[::-1]."""
    reversed = [a[len(a) - 1 - index] for index in range(len(a))]
    reversed = np.array(reversed)
    return reversed