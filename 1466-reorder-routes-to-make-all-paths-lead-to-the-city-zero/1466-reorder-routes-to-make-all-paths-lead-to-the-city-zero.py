class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        d=collections.defaultdict(set)
        road=set()
        for i,j in connections:
            road.add((i,j))
            d[i].add(j)
            d[j].add(i)
        self.ans=0
        def dfs(child,parent):
            self.ans+=(parent,child) in road
            for node in d[child]:
                if node!=parent:
                    dfs(node,child)
        dfs(0,-1)
        return self.ans