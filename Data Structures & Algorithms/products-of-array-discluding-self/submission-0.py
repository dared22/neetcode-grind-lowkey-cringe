class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        i = 0
        while i < len(nums):
            curr = 1
            for j in range(len(nums)):
                if j != i:
                    curr *= nums[j]
            res.append(curr)
            i += 1
        return res
