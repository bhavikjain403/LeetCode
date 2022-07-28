class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        l=len(triangle)
        for i in range(l-2, -1, -1): 
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1] if j+1< len(triangle[i+1]) else +float('inf'))          
        return triangle[0][0]