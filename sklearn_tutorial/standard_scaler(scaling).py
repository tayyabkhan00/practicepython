from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
X = iris.data

scaler = StandardScaler()
scaled = scaler.fit_transform(X)

print("Before scaling:\n", pd.DataFrame(X).head())
print("\nAfter scaling:\n", pd.DataFrame(scaled).head())
