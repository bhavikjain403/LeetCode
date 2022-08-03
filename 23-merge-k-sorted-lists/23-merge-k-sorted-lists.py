# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        data=[]
        d=0
        for i in lists:
            h=i
            while h:
                data.append(h.val)
                d+=1
                h=h.next
        if d==0:
            return None
        data.sort()
        head=ListNode()
        p=head
        for i in range(d):
            head.val=data[i]
            if i<d-1:
                head.next=ListNode()
                head=head.next
        return p