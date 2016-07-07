import urllib2
import StringIO
import requests
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import numpy.linalg as lin


#Problem 1a: Read files

file1=requests.get('https://raw.githubusercontent.com/cs109/2014_data/master/exprs_GSE5859.csv').content
exprs=pd.read_csv(StringIO.StringIO(file1))
file2=requests.get('https://raw.githubusercontent.com/cs109/2014_data/master/sampleinfo_GSE5859.csv').content
sampleInfo=pd.read_csv(StringIO.StringIO(file2))

#rearrange columns in sampledata
a=list(sampleInfo.filename.values)
b=list(exprs.columns.values)
order=[b.index(name) for name in a]
exprs=exprs[order]


#Problem 1b: Extract month and year as integers from YYYY-MM-DD format

sampleInfo['date']=pd.to_datetime(sampleInfo['date'])
sampleInfo['month']=map(lambda x: x.month, sampleInfo['date'])
sampleInfo['year']=[date.year for date in sampleInfo['date']]

#Problem 1c: Get the time elapsed in days from 2002-10-31

oct31=dt.datetime(2002,10,31,0,0)
sampleInfo['daysElapsed']=map(lambda x: (x-oct31).days, sampleInfo['date'])

#Problem 1d: Use SVD of gene expression data matrix 

ceuInfo=sampleInfo[sampleInfo['ethnicity']=='CEU']
exprsCEU=exprs[ceuInfo.filename]
normed=exprsCEU.apply(lambda x: x-exprsCEU.mean(axis=1),axis=0)
print normed.head()
U,S,V=np.linalg.svd(normed.values)
V=V.T

#Histogram of the values from PC1

plt.figure()
plt.hist(V[:,0],bins=25)
plt.xlabel('PC1')
plt.ylabel('Frequency')
plt.title('Distribution of the values from PC1')

plt.figure()
plt.scatter(ceuInfo.daysElapsed,V[:,0])
plt.xlabel('Days Elapsed from 10/31/2002')
plt.ylabel('PC1')
plt.title('Correlation between days elapsed and principal component')

plt.figure()
plt.scatter(ceuInfo.daysElapsed,V[:,0])
plt.xlabel('Days Elapsed from 10/31/2002')
plt.ylabel('PC1')
plt.title('Correlation between days elapsed and principal component')
plt.xlim([0,170])




plt.show()
