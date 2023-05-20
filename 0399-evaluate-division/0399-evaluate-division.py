class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        def buildgraph():
            for i, eq in enumerate(equations):
                st, end = eq[0], eq[1]
                graph[st][end] = values[i]
                graph[end][st] = 1.0/values[i]
        
        def dfs(st, end, cursum):
            if st not in graph:
                return -1.0
            self.visited.add(st)
            for adj in graph[st]: 
                if adj == end:
                    return cursum*graph[st][adj]
                
                if adj not in self.visited:
                    tmp = dfs(adj, end, cursum*graph[st][adj])
                    if tmp != -1.0:
                        return tmp
            return -1.0
        buildgraph()
        res = []
        for i, q in enumerate(queries):
            self.visited = set()
            res.append(dfs(q[0], q[1], 1.0))
        
        return res