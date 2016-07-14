import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import seaborn as sns
sns.set_style("darkgrid")
sns.set_context("poster")

print "This script analyzes a Baseball dataset showing statistics for each team across certain years \n"


#Problem 1a: download and extract zip file (run once)

import urllib2
import zipfile
import shutil
import os


if not(os.path.isfile('baseballfiles.zip')):
     webfile=urllib2.urlopen("http://www.seanlahman.com/files/database/baseballdatabank-master_2016-03-02.zip")
     webdata=webfile.read()

     with open("baseballfiles.zip","w") as f:
         f.write(webdata)

     z=zipfile.ZipFile("baseballfiles.zip")
     z.extractall()
     z.close()
     shutil.copytree('./baseballdatabank-master/core','BaseballFiles')



#Problem 1b: create a dataframe called Salaries to show the total salary for each team in each year


salaries=pd.read_csv("BaseballFiles/Salaries.csv")
salariesSum=salaries.groupby(["teamID","yearID"],as_index=False)["salary"].sum()
print "Total team salary grouped by team and year"
print salariesSum.head()

#Problem 1c: create a dataframe with both total salaries and wins for each team for each year (merge two dataframes)

teams=pd.read_csv("BaseballFiles/Teams.csv")
winsAndSalaries=pd.merge(salariesSum,teams,how='inner',on=['teamID','yearID'])[['teamID','yearID','salary','W']]
print "Total team salary and wins grouped by team and year"
print winsAndSalaries.head()

#Problem 1d: Make scatterplots of wins vs salaries for each year

from scipy.stats.stats import pearsonr

startYear=min(winsAndSalaries['yearID'])
endYear=max(winsAndSalaries['yearID'])
analyzedYears={}   

#extract only the data from years in which the correlation between the wins and salaries is significant

for year in range(startYear,endYear+1):
    filteredYear=winsAndSalaries[winsAndSalaries['yearID']==year]
    yearSalary=filteredYear['salary'].values
    yearWins=filteredYear['W'].values
    if pearsonr(yearSalary,yearWins)[1]<0.05:  
        analyzedYears[year]=[filteredYear['teamID'].values,yearSalary,yearWins]

#scatterplot

fig, axes = plt.subplots(5,3,sharex=True,sharey=True)
resids=[]
for i, year in enumerate(analyzedYears):
    
    subplot=axes[i/3,i%3]
    yearSalary=analyzedYears[year][1]
    yearWins=analyzedYears[year][2]
    #scatterplot of salary vs wins, put a red diamond for Oakland
    subplot.scatter(yearSalary,yearWins,color='blue')
    subplot.scatter(yearSalary[20],yearWins[20],color='red',marker='D',s=50)
    #get regression line
    fit=np.polyfit(yearSalary,yearWins,deg=1)
    subplot.plot(yearSalary,fit[0]*yearSalary + fit[1],color='black')
    subplot.set_title(year)
    subplot.set_xlim([0,1.5e8])
    subplot.set_yticks(np.arange(30,130,20))
    resids.append(yearWins-(fit[0]*yearSalary+fit[1]))

fig.suptitle('Correlation between salaries and wins by year',fontsize=20)
fig.text(0.5,0.01,'Salaries',ha='center')
fig.text(0.04,0.5,'Wins',va='center',rotation='vertical')
axes[4,2]=plt.subplot(5,3,15)
axes[4,2].set_xlim([0,1.5e8])
axes[4,2].set_yticklabels([])
p=mpatches.Patch(color='red',label='Oakland')
plt.legend(handles=[p])
#plt.show()


plt.figure()
r = zip(*resids)
#print resids
print len(resids)
print r[1]
print len(r[1])
print analyzedYears.keys()[1]
print len(analyzedYears.keys())
for i in range(len(r)):
    plt.plot(analyzedYears.keys(),r[i],color='black')

plt.plot(analyzedYears.keys(),r[20],color='red',label='Oakland')
plt.title('Residual plot')
plt.legend()

plt.show()

"""
#plt.show()


#problem 1e: residuals against time
plt.figure()
for i, year in enumerate(analyzedYears):
    
    resids[year]=corr[year][1] - (fit[0]*corr[year][2] + fit[1])
    ax.scatter(corr[year][2],resids[year])
    ax.set_title(year)
    plt.xlim([0,1.5e8])
    plt.ylim([-25,25])
    plt.axhline(color='black')
    
plt.suptitle('Residuals of salaries vs wages against time',fontsize=20)
plt.ylabel('Residuals')
plt.xlabel('Year')

"""

"""
SCRATCH: This is a messier version I wrote when first exploring matplotlib.pyplot. Very bad.


#Find years with significant correlations
corr={}
significant=[]
for year in range(startYear,endYear+1):
    corr[year]=[[],[],[],0]
    corr[year][0]=winsAndSalaries.query('yearID==%i' % year)['teamID'].values
    corr[year][1]=winsAndSalaries.query('yearID==%i' % year)['W'].values
    corr[year][2]=winsAndSalaries.query('yearID==%i' % year)['salary'].values
    corr[year][3]=pearsonr(corr[year][1],corr[year][2])
    if corr[year][3][1] < 0.05:
        significant.append(year)
    
fig_1c, axes = plt.subplots(5,3,sharex=True,sharey=True)
for i, year in enumerate(significant):
    ax=plt.subplot(5,3,i+1)
    ax.scatter(corr[year][2],corr[year][1],color='blue')
    ax.scatter(corr[year][2][19],corr[year][1][19],color='red',marker='D',s=50)
    fit=np.polyfit(corr[year][2],corr[year][1],deg=1)
    ax.plot(corr[year][2],fit[0]*corr[year][2] + fit[1],color='black')
    ax.set_title(year)
    plt.xlim([0,1.5e8])

plt.suptitle('Correlation between salaries and wins by year',fontsize=20)
plt.xlabel('Salaries',fontsize=16)
plt.ylabel('Wins',fontsize=16)
ax=plt.subplot(5,3,15)
p=mpatches.Patch(color='red',label='OAK')
plt.legend(handles=[p])


#fig_1c.show()


"""




        

