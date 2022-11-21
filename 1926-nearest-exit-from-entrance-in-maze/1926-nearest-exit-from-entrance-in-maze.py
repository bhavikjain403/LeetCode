class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited=set((entrance[0],entrance[1]))
        q=deque()
        q.append((entrance[0],entrance[1],0))
        m,n=len(maze),len(maze[0])
        while q:
            a,b,ans=q.popleft()
            if (a,b)!=(entrance[0],entrance[1]) and (a==0 or b==0 or a==m-1 or b==n-1):
                return ans
            for i,j in ((a+1,b),(a-1,b),(a,b+1),(a,b-1)):
                if 0<=i<m and 0<=j<n and maze[i][j]!="+" and (i,j) not in visited:
                    q.append((i,j,ans+1))
                    visited.add((i,j))
        return -1