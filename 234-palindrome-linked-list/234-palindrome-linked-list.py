# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        data=[]
        while head:
            data.append(head.val)
            head=head.next
        if data==data[::-1]:
            return 1
        return 0