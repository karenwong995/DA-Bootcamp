import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set(context='poster',style='whitegrid')

f = lambda x,l: l*np.exp(-l*x) * (x>=0)
xpts=np.arange(-2,3,0.1)
f=plt.figure()
plt.plot(xpts,f(xpts,2),'o')
plt.xlabel('x')
plt.ylabel('exponential pdf')
plt.show()
