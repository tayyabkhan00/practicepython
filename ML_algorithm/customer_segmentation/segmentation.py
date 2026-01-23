import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA


# Load dataset
df = pd.read_csv("/Users/tayyabkhan/python/customer_segmentation/data/train.csv")

# Rename columns for ease
df.rename(columns={
    'Annual Income (k$)': 'Income',
    'Spending Score (1-100)': 'Spending'
}, inplace=True)

df.head()

# Advanced EDA (Seaborn Visualizations)
sns.histplot(df['Income'], kde=True)
plt.title("Income Distribution")
plt.show()

sns.histplot(df['Spending'], kde=True)
plt.title("Spending Score Distribution")
plt.show()


# Pairplot
sns.pairplot(
    df[['Age', 'Income', 'Spending']],
    diag_kind='kde'
)
plt.show()

# Gender vs Spending
sns.boxplot(x='Gender', y='Spending', data=df)
plt.title("Gender vs Spending")
plt.show()

# Feature Scaling
X = df[['Age', 'Income', 'Spending']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


inertia = []

for k in range(1, 11):
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(X_scaled)
    inertia.append(km.inertia_)

plt.plot(range(1,11), inertia, marker='o')
plt.xlabel("K")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.show()


kmeans = KMeans(n_clusters=5, random_state=42)
df['Cluster_Before_PCA'] = kmeans.fit_predict(X_scaled)


sns.scatterplot(
    x='Income',
    y='Spending',
    hue='Cluster_Before_PCA',
    data=df,
    palette='Set1'
)
plt.title("Clusters BEFORE PCA")
plt.show()


pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print("Explained Variance:", pca.explained_variance_ratio_)


kmeans_pca = KMeans(n_clusters=5, random_state=42)
df['Cluster_After_PCA'] = kmeans_pca.fit_predict(X_pca)


plt.figure(figsize=(8,6))
sns.scatterplot(
    x=X_pca[:,0],
    y=X_pca[:,1],
    hue=df['Cluster_After_PCA'],
    palette='Set2'
)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("Clusters AFTER PCA")
plt.show()
