

class Solution:

    # Time complexity: O(n)
    # Space complexity: O(n)
    def findDisappearedNumbers_sol1(self, nums):
        """
        type nums: List[int]
        rtype: List[int]
        """
        counts = [i for i in range(1, len(nums)+1)]
        result = []

        for num in nums:
            counts[num - 1] = -1
        
        for count in counts:
            if count != -1:
                result.append(count)
                
        return result


    # Time complexity: O(n)
    # Space complexity: O(1)
    def findDisappearedNumbers_sol2(self, nums):
        for i in range(len(nums)):
            num = abs(nums[i])
            nums[num - 1] = -abs(nums[num - 1])
            
        return [i+1 for i in range(len(nums)) if nums[i] > 0]
        
        