import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    if norm_type == "l1":
        result_l1 = abs(arr)
        return float(result_l1.sum())
    elif norm_type == "l2":
        sqrd = arr ** 2
        result_l2 = sqrd.sum()
        result_l2 = np.sqrt(result_l2)
        return result_l2
    elif norm_type == "linf":
        result_inf = np.abs(arr)
        result_inf = result_inf.max()
        return float(result_inf)
    elif norm_type == "frobenius":
        if arr.ndim != 2:
            raise ValueError
        else:
            frob = np.linalg.norm(arr)
            return frob
    
        
