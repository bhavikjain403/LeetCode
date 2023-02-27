class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans=0
        m,n=len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                ans += 4*grid[i][j]
                if i > 0:
                    ans-= grid[i][j]*grid[i-1][j]
                if i < m-1:
                    ans -= grid[i][j]*grid[i+1][j]
                if j > 0:
                    ans-= grid[i][j]*grid[i][j-1]
                if j < n-1:
                    ans-= grid[i][j]*grid[i][j+1]
        return ans