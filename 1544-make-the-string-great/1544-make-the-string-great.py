class Solution:
    def makeGood(self, s: str) -> str:
        ans = ""
        i = 0
        while i<len(s) :
            if i<len(s)-1 and s[i]!=s[i+1] and (s[i]==s[i+1].lower() or s[i].lower()==s[i+1]):
                i += 2
            elif ans and ans[-1]!=s[i] and (ans[-1]==s[i].lower() or ans[-1].lower()==s[i]):
                ans = ans[:-1]
                i += 1
            else:
                ans += s[i]
                i += 1
        return ans