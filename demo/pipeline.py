'''
Created on Mar 10, 2017

@author: vashista
'''
from sklearn.pipeline import Pipeline
from sklearn.decomposition import RandomizedPCA
from sklearn.svm import SVC
from sklearn import svm
from sklearn import datasets

iris = datasets.load_iris()

svc = svm.SVC(kernel='linear')
pca = RandomizedPCA()

pipeline = Pipeline([
  ('pca', pca),
  ('svc', svc)])
pipeline.set_params(pca__n_components=5, svc__C=1, svc__gamma=0.0001)
pipeline.fit(iris.data, iris.target)
