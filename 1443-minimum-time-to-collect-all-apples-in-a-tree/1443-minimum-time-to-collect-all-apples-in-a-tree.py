class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        data=defaultdict(list)
        for i,j in edges:
            data[i].append(j)
            data[j].append(i)
        visited = set()
        def dfs(node):
            visited.add(node)
            cost=0
            for i in data[node]:
                if i in visited:
                    continue
                temp=dfs(i)
                if temp or hasApple[i]:
                    cost+=temp+2
            return cost
        return dfs(0)