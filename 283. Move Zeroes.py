class Solution:
    def moveZeroes(self, nums):
        """
        type nums: List[int]
        Do not return anything, modify nums in-place instead.
        """
        i, pos = 0, -1
        while i < len(nums):
            if nums[i] == 0:
                if pos == -1: pos = i
                while i < len(nums) - 1 and nums[i] == 0:
                    i += 1           
            
            if nums[i] != 0 and pos != -1:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1
            i += 1

    def moveZeroes_sol2(self, nums):
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1