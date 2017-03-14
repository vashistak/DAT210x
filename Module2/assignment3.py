import pandas as pd
import numpy as np

# TODO: Load up the dataset
# Ensuring you set the appropriate header column names
#
# .. your code here ..
df=pd.read_csv(r'D:\python\udacity\Module2\Datasets\servo.data',header=None )
print(df)
print(df.describe(percentiles, include, exclude))
# TODO: Create a slice that contains all entries
# having a vgain equal to 5. Then print the 
# length of (# of samples in) that slice:
#
# .. your code here ..
print(df[df.iloc[:,3]==5])
print(df[df.iloc[:,3]==5].shape)
print(df[df.iloc[:,3]==5].describe())

# TODO: Create a slice that contains all entries
# having a motor equal to E and screw equal
# to E. Then print the length of (# of
#samples in) that slice:

# .. your code here ..
print(df[(df.iloc[:,0]=='E') & (df.iloc[:,1]=='E')])
print(df[(df.iloc[:,0]=='E') & (df.iloc[:,1]=='E')].shape)


x=df[df.iloc[:,2]==4]
np.array(x)
print(x)
print(np.mean(x.loc[:,3]))