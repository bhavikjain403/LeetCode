class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        ans = [[1],[1,1]]
        for i in range(2,numRows):
            temp = [1]
            for j in range(i-1):
                temp.append(ans[i-1][j]+ans[i-1][j+1])
            temp.append(1)
            ans.append(temp)
        return ans