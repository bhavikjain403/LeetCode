class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a=Counter(nums).most_common(k)
        ans=[]
        for i in a:
            ans.append(i[0])
        return ans