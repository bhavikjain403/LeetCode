class Solution:
    
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m*n==r*c:
            new = []
            temp = []
            ans = []
            for i in range(m):
                for j in range(n):
                    new.append(mat[i][j])
            print(new)
            for i in range(r):
                t = new[:c]
                ans.append(t)
                new = new[c:]
            return ans
        return mat