class Solution:

    # dp[n] is maximum amount of money when robbed nth house lastly.
    # dp[n] = max(dp[:n - 2]) + nums[n]
    def rob(self, nums):
        dp = []
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        else:
            dp = [nums[0], nums[1]]

        for i in range(2, len(nums)):
            dp.append(max(dp[:i - 1]) + nums[i])
            print(dp)

        return max(dp)

    # The above solution used dp array with capacity N
    # use only 2 vairable so that reduce space complexity from O(N) to O(1)
    def rob_sol2(self, nums):
        if not nums:
            return 0

        prev1, prev2 = 0, 0
        for num in nums:
            tmp = prev1
            prev1 = max(prev2 + num, prev1)
            prev2 = tmp

        return max(prev1, prev2)