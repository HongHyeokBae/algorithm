

class Solution:
    def solveNQueens(self, n):
        """
        type n: int
        rtype: List[List[str]]
        """
        result = []
        self.placeQueens(0, [0] * n, n, result)

        for res in result:
            print(res)

    def placeQueens(self, row, columns, n, result):
        if row == n:
            res = [['.'] * n for _ in range(n)]
            for r, c in enumerate(columns):
                res[r][c] = 'Q'
            resStr = []
            for i in range(n):
                resStr.append(''.join(res[i]))
            
            result.append(resStr)

        else:
            for col in range(n):
                if self.checkValid(row, col, columns, n):
                    columns[row] = col
                    self.placeQueens(row+1, columns, n, result)


    def checkValid(self, row, col, columns, n):
        
        for placedRow, placedCol in enumerate(columns):
            if row <= placedRow:
                continue
            
            if col == placedCol:
                return False
            
            rowDist = row - placedRow
            colDist = abs(col - placedCol)
            
            if rowDist == colDist:
                return False

        return True