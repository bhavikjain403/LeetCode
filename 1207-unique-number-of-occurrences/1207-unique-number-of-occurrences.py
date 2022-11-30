class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d=dict()
        l=0
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
                l+=1
        v=d.values()
        if l==len(set(v)):
            return True
        return False