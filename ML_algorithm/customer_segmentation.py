import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Sample customer data
data = {
    'Age': [19,21,20,23,31,22,35,23,64,30],
    'Annual Income': [15,15,16,16,17,17,18,18,19,19],
    'Spending Score': [39,81,6,77,40,76,6,94,3,72]
}

df = pd.DataFrame(data)
print(df.head())

# Standardizing the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# Using the Elbow Method to find the optimal number of clusters
inertia = []

for k in range(1, 8):
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(scaled_data)
    inertia.append(km.inertia_)

plt.plot(range(1,8), inertia)
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.show()

kmeans = KMeans(n_clusters=3, random_state=42)
clusters_before = kmeans.fit_predict(scaled_data)


plt.scatter(
    scaled_data[:, 1], 
    scaled_data[:, 2], 
    c=clusters_before
)
plt.xlabel("Annual Income (scaled)")
plt.ylabel("Spending Score (scaled)")
plt.title("Customer Segmentation BEFORE PCA")
plt.show()


pca = PCA(n_components=2)
pca_data = pca.fit_transform(scaled_data)

print("Explained Variance:", pca.explained_variance_ratio_)


kmeans_pca = KMeans(n_clusters=3, random_state=42)
clusters_after = kmeans_pca.fit_predict(pca_data)


plt.scatter(
    pca_data[:, 0], 
    pca_data[:, 1], 
    c=clusters_after
)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("Customer Segmentation AFTER PCA")
plt.show()


