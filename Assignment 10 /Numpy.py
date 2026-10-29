import numpy as np

arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
arr2 = np.arange(1, 11)

print("Array:", arr1)

print("Data type:", arr1.dtype)
print("Shape:", arr1.shape)
print("Dimensions:", arr1.ndim)
print("Size:", arr1.size)

print("Both arrays equal:", np.array_equal(arr1, arr2))

print("Array * 2:", arr1 * 2)
print("Array + 100:", arr1 + 100)
print("Sum:", arr1.sum())
print("Mean:", arr1.mean())

print("First element:", arr1[0])
print("Last element:", arr1[-1])
print("First 5 values:", arr1[:5])
print("Every other element:", arr1[::2])
