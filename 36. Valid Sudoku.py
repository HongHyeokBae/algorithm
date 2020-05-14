

class Solution:
    def isValidSudoku(self, board):
        """
        type board: List[List[str]]
        rtype: bool
        """
        length = 9

        for i in range(length):
            row, col, cube = set(), set(), set()
            for j in range(length):
                if board[i][j] in row:
                    return False
                if board[i][j] != '.':  row.add(board[i][j])
                
                if board[j][i] in col:
                    return False
                if board[j][i] != '.':  col.add(board[j][i])

                rowIdx = (i // 3) * 3 + (j // 3) 
                colIdx = (i % 3) * 3 + (j % 3)
                if board[rowIdx][colIdx] in cube:
                    return False
                if board[rowIdx][colIdx] != '.':    cube.add(board[rowIdx][colIdx])

        return True
