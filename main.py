import numpy as np

from ANN import NeuralNetwork

# Example

training_inputs = np.array([
    [2,3,4,5],
    [5,3,4,3],
    [1,3,3,5],
    [3,2,2,0],
    [5,3,3,1]
])

np.random.seed(1)

ann = NeuralNetwork(training_inputs)