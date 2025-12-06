from sklearn.datasets import load_iris
import pandas as pd

# Load dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

print("Shape of X:", X.shape)
print("\nFirst 5 rows:\n", X.head())
print("\nUnique target values:", set(y))

