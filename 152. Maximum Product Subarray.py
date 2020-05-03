class Solution:
    def maxProduct(self, nums):
        """
        type nums: List[int]
        rtype: int
        """
        maxProduct = nums[0]
        curMax, curMin = nums[0], nums[0]

        for n in nums[1:]:
            if n < 0:
                curMax, curMin = curMin, curMax

            curMax = max(curMax * n, n)
            curMin = min(curMin * n, n)
            maxProduct = max(curMax, maxProduct)

        return maxProduct