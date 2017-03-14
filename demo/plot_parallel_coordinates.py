'''
Created on Feb 16, 2017

@author: vashista
'''
from sklearn.datasets import load_iris
from pandas.tools.plotting import parallel_coordinates

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

plt.style.use('ggplot')

data=load_iris()
df=pd.DataFrame(data.data,columns=data.feature_names)
print(data)
print(df)

df['target_names']=[data.target_names[i] for i in data.target]
print(data.target_names)
plt.figure()
parallel_coordinates(df,'target_names')
plt.show()
