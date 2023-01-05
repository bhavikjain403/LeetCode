class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        a=sorted(points,key=lambda x:x[1])
        ans=1
        curr=a[0][1]
        for i in range(1,len(a)):
            if a[i][0]>curr:
                curr=a[i][1]
                ans+=1
        return ans