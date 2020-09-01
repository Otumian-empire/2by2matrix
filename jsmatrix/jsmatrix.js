// Operations on 2by2 matrices

/*
multiplication of a matrix by a constant factor

A * k = |k*a k*b|
        |k*c k*d|
*/
function multiply_matrix_by_constant(matrix, CONSTANT) {
  let product_of_matrix_and_constant = [
    [0, 0],
    [0, 0]
  ]

  product_of_matrix_and_constant[0][0] = CONSTANT * matrix[0][0]
  product_of_matrix_and_constant[0][1] = CONSTANT * matrix[0][1]
  product_of_matrix_and_constant[1][0] = CONSTANT * matrix[1][0]
  product_of_matrix_and_constant[1][1] = CONSTANT * matrix[1][1]

  return product_of_matrix_and_constant
}


/*
addition of 2 matrices

A + B = |a + e  b + f|
        |c + g  d + h|
*/
function add_matrix_to_matrix(matrix_a, matrix_b) {

  let sum_of_matrices = [
    [0, 0],
    [0, 0]
  ]

  sum_of_matrices[0][0] = matrix_a[0][0] + matrix_b[0][0]
  sum_of_matrices[0][1] = matrix_a[0][1] + matrix_b[0][1]
  sum_of_matrices[1][0] = matrix_a[1][0] + matrix_b[1][0]
  sum_of_matrices[1][1] = matrix_a[1][1] + matrix_b[1][1]

  return sum_of_matrices
}


/*
multiplication of 2 matrices

A * B = |a * e + b * g a * f + b * h |
        |c * e + d * g c * f + d * h |
*/
function multiply_matrix_by_matrix(matrix_a, matrix_b) {
  let product_of_matrices = [
    [0, 0],
    [0, 0]
  ]

  product_of_matrices[0][0] = matrix_a[0][0] * matrix_b[0][0]
  product_of_matrices[0][0] += matrix_a[0][1] * matrix_b[1][0]

  product_of_matrices[0][1] = matrix_a[0][0] * matrix_b[0][1]
  product_of_matrices[0][1] += matrix_a[0][1] * matrix_b[1][1]

  product_of_matrices[1][0] = matrix_a[1][0] * matrix_b[0][0]
  product_of_matrices[1][0] += matrix_a[1][1] * matrix_b[1][0]

  product_of_matrices[1][1] = matrix_a[1][0] * matrix_b[0][1]
  product_of_matrices[1][1] += matrix_a[1][1] * matrix_b[1][1]

  return product_of_matrices
}

module.exports = { multiply_matrix_by_constant, add_matrix_to_matrix, multiply_matrix_by_matrix }
