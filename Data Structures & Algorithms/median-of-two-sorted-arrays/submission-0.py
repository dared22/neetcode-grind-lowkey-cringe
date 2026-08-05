class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        both = sorted(nums1 + nums2)
        n = len(both)
        
        if n % 2 == 0:
            idx1 = (n - 1) // 2
            idx2 = n // 2
            return (both[idx1] + both[idx2]) / 2.0
        else:
            idx = n // 2
            return float(both[idx])

        