import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import seaborn as sns
sns.set_context('poster')

#Problem 1a: Read files

countries=pd.read_csv("https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv").set_index('Country')

try:
    gdp=pd.read_excel("income.xlsx")
except IOError:
    print "go to https://docs.google.com/spreadsheets/d/1PybxH399kK6OjJI4T2M33UsLqgutwj3SuYbk7Yt6sxE/pub?gid=0 and change last part of address"
    print "change to https://docs.google.com/spreadsheets/d/1PybxH399kK6OjJI4T2M33UsLqgutwj3SuYbk7Yt6sxE/export?format=xls to download the needed file and rename it"
    sys.exit()
    
gdp.columns.values[0]='Country'
gdp=gdp.set_index('Country').transpose()
notNulls=[column for column in gdp.columns if pd.notnull(column)]
gdp=gdp[notNulls]



#Problem 2b: Display histogram of gdp per capita. Parameter: dataframe with data from a given region for a given year

def get_subplot(data,ax,year):
    plt.hist(data,bins=30)
    ax.set_title(year)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    

#Problem 2c: Given a region, get a dataframe merging countries[countries['Region'[==region] with gdp dataframe for any year.

def mergeDF(regionDF,year):
    yearGDP=gdp.loc[year]
    df=pd.concat([regionDF,yearGDP],axis=1)
    df.columns=['Region','GDP Per Capita']
    return df

#Problem 2d: For each region, show how the distribution of income has changed over time


figures=[]
for region in countries['Region'].unique():
    regionDF=countries[countries['Region']==region]
    f,axes=plt.subplots(5,1,figsize=(9,16))

    for i, year in enumerate(range(1800,2001,50)):
        regionGDP=mergeDF(regionDF,year).dropna()
        axes[i]=plt.subplot(5,1,i+1)
        get_subplot(regionGDP['GDP Per Capita'],axes[i],year)

    #for ax in axes:
        #ax.set_xlim([0,max(regionGDP['GDP Per Capita'])])

    plt.suptitle('Distribution of GDP Per Capita in '+region+ ' over time\n\n')
    plt.tight_layout()
    plt.subplots_adjust(top=0.93)
    figures.append(f)


plt.show()

"""
for fig in figures:
    
    plt.show()
"""



