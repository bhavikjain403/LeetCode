class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        def recurse(cur,start):
            if start==len(s):
                ans.append(cur)
            for i in range(len(s)-start):
                temp=s[start:start+i+1]
                if temp==temp[::-1]:
                    recurse(cur+[temp],start+i+1)
        recurse([],0)
        return ans