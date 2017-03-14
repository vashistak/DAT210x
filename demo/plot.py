'''
Created on Feb 13, 2017

@author: vashista
'''
import numpy
import matplotlib.pyplot as plt
year=[1950,1960,1970,1980]
pop=[2.519,4.566,2.455,3.999]
#plt.plot(year,pop)
plt.scatter(year,pop)
values=numpy.round(numpy.random.normal(50,1.23,100),2)
plt.hist(values,bins=3)
#plt.text(25, 50, text = "Scatter plot")
plt.show()