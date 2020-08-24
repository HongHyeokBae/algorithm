class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        left, right = 0, 0
        subs, longest = set(), 0
        
        while right < len(s):
            if s[right] not in subs:
                subs.add(s[right])
                right += 1
                longest = max(longest, right - left)
            else:
                subs.remove(s[left])
                left += 1
        
        return longest
        
