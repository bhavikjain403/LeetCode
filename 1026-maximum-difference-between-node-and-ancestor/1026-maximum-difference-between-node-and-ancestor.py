# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        def dfs(node,mini,maxi):
            if node:
                mini,maxi=min(mini,node.val),max(maxi,node.val)
                self.ans=max(self.ans,maxi-mini)
                dfs(node.left,mini,maxi),dfs(node.right,mini,maxi)
        dfs(root,float('inf'),-float('inf'))
        return self.ans