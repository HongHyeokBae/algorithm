class Solution:
    def maxSlidingWindow_sol1(self, nums: List[int], k: int) -> List[int]:
        left, right, maxIdx = 0, k, 0
        maxIdx = self.getMaxIndex(nums, left, right)
        result = [nums[maxIdx]]

        while right < len(nums):
            if maxIdx == left:
                maxIdx = self.getMaxIndex(nums, left+1, right+1)
            else:
                if nums[maxIdx] < nums[right]:
                    maxIdx = right
            left += 1
            right += 1
            result.append(nums[maxIdx])
            
        return result
        
    def getMaxIndex(self, nums: List[int], left, right) -> int:
        _max = max(nums[left:right])
        while left < right:
            if nums[left] == _max:  
                return left
            left += 1

    # solution using deque
    def maxSlidingWindow_sol2(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        result = []
        
        for i in range(len(nums)):
            while q and q[0] < i-k+1:
                q.popleft()
            
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            
            q.append(i)
            if i >= k-1:
                result.append(nums[q[0]])
            
        return result
            
            
    
