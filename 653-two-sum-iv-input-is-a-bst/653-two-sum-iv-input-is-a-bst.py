# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recur(self,root,a,k):
        if not root:
            return False
        if (k-root.val) in a:
            return True
        a.add(root.val)
        return self.recur(root.left,a,k) or self.recur(root.right,a,k)
    
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        return self.recur(root,set(),k)