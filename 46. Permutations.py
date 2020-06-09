from collections import deque

class Solution:
    def permute(self, nums):
        """
        type nums: List[int]
        rtype: List[List[int]]
        """
        if not nums:
            return []
        
        permutes = [[nums[0]]]

        for i in range(1, len(nums)):
            temp = []
            for permute in permutes:
                for j in range(len(permute) + 1):
                    per = []
                    per.extend(permute[:j])
                    per.append(nums[i])
                    per.extend(permute[j:])
                    temp.append(per)

            permutes = temp
                        
        return permutes

    # permutations(a1, a2, a3) = {a1 + p(a2, a3)} + {a2 + p(a1, a3)} + {a3 + p(a1, a2)}
    def permute_sol2(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)

        
