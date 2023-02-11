class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        data=[]
        for i in range(n):
            data.append([set(),set()])
        for i,j in redEdges:
            data[i][0].add(j)
        for i,j in blueEdges:
            data[i][1].add(j)
        ans=[float('inf')]*n
        q=deque([(0,0),(0,1)])
        level=-1
        while q:
            level+=1
            for i in range(len(q)):
                node,color=q.popleft()
                ans[node]=min(ans[node],level)
                child=data[node][1-color]
                for j in list(child):
                    data[node][1-color].remove(j)
                    q.append((j,1-color))
        for i in range(n):
            if ans[i]==float('inf'):
                ans[i]=-1
        return ans