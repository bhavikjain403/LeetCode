class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans,i,n=0,0,len(s)
        while i<n:
            l,r=0,0
            while i<n:
                if s[i]=="L":
                    l+=1
                else:
                    r+=1
                if l==r:
                    ans+=1
                    break
                i+=1
            i+=1
        return ans