class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        q=deque()
        m=len(grid)
        n=len(grid[0])
        directions=[(1,0),(-1,0),(0,-1),(0,1)]
        q.append((0,0,k))
        visited=set()
        visited.add((0,0,k))
        ans=0
        while q:
            for v in range(len(q)):
                i,j,limit=q.popleft()
                if i==m-1 and j==n-1:
                    return ans
                for d in directions:
                    new_i=i+d[0]
                    new_j=j+d[1]
                    if 0<=new_i<m and 0<=new_j<n:
                        if grid[new_i][new_j]==0 and (new_i,new_j,limit) not in visited:
                            q.append((new_i,new_j,limit))
                            visited.add((new_i,new_j,limit))
                        elif limit>0 and (new_i,new_j,limit-1) not in visited:
                            q.append((new_i,new_j,limit-1))
                            visited.add((new_i,new_j,limit-1))
            ans+=1
        return -1