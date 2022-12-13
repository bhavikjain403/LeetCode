class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        l=len(matrix)
        for i in range(1,l):
            for j in range(l):
                matrix[i][j] += min(matrix[i-1][max(0,j-1):min(j+2,l)])
        return min(matrix[-1])