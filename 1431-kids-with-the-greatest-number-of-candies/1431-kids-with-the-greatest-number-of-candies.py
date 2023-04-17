class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[True]*len(candies)
        m=max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies<m:
                ans[i]=False
        return ans