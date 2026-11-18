import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    if norm_type == "l1":
        values = [abs(value) for value in arr]
        l1 = np.sum(values)
        return l1

    if norm_type == "l2":
        values = [value ** 2 for value in arr]
        l2 = np.sqrt(np.sum(values))
        return l2

    if norm_type == "linf":
        values = [abs(value) for value in arr]
        linf = np.max(values)
        return linf

    if norm_type == "frobenius" and arr.ndim == 2:
        value = 0
        for row in range(len(arr)):
            for i in range(len(arr[row])):
                value += arr[row][i] ** 2

        return np.sqrt(value)
    else:
        raise ValueError

    raise ValueError
