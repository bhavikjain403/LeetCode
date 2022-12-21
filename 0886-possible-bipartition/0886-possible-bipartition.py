class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        l=len(dislikes)
        for i in range(l):
            graph[dislikes[i][0]-1].append(dislikes[i][1]-1)
            graph[dislikes[i][1]-1].append(dislikes[i][0]-1)
            
        group = dict()
        
        def dfs(i):
            for node in graph[i]:
                if node not in group:
                    group[node]=-group[i]
                    if not dfs(node):
                        return False  
                elif group[node]==group[i]:
                    return False
                
            return True
        
        for i in range(n):
            if i not in group:
                group[i] = 1
                if not dfs(i):
                    return False
        return True