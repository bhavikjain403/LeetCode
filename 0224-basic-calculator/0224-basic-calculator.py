class Solution:
    def calculate(self, s: str) -> int:
        l,i=len(s),0
        def recursion(s):
            nonlocal i
            sign,ans=1,0
            while i<l:
                if s[i]==" ": 
                    i+=1
                    continue
                elif s[i]=='+':
                    sign=1
                elif s[i]=='-':
                    sign=-1
                elif s[i]=='(':
                    i+=1
                    ans+=sign*recursion(s)
                    sign=1
                elif s[i]==')':
                    return ans
                else:
                    num=int(s[i])
                    while i<l-1 and s[i+1].isdigit():
                        num=num*10+int(s[i+1])
                        i+=1
                    ans+=num*sign
                    sign=1
                i+=1
            return ans
        
        return recursion(s)