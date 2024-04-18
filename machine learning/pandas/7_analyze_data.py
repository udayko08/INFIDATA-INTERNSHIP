import pandas as pd

df = pd.read_csv("diabetes.csv")

print("Accessing from the dataset from first 10 Rows\n",df.head(10))
print("Accessing from the dataset from first 5 rows\n",df.head())

print("Accessing from the dataset from last 10 rows\n",df.tail(10))
print("Accessing from the dataset from last 5 rows\n",df.tail(5))

print(df.shape)
print(df.columns[df.isna().any()])

print("Baic info:\n",df.info())

print("Statistical info:\n",df.describe())