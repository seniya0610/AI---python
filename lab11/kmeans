import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Generate random data - 150 points, 3 natural groups
np.random.seed(42)
group1 = np.random.randn(50, 2) + [1, 1]
group2 = np.random.randn(50, 2) + [6, 6]
group3 = np.random.randn(50, 2) + [1, 8]
x = np.vstack([group1, group2, group3])

# Scale
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# Elbow Method
wcss = []
for i in range(1, 11):
    km = KMeans(n_clusters=i, init='k-means++', random_state=42)
    km.fit(x_scaled)
    wcss.append(km.inertia_)

plt.figure(figsize=(8, 4))
plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method - Find Optimal K')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('WCSS')
plt.grid(True)
plt.show()

k = KMeans(n_clusters=3, init='k-means++', random_state=42)
y_pred = k.fit_predict(x_scaled)

plt.figure(figsize=(8, 6))
plt.scatter(x[y_pred == 0,0], x[y_pred == 0,1], s=100, c='blue', label='Cluster 1')
plt.scatter(x[y_pred == 1,0], x[y_pred == 1,1], s=100, c='red', label='Cluster 2')
plt.scatter(x[y_pred== 2,0], x[y_pred == 2,1], s=100, c='green', label='Cluster 3')

centers = scaler.inverse_transform(k.cluster_centers_)
plt.scatter(centers[:,0], centers[:,1], s=100, c='yellow', edgecolors='black', label='Centroids')
plt.title('K-Means Clustering')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
