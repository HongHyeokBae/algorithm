

class Solution:
    def twoSum(self, nums, target):
        """
        type nums: List[int]
        type target: int
        rtype: List[int]
        """
        nDict = {}
        
        for i, n in enumerate(nums):
            compl = target - n
            if compl in nDict and nDict[compl] != i:
                return [nDict[compl], i]
            
            nDict[n] = i

