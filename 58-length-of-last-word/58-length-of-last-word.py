class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans=0
        l=len(s)
        while s[l-1]==" ":
            l-=1
        for i in range(l-1,-1,-1):
            if s[i]==" ":
                return ans
            ans+=1
        return ans