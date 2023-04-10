class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        n=len(s)
        for i in range(n):
            if s[i]=="(":
                a.append("(")
            elif s[i]==")" and len(a)==0:
                return False
            elif s[i]==")" and a[-1]=="(":
                a.pop()
            elif s[i]==")" and a[-1]!="(":
                return False
            elif s[i]=="{":
                a.append("{")
            elif s[i]=="}" and len(a)==0:
                return False
            elif s[i]=="}" and a[-1]=="{":
                a.pop()
            elif s[i]=="}" and a[-1]!="{":
                return False
            elif s[i]=="[":
                a.append("[")
            elif s[i]=="]" and len(a)==0:
                return False
            elif s[i]=="]" and a[-1]=="[":
                a.pop()
            elif s[i]=="]" and a[-1]!="[":
                return False
        if len(a)==0:
            return True
        return False