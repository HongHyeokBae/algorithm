

class Solution:
    def removeDuplicates(self, nums):
        """
        type nums: List[int]
        rtype: int
        """
        if not nums:
            return 0
        
        last_num = nums[0]
        length = 1
        for i in range(1, len(nums)):
            if nums[i] != last_num:
                nums[length] = nums[i]
                last_num = nums[i]
                length += 1
        
        return length