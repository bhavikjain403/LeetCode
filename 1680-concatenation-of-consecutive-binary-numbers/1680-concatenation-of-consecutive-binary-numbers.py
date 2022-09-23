class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans=""
        for i in range(1,n+1):
            ans+=bin(i).replace("0b","")
        ans=int(ans,2)%(10**9+7)
        return ans