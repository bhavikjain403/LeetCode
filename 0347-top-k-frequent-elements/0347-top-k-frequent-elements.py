class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if d.get(i,0):
                d[i]+=1
            else:
                d[i]=1
        d=sorted(d.items(),key=lambda x:-x[1])
        ans=[]
        for x,y in d:
            ans.append(x)
        return ans[:k]