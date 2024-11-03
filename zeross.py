import numpy as np
#Using zeros to create a numpy array

#Creating a 1D array
print("This is a 1D array using zeros")
arr = np.zeros(4)
print(arr)

arrr = np.zeros(5)
print(arr)

#Creating a 2D numpy array of zeros
print("This is a 2D array using zeros")
arr1 = np.zeros((2,2))
print(arr1)

arr2 = np.zeros((4,3))
print(arr2)

arr3 = np.zeros((3, 4))
print(arr3)

#Creating a 3D array of zeros
print("This is a 3D array using zeros")
arrr1 = np.zeros((2,3,4))  # (b,r,c) b-blocks,r-rows, c-columns
print(arrr1)

arrr2 = np.zeros((4,2,2))
print(arrr2)

#Specifying Data Type
print("Specifying the datatype you want")
arrr5 = np.zeros((2,2), dtype = int)
print(arrr5)
print(arrr5.dtype)

# The created array will always be filled with the value 0.
# The default dtype is float, which means if you do not specify a data type, the array will contain floating-point zeros (e.g., 0.0).
# np.zeros() is particularly useful for initializing weight matrices in machine learning models or for creating empty arrays that you plan to fill with calculations later.
#








