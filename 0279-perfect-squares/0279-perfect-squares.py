class Solution:
    def numSquares(self, n: int) -> int:
        q=deque()
        visited=set()
        q.append((0,0))
        while q:
            s,count=q.popleft()
            count+=1
            for i in range(1,n+1):
                temp=s+i*i
                if temp>n:
                    break
                if temp==n:
                    return count
                if temp not in visited:
                    visited.add(temp)
                    q.append((temp,count))