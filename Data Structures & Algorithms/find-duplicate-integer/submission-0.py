class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        int_set = set()
        for num in nums:
            if num not in int_set:
                int_set.add(num)
            elif num in int_set:
                return num
                

