import numpy as np

def roll(a: np.ndarray) -> np.ndarray:
    """Circular left shift by one."""
    output = [a[(value + 1) % len(a)] for value in range(len(a))]
    output = np.array(output)
    return output