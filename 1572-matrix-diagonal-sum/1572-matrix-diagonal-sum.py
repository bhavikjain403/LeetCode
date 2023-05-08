class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans=0
        for i in range(len(mat)):
            ans+=mat[i][i]+mat[i][len(mat)-i-1]
        if len(mat)%2:
            ans-=mat[len(mat)//2][len(mat)//2]
        return ans