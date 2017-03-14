import pandas as pd
import matplotlib.pyplot as plt


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..

df=pd.read_csv(r'D:\python\udacity\Module3\Datasets\wheat.data')
print(df)

#
# TODO: Drop the 'id' feature, if you included it as a feature
# (Hint: You shouldn't have)
# 
# .. your code here ..
df1=df.drop(['id'], 1)

#
# TODO: Compute the correlation matrix of your dataframe
# 
# .. your code here ..
print(df1.corr())

#
# TODO: Graph the correlation matrix using imshow or matshow
# 
# .. your code here ..
plt.imshow(df1.corr(), interpolation='nearest')

plt.colorbar()
plt.show()

plt.show()


