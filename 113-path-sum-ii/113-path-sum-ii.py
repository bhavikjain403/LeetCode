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
        
        # Initialize variables
        result = []  
        deq = deque()
        
        # Start traversal
        # Every element of deque is a state describing current node
        # As a state we need the following: node itself, remaining sum, path from the root
        deq.append((root, targetSum, []))
        
        # Breath-first-search part
        while deq:
            node, left_sum, path = deq.popleft()
            
            left_sum -= node.val
            path.append(node.val)
            
            if node.left or node.right:  # Try to go into children
                if node.left:
                    deq.append((node.left, left_sum, path.copy()))
                    
                if node.right:
                    deq.append((node.right, left_sum, path.copy()))
            elif left_sum == 0:  # End of a traversal, check if the total path sum is equal to 0
                result.append(path)  # Put path values into the result
        
        return result
    
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