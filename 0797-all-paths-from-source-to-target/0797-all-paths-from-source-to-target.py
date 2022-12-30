class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        l=len(graph)
        ans=[]
        def dfs(cur,path):
            if cur==l-1:
                ans.append(path)
            else:
                for i in graph[cur]:
                    dfs(i,path+[i])
        dfs(0,[0])
        return ans