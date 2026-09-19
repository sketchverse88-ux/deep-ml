import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	gradient = np.array(gradient)
	
	 
	magnitude = np.sqrt(np.sum(gradient ** 2))

	if magnitude != 0.0:
		direction = gradient / magnitude
		descent_direction = direction * -1.0

	else:
		direction = np.zeros_like(gradient)
		descent_direction = 0.0

	keys = ["magnitude", "direction", "descent_direction"]
	values = [magnitude, direction, descent_direction]
	result = dict(zip(keys, values))

	return result