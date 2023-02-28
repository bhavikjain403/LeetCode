# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        order=[]
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            order.append(root.val)
            inorder(root.right)
        inorder(root)
        c=Counter(order)
        m=max(c.values())
        ans=set()
        for i in c:
            if c[i]==m:
                ans.add(i)
        return list(ans)