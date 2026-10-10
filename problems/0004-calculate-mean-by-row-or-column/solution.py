def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	if mode == 'column':
		for column in range(len(matrix[0])):
			value = 0
			for row in range(len(matrix)):
				value += matrix[row][column]
			value /= len(matrix)
			means.append(value)

	if mode == 'row':
		for row in range(len(matrix)):
			value = 0
			for column in range(len(matrix[row])):
				value += matrix[row][column]
			value /= len(matrix[row])
			means.append(value)


	return means
