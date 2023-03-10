# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.a=[]
        p=head
        while p:
            self.a.append(p.val)
            p=p.next
        self.l=len(self.a)

    def getRandom(self) -> int:
        return self.a[randint(0,self.l-1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()