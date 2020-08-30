class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        start, result = 0, 1
        
        for end in range(1, len(A)):
            comp = self.cmp(A[end-1], A[end])
            
            if comp == 0:
                start = end
            elif end == len(A) - 1 or comp * self.cmp(A[end], A[end+1]) != -1:
                result = max(result, end - start + 1)
                start = end
                
        return result
    
    def cmp(self, a, b):
        return (a > b) - (a < b)
                
