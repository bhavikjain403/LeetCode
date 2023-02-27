class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        binx,biny=bin(x).replace('0b','0'),bin(y).replace('0b','0')
        lx,ly=len(binx),len(biny)
        ans=0
        i,j=lx-1,ly-1
        while i>=0 and j>=0:
            ans+=binx[i]!=biny[j]
            i-=1
            j-=1
        while i>=0:
            ans+=binx[i]=="1"
            i-=1
        while j>=0:
            ans+=biny[j]=="1"
            j-=1
        return ans