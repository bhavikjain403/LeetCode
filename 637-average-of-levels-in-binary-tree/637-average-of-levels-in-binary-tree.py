# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q=deque()
        ans=[]
        q.append(root)
        while len(q):
            l=len(q)
            temp=0
            for i in range(l):
                root=q.popleft()
                temp+=root.val
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            ans.append(temp/l)
        return ans