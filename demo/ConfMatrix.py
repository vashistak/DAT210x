'''
Created on Mar 9, 2017

@author: vashista
'''
import sklearn.metrics as metrics
import matplotlib.pyplot as plt
y_true=[1,1,2,2,3,3]
y_pred=[1,1,1,3,2,3]
confusion = metrics.confusion_matrix(y_true, y_pred)

#You already know how to calculate the accuracy_score,
# which is the same value you get from using model.score() on your predictor:
print(metrics.accuracy_score(y_true, y_pred))
print(metrics.accuracy_score(y_true, y_pred, normalize=False))

#To calculate the recall score, or the ratio of true_positives / (true_positives + false_negatives):

print(metrics.recall_score(y_true, y_pred, average='weighted'))
print(metrics.precision_score(y_true, y_pred, average=None))

#The F1 Score is a weighted average of the precision and recall. 
#Defined as 2 * (precision * recall) / (precision + recall), the 
#best possible result is 1 and the worst possible score is 0:
metrics.f1_score(y_true, y_pred, average='weighted')
metrics.f1_score(y_true, y_pred, average=None)

#As a convenience, SciKit-Learn also has a built-in method for producing 
#a full report of the above scores for you simultaneously, on a per label basis:

target_names = ['Fruit 1', 'Fruit 2', 'Fruit 3']
print(metrics.classification_report(y_true, y_pred, target_names=target_names))


#confusion matrix
print(metrics.confusion_matrix(y_true,y_pred))

#from sklearn import cross_validation as cval
#cval.cross_val_score(model, X_train, y_train, cv=10)
#array([ 0.93513514,  0.99453552,  0.97237569,  0.98888889,  0.96089385,
#        0.98882682,  0.99441341,  0.98876404,  0.97175141,  0.96590909])
#
#cval.cross_val_score(model, X_train, y_train, cv=10).mean()
#0.97614938602520218

columns = ['Cat', 'Dog', 'Monkey']
plt.imshow(confusion, cmap=plt.cm.Blues, interpolation='nearest')
plt.xticks([0,1,2], columns, rotation='vertical')
plt.yticks([0,1,2], columns)
plt.colorbar()
plt.show()