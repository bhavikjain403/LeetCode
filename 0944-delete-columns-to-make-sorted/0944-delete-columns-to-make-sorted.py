class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m=len(strs)
        if m<2:
            return 0
        l=len(strs[0])
        i=0
        ans=0
        while i<l:
            for j in range(m-1):
                if strs[j][i]>strs[j+1][i]:
                    ans+=1
                    break
            i+=1
        return ans