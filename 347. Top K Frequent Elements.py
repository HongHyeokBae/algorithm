from collections import Counter
import heapq

class Solution:

    # heap solution
    # Time Complexity: O(nlogk)
    def topKFrequent(self, nums, k):
        """
        type nums: List[int]
        type k: int
        rtype: List[int]
        """
        freq = Counter(nums)

        return heapq.nlargest(k, freq.keys(), key=freq.get)

    # bucket sort
    # Time Complexity: O(n)
    def topKFrequent_sol2(self, nums, k):
        freq = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]

        for key, count in freq.items():
            bucket[count].append(key)
        
        res = []
        for i in range(len(bucket) - 1, -1, -1):
            res.extend(bucket[i])
            if len(res) >= k:   
                break
                
        return res
        

    
