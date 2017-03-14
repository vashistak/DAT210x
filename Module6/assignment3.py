#
# This code is intentionally missing!
# Read the directions on the course lab page!
#
import pandas as pd
import numpy as np

X=pd.read_csv(r'D:\python\udacity\Module6\Datasets\parkinsons.data')

X=X.drop('name',axis=1)
print(X)

y=X.status

print(y)
print(y.shape)

X=X.drop('status',axis=1)
from sklearn import preprocessing

#T = preprocessing.StandardScaler().fit_transform(X)
#T = preprocessing.MinMaxScaler().fit_transform(X)
#T = preprocessing.Normalizer().fit_transform(X)
T = preprocessing.scale(X)
from sklearn.decomposition import PCA
pca = PCA(n_components = 14)
X_pca = pca.fit_transform(T)
from sklearn.manifold import Isomap

# You're going to have to write nested for loops that wrap around everything from here on down!
best_score = 0
for k in range(2, 6):
    for l in range(4, 7):
        iso = Isomap(n_neighbors = k, n_components = l)
        X_iso = iso.fit_transform(T)

        # Perform a train/test split. 30% test group size, with a random_state equal to 7.
        from sklearn.cross_validation import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X_iso, y, test_size = 0.3, random_state = 7)

        # Create a SVC classifier. Don't specify any parameters, just leave everything as default.
        # Fit it against your training data and then score your testing data.
        from sklearn.svm import SVC
        # Lines below are for the first lab question:
        
        '''model = SVC()
        model.fit(X_train, y_train)
        score = model.score(X_test, y_test)
        print (score)'''
        

        # Program a naive, best-parameter searcher by creating a nested for-loops. The outer for-loop should iterate a variable C
        # from 0.05 to 2, using 0.05 unit increments. The inner for-loop should increment a variable gamma from 0.001 to 0.1, using
        # 0.001 unit increments. As you know, Python ranges won't allow for float intervals, so you'll have to do some research on
        # NumPy ARanges, if you don't already know how to use them.

        # Since the goal is to find the parameters that result in the model having the best score, you'll need a best_score = 0 variable
        # that you initialize outside of the for-loops. Inside the for-loop, create a model and pass in the C and gamma parameters into
        # the class constructor. Train and score the model appropriately. If the current best_score is less than the model's score, then
        # update the best_score, being sure to print it out, along with the C and gamma values that resulted in it.        
        for i in np.arange(start = 0.05, stop = 2.05, step = 0.05):
            for j in np.arange(start = 0.001, stop = 0.101, step = 0.001):
                model = SVC(C = i, gamma = j)
                model.fit(X_train, y_train)
                score = model.score(X_test, y_test)
                if score > best_score:
                    best_score = score
                    best_C = model.C
                    best_gamma = model.gamma
                    best_n_neighbors = iso.n_neighbors
                    best_n_components = iso.n_components
print( "The highest score obtained:", best_score)
print( "C value:", best_C )
print ("gamma value:", best_gamma)
print ("isomap n_neighbors:", best_n_neighbors)
print( "isomap n_components:", best_n_components)



