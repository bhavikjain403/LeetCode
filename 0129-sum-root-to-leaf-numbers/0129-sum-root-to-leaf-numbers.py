# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        q=deque()
        q.append((root,0))
        l=1
        ans=0
        while l:
            r,s=q.pop()
            l-=1
            s=s*10+r.val
            if not r.left and not r.right:
                ans+=s
            if r.left:
                q.append((r.left,s))
                l+=1
            if r.right:
                q.append((r.right,s))
                l+=1
        return ans