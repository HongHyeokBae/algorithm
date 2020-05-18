import collections

class Solution:
    def isAnagram(self, s, t):
        """
        type s: str
        type t: str
        rtype: bool
        """
        charInT = {}
        
        for ch in t:
            charInT[ch] = charInT.get(ch, 0) + 1
        
        for ch in s:
            if ch not in charInT:
                return False
            else:
                charInT[ch] -= 1

        for v in charInT.values():
            if v != 0:
                return False
            
        return True

    def isAnagram_sol2(self, s, t):
        sCounter = collections.Counter(s)
        tCounter = collections.Counter(t)
        return sCounter == tCounter