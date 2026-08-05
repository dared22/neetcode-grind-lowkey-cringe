class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in visited.keys():
                return sorted(list((i, visited[difference])))
            visited[nums[i]] = i


