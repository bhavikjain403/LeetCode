class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 1
        x,y,z=0,1,1
        ans=0
        for i in range(3,n+1):
            ans=x+y+z
            x,y=y,z
            z=ans
        return ans