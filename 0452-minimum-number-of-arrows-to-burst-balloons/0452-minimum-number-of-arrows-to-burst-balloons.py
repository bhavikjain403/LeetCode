class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        ans=1
        if len(points)==1:
            return ans
        i=0
        for j in range(1,len(points)):
            if points[j][0]>points[i][1]:
                ans+=1
                i=j
        return ans