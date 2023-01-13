class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        def dfs(node):
            char=s[node]            
            a,b=0,0
            for child in data[node]:
                path=dfs(child)
                if s[child]!=char:                    
                    if path>=a:
                        b=a
                        a=path 
                    elif path>b:
                        b=path         
            self.result = max(self.result,a+b+1)        
            return a+1
        data = defaultdict(list)
        for n in range(1, len(parent)):
            data[parent[n]].append(n)  
        self.result = 0
        dfs(0)
        return self.result