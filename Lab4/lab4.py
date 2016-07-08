import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn
import statsmodels.api as sm
import seaborn as sns
sns.set_context('poster')
from matplotlib import rcParams

#load data

from sklearn.datasets import load_boston
boston=load_boston()
bos=pd.DataFrame(boston.data)
bos.columns=boston.feature_names
bos['PRICE']=boston.target


#Plot a regression using seaborn: PRICE~RM

plt.figure()
sns.regplot(y='PRICE',x='RM',data=bos)
plt.title('Regplot using seaborn')

#Plot a regresion using statsmodels.formula.api.ols(): PRICE~RM

from statsmodels.formula.api import ols
m=ols('PRICE~RM',bos).fit()
m.summary()

plt.figure()
params=m.params
plt.scatter(bos['RM'],bos['PRICE'],color='blue',marker='s')
plt.plot(bos['RM'],m.fittedvalues,color='black')
plt.title('Regression and scatterplot')

#compare regression-fitted values with actual
plt.figure()
plt.scatter(bos['PRICE'],m.fittedvalues)
ref=np.linspace(min(bos.PRICE),max(bos.PRICE),10)
plt.plot(ref,ref,color='black',label='reference')
plt.ylabel('Predicted prices: $\hat{Y}_i$')
plt.xlabel('Actual prices: $Y_i$')
plt.title('Regression-fitted values vs actual values')
plt.legend()

#Predict PRICE using sklearn.linear_model.LinearRegression(): PRICE ~ all other vars

from sklearn.linear_model import LinearRegression
X=bos.drop('PRICE',axis=1)
lm = LinearRegression()
lm.fit(X,bos['PRICE'])
print lm.coef_
print lm.intercept_
#Predicted values using the fit
fig,axes=plt.subplots(2,1)
axes[0]=plt.subplot(2,1,1)
plt.hist(lm.predict(X))
axes[0].set_title('Predicted distribution')
axes[1]=plt.subplot(2,1,2)
plt.hist(bos['PRICE'])
axes[1].set_title('Actual Distribution')
plt.suptitle('Comparing Actual with Predicted Distribution by LSQR')
plt.subplots_adjust(top=0.85)


#train and test
X_train,X_test,Y_train,Y_test = sklearn.cross_validation.train_test_split(X,bos.PRICE,test_size=0.33,random_state=5)
lm=LinearRegression()
lm.fit(X_train,Y_train)
predictTrain=lm.predict(X_train)
predictTest=lm.predict(X_test)
predictTotal=lm.predict(X)

mseTrain=np.mean((predictTrain-Y_train)**2)
mseTest=np.mean((predictTest-Y_test)**2)
mseTotal=np.mean((predictTotal-bos.PRICE)**2)


plt.show()
