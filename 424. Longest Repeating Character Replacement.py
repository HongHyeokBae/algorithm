class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = max_count = 0
        result = 0
        
        count = {}
        for end, ch in enumerate(s):
            count[ch] = count.get(ch, 0) + 1
            max_count = max(max_count, count[ch])
            
            if end - start + 1 > max_count + k:
                count[s[start]] -= 1
                start += 1
            
            result = max(result, end - start + 1)
        return result
        
