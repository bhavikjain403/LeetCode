class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l=len(s)
        # if s.count(s[0])==l:
        #     if l>=11:
        #         return [s[:10]]
        #     return []
        # ans=set()
        # for i in range(l-9):
        #     temp=s[i:i+10]
        #     if s.count(temp)>=2:
        #         ans.add(temp)
        # return list(ans)
        d=dict()
        ans=set()
        for i in range(l-9):
            temp=s[i:i+10]
            if temp in d:
                ans.add(temp)
            else:
                d[temp]=1
        return list(ans)