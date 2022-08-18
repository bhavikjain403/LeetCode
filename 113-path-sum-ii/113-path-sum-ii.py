# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        ans=[]
        q=deque()
        q.append((root,targetSum,[]))
        while q:
            node, nsum, path = q.popleft()
            nsum-=node.val
            path.append(node.val)
            if node.left or node.right:
                if node.left:
                    q.append((node.left,nsum,path.copy()))
                if node.right:
                    q.append((node.right,nsum,path.copy()))
            elif nsum==0:
                ans.append(path)
        return ans