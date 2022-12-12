class Solution:
    def climbStairs(self, n: int) -> int:
        a=[[1]]
        for i in range(n):
            a.append([1])
            a[0].append(0)
        for i in range(1,n+1):
            for j in range(0,i):
                a[i].append(a[i-1][j]+a[i-1][j+1])
            a[i].append(0)
        i,j=n,0
        ans=0
        while i>=j:
            ans+=a[i][j]
            i-=1
            j+=1
        return ans