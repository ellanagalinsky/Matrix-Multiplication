# Each element will act as a row of the matrix
# We will work with a 3 x 4 matrix and a 4 x 3 matrix
# When multiplying matrices, the column of the first element must = the row of the second element

x = [[12,5,1,0],
    [1,3,5,4],
    [0,2,1,3]]

y = [[3,2,1],
    [1,4,5],
    [3,9,10],
    [1,4,5]]

# The dimension of x is a x b
# The dimension of y is b x c
# The resulting dimension will be a x c = 3 x 3


matrixResult = [[sum(a*b for a,b in zip(x_row, y_col)) for y_col in zip(*y)] for x_row in x]

for r in matrixResult:
    print (r)