import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	#if v1.shape != v2.shape:
		#return 0
	
	#Dot product of the vectors
	ans = 0
	for i in range(len(v1)):
		ans = v1 * v2

	#Euclidian norm
	out = np.sqrt(sum(v1 ** 2)) * np.sqrt(sum(v2 ** 2))

	#Cosine similarity
	output = sum(ans)/out

	return output
