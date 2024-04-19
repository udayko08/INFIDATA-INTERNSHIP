import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,6])
ypoints= np.array([0,10])

plt.plot(ypoints,linestyle = "dotted", color ='red')
plt.show()

plt.plot(ypoints,linestyle = "dashed", color ='#ffcee0')
plt.show()

plt.plot(ypoints,linestyle = "dashot",lw=10)
plt.show()

plt.plot(ypoints,ls="solid")
plt.show()