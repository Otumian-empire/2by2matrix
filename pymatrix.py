# Operations on 2by2 matrices

# Given 2 matrices, A and B
A = [[1, 3],
     [5, 4]]

B = [[-2, 0],
     [3, 7]]

# let our constant be k = 5
k = 5

# kA and kB


def multiply_matrix_by_constant(CONSTANT, matrix):
    '''
    multiplication of a matrix by a constant factor
    '''
    productOfMatrixandConstant = [[0, 0], [0, 0]]

    productOfMatrixandConstant[0][0] = CONSTANT * matrix[0][0]
    productOfMatrixandConstant[0][1] = CONSTANT * matrix[0][1]
    productOfMatrixandConstant[1][0] = CONSTANT * matrix[1][0]
    productOfMatrixandConstant[1][1] = CONSTANT * matrix[1][1]

    return productOfMatrixandConstant


def addition_of_matrices(matrixA, matrixB):
    '''
    addition of matrices
    '''
    productOfMatrixandConstant = [[0, 0], [0, 0]]

    productOfMatrixandConstant[0][0] = matrixA[0][0]+ matrixB[0][0]
    productOfMatrixandConstant[0][1] = matrixA[0][1]+ matrixB[0][1]
    productOfMatrixandConstant[1][0] = matrixA[1][0]+ matrixB[1][0]
    productOfMatrixandConstant[1][1] = matrixA[1][1]+ matrixB[1][1]

    return productOfMatrixandConstant

def multiplyMatrixByConstant_of_matrices(matrixA, matrixB):
    '''
    addition of matrices
    '''
    productOfMatrixandConstant = [[0, 0], [0, 0]]

    productOfMatrixandConstant[0][0] = matrixA[0][0]+ matrixB[0][0]
    productOfMatrixandConstant[0][1] = matrixA[0][1]+ matrixB[0][1]
    productOfMatrixandConstant[1][0] = matrixA[1][0]+ matrixB[1][0]
    productOfMatrixandConstant[1][1] = matrixA[1][1]+ matrixB[1][1]

    return productOfMatrixandConstant

def print_matrix(matrix):
    print(matrix[0][0], matrix[0][1])
    print(matrix[1][0], matrix[1][1])


kA = multiply_matrix_by_constant(k, A)
kB = multiply_matrix_by_constant(k, B)

print(A)
# multiplication of matrices
