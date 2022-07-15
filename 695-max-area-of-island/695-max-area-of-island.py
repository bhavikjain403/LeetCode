class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def recursive(i,j,area=0):
            grid[i][j]=0
            if i>0 and grid[i-1][j]==1:
                area+= 1+recursive(i-1,j)
            if i<m-1 and grid[i+1][j]==1:
                area+= 1+recursive(i+1,j)
            if j>0 and grid[i][j-1]==1:
                area+=1+ recursive(i,j-1)
            if j<n-1 and grid[i][j+1]==1:
                area+= 1+recursive(i,j+1)
            return area
        
        ans = 0
        for a in range(m):
            for b in range(n):
                if grid[a][b]==1:
                    i,j=a,b
                    ans = max(ans,1+recursive(i,j))
                        
        return ans