class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        ans=""
        c=s.count(")")
        for i in s:
            if i=="(":
                stack.append("(")
                if c:
                    c-=1
                    ans+="("
            elif i==")":
                if not stack:
                    c-=1
                    continue
                else:
                    stack.pop()
                    ans+=")"
            else:
                ans+=i
        return ans