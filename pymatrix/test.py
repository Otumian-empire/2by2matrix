import unittest
from pymatrix import multiply_matrix_by_constant, multiply_matrix_by_matrix, add_matrix_to_matrix


class TestPyMatrix(unittest.TestCase):

    def test_multiply_matrix_by_constant(self):
        A = [[1, 3],
             [5, 4]]

        self.assertEqual(
            multiply_matrix_by_constant(A, 5), [[5, 15], [25, 20]])

    def test_multiply_matrix_by_matrix(self):
        A = [[1, 3],
             [5, 4]]
        B = [[2, -1],
             [6, 4]]
        self.assertEqual(
            multiply_matrix_by_matrix(A, B), [[20, 11], [34, 11]])

    def test_add_matrix_to_matrix(self):
        A = [[1, 3],
             [5, 4]]
        B = [[2, -1],
             [6, 4]]
        self.assertEqual(
            add_matrix_to_matrix(A, B), [[3, 2], [11, 8]])

if __name__ == "__main__":
    unittest.main()
