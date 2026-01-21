import numpy as np

# Example attention scores
scores = np.array([2.0, 1.0, 0.1])

# Softmax
attention_weights = np.exp(scores) / np.sum(np.exp(scores))

print(attention_weights)
