import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR

# Data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([3, 4, 5, 6, 20])

# X for smooth curve
X_test = np.linspace(0, 6, 100).reshape(-1, 1)

# Models with different C and epsilon
models = {
    "Balanced (C=1, ε=0.5)": SVR(kernel="linear", C=1, epsilon=0.5),
    "Overfitting (C=100, ε=0.1)": SVR(kernel="linear", C=100, epsilon=0.1),
    "Underfitting (C=0.1, ε=1)": SVR(kernel="linear", C=0.1, epsilon=1)
}

plt.figure(figsize=(12, 8))

for i, (title, model) in enumerate(models.items(), 1):
    model.fit(X, y)
    y_pred = model.predict(X_test)

    plt.subplot(2, 2, i)
    plt.scatter(X, y)
    plt.plot(X_test, y_pred)
    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")

plt.tight_layout()
plt.show()
