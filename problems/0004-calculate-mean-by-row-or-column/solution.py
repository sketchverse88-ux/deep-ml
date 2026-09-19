def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	result = []
	if mode == "row":
		denominator = len(matrix[0])
		for i in range(len(matrix)):
			sums = 0
			for r in range(len(matrix[0])):
				sums += matrix[i][r]
			result.append(sums / denominator)

	elif mode == "column":
		denominator = len(matrix)
		for c in range(len(matrix[0])):
			sums = 0
			for i in range(len(matrix)):
				sums += matrix[i][c]
			result.append(sums / denominator)



	return result