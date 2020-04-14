class Solution:
    def minPathSum(self, grid):
        """
        type grid: List[List[int]]
        rtype: int
        """
        if not grid:
            return 0
        
        n = len(grid)
        m = len(grid[0])
        table = [[0] * m for _ in range(n)]
        table[0][0] = grid[0][0]
        for i in range(1, m):
            table[0][i] = table[0][i-1] + grid[0][i]
        for i in range(1, n):
            table[i][0] = table[i-1][0] + grid[i][0]

        for i in range(1, n):
            for j in range(1, m):
                table[i][j] = min(table[i][j-1], table[i-1][j]) + grid[i][j]

        return table[n-1][m-1]
        
         

s = Solution()
p = s.minPathSum([
  [1,3,1]
])
print(p)

