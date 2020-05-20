

class Solution:
    def longestCommonPrefix(self, strs):
        """
        type strs: List[List[str]]
        rtype: str
        """
        if not strs:
            return ""
        
        minLen = min([len(s) for s in strs])
        commonPrefix = ""
        for i in range(minLen):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if char != strs[j][i]:
                    return commonPrefix
            commonPrefix += char

        return commonPrefix
