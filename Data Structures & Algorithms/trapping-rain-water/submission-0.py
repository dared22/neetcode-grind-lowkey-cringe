class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        for i in range(1, len(height) - 1):
            left_list = []
            right_list = []
            for l in range(i - 1, -1, -1):
                left_list.append(height[l])
            for r in range(i+1, len(height)):
                right_list.append(height[r])

            area = min(max(left_list),max(right_list)) - height[i]
            result += max(area, 0)

        return result
            
                

