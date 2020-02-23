

# Hash Table, Bit Manipulation
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sets = set()
        for n in nums:
            if n in sets:
                sets.remove(n)
            else:
                sets.add(n)
                
        return sets.pop()
