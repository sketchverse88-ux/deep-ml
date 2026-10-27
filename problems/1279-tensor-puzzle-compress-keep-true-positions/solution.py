import numpy as np

def compress(g: np.ndarray, v: np.ndarray) -> np.ndarray:
    """Pack v[g] into the front of a zero vector of length len(v)."""
    output = []
    for boolean in range(len(g)):
        if g[boolean]:
            output.append(v[boolean])
    for length in range(len(v)):
        if len(output) != len(v):
            output.append(0.0)

    output = np.array(output)
    return output