import numpy as np

array1 = np.array([1, 2, 3])
array2 = np.array([[1, 2, 3], [4, 5, 6]])
print(array2)
print(array2.shape)

array3 = np.zeros((3, 4), dtype=int)
array4 = np.ones((3, 4), dtype=int)
array5 = np.full((3, 4), 5, dtype=int)
array6 = np.random.random((3, 4))
print(array6)
print(array6[0, 0])
print(array6 > 0.2)
print(array6[array6 > 0.2])
print(np.sum(array6))
print(np.floor(array6))
print(np.ceil(array6))
print(np.round(array6))

first = np.array([1, 2, 3])
second = np.array([4, 5, 6])
print(first + second)
print(first + 2)

dimensions_inch = np.array([1, 2, 3])
dimensions_cm = dimensions_inch * 2.54
print(dimensions_cm)
