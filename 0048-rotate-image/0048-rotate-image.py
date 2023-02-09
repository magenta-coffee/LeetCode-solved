class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matrix_len = len(matrix)
        half_len = matrix_len//2
        ma_in = matrix_len - 1
        for i in range(half_len):
            re_len = ma_in - i
            for j in range(i, re_len):
                temp = matrix[i][j]
                matrix[i][j] = matrix[ma_in - j][i]
                matrix[ma_in - j][i] = matrix[ma_in - i][ma_in - j]
                matrix[ma_in - i][ma_in - j] = matrix[j][ma_in - i]
                matrix[j][ma_in - i] = temp
                