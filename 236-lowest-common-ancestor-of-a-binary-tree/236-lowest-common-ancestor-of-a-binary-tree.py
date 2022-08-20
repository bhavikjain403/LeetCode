# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root) :
            if not root :
                return False            
            left = dfs(root.left)
            right = dfs(root.right)            
            if root == p or root == q :
                r=True
            else :
                r=False                
            if (left and right) or (r and left) or (r and right):
                return root      
            return left or right or r        
        return dfs(root)