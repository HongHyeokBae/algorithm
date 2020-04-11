class Solution:

    # using divide and conquer method
    def majorityElement(self, nums):
        """
        type nums: List[int]
        rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        mid = len(nums) // 2
        left_majority = self.majorityElement(nums[:mid])
        right_majority = self.majorityElement(nums[mid:])

        left_cnt, right_cnt = 0, 0
        for n in nums:
            if left_majority != None and n == left_majority:
                left_cnt += 1
            if right_majority != None and n == right_majority:
                right_cnt += 1
        
        if max(left_cnt, right_cnt) <= mid:
            return None
        if left_cnt >= right_cnt:    
            return left_majority
        else:   
            return right_majority


    # using HashMap
    def majorityElement_sol2(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        counts = {}
        for n in nums:
            if n not in counts.keys():
                counts[n] = 1
            else:
                counts[n] += 1
                
        return max(counts, key=counts.get)