from typing import List

# Math
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decomp_nums = []
        
        for i in range(0, len(nums), 2):
            for j in range(nums[i]):
                decomp_nums.append(nums[i+1])
        
        return decomp_nums

                
        