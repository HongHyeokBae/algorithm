from typing import List


# Hash Table, Two Pointers, Binary Search, Sort
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        interSet = set()
        nums1Set = set(nums1)
        for n in nums2:
            if n in nums1Set:
                interSet.add(n)
        
        return list(interSet)