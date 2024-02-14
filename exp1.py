import numpy as np

row_vector=np.array([10,15,20])
print(row_vector)

#create a column vector
column_vector=np.array([[10],[20],[30]])
print(column_vector)

#create matrix
matrix=np.array([[10,20,30],[40,50,60]])#this is 2x2 matrix
print(matrix)

#accessing the elements
row_vector=np.array([10,20,30,40,50,60])
print("row vector:",row_vector)

#create a matrix
matrix=np.array([[10,20,30],[40,50,60],[70,80,90]])
print("matris is:",matrix)

#acces the second element
print("the second elemnet is:",row_vector[1])

#access 3rd row 3rd column
print("matrix[2,2]:",matrix[2,2])

#select all the elemnts of a vector
print("row_vector[:]",row_vector[:])

#select the last element
print("last elemnt is:",row_vector[-1])

#select first 2 rows and all the columns of the matrix
print("matrix[:2,:]:",matrix[:2,:])

#view the no of rows and columns
print("Rows and Columns:",matrix.shape)

#view the no of elements(rows*elements)
print("no of elements:",matrix.size)

#view the no of dimensions(2 in this case)
print("Dimension:",matrix.ndim)

#max element
print("max eleemnt:",np.max(matrix))
print("min of matrix",np.min(matrix))
#to find the max elemenet in each column
print(np.max(matrix,axis=0))
#to find the max element in each row
print(np.max(matrix,axis=1))
#to find the min elemenet in each column
print(np.min(matrix,axis=0))
#to find the min element in each row
print(np.min(matrix,axis=1))


#calculating average
#for avrage we use mean func in the np library
print("mean of matrix is:",np.mean(matrix))

#reshaping of the matrix
#here we use reshape func
print(matrix.reshape(9,1))

#here -1 says as many columns as needed and 1 row
print(matrix.reshape(1,-1))

#if we provide only one value reshape would return a 1-d array of that length
print(matrix.reshape(9))

#we can also use the flatten method to  convert a matrix to 1-d array
print(matrix.flatten())
#flatten will generate any arrat inti the 1d array

#transposing the matrix
print("transposed matrix is:",matrix.T)

#diagonal of a matrix
print("diagonal matrix is:",matrix.diagonal())

#dot product of a matrix
v1=np.array([10,20,30])
v2=np.array([40,50,60])
print("dot proct of two matrixs is:",np.dot(v1,v2))

#adding,subtracting and multiplying matrices
m1=np.array([[1,2,3],[4,5,6],[7,8,9]])
m2=np.array([[4,5,6],[7,8,9],[1,2,3]])
print("addition of two matrices",np.add(m1,m2))
print("subtraction of two matrices is:",np.subtract(m1,m2))
print("multiplicarion if two matrices is:",m1*m2)
#multiplication (row column wise)
print("multipication row and column wise:",np.matmul(m1,m2))

#zeros and ones
zeros=np.zeros([4,4])
print("zeros",zeros)
ones=np.ones([3,3])
print("ones:",ones)

#generating random variables
print("Random variable is:",np.random.randint(0,11,3))#generatung 3 randiom variables b/w 0 to 10
#draw 3 numbers from a normal distribution with mean 1.0 and std 2.0
print("mean and standard deviation is:",np.random.normal(1.0,2.0,6))