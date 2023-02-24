import numpy as np

a = np.array([1, 2, 8, -2, 0])
b = np.array([1 + 1j, 1 + 3j])

print(np.gradient(a, 10))
