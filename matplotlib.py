'''
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 50, endpoint=True) #在指定的间隔内返回均匀间隔的数字。


C,S = np.cos(X), np.sin(X)


#print( type(C))
 

 
plt.plot(X,C)
plt.plot(X,S)

plt.show()
'''

from pylab import *

n = 256
X = np.linspace(-np.pi,np.pi,n,endpoint=True)
Y = np.sin(2*X)

plot (X, Y+1, color='blue', alpha=1.00)
plot (X, Y-1, color='blue', alpha=1.00)
show()

