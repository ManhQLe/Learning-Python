import numpy as np

s = np.array(5)
print("Scalar")
print(s)

v = np.array([1,2,3])
v2 = v + 3
print("Vectors")
print(v)
print(v2)
print(v[0] )

m = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print("Matrix")
print(m)
print(m.shape)