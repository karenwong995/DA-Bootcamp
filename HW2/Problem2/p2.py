import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
import seaborn as sns
sns.set_context('poster')


#Problem 2a; Read files

polls=pd.read_csv('http://elections.huffingtonpost.com/pollster/2012-general-election-romney-vs-obama.csv')
polls['Start Date']=pd.to_datetime(polls['Start Date'])

pollsNov=polls[map(lambda x: (x.month==11) & (x.year==2012), polls['Start Date'])]
numPollsNov=len(pollsNov.Pollster.unique())
medianObs=np.median(pollsNov['Number of Observations'])



#Problem 2b: Distribution of results from a single poll

#Histogram of distribution of results from a single poll

from scipy.stats import binom
N=float(medianObs)
p=0.53

def simulatePoll(N,p):
    return binom.rvs(N,p)/N

numSims=1000

singlePollDistr=[simulatePoll(N,p) for i in range(numSims)]
meanSinglePoll=np.mean(singlePollDistr)
singlePollDistrSE=np.std(singlePollDistr)

plt.figure()
plt.hist(singlePollDistr)
plt.title('Distribution of the Obama success percentage on a single poll, $\mu=%.4f,\ \sigma=%.4f$'%(meanSinglePoll,singlePollDistrSE))

#Use a probability plot to show tha the distribution is normal
plt.figure()
scipy.stats.probplot(((singlePollDistr-np.mean(singlePollDistr))/np.std(singlePollDistr)),dist='norm',plot=plt)
plt.title('Probability plot for distribution of results from a single poll')    




#Problem 2c: Statistics on the distribution of the mean of the result from M polls
M=numPollsNov

def simulateMPolls(N,p,M):
    return [simulatePoll(N,p) for i in range(M)]

MPollsMeans=[np.mean(simulateMPolls(N,p,M)) for i in range(numSims)]
MPollsMeansSE=np.std(MPollsMeans)
plt.figure()
plt.hist(MPollsMeans)
plt.title('Distribution of the mean from M polls,$\mu=%.4f,\ \sigma=%.4f$'%(np.mean(MPollsMeans),MPollsMeansSE))


print 'The Standard error of the distribution of results from one poll is %f' % singlePollDistrSE
print 'The Standard error of the distribution of the mean of results from M polls is %f' % MPollsMeansSE


#Problem 2d: Statistics on the distribution of the Standard Deviation across M polls

MPollsStd=[np.std(simulateMPolls(N,p,M)) for i in range(numSims)]
MPollsStdMean=np.mean(MPollsStd)
plt.figure()
plt.hist(MPollsStd)
plt.title('Distribution of the standard deviation across M polls, $\mu=%.3f,\ \sigma=%.3f$' %(np.mean(MPollsStd),np.std(MPollsStd)))

#What is the distribution of the standard deviation? (normal)
plt.figure()
obs=MPollsStd
scipy.stats.probplot( (obs-np.mean(obs))/np.std(obs),plot=plt)
plt.title('Probability plot of the distribution of the standard deviation across M polls')


#Problem 2e: What is the Standard Deviation across M polls in the real (not simulated) presidential election data?

std =np.std(pollsNov['Obama']/100)
ratio = np.mean(MPollsStd)/std


print 'The actual standard deviation across the M Polls is: ' + str(np.std(pollsNov['Obama']/100))

plt.show()


