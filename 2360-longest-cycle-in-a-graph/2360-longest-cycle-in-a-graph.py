class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        ans=-1
        n=len(edges)
        length=1
        seen=[0]*n
        for i in range(n):
            if seen[i]==0:
                cyc=length
                temp=i
                while temp!=-1 and seen[temp]==0:
                    seen[temp]=length
                    length+=1
                    temp=edges[temp]
                if temp!=-1 and seen[temp]>=cyc:
                    ans=max(ans,length-seen[temp])
        return ans