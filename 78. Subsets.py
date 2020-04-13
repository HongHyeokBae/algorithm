class Solution:

    # Recursion
    def subsets(self, nums):
        """
        type nums: List[int]
        rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        if len(nums) == 1:
            return [[], nums]

        mid = len(nums) // 2
        left_subsets = self.subsets(nums[:mid])
        right_subsets = self.subsets(nums[mid:])

        subsets = []
        for elm1 in left_subsets:
            for elm2 in right_subsets:
                subsets.append(elm1 + elm2)
        
        return subsets

    # Backtracking
    def subsets_sol2(self, nums):
        def backtrack(first = 0, curr = []):
            # if the combination is done
            if k == len(curr):
                return output.append(curr[:])
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integer to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
    
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()

        return output

    # Lexiographic(Binary Sorted) Subsets
    
    # The idea is that we map each subset to a bitmask of length n, 
    # where 1 on the ith position in bitmask means the presence of nums[i] in the subset, 
    # and 0 means its absence.
    def subsets_sol3(self, nums):
        n = len(nums)
        output = []

        for i in range(2**n, 2**(n+1)):
            bitmask = bin(i)[3:]

            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])

        return output


s = Solution()
ans = s.subsets_sol3([1, 2, 3])
print(ans)
        
        
