import pandas as pd
from datetime import timedelta
import matplotlib.pyplot as plt
import matplotlib

plt.style.use('ggplot') # Look Pretty

#
# INFO: This dataset has call records for 10 users tracked over the course of 3 years.
# Your job is to find out where the users likely live at!
df=pd.read_csv(r'Datasets/CDR.csv')
#print(df)
#exit()
def showandtell(title=None):
  if title != None: plt.savefig(title + ".png", bbox_inches='tight', dpi=300)
  plt.show()
  # exit()

def clusterInfo(model):
  print("Cluster Analysis Inertia: ", model.inertia_)
  print ('------------------------------------------')
  for i in range(len(model.cluster_centers_)):
    print( "\n  Cluster ", i)
    print ("    Centroid ", model.cluster_centers_[i])
    print( "    #Samples ", (model.labels_==i).sum()) # NumPy Power

# Find the cluster with the least # attached nodes
def clusterWithFewestSamples(model):
  # Ensure there's at least on cluster...
  minSamples = len(model.labels_)
  minCluster = 0
  for i in range(len(model.cluster_centers_)):
    if minSamples > (model.labels_==i).sum():
      minCluster = i
      minSamples = (model.labels_==i).sum()
  print ("\n  Cluster With Fewest Samples: ", minCluster)
  return (model.labels_==minCluster)


def doKMeans(data, clusters):
  #
  # TODO: Be sure to only feed in Lat and Lon coordinates to the KMeans algo, since none of the other
  # data is suitable for your purposes. Since both Lat and Lon are (approximately) on the same scale,
  # no feature scaling is required. Print out the centroid locations and add them onto your scatter
  # plot. Use a distinguishable marker and color.
  #
  # Hint: Make sure you fit ONLY the coordinates, and in the CORRECT order (lat first). This is part
  # of your domain expertise. Also, *YOU* need to instantiate (and return) the variable named `model`
  # here, which will be a SKLearn K-Means model for this to work.
  #
  # .. your code here ..
  from sklearn.cluster import KMeans 
  model=KMeans(n_clusters=clusters).fit(data)  
  centroids = model.cluster_centers_
  print(centroids)
  print([centroids[:,0].mean(),centroids[:,1].mean()])
  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.scatter(centroids[:,0], centroids[:,1], marker='x', c='red', alpha=0.5, linewidths=3, s=169)
  ax.set_title('plot for:')
 
 
  return model

num=df.In.unique()
 
import numpy as np
X=df['In']
users=np.array(X)
#print(users)
print(len(users))
Y=np.array(df['DOW'])
#print(Y)

import datetime as dt

df['CallTime'] = df['CallTime'].apply(lambda x:  dt.datetime.strptime(x,'%H:%M:%S.%f').strftime('%H:%M:%S'))
Z=np.array(df['CallTime'])
print(Z)
for i in range(len(num)):
    user1=[]
    user2=[]
    print(i)
    user1=df[users==num[i]]
    #print(len(user1))
    
    user1.plot.scatter(x='TowerLon', y='TowerLat',c='gray', alpha=0.1, title='Call Locations')

    user1=df[((users==num[i])) & ((Y== ['Mon']) | (Y=='Tue')| (Y=='Wed')| (Y=='Thr')| (Y=='Fri'))]

    user2=df[((users==num[i])) & ((Z<'17:00:00')) & ((Y== ['Mon']) | (Y=='Tue')| (Y=='Wed')| (Y=='Thr')| (Y=='Fri'))]

    #print(user2)
   # print(len(user2))
    
    fig = plt.figure()
  
    ax = fig.add_subplot(111)
    ax.scatter(user2.TowerLon,user2.TowerLat, c='g', marker='o', alpha=0.2)
    ax.set_title('Weekend Calls (<6am or >10p)')
    
    print ("\n\nExamining person: ", num[i])
    
    user3=user2.loc[:,['TowerLon','TowerLat']]
    
    model= doKMeans(user3, 3)
    
    clusterInfo(model)  
 
  
    midWayClusterIndices = clusterWithFewestSamples(model)
    
    midWaySamples = user2[midWayClusterIndices==True]
    print(midWaySamples)
    #print ("Its Waypoint Time: ", midWaySamples.CallTime.mean())

   


#
# Let's visualize the results!
# First draw the X's for the clusters:
    ax.scatter(model.cluster_centers_[:,1], model.cluster_centers_[:,0], s=169, c='r', marker='x', alpha=0.8, linewidths=2)
#
# Then save the results:
#showandtell('Weekday Calls Centroids')
# 
# TODO: Create a slice called user1 that filters to only include dataset records where the
# "In" feature (user phone number) is equal to the first number on your unique list above
#
# .. your code here ..
plt.show() 

#
# TODO: Alter your slice so that it includes only Weekday (Mon-Fri) values.
#
# .. your code here ..


#
# TODO: The idea is that the call was placed before 5pm. From Midnight-730a, the user is
# probably sleeping and won't call / wake up to take a call. There should be a brief time
# in the morning during their commute to work, then they'll spend the entire day at work.
# So the assumption is that most of the time is spent either at work, or in 2nd, at home.
#
# .. your code here ..


#
# TODO: Plot the Cell Towers the user connected to
#
# .. your code here ..



#
# INFO: Run K-Means with K=3 or K=4. There really should only be a two areas of concentration. If you
# notice multiple areas that are "hot" (multiple areas the usr spends a lot of time at that are FAR
# apart from one another), then increase K=5, with the goal being that all centroids except two will
# sweep up the annoying outliers and not-home, not-work travel occasions. the other two will zero in
# on the user's approximate home location and work locations. Or rather the location of the cell
# tower closest to them.....



#
# INFO: Print out the mean CallTime value for the samples belonging to the cluster with the LEAST
# samples attached to it. If our logic is correct, the cluster with the MOST samples will be work.
# The cluster with the 2nd most samples will be home. And the K=3 cluster with the least samples
# should be somewhere in between the two. What time, on average, is the user in between home and
# work, between the midnight and 5pm?
  # Comment this line out when you're ready to proceed
