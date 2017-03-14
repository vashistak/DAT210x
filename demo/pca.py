import numpy as np
from sklearn.decomposition import IncrementalPCA
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
pca = IncrementalPCA(n_components=1, batch_size=3)
print(pca.fit(X))


#print(pca.explained_variance_ratio_)  

pca.transform(X)
