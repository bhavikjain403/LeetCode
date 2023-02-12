class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(list)
        for i,j in roads:
            graph[i].append(j)
            graph[j].append(i)
        visited = set()
        fuel=[0]
        def dfs(node):
            visited.add(node)
            people = 0
            for n in graph[node]:
                if n in visited:
                    continue
                p = dfs(n)
                people += p
                fuel[0] += ceil(p/seats)
            return people+1
        dfs(0)
        return fuel[0]