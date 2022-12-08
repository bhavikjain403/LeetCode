# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return 1
        d1,d2=[],[]
        q1,q2=deque(),deque()
        q1.append(root1)
        q2.append(root2)
        l1,l2=len(q1),len(q2)
        while l1:
            r1=q1.pop()
            l1-=1
            if not r1.left and not r1.right:
                d1.append(r1.val)
            if r1.left:
                q1.append(r1.left)
                l1+=1
            if r1.right:
                q1.append(r1.right)
                l1+=1
        while l2:
            r2=q2.pop()
            l2-=1
            if not r2.left and not r2.right:
                d2.append(r2.val)
            if r2.left:
                q2.append(r2.left)
                l2+=1
            if r2.right:
                q2.append(r2.right)
                l2+=1
        print(d1,d2)
        return d1==d2