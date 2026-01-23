import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

st.title("🛍️ Customer Segmentation Dashboard")

# Load data
df = pd.read_csv("/Users/tayyabkhan/python/ML_algorithm/customer_segmentation/data/train.csv")
df.rename(columns={
    'Annual Income (k$)': 'Income',
    'Spending Score (1-100)': 'Spending'
}, inplace=True)

st.subheader("Dataset Preview")
st.dataframe(df.head())

# Features
X = df[['Age', 'Income', 'Spending']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Sidebar
k = st.sidebar.slider("Select number of clusters (K)", 2, 8, 5)

# PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# KMeans
kmeans = KMeans(n_clusters=k, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_pca)

st.subheader("Cluster Visualization (After PCA)")

fig, ax = plt.subplots()
sns.scatterplot(
    x=X_pca[:,0],
    y=X_pca[:,1],
    hue=df['Cluster'],
    palette='Set2',
    ax=ax
)
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
st.pyplot(fig)
