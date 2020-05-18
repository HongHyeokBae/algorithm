

class Solution:
    def checkInclusion(self, s1, s2):
        """
        type s1: str
        type s2: str
        rtype: bool
        """
        if len(s1) > len(s2):
            return False

        ch_dict = {}
        l, r = 0, len(s1)
        for i in range(l, r):
            ch_dict[s1[i]] = ch_dict.get(s1[i], 0) + 1
            ch_dict[s2[i]] = ch_dict.get(s2[i], 0) - 1
        if self.checkPermutation(ch_dict):
            return True
        
        while r < len(s2):
            ch_dict[s2[r]] = ch_dict.get(s2[r], 0) - 1
            ch_dict[s2[l]] = ch_dict.get(s2[l], 0) + 1
            
            if self.checkPermutation(ch_dict):
                return True
            l += 1; r += 1
        
        return False

    def checkPermutation(self, ch_dict):
        isPermutation = True
        for v in ch_dict.values():
            if v:
                isPermutation = False
        return isPermutation
        


