# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
# start: Starting value of the sequence.
# stop: End value of the sequence.
# num: Number of values to generate (default is 50).
# endpoint: If True (default), includes the stop value; if False, excludes it.
# retstep: If True, returns a tuple (array, step), where step is the spacing between values.
# dtype: Desired data type of the output array.
# axis: Specifies the axis in the output for inserting the new dimension.

import numpy as np
arr = np.linspace(0, 5, 10) #10 points between 0 and 5
print(arr)


# arry = np.linspace(2,20, num = 5)
# print(arry)
#
# arrr = np.linspace(0, 10, num = 5, endpoint = False)
# print(arrr)
#
# my_arr, step = np.linspace(0, 10, num = 5, retstep = True)
# print(my_arr, step)
#
# arrr1 = np.linspace(1, 10, 5, retstep = True)
# print(arrr1)

#Creating an Integer Array
myarray = np.linspace(1, 20, 5, dtype = int)
print(myarray)


#Generating a High-Resolution Array
arr_1 = np.linspace(0, 2, 20)
print(arr_1)

print("-------------------------------------------------------")

##This is the Identity Matrix
print("IDENTITY MATRIX")
eye_matrix = np.eye(3)
print(eye_matrix)
































