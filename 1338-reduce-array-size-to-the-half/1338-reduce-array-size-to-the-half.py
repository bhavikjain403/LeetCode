class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d=dict()
        l=len(arr)//2
        for i in arr:
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1
        d=list(d.values())
        d.sort(reverse=True)
        ans,rem,i=0,0,0
        while rem<l:
            ans+=1
            rem+=d[i]
            i+=1
        return ans