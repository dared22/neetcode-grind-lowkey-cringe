class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
            l,r = 0, k
            max_list = []
            while r <= len(nums):
                max_list.append(max(nums[l:r]))
                l += 1
                r += 1
            return max_list