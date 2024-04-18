import numpy as np

a1 = np.array([1,2,3,4,5,6])
print("Addaing 1 to evry element:", a1+1)

print("Subtracting 2 from each element:", a1*10)

print("Squaring each element:", a1**2)

a1 *= 2
print("Doubled each element of orginal array:",a1)

a2 = np.array([[1,2,3],[4,5,6],[9,6,0]])

print("\n Orginal array:\n",a2)
print("Transpose of array:\n",a2.T)