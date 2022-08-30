# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same_tree(node, subRoot):
            if not node and not subRoot:
                return True
            if (not node and subRoot) or (node and not subRoot):
                return False
            if node.val != subRoot.val:
                return False
            return is_same_tree(node.left, subRoot.left) and is_same_tree(node.right, subRoot.right)
        q=deque()
        q.append(root)
        l=len(q)
        while l:
            root=q.popleft()
            l-=1
            if is_same_tree(root,subRoot):
                return True
            if root.left:
                q.append(root.left)
                l+=1
            if root.right:
                q.append(root.right)
                l+=1
        return False