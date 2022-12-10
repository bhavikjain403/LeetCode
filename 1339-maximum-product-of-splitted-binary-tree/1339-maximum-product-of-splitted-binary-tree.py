# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        data=[]
        def dfs(root):
            if not root:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            total=root.val+left+right
            data.append(total)
            return total
        
        total=dfs(root)
        ans=-float('inf')
        for i in data:
            ans=max(ans,(total-i)*i)
        return ans%(1000000007)