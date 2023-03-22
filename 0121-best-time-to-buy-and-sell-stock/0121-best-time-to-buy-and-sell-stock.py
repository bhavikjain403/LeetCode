class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n,mini=len(prices),prices[0]
        ans=0
        for i in range(1,n):
            if prices[i]>mini:
                ans=max(ans,prices[i]-mini)
            else:
                mini=prices[i]
        return ans