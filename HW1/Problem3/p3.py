from scipy.stats import norm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_context('poster')

#Problem 3a#

def ratioAboveA(diff,a):
    x=norm.sf(a,loc=diff)
    y=norm.sf(a)
    return x/y

plt.figure()

diffs=np.arange(1,3,0.25)
avals=np.arange(2,6)
for a in avals:
    plt.semilogy(diffs,[ratioAboveA(diff,a) for diff in diffs],label='a=%i'%a)

plt.xlabel('Difference in means')
plt.ylabel('Ratio of P(Y>a)/P(X>a)')
plt.title('Ratio of P(Y>a)/P(X>a) as a function of the difference in mean between Y and X')
plt.legend()


plt.show()


#Problem 3b: Compare distribution of income in Asia and South America#

gdp=pd.read_excel('income.xlsx')
gdp.columns.values[0]='Country'
gdp=gdp.set_index('Country')
notNull=[row for row in gdp.index if pd.notnull(row)]
gdp=gdp.loc[notNull]
regions=pd.read_csv('countries.csv')
regions=regions.set_index('Country')

gdp2012=gdp[2012]
asia=regions[regions['Region']=='ASIA']
gdpAsia2012=pd.concat([asia,gdp2012],axis=1).dropna()[2012]
sa=regions[regions['Region']=='SOUTH AMERICA']
gdpSa2012=pd.concat([sa,gdp2012],axis=1).dropna()[2012]


print 'Average GDP Per Capita in Asian countroes: ' + str(np.mean(gdpAsia2012))
print 'Average GDP Per Capita in South American countries: ' + str(np.mean(gdpSa2012))


#Problem 3c: Proportion of countries with gdp per capita > 10,000 in Asia and South America

richAsia=gdpAsia2012[gdpAsia2012>10000]
richSa=gdpSa2012[gdpSa2012>10000]

print 'Proportion of countries in Asia with GDP per capita > 10,000: ' + str(float(len(richAsia))/len(gdpAsia2012))

print 'Proportion of countries in South America with GDP per capita > 10,000: ' + str(float(len(richSa))/len(gdpSa2012))


#Asia has higher mean gdp per capita (23500.4324324) than South America (13015.75). However, Asia has a smaller proportion of countries with gdp per capita > 10,000 (0.567567567568) than South America (0.75). This means that the distribution of income in Asia is more skewed (there is greater income inequality, with a small number of very wealthy individuals)e


#Problem 3d: Compute GDP per capita across the entire region, rather than average of each country's GDP per capita in each regione

population=pd.read_csv('population.csv')
population.columns.values[0]='Country'
pop2012=population.set_index('Country')['2012']
for i, entry in enumerate(pop2012):
    if type(entry)==str:
        pop2012[i]=float(entry.replace(',',''))
    
dfAsia=pd.concat([gdpAsia2012,pop2012],axis=1,keys=['GDP Per Capita','Population']).dropna()
dfSa=pd.concat([gdpSa2012,pop2012],axis=1,keys=['GDP Per Capita','Population']).dropna()



print 'GDP Per Capita in Asia: ' + str(sum(dfAsia['GDP Per Capita'].values*dfAsia['Population'].values)/sum(dfAsia['Population'].values))
print 'GDP Per Capita in South America: ' + str(sum(dfSa['GDP Per Capita'].values*dfSa['Population'].values)/sum(dfSa['Population'].values))



