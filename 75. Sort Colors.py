class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        start, end = 0, len(nums) - 1
        
        for i in range(len(nums)):
            print(nums, start, end)
            while i < end and nums[i] == 2:
                nums[i] = nums[end]
                nums[end] = 2
                end -= 1
            while i > start and nums[i] == 0:
                nums[i] = nums[start]
                nums[start] = 0
                start += 1

        print(nums)

s = Solution()
s.sortColors([1, 2, 0])
            