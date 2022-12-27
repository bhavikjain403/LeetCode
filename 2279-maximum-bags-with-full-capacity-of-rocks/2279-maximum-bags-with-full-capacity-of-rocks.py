class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n=len(rocks)
        diff=[0]*n
        for i in range(n):
            diff[i]=capacity[i]-rocks[i]
        diff.sort()
        ans=0
        for i in diff:
            if i<=additionalRocks:
                ans+=1
                additionalRocks-=i
            if additionalRocks<i:
                return ans
        return ans