

class Solution:
    def minWindow(self, s, t):
        """
        type s: str
        type t: str
        rtype: str
        """
        charInT, result = {}, ""
        for ch in t:
            charInT[ch] = charInT.get(ch, 0) + 1
        
        count = len(t)
        slow, fast = 0, 0
        
        while fast < len(s):
            # grow window until window contains all the characters in T
            if s[fast] in charInT:
                charInT[s[fast]] -= 1
                if charInT[s[fast]] >= 0:
                    count -= 1  
            fast += 1
            
            if count == 0:
                # shirnk window to minimum size
                while s[slow] not in charInT or charInT[s[slow]] < 0:
                    if s[slow] in charInT:
                        charInT[s[slow]] += 1
                    slow += 1
                
                # update the result if current substring is shorter than previous one
                if not result or len(s[slow:fast]) < len(result):  
                    result = s[slow:fast]
                
                # move slow pointer by 1
                if s[slow] in charInT:
                    charInT[s[slow]] += 1
                    count += 1
                slow += 1
        
        return result