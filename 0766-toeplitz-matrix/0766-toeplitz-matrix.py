class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m,n=len(matrix),len(matrix[0])
        for i in range(1,m):
            if matrix[i][1:]!=matrix[i-1][:n-1]:
                return False
        return True