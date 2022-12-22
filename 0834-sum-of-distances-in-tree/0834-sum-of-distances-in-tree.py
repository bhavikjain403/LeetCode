class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        count, dist = [1]*n, [0]*n
        def dfs1(node, parent):
            for child in graph[node]:
                if child != parent:
                    dfs1(child, node)
                    count[node] += count[child]
                    dist[node] += dist[child] + count[child]
        def dfs2(node, parent):
            for child in graph[node]:
                if child != parent:
                    dist[child] = dist[node] - count[child] + (n - count[child])
                    dfs2(child, node)
        dfs1(0, None)
        dfs2(0, None)
        return dist