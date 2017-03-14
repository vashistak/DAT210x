import numpy as np
from sklearn import svm
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
y = np.array([1, 1, 2, 2])
from sklearn.svm import SVC
clf = svm.SVC(decision_function_shape='ovo')
clf.fit(X,y) 

print(clf.predict([[-0.8, -1]]))

# get support vectors
print(clf.support_vectors_)


# get indices of support vectors
print(clf.support_ )

# get number of support vectors for each class
print(clf.n_support_ )


clf.decision_function_shape = "ovr"
dec = clf.decision_function([[1]])
print(dec.shape[1] )
