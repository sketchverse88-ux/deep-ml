def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:

	new_Matrix = []
	for row in range(len(matrix)):
		result = 0
		new_row = []
		for column in range(len(matrix[0])):
			result = matrix[row][column] * scalar
			new_row.append(result)
		new_Matrix.append(new_row)

	return new_Matrix