

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        min_, max_ = float('inf'), float('-inf')
        
        flag = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                flag = True
            if flag:
                min_ = min(min_, nums[i+1])
                
        flag = False
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] < nums[i-1]:
                flag = True
            if flag:
                max_ = max(max_, nums[i-1])
                
        l, r = 0, len(nums) - 1
        while l < len(nums):
            if min_ < nums[l]:
                break
            l += 1
            
        while r >= 0:
            if max_ > nums[r]:
                break
            r -= 1
        
        return r - l + 1 if r > l else 0