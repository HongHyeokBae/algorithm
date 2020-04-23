class Solution:

    # dp solution
    def combinationSum(self, candidates, target):
        """
        type candidates: List[int]
        type target: int
        rtype: List[List[int]]
        """
        sums = {}
        for i in range(1, target + 1):
            sums[i] = []

        for number in candidates:
            if number <= target:
                sums[number].append([number])

            for k in sums.keys():
                if number + k <= target:
                    for comb in sums[k]:
                        sums[number + k].append(comb + [number])
        
        return sums[target]

    # backtracking solution
    def combinationSum_sol2(self, candidates, target):
        res = []
        candidates.sort()
        self.backtrack(candidates, target, 0, [], res)
        
        return res

    def backtrack(self, nums, target, index, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return

        for i in range(index, len(nums)):
            self.backtrack(nums, target-nums[i], i, path+[nums[i]], res)   

            

