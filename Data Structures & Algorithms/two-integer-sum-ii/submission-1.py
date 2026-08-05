class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for num in numbers:
            end  = len(numbers) - 1
            while numbers.index(num) < end:
                if num + numbers[end] == target:
                    return [numbers.index(num) + 1, end + 1]
                end -=1

        return False