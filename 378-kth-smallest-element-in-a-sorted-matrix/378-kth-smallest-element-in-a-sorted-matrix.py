class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        data=[]
        n=len(matrix)
        for i in range(n):
            for j in matrix[i]:
                data.append(j)
        data.sort()
        return data[k-1]