class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        data=[]
        c=0
        for i in points:
            data.append([c,(i[0]*i[0]+i[1]*i[1])**0.5])
            c+=1
        data.sort(key=lambda x:x[1])
        data=data[:k]
        ans=[]
        for i in data:
            ans.append(points[i[0]])
        return ans