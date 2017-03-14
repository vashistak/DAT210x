import pandas as pd

import matplotlib.pyplot as plt
import matplotlib

plt.style.use('ggplot') # Look Pretty

def showandtell(title=None):
  if title != None: plt.savefig(title + ".png", bbox_inches='tight', dpi=300)
  plt.show()
  # exit()

#
# INFO: This dataset has call records for 10 users tracked over the course of 3 years.
# Your job is to find out where the users likely live and work at!

#
# TODO: Load up the dataset and take a peek at its head
# Convert the date using pd.to_datetime, and the time using pd.to_timedelta
#
# .. your code here ..
df=pd.read_csv(r'Datasets/CDR.csv')
#print(df.head(15))
#exit()
#
# TODO: Get a distinct list of "In" phone numbers (users) and store the values in a
# regular python list.
# Hint: https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.tolist.html
#
# .. your code here .
num=df.In.unique()
print(len(num))
 
import numpy as np
X=df['In']
users=np.array(X)
print(users)
print(len(users))
Y=np.array(df['DOW'])
print(Y)
import datetime as dt
    
    #df['CallTime']=pd.to_datetime(df['CallTime'])
    #df['CallTime'] = dt.strftime('%H:%M:%S') for 
    #df['CallTime'] = [dt.strftime('%H:%M:%S') for CallTime in df['CallTime']]
df['CallTime'] = df['CallTime'].apply(lambda x:  dt.datetime.strptime(x,'%H:%M:%S.%f').strftime('%H:%M:%S'))

Z=np.array(df['CallTime'])

print(Z)
    
for i in range(len(num)):
    user1=[]
    user2=[]
# TODO: Create a slice called user1 that filters to only include dataset records where the
# "In" feature (user phone number) is equal to the first number on your unique list above;
# that is, the very first number in the dataset
#
# .. your code here ..

    print(i)
    user1=df[users==num[i]]
    print(len(user1))
    
# INFO: Plot all the call locations
    user1.plot.scatter(x='TowerLon', y='TowerLat',c='gray', alpha=0.1, title='Call Locations')
#showandtell()  # Comment this line out when you're ready to proceed

#
# TODO: Add more filters to the user1 slice you created. Add bitwise logic so that you're
# only examining records that came in on weekends (sat/sun).
#
# .. your code here ..

    user1=df[((users==num[i])) & ((Y== ['Sat']) | (Y=='Sun'))]
#print(user1)
#exit()
#
# TODO: Further filter it down for calls that are came in either before 6AM OR after 10pm (22:00:00).
# You can use < and > to compare the string times, just make sure you code them as military time
# strings, eg: "06:00:00", "22:00:00": https://en.wikipedia.org/wiki/24-hour_clock
#
# You might also want to review the Data Manipulation section for this. Once you have your filtered
# slice, print out its length:
#
# .. your code here ..    
    
    
    user2=df[((users==num[i])) & ((Z<'06:00:00') | (Z>'22:00:00')) & ((Y== ['Sat']) | (Y=='Sun'))]

    print(user2)
    print(len(user2))

# INFO: Visualize the dataframe with a scatter plot as a sanity check. Since you're familiar
# with maps, you know well that your X-Coordinate should be Longitude, and your Y coordinate
# should be the tower Latitude. Check the dataset headers for proper column feature names.
# https://en.wikipedia.org/wiki/Geographic_coordinate_system#Geographic_latitude_and_longitude
#
# At this point, you don't yet know exactly where the user is located just based off the cell
# phone tower position data; but considering the below are for Calls that arrived in the twilight
# hours of weekends, it's likely that wherever they are bunched up is probably near where the
# caller's residence:
    fig = plt.figure()
  
    ax = fig.add_subplot(111)
    ax.scatter(user2.TowerLon,user2.TowerLat, c='g', marker='o', alpha=0.2)
    ax.set_title('Weekend Calls (<6am or >10p)')
    
#showandtell()  # TODO: Comment this line out when you're ready to proceed



#
# TODO: Run K-Means with a K=1. There really should only be a single area of concentration. If you
# notice multiple areas that are "hot" (multiple areas the usr spends a lot of time at that are FAR
# apart from one another), then increase K=2, with the goal being that one of the centroids will
# sweep up the annoying outliers; and the other will zero in on the user's approximate home location.
# Or rather the location of the cell tower closest to their home.....
#
# Be sure to only feed in Lat and Lon coordinates to the KMeans algo, since none of the other
# data is suitable for your purposes. Since both Lat and Lon are (approximately) on the same scale,
# no feature scaling is required. Print out the centroid locations and add them onto your scatter
# plot. Use a distinguishable marker and color.
#
# Hint: Make sure you graph the CORRECT coordinates. This is part of your domain expertise.
#
# .. your code here ..
    from sklearn.cluster import KMeans 
    model=KMeans(n_clusters=1).fit(user2.loc[:,['TowerLon','TowerLat']])  
    centroids = model.cluster_centers_
    print(centroids)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(centroids[:,0], centroids[:,1], marker='x', c='red', alpha=0.5, linewidths=3, s=169)
    ax.set_title('plot for:')
 
    plt.show()   

#showandtell()  # TODO: Comment this line out when you're ready to proceed



#
# TODO: Repeat the above steps for all 10 individuals, being sure to record their approximate home
# locations. You might want to use a for-loop, unless you enjoy typing.
#
# .. your code here ..

