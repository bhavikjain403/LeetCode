class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # n,m=len(grid),len(grid[0])
        # vis=set()
        # q=deque()
        # for i in range(n):
        #     for j in range(m):
        #         if grid[i][j]==2:
        #             q.append((i,j,0))
        #             vis.add((i,j))
        # ans=0
        # dx,dy=[-1,0,1,0],[0,1,0,-1]
        # while q:
        #     x,y,t=q.popleft()
        #     ans=max(ans,t)
        #     for d in range(4):
        #         if x+dx[d]>=0 and x+dx[d]<n and y+dy[d]>=0 and y+dy[d]<m and ((x+dx[d],y+dy[d]) not in vis):
        #             vis.add((x+dx[d],y+dy[d]))
        #             if grid[x+dx[d]][y+dy[d]]==1:
        #                 q.append((x+dx[d],y+dy[d],t+1))
        #                 grid[x+dx[d]][y+dy[d]]=2
        # for i in range(n):
        #     for j in range(m):
        #         if grid[i][j]==1:
        #             return -1
        # return ans
        
        n,m=len(grid),len(grid[0])
        vis=set()
        q=deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    vis.add((i,j))
                    q.append((i,j,0))
        ans=0
        dx,dy=[-1,0,1,0],[0,1,0,-1]
        while q:
            x,y,t=q.popleft()
            ans=max(ans,t)
            for d in range(4):
                nx,ny=x+dx[d],y+dy[d]
                if 0<=nx<n and 0<=ny<m and ((nx,ny) not in vis):
                    vis.add((nx,ny))
                    if grid[nx][ny]==1:
                        q.append((nx,ny,t+1))
                        grid[nx][ny]=2
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    return -1
        return ans
            