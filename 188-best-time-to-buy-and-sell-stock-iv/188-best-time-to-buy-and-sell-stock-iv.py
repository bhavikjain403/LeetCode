class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        min_price = [float("inf")] * (k + 1)
        max_profit = [0] * (k + 1)
        for price in prices:
            for i in range(1, k + 1):
                min_price[i] = min(min_price[i], price - max_profit[i-1])
                max_profit[i] = max(max_profit[i], price - min_price[i])
        return max_profit[k]