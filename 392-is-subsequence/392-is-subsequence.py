class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)-1
        m = len(t)-1
        while n>=0 and m>=0:
            if s[n]==t[m]:
                n-=1
                m-=1
            else:
                m-=1
        if n>=0:
            return False
        return True