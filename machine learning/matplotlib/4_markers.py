import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,6,8])
y = np.array([3,8,7,9])

plt.plot(x,y, linewidth=1,color='#ff0000',marker='*')
plt.show()