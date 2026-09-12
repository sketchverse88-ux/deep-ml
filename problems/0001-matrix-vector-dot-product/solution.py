def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	output = []
	result = 0
	if len(a[0]) != len(b):
		return -1
	
	else:
		for i in range(len(a)):
			result = 0
			for p in range(len(b)):
				result = result + (a[i][p] * b[p])

			output.append(result)
	
	return output