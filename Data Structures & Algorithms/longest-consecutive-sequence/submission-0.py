class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        new_set = set(nums)

        for num in nums:
            streak, curr = 0, num
            while num in new_set:
                streak += 1
                num += 1
            if streak > res:
                res = streak
        return res


