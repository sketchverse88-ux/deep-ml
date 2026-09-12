def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	# Return the element-wise sum of vectors 'a' and 'b'.
	# If vectors have different lengths, return -1.
	output = []
	if len(b) != len(a):
		return -1

	else:
		for i in range(len(a)):
			result = 0
			result += a[i] + b[i]
			output.append(result)

	return output