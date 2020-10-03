#include "cmatrix.h"

int** multiply_matrix_by_constant(int** matrix, int CONSTANT) {

    int** product_of_matrix_and_constant = { {0, 0}, {0, 0} };

    product_of_matrix_and_constant[0][0] = CONSTANT * matrix[0][0];
    product_of_matrix_and_constant[0][1] = CONSTANT * matrix[0][1];
    product_of_matrix_and_constant[1][0] = CONSTANT * matrix[1][0];
    product_of_matrix_and_constant[1][1] = CONSTANT * matrix[1][1];

    return product_of_matrix_and_constant;
}



int** add_matrix_to_matrix(int** matrix_a, int** matrix_b) {
    int** sum_of_matrices = { {0, 0}, {0, 0} };

    sum_of_matrices[0][0] = matrix_a[0][0] + matrix_b[0][0];
    sum_of_matrices[0][1] = matrix_a[0][1] + matrix_b[0][1];
    sum_of_matrices[1][0] = matrix_a[1][0] + matrix_b[1][0];
    sum_of_matrices[1][1] = matrix_a[1][1] + matrix_b[1][1];

    return sum_of_matrices;
}



int** multiply_matrix_by_matrix(int** matrix_a, int** matrix_b) {
    int** product_of_matrices = { {0, 0}, {0, 0} };

    product_of_matrices[0][0] =  matrix_a[0][0] * matrix_b[0][0];
    product_of_matrices[0][0] += matrix_a[0][1] * matrix_b[1][0];

    product_of_matrices[0][1] =  matrix_a[0][0] * matrix_b[0][1];
    product_of_matrices[0][1] += matrix_a[0][1] * matrix_b[1][1];

    product_of_matrices[1][0] =  matrix_a[1][0] * matrix_b[0][0];
    product_of_matrices[1][0] += matrix_a[1][1] * matrix_b[1][0];

    product_of_matrices[1][1] =  matrix_a[1][0] * matrix_b[0][1];
    product_of_matrices[1][1] += matrix_a[1][1] * matrix_b[1][1];

    return product_of_matrices;
}
