import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load and preprocess data
file_path = 'dataset/normalised_data.csv'
data_fillmean = pd.read_csv(file_path)

# Assuming outlier removal and normalization are completed
# Let's consider these features: 'sqft_living', 'bathrooms', 'bedrooms', 'floors'
features_to_cluster = ['sqft_living', 'bathrooms', 'bedrooms', 'floors']

# Normalize these features
scaler = MinMaxScaler()
data_fillmean[features_to_cluster] = scaler.fit_transform(data_fillmean[features_to_cluster])

# Determine the optimal number of clusters
sse = []
list_k = list(range(1, 10))
for k in list_k:
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(data_fillmean[features_to_cluster])
    sse.append(km.inertia_)

# Plot SSE for each k
plt.figure(figsize=(8, 4))
plt.plot(list_k, sse, '-o')
plt.xlabel('Number of clusters *k*')
plt.ylabel('Sum of squared distance')
plt.title('Elbow Method For Optimal k')
plt.show()

# Assuming the elbow is observed at k=3 (adjust based on your plot)
kmeans = KMeans(n_clusters=3, random_state=42)
data_fillmean['Cluster'] = kmeans.fit_predict(data_fillmean[features_to_cluster])

# Now let's see the centroids and cluster assignments
print(data_fillmean['Cluster'].value_counts())
print(kmeans.cluster_centers_)