class Solution:
    def threeSum(self, nums):
        """
        type nums: List[int]
        rtype: List[List[int]]
        """
        length = len(nums)
        nums.sort()
        ans = []

        for i in range(length - 2):
            if(i == 0 or nums[i] != nums[i-1]):
                lo, hi = i + 1, length - 1
                sums = 0 - nums[i]
                while lo < hi:
                    if nums[lo] + nums[hi] == sums:
                        ans.append([nums[i], nums[lo], nums[hi]])
                        while(lo < hi and nums[lo] == nums[lo + 1]): lo += 1
                        while(lo < hi and nums[hi] == nums[hi - 1]): hi -= 1
                        lo, hi = lo + 1, hi - 1
                    elif nums[lo] + nums[hi] < sums:
                        lo += 1
                    else:
                        hi -= 1

        return ans