import  seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")

sns.barplot(x="sepal_length", y="sepal_width", color="red", data=df)
plt.show()