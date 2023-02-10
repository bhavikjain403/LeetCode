class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        q=deque()
        m=len(grid)
        for i in range(m):
            for j in range(m):
                if grid[i][j]==1:
                    q.append((i,j))
        l=len(q)
        if l==m*m or l==0:
            return -1
        ans=-1
        while q:
            for i in range(l):
                x,y=q.popleft()
                l-=1
                for a,b in [(1,0),(0,1),(-1,0),(0,-1)]:
                    xn,yn=x+a,y+b
                    if 0<=xn<m and 0<=yn<m and grid[xn][yn]==0:
                        q.append((xn,yn))
                        grid[xn][yn]=1
                        l+=1
            ans+=1
        return ans