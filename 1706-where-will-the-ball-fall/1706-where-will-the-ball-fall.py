class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m,n = len(grid), len(grid[0])
        res = [-1]*n
        for i in range(n):
            y, x = 0, i
            while y<m:
                delta = grid[y][x]
                if not 0<=x+delta<n: break
                if grid[y][x]==grid[y][x+delta]:
                    x += grid[y][x]
                    y += 1
                else:
                    break
            if y==m: res[i] = x
        return res