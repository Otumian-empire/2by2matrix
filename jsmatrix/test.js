const assert = require('assert')
const {
  multiply_matrix_by_constant,
  multiply_matrix_by_matrix,
  add_matrix_to_matrix
} = require('./jsmatrix')


describe('TestJsMatrix', () => {

  describe('test multiply_matrix_by_constant', () => {
    const A = [
      [1, 3],
      [5, 4]
    ]

    const result = multiply_matrix_by_constant(A, 5) 

    it('returns a matrix of the product of a matrix and a constant', () => {
      assert.equal(result[0][0], 5)
      assert.equal(result[0][1], 15)
      assert.equal(result[1][0], 25)
      assert.equal(result[1][1], 20)
    })
  })

  describe('test multiply_matrix_by_matrix', () => {
    const A = [
        [1, 3],
        [5, 4]
      ],
      B = [
        [2, -1],
        [6, 4]
      ]

      const result = multiply_matrix_by_matrix(A, B)

    it('returns the product of 2 matrices', () => {
      assert.equal(result[0][0], 20)
      assert.equal(result[0][1], 11)
      assert.equal(result[1][0], 34)
      assert.equal(result[1][1], 11)

    })
  })

  describe('test add_matrix_to_matrix', () => {
    const A = [
        [1, 3],
        [5, 4]
      ],
      B = [
        [2, -1],
        [6, 4]
      ]

      const result = add_matrix_to_matrix(A, B)

    it('returns the sum of two matrices', () => {
      assert.equal(result[0][0], 3)
      assert.equal(result[0][1], 2)
      assert.equal(result[1][0], 11)
      assert.equal(result[1][1], 8)
    })
  })

})
