#User function Template for python3
import heapq
from collections import deque
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        a=[(0,0,-1)]
        h=heapq.heapify(a)
        data={}
        for u in range(len(adj)):
            for v,w in adj[u]:
                if data.get(u,0)==0:
                    data[u]=[(v,w)]
                else:
                    data[u].append((v,w))
                if data.get(v,0)==0:
                    data[v]=[(u,w)]
                else:
                    data[v].append((u,w))
        vis=[0]*V
        ans=0
        while len(a):
            w,u,v=heapq.heappop(a)
            if vis[u]==0:
                ans+=w
                vis[u]=1
            else:
                continue
            for c in data[u]:
                if vis[c[0]]==0:
                    heapq.heappush(a,(c[1],c[0],u))
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends