class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest, curr, best = prices[0], 0, 0
        for r in range(len(prices)):
            curr = prices[r] - lowest
            best = max(curr, best)
            lowest = min(prices[r], lowest)
        return best