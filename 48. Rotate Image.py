class Solution:
    def rotate(self, matrix):
        """
        type matrix: List[List[int]]
        rtype: None, modify matrix in-place instead.
        """
        n = len(matrix)
        # offset = 0
        # while offset < (n // 2):
        #     for i in range(offset, n - offset - 1):
        #         matrix[offset][i], matrix[i][-(offset+1)] = \
        #                                         matrix[i][-(offset+1)], matrix[offset][i]
        #         matrix[offset][i], matrix[n-(offset+1)][-(i+1)] = \
        #                                         matrix[n-(offset+1)][-(i+1)], matrix[offset][i]
        #         matrix[offset][i], matrix[-(i+1)][offset] = \
        #                                         matrix[-(i+1)][offset], matrix[offset][i]
        
        #     offset += 1

        # More simple Solution
        # arr[~i] == arr[n-i-1]
        for i in range(n // 2):
            for j in range(i, n-i-1):
                matrix[i][j], matrix[j][~i], matrix[~i][~j], matrix[~j][i] = \
                    matrix[~j][i], matrix[i][j], matrix[j][~i], matrix[~i][~j]