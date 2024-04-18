import numpy as np

a1 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print("array contents are\n",a1)
s1= a1[:2,:3]
print("Array with first 2 rows and first 3 coloumns:\n",s1)
s2 = a1[:2, ::2]
print("Array with first 2 rows and alternate  coloumns:\n",s2)
 