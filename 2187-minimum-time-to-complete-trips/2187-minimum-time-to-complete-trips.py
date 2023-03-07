class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        low,high=1,min(time)*totalTrips
        while low<=high:
            mid=low+(high-low)//2
            total=0
            for i in time:
                total+=mid//i
            if total>=totalTrips:
                high=mid-1
            else:
                low=mid+1
        return low