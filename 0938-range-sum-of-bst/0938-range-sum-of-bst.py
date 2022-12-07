# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ans=0
        def dfs(root):
            if not root:
                return 0
            if low<=root.val<=high:
                self.ans+=root.val
            if root.val<=high:
                dfs(root.right)
            if root.val>=low:
                dfs(root.left)
        dfs(root)
        return self.ans