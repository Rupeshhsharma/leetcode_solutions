link- https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/
code:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        current=head
        prev=None
        slow=current
        fast=current
        if current.next is None:
            return None
        while fast is not None and fast.next is not None:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        
        prev.next=slow.next
        slow=None
        return head
