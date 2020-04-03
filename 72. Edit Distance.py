class Solution:
    # recursive solution
    def minDistance(self, word1: str, word2: str):
        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])

        insert = self.minDistance(word1, word2[1:])
        remove = self.minDistance(word1[1:], word2)
        replace = self.minDistance(word1[1:], word2[1:])

        return min(insert, remove, replace) + 1

    # memoization
    def minDistance2(self, word1, word2):
        memo = {}
        return self.recur(word1, word2, 0, 0, memo)
    
    def recur(self, word1, word2, i, j, memo):
        if i == len(word1) and j == len(word2):
            return 0
        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i

        if (i, j) not in memo:
            if word1[i] == word2[j]:
                ans = self.recur(word1, word2, i + 1, j + 1, memo)
            else:
                insert = self.recur(word1, word2, i, j + 1, memo)
                remove = self.recur(word1, word2, i + 1, j, memo)
                replace = self.recur(word1, word2, i + 1, j + 1, memo)
                ans = min(insert, remove, replace) + 1

            memo[(i, j)] = ans
        return memo[(i, j)] 

    # dynamic programming
    def minDistance3(self, word1, word2):
        n = len(word1)
        m = len(word2)
        table = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            table[0][i] = i
        for j in range(n + 1):
            table[j][0] = j

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[j - 1] == word2[i - 1]:
                    table[i][j] = table[i - 1][j - 1]
                else:
                    table[i][j] = min(table[i-1][j-1], table[i-1][j], table[i][j-1]) + 1

        return table[m][n] 
