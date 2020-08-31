# Operations on 2by2 matrices


def multiply_matrix_by_constant(matrix, CONSTANT):
    '''
    multiplication of a matrix by a constant factor

    A * k = |k*a k*b|
            |k*c k*d|
    '''
    product_of_matrix_and_constant = [[0, 0], [0, 0]]

    product_of_matrix_and_constant[0][0] = CONSTANT * matrix[0][0]
    product_of_matrix_and_constant[0][1] = CONSTANT * matrix[0][1]
    product_of_matrix_and_constant[1][0] = CONSTANT * matrix[1][0]
    product_of_matrix_and_constant[1][1] = CONSTANT * matrix[1][1]

    return product_of_matrix_and_constant


def add_matrix_to_matrix(matrix_a, matrix_b):
    '''
    addition of 2 matrices

    A + B = |a+e b+f|
            |c+g d+h|
    '''
    sum_of_matrices = [[0, 0], [0, 0]]

    sum_of_matrices[0][0] = matrix_a[0][0] + matrix_b[0][0]
    sum_of_matrices[0][1] = matrix_a[0][1] + matrix_b[0][1]
    sum_of_matrices[1][0] = matrix_a[1][0] + matrix_b[1][0]
    sum_of_matrices[1][1] = matrix_a[1][1] + matrix_b[1][1]

    return sum_of_matrices


def multiply_matrix_by_matrix(matrix_a, matrix_b):
    '''
    multiplication of 2 matrices

    A * B = |a*e + b*g  a*f + b*h|
            |c*e + d*g  c*f + d*h|
    '''
    product_of_matrices = [[0, 0], [0, 0]]

    product_of_matrices[0][0] = matrix_a[0][0] * matrix_b[0][0]
    product_of_matrices[0][0] += matrix_a[0][1] * matrix_b[1][0]

    product_of_matrices[0][1] = matrix_a[0][0] * matrix_b[0][1]
    product_of_matrices[0][1] += matrix_a[0][1] * matrix_b[1][1]

    product_of_matrices[1][0] = matrix_a[1][0] * matrix_b[0][0]
    product_of_matrices[1][0] += matrix_a[1][1] * matrix_b[1][0]

    product_of_matrices[1][1] = matrix_a[1][0] * matrix_b[0][1]
    product_of_matrices[1][1] += matrix_a[1][1] * matrix_b[1][1]

    return product_of_matrices


# Uncomment these and run this script to see how the matrices are displayed

# def print_matrix(matrix):
#     '''
#     prints a mtrix

#     |a b|
#     |c d|
#     '''
#     print('|', matrix[0][0], matrix[0][1], '|')
#     print('|', matrix[1][0], matrix[1][1], '|', end='\n\n')


# # Given 2 matrices, A and B
# A = [[1, 3],
#      [5, 4]]

# B = [[-2, 0],
#      [3, 7]]

# # let our constant be k = 5
# k = 5

# # kA and kB
# kA = multiply_matrix_by_constant(k, A)
# kB = multiply_matrix_by_constant(k, B)


# # addition of matrices
# A_plus_B = add_matrix_to_matrix(A, B)
# print_matrix(A_plus_B)

# # multiplication of matrices
# A_times_B = multiply_matrix_by_matrix(A, B)
# print_matrix(A_times_B)
