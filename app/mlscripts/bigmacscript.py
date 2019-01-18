import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib
from app import BASEDIR

df = pd.read_csv(BASEDIR + "/mldata/BigMac.csv", sep = '\t')
reg = LinearRegression().fit(df[['Wage']], df[['Price']])
print(reg.score(df[['Wage']], df[['Price']]))
joblib.dump(reg, BASEDIR + '/mlmodels/linreg.joblib')
