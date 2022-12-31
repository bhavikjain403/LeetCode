class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.ans=0
        self.visit=0
        for i in grid:
            for j in i:
                if j!=-1:
                    self.visit+=1
        m,n=len(grid),len(grid[0])
        def dfs(i,j,visit):
            if grid[i][j]==2:
                if visit==self.visit:
                    self.ans+=1
                return
            for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if 0<=x<m and 0<=y<n and grid[x][y]!=-1:
                    grid[i][j]-=1
                    dfs(x,y,visit+1)
                    grid[i][j]+=1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    grid[i][j]-=1
                    dfs(i,j,1)
        return self.ans
                