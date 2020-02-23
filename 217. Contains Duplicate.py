from typing import List


# Array, Hash Table
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsSet = set(nums)
        if len(nums) != len(numsSet):
            return True
        else:
            return False
        