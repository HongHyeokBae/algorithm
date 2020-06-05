from collections import deque

class Solution:
    def climbStairs(self, n):
        """
        type n: int
        rtype: int
        """
        path = {0: 1}
        for i in range(1, n+1):
            path[i] = path.get(i-1, 0) + path.get(i-2, 0)
            print(path)

        return path[n]

    def climbStairs_sol2(self, n):
        prev, pprev = 1, 1
        for _ in range(n):
            pprev, prev = prev, prev + pprev

        return pprev