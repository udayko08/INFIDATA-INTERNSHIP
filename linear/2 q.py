import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

import statsmodels.api as sm

df = pd.read_csv('exam_marks.csv')
# Add a constant term to the predictor variable
x = sm.add_constant(df['Study Hours'])

# Create the dependent variable
y = df['Exam Score']

# Fit the linear regression model
model = sm.OLS(y, x).fit()

# Print the model summary
print(model.summary())