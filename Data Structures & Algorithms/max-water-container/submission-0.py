class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        for i in range(len(heights)):
            for n in range(len(heights)):
                step_result = abs(i - n) * min(heights[i], heights[n])
                if step_result > result:
                    result = step_result

        return result
