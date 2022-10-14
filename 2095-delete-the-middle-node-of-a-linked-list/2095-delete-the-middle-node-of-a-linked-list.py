# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head) or (not head.next):
            return None
        l=0
        p=head
        while p:
            l+=1
            p=p.next
        i,p=0,head
        while i<(l//2-1):
            p=p.next
            i+=1
        if p.next.next:
            p.next=p.next.next
        else:
            p.next=None
        return head