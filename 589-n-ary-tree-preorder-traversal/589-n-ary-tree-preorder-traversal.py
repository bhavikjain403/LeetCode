"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        def recursive(root):
            if not root:
                return ans
            if ans==None:
                return []
            ans.append(root.val)
            for i in root.children:
                recursive(i)
        recursive(root)
        return ans