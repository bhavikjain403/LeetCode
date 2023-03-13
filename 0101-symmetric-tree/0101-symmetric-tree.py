# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def recursive(root1,root2):
            if(root1==None or root2==None):
                return root1==root2
            return root1.val==root2.val and recursive(root1.left,root2.right) and recursive(root1.right,root2.left)
        return recursive(root,root)