class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        r,l=sum(weights),max(weights)
        n=len(weights)
        while l<r:
            mid=l+(r-l)//2
            day,w=1,0
            for i in weights:
                w+=i
                if w>mid:
                    day+=1
                    w=i
            if day<=days:
                r=mid
            else:
                l=mid+1
        return l