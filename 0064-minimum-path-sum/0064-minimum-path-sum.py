class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rec = [[0]*n for _ in range(m)]
        rec[0][0] = grid[0][0]
        for i in range(1,n):
            rec[0][i] = rec[0][i-1] + grid[0][i]
        for i in range(1,m):
            rec[i][0] = rec[i-1][0] + grid[i][0]
        for i in range(1,m):
            for j in range(1,n):
                rec[i][j] = min(rec[i-1][j],rec[i][j-1]) + grid[i][j]
        return rec[-1][-1]