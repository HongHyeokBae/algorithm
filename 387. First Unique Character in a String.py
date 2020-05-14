

class Solution:
    def firstUniqChar(self, s):
        """
        type s: str
        rtype: int
        """
        res, dic = -1, {}
        i_max = len(s)
        
        for i, ch in enumerate(s):
            if ch in dic:
                dic[ch] = i_max
            else:
                dic[ch] = i
        
        print(dic)
        res = min(dic.values())
        return res if res < i_max else -1