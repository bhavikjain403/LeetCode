# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recur(root):
            if not root:
                return None
            root.left=recur(root.left)
            root.right=recur(root.right)
            if root.val or root.left or root.right:
                return root
        return recur(root)