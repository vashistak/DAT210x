'''
Created on Feb 16, 2017

@author: vashista
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.DataFrame(np.random.randint(0,100, size=(100,5)), columns=list('ABCDE'))

print(df)

plt.imshow(df.corr(), interpolation='nearest')

plt.colorbar()
plt.show()






