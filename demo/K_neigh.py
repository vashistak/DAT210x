X = [[0], [1], [2], [3]]
y = [0, 0, 1, 1]
from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X, y) 

print(neigh.predict([[1.1]]))

print(neigh.predict_proba([[0.9]]))

from sklearn.neighbors import NearestNeighbors

samples = [[0., 0., 0.], [0., .5, 0.], [1., 1., .5]]

neigh1 = NearestNeighbors(n_neighbors=1)
neigh1.fit(samples) 

print(neigh1.kneighbors([[1., 1., 1.]])) 


P = [[0., 1., 0.], [1., 0., 1.]]
neigh1.kneighbors(P, return_distance=False) 
'''
Created on Feb 23, 2017

@author: vashista
'''
