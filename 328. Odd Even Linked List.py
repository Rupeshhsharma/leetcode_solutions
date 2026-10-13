link- https://leetcode.com/problems/odd-even-linked-list/description/
code:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        slow=head
        if head is None:
            return head
        fast=head.next
        demo=head.next
        while fast is not None and fast.next is not None:
            slow.next=slow.next.next
            fast.next=fast.next.next
            slow=slow.next
            fast=fast.next
        slow.next=demo
        return head
        
