class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        l=len(points)
        if l<=2:
            return l
        ans=[]
        for i in range(l-1):
            x1,y1=points[i][0],points[i][1]
            for j in range(i+1,l):
                temp=2
                x2,y2=points[j][0],points[j][1]
                if x2!=x1:
                    m=(y2-y1)/(x2-x1)
                else:
                    m=float('inf')
                for k in range(l):
                    if k!=i and k!=j:
                        x3,y3=points[k][0],points[k][1]
                        if x1!=x3 and m==(y3-y1)/(x3-x1):
                            temp+=1
                        elif x1==x3 and m==float('inf'):
                            temp+=1
                ans.append(temp)
        return max(ans)