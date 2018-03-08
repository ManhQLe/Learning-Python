import numpy as np

x = np.array([1,2,3,4])

print x.shape

x = x.reshape(1,4)
y = x.reshape(4,1)
print x.shape

print y.shape

m = np.array([
    [1,2,3],
    [2,3,4]
])

print m.shape

n = m.reshape(3,2)

print n
