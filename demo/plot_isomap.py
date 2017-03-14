'''
Created on Feb 20, 2017

@author: vashista
'''
from sklearn import manifold
iso=manifold.isomap(n_neighbors=4,n_components=2)
iso.fit(df)
