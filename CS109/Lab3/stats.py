import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_context('poster')

xpts=np.linspace(-5,5,100)
colors=sns.color_palette()

for mu, sigma, c in zip([0.5]*3,[0.2,0.5,0.8],colors):
    plt.plot(xpts,norm.pdf(xpts,mu,sigma),lw=2,color=c,label="$\sigma=%.1f$"%sigma)
    plt.fill_between(xpts,norm.pdf(xpts,mu,sigma),color=c,alpha=0.4)

plt.xlim([-5,5])
plt.legend()

from scipy.stats import bernoulli


#confirm standard error of sampling distrubtion 
def tossCoin(n):
    return bernoulli.rvs(0.5,size=n)

def getSampleMeans(numSamples,sampleSize):
    samples=np.zeros((numSamples,sampleSize))
    for i in range(numSamples):
        samples[i,:]=tossCoin(sampleSize)
    return np.mean(samples,axis=1)


sampleSizes=np.arange(1,1001,1)
standardErrors=[np.std(getSampleMeans(numSamples=200,sampleSize=N)) for N in sampleSizes]
plt.figure()
plt.plot(np.log10(sampleSizes),np.log10(standardErrors)


#mean of sample Means
meanOfMeans=[np.mean(getSampleMeans(numSamples=200,sampleSize=N)) for N in sampleSizes]
plt.figure()
plt.plot(sampleSizes,meanOfMeans)

#visualize sampling distribution

sampleMeans=[getSampleMeans(numSamples=200,sampleSize=N) for N in sampleSizes]
plt.figure()
plt.hist(sampleMeans[9],bins=np.arange(0,1,0.01), alpha=0.5)
plt.hist(sampleMeans[99],bins=np.arange(0,1,0.01),alpha=0.4)
plt.hist(sampleMeans[999],bins=np.arange(0,1,0.01),alpha=0.3)



