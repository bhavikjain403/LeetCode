class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans=[]
        def recurse(cur,start):
            if len(cur)==4 and start==len(s):
                ans.append(".".join(cur))
                return
            if len(cur)>4:
                return
            for i in range(start,min(start+3,len(s))):
                if s[start]=="0" and i>start:
                    continue
                if int(s[start:i+1])<256:
                    recurse(cur+[s[start:i+1]],i+1)
        recurse([],0)
        return ans