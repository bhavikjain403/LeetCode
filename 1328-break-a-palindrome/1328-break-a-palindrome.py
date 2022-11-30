class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        l=len(palindrome)
        if l==1:
            return ""
        s=list(palindrome)
        if s[0]!="a":
            s[0]="a"
            return "".join(s)
        if s.count("a")==l:
            s[l-1]="b"
            return "".join(s)
        if l%2==0:
            for i in range(l):
                if s[i]!="a":
                    s[i]="a"
                    return "".join(s)
        flag=1
        for i in range(l):
            if s[i]!="a" and i!=l//2:
                flag=0
                s[i]="a"
                return "".join(s)
        if flag:
            s[l-1]="b"
            return "".join(s)  