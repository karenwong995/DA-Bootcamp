import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import seaborn as sns
sns.set_context('poster')


#Problem 3a: Add a new column for Obama-Romney

polls=pd.read_csv('http://elections.huffingtonpost.com/pollster/2012-general-election-romney-vs-obama.csv')
polls['Start Date']=pd.to_datetime(polls['Start Date'])
polls['Diff']=(polls.Obama-polls.Romney)/100
electionday=dt.datetime(2012,11,06)
weekBefore=polls[map(lambda x: ((x-electionday).days)>=-7,polls['Start Date'])]



#Problem 3b: Plot the percentage difference between Obama and Romney in polls taken one week before election day

pollsterColor={}
for p in set(weekBefore.Pollster):
    pollsterColor[p]=(np.random.rand(), np.random.rand(), np.random.rand())
    
plt.figure()
numDaysBefore=map(lambda x: (x-electionday).days, weekBefore['Start Date'])
plt.scatter(numDaysBefore,weekBefore.Diff,color=map(lambda x: pollsterColor[x], weekBefore.Pollster),s=40)
plt.axhline(0.039,0,1,color='red',label='Actual percent difference on election day')
plt.axhline(np.mean(weekBefore['Diff']),color='blue',label='Mean percent difference among polls')
plt.title('Poll-predicted Obama-Romney gap one week before election day')
plt.xlabel('Days before election')
plt.ylabel('Percent difference according to polls')
plt.legend()


#Problem 3c: Plot the poll-predicted Obama-Romney gap minus actual gap by pollster

grouped = polls.groupby(['Pollster','Affiliation'])
percentByPollster=grouped['Diff'].mean()-0.039  #If a pollster made more than one poll, average the results
plt.figure()
plt.bar(np.arange(len(percentByPollster)),percentByPollster)
plt.xlim([0,len(percentByPollster)])
plt.title('Poll-predicted Obama-Romney gap minus actual Obama-Romney gap')
plt.xlabel('Pollsters (see Pollsters printout for names)')
plt.ylabel('Difference between polls and actual results')

#print table showing the names of the pollsters next to their predicted Obama-Romney differences (no space to put names on plot)

table=percentByPollster.reset_index()   #add number indexes next to pollster names to make it easier to reference on plot
#print table
table.to_csv('percentByPollster.csv')


#Problem 3d: Get the average of the average for each pollster
print 'The average of the average result from each pollster is: ' + str(np.mean(percentByPollster))

plt.show()






