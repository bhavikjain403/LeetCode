# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result, nodes = [], deque()
        nodes.append(root)
        if root!=None:
            while len(nodes)>0:
                result.append(nodes[-1].val)
                childNodes = []
                while len(nodes)>0:
                    temp = nodes.popleft()
                    childNodes.extend([temp.left, temp.right])
                nodes.extend([node for node in childNodes if node!=None])
        return result