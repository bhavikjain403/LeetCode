# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        q,r=head,head
        l=0
        while q:
            l+=1
            q=q.next
        t=l//k
        data=[]
        while t:
            temp=k
            var=[]
            while temp:
                var.append(r.val)
                r=r.next
                temp-=1
            data.append(var[::-1])
            t-=1
        ans=ListNode()
        p=ans
        for i in range(l//k):
            for j in range(k):
                ans.val=data[i][j]
                if i==l//k-1 and j==k-1:
                    ans.next=r
                else:
                    ans.next=ListNode()
                    ans=ans.next
        return p