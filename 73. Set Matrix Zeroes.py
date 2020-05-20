

class Solution:
    # solution with O(m+n) space complexity and O(mm) time complexity
    def setZeroes(self, matrix):
        """
        type matrix: List[List[int]]
        rtype: None. Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return None
        
        m, n = len(matrix), len(matrix[0])
        row = [1] * m
        col = [1] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = 0
                    col[j] = 0

        for i, flag in enumerate(row):
            if not flag:
                matrix[i] = [0] * n

        for i, flag in enumerate(col):
            if not flag:
                for j in range(m):
                    matrix[j][i] = 0

    # solution with O(1) space complexity and O(mn) time complexity
    def setZeros_sol2(self, matrix):
        if not matrix:
            return None
        
        m, n = len(matrix), len(matrix[0])
        firstRow, firstCol = False, False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if j != 0:  
                        matrix[0][j] = 0    
                    else: 
                        firstCol = True
                    if i != 0:  
                        matrix[i][0] = 0    
                    else: 
                        firstRow = True

        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
                    
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        
        if firstRow:
            matrix[0] = [0] * len(matrix[0])
        
        if firstCol:
            for i in range(m):
                matrix[i][0] = 0