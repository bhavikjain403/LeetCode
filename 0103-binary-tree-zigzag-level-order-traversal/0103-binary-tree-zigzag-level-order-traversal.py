# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        vals, q = [], [(root, 0)]
        for node, d in q:
            if node:
                if len(vals) <= d: vals.append([])
                q += [(node.left, d+1), (node.right, d+1)]
                vals[d] = [node.val] + vals[d] if d & 1 else vals[d] + [node.val]
        return vals