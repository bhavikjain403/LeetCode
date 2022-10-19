class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d=defaultdict(int)
        for i in words:
            d[i]+=1
        d=sorted(d.items(), key=lambda x:(-x[1],x[0]))
        ans=[]
        i=0
        while k:
            ans.append(d[i][0])
            i+=1
            k-=1
        return ans