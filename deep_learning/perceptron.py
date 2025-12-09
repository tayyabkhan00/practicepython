import math

# Activation function (sigmoid)
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Inputs
x = 2

# Weight and bias
w = 0.5
b = 1

# Forward pass
z = w * x + b
output = sigmoid(z)

print("Z value:", z)
print("Output:", output)
