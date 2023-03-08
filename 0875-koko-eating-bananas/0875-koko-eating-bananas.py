class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low,high=1,max(piles)
        while low<high:
            mid=low+(high-low)//2
            total=0
            for i in piles:
                total+=i//mid
                if i%mid:
                    total+=1
            if total<=h:
                high=mid
            else:
                low=mid+1
        return low