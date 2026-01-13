import numpy as np
import matplotlib.pyplot as plt

# Input range for single-value activations
x = np.linspace(-10, 10, 1000)

# Activation functions
sigmoid = 1 / (1 + np.exp(-x))
relu = np.maximum(0, x)
tanh = np.tanh(x)

print(relu)
print(tanh)
print(sigmoid)

# Softmax works on a vector, not a single x
vec = np.array([1.0, 2.0, 3.0, 4.0])
softmax = np.exp(vec) / np.sum(np.exp(vec))

# Plot normal activations
plt.figure(figsize=(10, 6))
plt.plot(x, sigmoid, label="Sigmoid")
plt.plot(x, relu, label="ReLU")
plt.plot(x, tanh, label="Tanh")
plt.title("Activation Functions")
plt.legend()
plt.grid(True)
plt.show()
'''
# Plot softmax separately
plt.figure(figsize=(6, 4))
plt.bar(range(len(vec)), softmax)
plt.title("Softmax Output (Probability Distribution)")
plt.xticks(range(len(vec)), vec)
plt.ylabel("Probability")
plt.grid(True, axis='y')
plt.show()
'''