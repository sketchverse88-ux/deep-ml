import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	
	import numpy as np

	features = np.array(features)
	weights = np.array(weights)
	bias = np.array(bias)
	labels = np.array(labels)

	forward = features @ weights + bias
	probabilities = []
	for i in range(len(forward)):
		probability =round((1 / (1 + math.exp(-forward[i]))), 4)
		probabilities.append(probability)

	mse = np.sum(((labels - probabilities) **2) / len(labels))

	return probabilities, round(mse, 4)