class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not s:
            return 0
        g.sort()
        s.sort()
        j=0
        ans=0
        l=len(s)
        for i in g:
            while j<l-1 and s[j]<i:
                j+=1
            if j<l and s[j]>=i:
                ans+=1
            j+=1
        return ans