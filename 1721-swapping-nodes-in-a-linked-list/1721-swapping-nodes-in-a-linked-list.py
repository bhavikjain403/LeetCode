# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p=head
        cpy=k
        l=0
        while p:
            l+=1
            p=p.next
        v1,v2,temp,le=0,0,k,l
        p=head
        while p:
            if k==1:
                v1=p.val
            if l==temp:
                v2=p.val
            k-=1
            l-=1
            p=p.next
        temp2=temp
        p=head
        while p:
            if temp==1:
                p.val=v2
            if le==temp2:
                p.val=v1
            p=p.next
            temp-=1
            le-=1
        return head