from typing import List

class Solution:

    # dp solution
    # curSum is the largest sum of subarray that ends with nums[i] for nums[0:i]
    # maxSum is the largest sum of subarray for nums[0:i]
    def maxSubArray(self, nums: List[int]):
        if not nums:
            return 0
        
        curSum, maxSum = nums[0], nums[0]
        for n in nums[1:]:
            curSum = max(curSum+n, n)
            maxSum = max(maxSum, curSum)

        return maxSum