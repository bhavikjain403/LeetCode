class Solution:
    def partitionString(self, s: str) -> int:
        ans=0
        l=len(s)
        if l==1:
            return 1
        i=0
        while i<l:
            x=set()
            for j in range(i,l):
                if s[j] not in x:
                    x.add(s[j])
                else:
                    ans+=1
                    break
            i=j
            if i==l-1:
                ans+=1
                break
        return ans