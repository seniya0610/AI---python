import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# ── 1. LOAD ──────────────────────────────
df = pd.read_csv('fitness_data.csv')
print(df.head())

# ── 2. CLEAN ─────────────────────────────
df.fillna(df.mean(numeric_only=True), inplace=True)  # fill missing with mean
df.drop_duplicates(inplace=True)                      # remove duplicate rows
print("\nMissing values:", df.isnull().sum().sum())    # should print 0

# ── 3. PICK FEATURES ─────────────────────
features = ['Steps', 'Workout_Duration', 'Calories_Burned', 'Heart_Rate', 'Sleep_Hours']
x = df[features].values

# ── 4. SCALE ─────────────────────────────
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# ── 5. ELBOW METHOD ──────────────────────
wcss = []
for i in range(1, 8):
    km = KMeans(n_clusters=i, init='k-means++', random_state=42)
    km.fit(x_scaled)
    wcss.append(km.inertia_)

plt.plot(range(1, 8), wcss, marker='o')
plt.title('Elbow Method')
plt.xlabel('K')
plt.ylabel('WCSS')
plt.show()

# ── 6. TRAIN K=3 ─────────────────────────
kmeans = KMeans(n_clusters=3, init='k-means++', random_state=42)
y_pred = kmeans.fit_predict(x_scaled)
df['Cluster'] = y_pred

# ── 7. PLOT CLUSTERS ─────────────────────
plt.figure(figsize=(8, 6))
plt.scatter(df[df['Cluster']==0]['Steps'], df[df['Cluster']==0]['Calories_Burned'], c='blue',   s=100, label='Cluster 0')
plt.scatter(df[df['Cluster']==1]['Steps'], df[df['Cluster']==1]['Calories_Burned'], c='green',  s=100, label='Cluster 1')
plt.scatter(df[df['Cluster']==2]['Steps'], df[df['Cluster']==2]['Calories_Burned'], c='red',    s=100, label='Cluster 2')

centers = scaler.inverse_transform(kmeans.cluster_centers_)
plt.scatter(centers[:, 0], centers[:, 1], s=100, c='yellow', edgecolors='black', label='Centroids')

plt.title('User Clusters')
plt.xlabel('Steps')
plt.ylabel('Calories Burned')
plt.legend()
plt.show()

# ── 8. PRINT CLUSTER CENTERS ─────────────
centers_df = pd.DataFrame(centers, columns=features)
print("\nCluster Centers:")
print(centers_df.round(2))
