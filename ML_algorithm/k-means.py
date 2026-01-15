from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np

# Sample data
X = np.array([[1,2], [1,4], [1,0],
              [10,2], [10,4], [10,0]])

# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# KMeans
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X_scaled)

print("Cluster labels:", kmeans.labels_)
print("Centroids:", kmeans.cluster_centers_)
print("Inertia:", kmeans.inertia_)
print("Scaled Data:\n", X_scaled)
print("Original Data:\n", X)
