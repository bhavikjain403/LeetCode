class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=len(strs)
        if n==0:
            return ""
        if n==1:
            return strs[0]
        strs.sort()
        a=strs[0]
        na=len(a)
        ans=""
        for i in range(na):
            flag=1
            for j in range(1,n):
                if strs[j][i]!=a[i]:
                    return ans
            ans+=a[i]
        return ans