

class Solution:
    def reverseString(self, s):
        """
        type s: List[str]
        rtype: None
        """
        for i in range(len(s) // 2):
            s[i], s[~i] = s[~i], s[i]