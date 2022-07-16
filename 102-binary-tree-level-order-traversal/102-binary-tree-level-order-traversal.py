# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root!=None:
            q = [root]
            while len(q):
                qlen = len(q)
                temp = []
                for i in range(qlen):
                    e = q.pop(0)
                    temp.append(e.val)
                    if e.left:
                        q.append(e.left)
                    if e.right:
                        q.append(e.right)
                ans.append(temp)
        return ans