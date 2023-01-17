class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        o=0
        ans=0
        for i in s:
            if i=="0":
                if o!=0:
                    ans += 1
            else:
                o+=1
            ans=min(ans,o)
        return ans