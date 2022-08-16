class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        data=[]
        for i in range(1,n+1):
            data.append(i)
        while len(data)>1:
            for i in range(k-1):
                data.append(data.pop(0))
            data.pop(0)
        return data[0]