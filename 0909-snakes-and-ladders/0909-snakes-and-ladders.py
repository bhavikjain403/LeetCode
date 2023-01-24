class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        data=[0]
        i=0
        for j in board[::-1]:
            if i%2:
                data+=j[::-1]
            else:
                data+=j
            i+=1
        q=[1]
        seen=set()
        n=len(board)
        ans=0
        while q:
            temp=[]
            for i in q:
                if i==n*n:
                    return ans
                for j in range(i+1,min(i+6,n*n)+1):
                    if j not in seen:
                        seen.add(j)
                        if data[j]==-1:
                            temp.append(j)
                        else:
                            temp.append(data[j])
            q=temp
            ans+=1
        return -1