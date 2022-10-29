class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        ans,grow=0,0
        data=sorted(zip(growTime, plantTime),reverse=True)
        for i,j in data:
            grow+=j
            ans=max(ans,grow+i)
        return ans