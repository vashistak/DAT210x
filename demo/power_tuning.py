'''
Created on Mar 10, 2017

@author: vashista
'''
from sklearn import svm, grid_search, datasets
import scipy.stats

iris = datasets.load_iris()
parameters = {'kernel':('linear', 'rbf'), 'C':[1, 5, 10]}
model = svm.SVC()
classifier = grid_search.GridSearchCV(model, parameters)
print(classifier.fit(iris.data, iris.target))
parameter_dist = {
  'C': scipy.stats.expon(scale=100),
  'kernel': ['linear'],
  'gamma': scipy.stats.expon(scale=.1),
}

classifier = grid_search.RandomizedSearchCV(model, parameter_dist)
classifier.fit(iris.data, iris.target)