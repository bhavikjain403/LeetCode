"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        def walk(x):
            q = collections.deque()
            q.append(x)
            while q:
                t = []
                for i in range(len(q)):
                    x = q.popleft()
                    t.append(x.val)
                    for c in x.children:
                        q.append(c)
                A.append(t)
        A = []
        if root:
            walk(root)
        return A