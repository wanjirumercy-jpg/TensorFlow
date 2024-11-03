import numpy as np
#arange() returns an array of type int or float depending on the input values
#using arange (basic usage)
arange_arr = np.arange(10) #prints from 0 to 9
print(arange_arr)

arrange = np.arange(5)
print(arrange)

#Specifying a start and a stop using arange
#The stop value is exclusive, meaning the generated array will not include this value.
arr_1 = np.arange(2,10) # prints from 2 to 9
print(arr_1)

#Specifying a step using arange
#If the step is zero, it will raise a ValueError
arr7 = np.arange(0, 20, 2)
print(arr7)

#Negative step(Decreasing values) using arange
arn = np.arange(10, 0, -2)
print(arn)

#Float step
arr12 = np.arange(0,1, 0.1)
print(arr12)

# Using arange to reshape
arr31 = np.arange(12).reshape(3, 4) # it prints from 0 to 11 in a 3 by 4 matrix
print(arr31)
