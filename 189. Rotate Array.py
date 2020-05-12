class Solution:
    def rotate(self, nums, k):
        """
        type nums: List[int]
        type k: int
        rtype: None. Do not return anything, modify nums in-place instead.
        """
        while k:
            temp = nums[-1]
            for i in range(len(nums) - 1, 0, -1):
                nums[i] = nums[i - 1]
            nums[0] = temp
            k -= 1

    def rotate_sol2(self, nums, k):
        n = len(nums)
        temp = nums[:n-k]
        nums[:k] = nums[n-k:]
        nums[k:] = temp

    def rotate_sol3(self, nums, k):
        nums.reverse()
        k = k % len(nums)

        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

        # for i in range(k // 2):
        #     nums[i], nums[k-1-i] = nums[k-1-i], nums[i]

        # for i in range(k, (len(nums) + k) // 2):
        #     nums[i], nums[~(i-k)] = nums[~(i-k)], nums[i]

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate_sol4(self, nums, k):
        n = len(nums)
        k = k % len(nums)
        
        start = count = 0
        while count < n:
            curr, prev = start, nums[start]
            while True:
                next_idx = (curr + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                curr = next_idx
                count += 1

                if start == curr:
                    break
            start += 1