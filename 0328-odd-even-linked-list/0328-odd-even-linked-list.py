# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next or not head.next.next:
            return head
        o=[]
        e=[]
        le=0
        i=1
        while head:
            if i%2:
                o.append(head.val)
            else:
                e.append(head.val)
                le+=1
            i+=1
            head=head.next
        p=ListNode()
        q=p
        for i in o:
            p.val=i
            p.next=ListNode()
            p=p.next
        for i in range(le):
            p.val=e[i]
            if i<le-1:
                p.next=ListNode()
                p=p.next
        return q