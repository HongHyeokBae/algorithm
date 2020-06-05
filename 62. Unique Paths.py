

class Solution:
    def uniquePaths(self, m, n):
        """
        type m: int
        type n: int
        rtype: int
        """
        paths = [[0] * m for _ in range(n)]
        
        for i in range(m):
            paths[0][i] = 1
        for i in range(n):
            paths[i][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                paths[i][j] = paths[i-1][j] + paths[i][j-1]
                self.printArr(paths, n)
                print()
        
        return paths[-1][-1]
    def printArr(self, arr, n):
        for i in range(n):
            print(arr[i])