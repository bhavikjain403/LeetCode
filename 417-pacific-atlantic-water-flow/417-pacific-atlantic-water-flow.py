class Solution(object):
    def dfs(self,i,j,matrix,explored,prev):
        m,n = len(matrix),len(matrix[0])
        if i < 0 or i >= m or j < 0 or j >= n or (i,j) in explored:
            return
        if matrix[i][j] < prev:
            return
        explored.add((i,j))
        self.dfs(i-1,j,matrix,explored,matrix[i][j]) #up
        self.dfs(i+1,j,matrix,explored,matrix[i][j]) #down
        self.dfs(i,j-1,matrix,explored,matrix[i][j]) #left
        self.dfs(i,j+1,matrix,explored,matrix[i][j]) #right
        
    def pacificAtlantic(self, matrix):
        if not matrix: return []
        pacific,atlantic = set(),set()
        m,n = len(matrix),len(matrix[0])
        for i in range(n):
            self.dfs(0,i,matrix,pacific,-1)
            self.dfs(m-1,i,matrix,atlantic,-1)
        for i in range(m):
            self.dfs(i,0,matrix,pacific,-1)
            self.dfs(i,n-1,matrix,atlantic,-1)
        return list(pacific&atlantic)