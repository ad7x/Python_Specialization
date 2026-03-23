import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])

m,n= a.shape

print(a)
print(a.shape)
print(f"the no of row in the array is {m}")
print(f"the no of column in the array is {n}")

print(""" 
row slicing

  """)

print(a[:2])

print(""" 
column slicing

  """)

print(a[:,1])