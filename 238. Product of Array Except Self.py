

class Solution:
    def productExceptSelf(self, nums):
        """
        type nums: List[int]
        rtype: List[int]
        """
        l, r = [0] * len(nums), [0] * len(nums)
        l[0], r[-1] = 1, 1
        
        for i in range(0, len(nums) - 1):
            l[i+1] = l[i] * nums[i]
        
        for i in range(len(nums) - 1, 0, -1):
            r[i - 1] = r[i] * nums[i]
        
        result = []
        for i in range(len(nums)):
            result.append(l[i] * r[i])
            
        return result
        