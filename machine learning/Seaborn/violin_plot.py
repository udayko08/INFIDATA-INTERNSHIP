import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")

sns.violinplot(x='species', y='sepal_width', data=df)
# violin plot
plt.show()