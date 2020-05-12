

class Solution:
    def intersect(self, nums1, nums2):
        """
        type nums1: List[int]
        type nums2: List[int]
        rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        result = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                result.append(nums1[i])
                i += 1
                j += 1

        return result

    def intersect_sol2(self, nums1, nums2):
        counts = {}
        result = []

        for num in nums1:
            counts[num] = counts.get(num, 0) + 1
        
        for num in nums2:
            if num in counts and counts[num] > 0:
                result.append(num)
                counts[num] -= 1

        return result

s = Solution()
s.intersect_sol2([1,2,2,1], [2,2,1])

