class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell,prev_sell=float('inf'),0,0
        for cur in prices:
            buy,sell,prev_sell=min(buy,cur-prev_sell),max(cur-buy,sell),sell
        return sell