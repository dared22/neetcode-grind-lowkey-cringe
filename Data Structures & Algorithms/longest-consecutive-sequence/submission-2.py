class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        new_set = set(nums)
        streak = 0
        for num in nums:
            if num - 1 not in nums:
                streak, curr = 0, num
                while num in new_set:
                    streak += 1
                    num += 1
            if streak > res:
                res = streak
        return res


