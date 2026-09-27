class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        left = 0
        for right in range(1, len(prices)):
            profit = prices[right] - prices[left]
            if profit < 0:
                left = right
            else:
                result = max(result, profit)

        return result