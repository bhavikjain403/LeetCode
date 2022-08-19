# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        q=deque()
        q.append(root)
        l=1
        data=[]
        while l:
            root=q.popleft()
            l-=1
            data.append(root.val)
            if root.left:
                q.append(root.left)
                l+=1
            if root.right:
                l+=1
                q.append(root.right)
        data.sort()
        return data[k-1]