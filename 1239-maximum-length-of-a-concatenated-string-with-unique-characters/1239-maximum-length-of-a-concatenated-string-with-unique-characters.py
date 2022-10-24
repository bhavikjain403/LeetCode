class Solution:
    def maxLength(self, arr: List[str]) -> int:
        s,ans=[""],0
        for i in arr:
            if len(i)==len(set(i)):
                for j in s:
                    if len(i)+len(j)==len(set(i+j)):
                        s.append(i+j)
                        ans=max(ans,len(i+j))
        return ans