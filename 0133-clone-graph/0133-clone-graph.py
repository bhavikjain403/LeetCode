"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        q,ans=deque([node]),{node.val:Node(node.val,[])}
        while q:
            cur=q.popleft()
            temp=ans[cur.val]
            for i in cur.neighbors:
                if ans.get(i.val,0)==0:
                    ans[i.val]=Node(i.val,[])
                    q.append(i)
                temp.neighbors.append(ans[i.val])
        return ans[node.val]