class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for edge in edges:
            u, v = edge
            graph[u].append(v)
        visited = [-1] * len(colors)
        max_colors = defaultdict(lambda:[0]*26)
        
        def explore(node):
            if visited[node] == 0:
                return True
            elif visited[node] == 1:
                return False
            visited[node] = 0
            mc = [0] * 26
            for neighbor in graph[node]:
                have_cycle = explore(neighbor)
                if have_cycle: return have_cycle
                mc = [max(mc[i], max_colors[neighbor][i]) for i in range(len(mc))]
            mc[ord(colors[node]) - ord('a')] += 1
            max_colors[node] = mc
            visited[node] = 1
            return False

        for v in range(len(colors)):
            if explore(v): return -1
        res = 0
        for v in max_colors.keys():
            res = max(res, max(max_colors[v]))
        return res