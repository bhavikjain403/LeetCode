class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans,t=0,0
        for i in timeSeries:
            if i<t:
                newt=i+duration+1
                ans+=newt-t
                t=newt
            else:
                t=i+duration+1
                ans+=duration
        return ans
            