class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans=0
        n,m=len(grid),len(grid[0])
        vis=set()
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1" and ((i,j) not in vis):
                    q=deque()
                    q.append((i,j))
                    dx,dy=[-1,0,1,0],[0,1,0,-1]
                    vis.add((i,j))
                    while q:
                        x,y=q.popleft()
                        for idx in range(4):
                            nx,ny=x+dx[idx],y+dy[idx]
                            if 0<=nx<n and 0<=ny<m and grid[nx][ny]=="1" and ((nx,ny) not in vis):
                                vis.add((nx,ny))
                                q.append((nx,ny))
                    ans+=1
        return ans