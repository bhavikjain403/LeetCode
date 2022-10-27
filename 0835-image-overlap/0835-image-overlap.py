class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        a,b,n=[],[],len(img1)
        d=collections.defaultdict(int)
        for i in range(n):
            for j in range(n):
                if(img1[i][j]==1):
                    a.append((i,j))
                if(img2[i][j]==1):
                    b.append((i,j))
        ans=0
        for i in a:
            for j in b:
                k=(j[0]-i[0],j[1]-i[1])
                d[k]+=1
                ans=max(ans,d[k])
        return ans