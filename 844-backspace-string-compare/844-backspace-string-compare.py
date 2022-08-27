class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i=1
        while i<len(s):
            if s[i]=="#" and i>0:
                s=s[:i-1]+s[i+1:]
                i-=1
            else:
                i+=1
        print(s)
        i=1
        while i<len(t):
            if t[i]=="#" and i>0:
                t=t[:i-1]+t[i+1:]
                i-=1
            else:
                i+=1
        print(t)
        while s and s[0]=="#":
            s=s[1:]
        while t and t[0]=="#":
            t=t[1:]
        return s==t