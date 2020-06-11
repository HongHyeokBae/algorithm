import collections

class Solution:
    # if nums is [1,1,2], then
    # 1(first 1) + permutations of [1,2] and 1(second 1) + permutations of [1,2] will be the same
    # So, skip the used prefix
    def permuteUnique(self, nums):
        """
        type nums: List[int]
        rtype: List[List[int]]
        """
        permutes = []
        self.permute(nums, [], permutes)
        
        return permutes

    def permute(self, nums, path, permutes):
        if not nums:
            permutes.append(path)
        
        perfixes = set()
        for i in range(len(nums)):
            if nums[i] not in perfixes:
                self.permute(nums[:i] + nums[i+1:], path + [nums[i]], permutes)
                perfixes.add(nums[i])
                
    # P([1,1,2]) -> [1 + P({1: 1, 2: 1})] + [2 + P({1: 2})]
    def permuteUnique_sol2(self, nums):
        counts = dict(collections.Counter(nums))
        result = []
        self.permutes(counts, [], len(nums), result)
        return result

    def permutes(self, counts, prefix, length, result):
        if len(prefix) == length:
            result.append(prefix)
        
        for num, count in counts.items():
            if count > 0:
                counts[num] -= 1
                self.permutes(counts, prefix + [num], length, result)
                counts[num] += 1


s = Solution()
print(s.permuteUnique_sol2([1,1,2]))
