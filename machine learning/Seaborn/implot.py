import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset("iris")
sns.lmplot(x='petal_length',y='petal_width',data=df)
plt.show()