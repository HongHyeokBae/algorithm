import collections

class Solution:
    def findAnagrams(self, s, p):
        """
        type s: str
        type p: str
        rtype: List[int]
        """
        if len(s) < len(p):
            return None
        
        hash_ = dict(collections.Counter(p))
        left, right, count = 0, 0, len(p)
        result = []
        
        while right < len(s):
            if s[right] in hash_:
                hash_[s[right]] -= 1
                if hash_[s[right]] >= 0:
                    count -= 1
                    
            if count == 0:
                result.append(left)
                
            if right - left == len(p) - 1:
                if s[left] in hash_:
                    if hash_[s[left]] >= 0:
                        count += 1
                    hash_[s[left]] += 1
                left += 1
            right += 1
                
        return result