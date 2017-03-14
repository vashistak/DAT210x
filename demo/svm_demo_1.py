'''
Created on Feb 26, 2017

@author: vashista
'''
from sklearn.svm import SVC
model=SVC(kernel='linear')
model.fit(X,y)
