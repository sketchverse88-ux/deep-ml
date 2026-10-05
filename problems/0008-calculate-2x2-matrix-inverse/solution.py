def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    #Calculate determinant
    det = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

    A_inv = []
    row_one = []
    row_two = []

    if det == 0:
        return None
    else:
        row_one.append(1/det * matrix[1][1])
        row_one.append(1/det * -matrix[0][1])
        row_two.append(1/det * -matrix[1][0])
        row_two.append(1/det * matrix[0][0])

        A_inv.append(row_one)
        A_inv.append(row_two)

        return A_inv