# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        q=deque()
        q.append(root)
        ans=0
        while len(q):
            k=q.popleft()
            if k.left:
                if not k.left.left and not k.left.right:
                    ans+=k.left.val
                else:
                    q.append(k.left)
            if k.right:
                q.append(k.right)
        return ans