import numpy as np
import pandas as pd

example1_data = pd.DataFrame({'x':[0,1,2,3,4,],'y':[1,2,3,4,5]})

print(example1_data)

x= example1_data['x'].values.reshape(-1,1)
y= example1_data['x'].values.reshape(-1,1)

from sklearn.linear_model import LinearRegression
linear_regressor = LinearRegression()
linear_regressor.fit(x,y)
print('[info] linear regression model training completed..')

m= linear_regressor.coef_
c= linear_regressor.intercept_

print(f"m values is :{m}")
print(f"m values is :{c}")
print(f"equation of line is :y={m}x+c")