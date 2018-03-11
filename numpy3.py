import numpy as np

m1 = np.array([1,2,3,4])

m2 = np.array([5,6,7,8])

m3 = m1 + m2

m4 = np.array([
    [1,2],
    [3,4]
])

m5 = np.array([
    [5,6],
    [7,8]
])

m6 = m4 + m5


print(m3)

print(m6)


m7 = np.multiply(m4,m5)

print(m7)


m8 = np.array([
    [1,2],
    [3,4],
    [5,6]    
])

print(m8.shape)

m9 = np.array([
    [1,1,1],
    [2,2,2],
    [3,3,3]
])
print(m9.shape[0])

m10 = np.matmul(m9,m8)

print(m10.shape)
print(m10)


m11 = np.transpose(m8)

print(m11)

print(np.average([1,2]))


