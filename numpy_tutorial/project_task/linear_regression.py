import numpy as np

X = np.array([1,2,3,4,5])
y = np.array([3,4,2,5,6])

mean_x = np.mean(X)
mean_y = np.mean(y)

# compute slope (m) and intercept (c)
# m = Σ[(X - meanX)*(y - meanY)] / Σ[(X - meanX)^2]

num = np.sum((X - mean_x) * (y - mean_y))
den = np.sum((X - mean_x)**2)

m = num / den
print("Slope m:", m)

c = mean_y - m * mean_x
print("Intercept c:", c)

y_pred = m*X + c
print("Predicted y:", y_pred)

mse = np.mean((y - y_pred)**2)
print("MSE:", mse)
