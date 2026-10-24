import numpy as np

def ones(n: int) -> np.ndarray:
    """Return a length-n float vector of ones without calling np.ones."""
    value = 1.0
    output = [value for i in np.arange(1, n + 1, 1)]
    return output
