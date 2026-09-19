import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):

	import numpy as np
	features = np.array(features)
	labels = np.array(labels)
	probabilities = []

	#Neuron calculations
	z = features @ weights + bias

	#Sigmoid activation
	for element in z:
		a = 1 / (1 + math.exp(-element))
		probabilities.append(a)
	
	#Loss calculation
	mse = np.sum(((labels - probabilities) ** 2) / len(labels))
	
	return probabilities, mse