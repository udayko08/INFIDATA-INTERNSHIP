import pandas as pd

df=pd.read_csv('data.csv') #loading the dataset
print('[info] data loaded successfully...')

print('[info] checking for NaN values....')
print(df.columns[df.isna().any()])

print('[info] removing NaN values..')
df=df.dropna() #this line remove entire row which has NaN value

print('[info] checking for NaN again...')
print(df.columns[df.isna().any()])