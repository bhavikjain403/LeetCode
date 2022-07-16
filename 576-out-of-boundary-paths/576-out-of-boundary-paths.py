class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if maxMove == 0:
            return 0
        dpI = [[0] * (n+2) for _ in range(m+2)]
        dpF = [[0] * (n+2) for _ in range(m+2)]
        for i in range(1, m+1):
            dpI[i][1] += 1
            dpI[i][n] += 1
        for j in range(1, n+1):
            dpI[1][j] += 1
            dpI[m][j] += 1
        ans = dpI[startRow+1][startColumn+1]
        for d in range(maxMove-1):
            dpI, dpF = dpF, dpI
            for i, j in product(range(1, m+1), range(1, n+1)):
                dpI[i][j] = (dpF[i-1][j] + dpF[i+1][j] + dpF[i][j-1] + dpF[i][j+1]) % 1000000007
            ans = (ans + dpI[startRow+1][startColumn+1]) % 1000000007
        return ans