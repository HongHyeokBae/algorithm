

# Hash Table
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        
        for j in J:
            for s in S:
                if s == j:
                    count += 1
        
        return count
        