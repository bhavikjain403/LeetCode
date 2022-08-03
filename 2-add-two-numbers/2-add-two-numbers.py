# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1=""
        num2=""
        head1=l1
        head2=l2
        while head1:
            num1+=str(head1.val)
            head1=head1.next
        while head2:
            num2+=str(head2.val)
            head2=head2.next
        ans=str(int(num1[::-1])+int(num2[::-1]))[::-1]
        l=len(ans)
        if l==0:
            return None
        head=ListNode()
        p=head
        for i in range(l):
            head.val=int(ans[i])
            if i<l-1:
                head.next=ListNode()
                head=head.next
        return p