'''
Created on Feb 16, 2017

@author: vashista
'''

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


import pandas as pd
#from matplotlib.pyplot import title

df=pd.DataFrame(np.random.randint(0,100,size=(100,5)), columns=list('ABCDE'))
print(df)

plt.style.use('ggplot')

fig=plt.figure()
plt.suptitle('A and B and C')
ax=fig.add_subplot(111, projection='3d')
ax.set_xlabel('A')
ax.set_ylabel('B')
ax.set_zlabel('C')
ax.scatter(df.A,df.B,df.C,c='r', marker='o')


fig=plt.figure()
plt.suptitle('A and D and C')
ax=fig.add_subplot(111, projection='3d')
ax.set_xlabel('A')
ax.set_ylabel('D')
ax.set_zlabel('C')
ax.scatter(df.A,df.D,df.C,c='g', marker='o')


fig=plt.figure()
plt.suptitle('A andE and C')
ax=fig.add_subplot(111, projection='3d')
ax.set_xlabel('A')
ax.set_ylabel('E')
ax.set_zlabel('C')
ax.scatter(df.A,df.E,df.C,c='b', marker='o')
plt.show()



