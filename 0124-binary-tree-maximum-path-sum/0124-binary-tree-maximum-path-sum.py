# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            l_sum = dfs(root.left)
            r_sum = dfs(root.right)
            l = max(0, l_sum)
            r = max(0, r_sum)
            self.res = max(self.res, root.val + l + r)
            return root.val + max(l, r)
        
        self.res = -float('inf')
        dfs(root)
        return self.res