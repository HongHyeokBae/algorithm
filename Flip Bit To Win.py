

class Solution:
    def flipBit(self, n):
        """
        type n: int
        rtype: int
        """
        prevLen, currLen = 0, 0
        maxLen = 1
        while n:
            if n & 1:
                currLen += 1
            else:
                prevLen = currLen if n & 2 else 0
                currLen = 0
            maxLen = max(prevLen + currLen + 1, maxLen)
            n >>= 1
        
        return maxLen