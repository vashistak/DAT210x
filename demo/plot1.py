'''
Created on Feb 15, 2017

@author: vashista
'''

import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
#from matplotlib.pyplot import title
plt.style.use('ggplot')


df=pd.DataFrame(np.random.randn(100, 4), columns=list('ABCD'))
print(df)

plt.figure()
df.plot.scatter(x='A',y='B')
plt.xlabel('Acol')
plt.ylabel('B col')
plt.title('PIC')
plt.suptitle('MINI')


plt.figure()
df[df.A<=0].A.plot.hist(alpha=0.3)

plt.figure()
df.plot.hist(df,bins=6,alpha=0.6)


plt.figure()
plt.hist(df.B,bins=10)
plt.show()


