import numpy as np
# identity_matrix = np.eye(4) #Basic identity matrix
# print(identity_matrix)
#
#
# #Non-Square Identity Matrix
# matrix = np.eye(3,4)
# print(matrix)
#
# print(type(matrix))


#Shifting the Diagonal
my_matrix = np.eye(3, 4, k = 1)
print(my_matrix)


my_matrix1 = np.eye(4, 5, k = -1)
print(my_matrix1)


#Specifying the datatype
matrix_x = np.eye(3, dtype = int)
print(matrix_x)






