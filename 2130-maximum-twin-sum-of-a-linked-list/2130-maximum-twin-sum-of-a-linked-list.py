# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow_ptr = head
        fast_ptr = head
        prev_ptr = None
        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            next_node = slow_ptr.next
            slow_ptr.next = prev_ptr
            prev_ptr = slow_ptr
            slow_ptr = next_node
        max_sum = float('-inf')
        while slow_ptr:
            max_sum = max(max_sum, slow_ptr.val + prev_ptr.val)
            slow_ptr = slow_ptr.next
            prev_ptr = prev_ptr.next
        return max_sum