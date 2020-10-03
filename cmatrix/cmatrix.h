// Operations on 2by2 matrices
#ifndef CMATRIX_H
#define CMATRIX_H


/*
multiplication of a matrix by a constant factor
A * k = |k*a k*b|
        |k*c k*d|
*/
int** multiply_matrix_by_constant(int[2][2] matrix, int CONSTANT);


/*
addition of 2 matrices
A + B = |a+e b+f|
        |c+g d+h|
*/
int** add_matrix_to_matrix(int[2][2] matrix_a, int[2][2] matrix_b);


/*
multiplication of 2 matrices
A * B = |a*e + b*g  a*f + b*h|
        |c*e + d*g  c*f + d*h|
*/
int** multiply_matrix_by_matrix(int[2][2] matrix_a, int[2][2] matrix_b);


#endif
