def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	import numpy
	matrix = numpy.array(matrix)
	output = matrix * scalar
	return output