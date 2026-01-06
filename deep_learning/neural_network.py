import math
import random

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# 784 inputs (flattened image)
inputs = [random.random() for _ in range(784)]

hidden_outputs = []

for neuron in range(100):   # 100 neurons
    weights = [random.random() for _ in range(784)]
    bias = random.random()

    z = 0
    for i in range(784):
        z += inputs[i] * weights[i]

    z += bias
    output = sigmoid(z)

    hidden_outputs.append(output)

weights = [random.random() for _ in range(100)]
bias = random.random()

z = 0
for i in range(100):
    z += hidden_outputs[i] * weights[i]

z += bias
final_output = sigmoid(z)

print("Final Output:", final_output)

