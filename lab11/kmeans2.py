import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load CSV
df = pd.read_csv('Mall_Customers.csv')
print(df.head())
print(df.columns)

x = df[['Annual Income (k$)', 'Spending Score (1-100)']].values

# Scale
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# Elbow Method
wcss = []
for i in range(1, 11):
    km = KMeans(n_clusters=i, init='k-means++', random_state=42)
    km.fit(x_scaled)
    wcss.append(km.inertia_)

plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method')
plt.xlabel('K')
plt.ylabel('WCSS')
plt.show()

# From elbow - say optimal K = 5
kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
y_pred = kmeans.fit_predict(x_scaled)

# Add cluster column back to dataframe (useful to see results)
df['Cluster'] = y_pred
print(df.head())

# Plot
centers = scaler.inverse_transform(kmeans.cluster_centers_)

plt.scatter(x[y_pred == 0, 0], x[y_pred == 0, 1], s=100, c='blue',   label='Cluster 1')
plt.scatter(x[y_pred == 1, 0], x[y_pred == 1, 1], s=100, c='green',  label='Cluster 2')
plt.scatter(x[y_pred == 2, 0], x[y_pred == 2, 1], s=100, c='red',    label='Cluster 3')
plt.scatter(x[y_pred == 3, 0], x[y_pred == 3, 1], s=100, c='black',  label='Cluster 4')
plt.scatter(x[y_pred == 4, 0], x[y_pred == 4, 1], s=100, c='purple', label='Cluster 5')
plt.scatter(centers[:, 0], centers[:, 1], s=300, c='yellow', edgecolors='black', label='Centroids')

plt.title('Customer Segments')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()
