class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph=defaultdict(dict)
        for u,v,w in roads:
            graph[u][v]=graph[v][u]=w
        res=inf
        vis=set()
        q=deque([1])
        while q:
            node=q.popleft()
            for i,j in graph[node].items():
                if i not in vis:
                    q.append(i)
                    vis.add(i)
                res = min(res,j)
        return res