link- https://leetcode.com/problems/swap-nodes-in-pairs/description/?envType=problem-list-v2&envId=linked-list
code:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        current=head
        
        dummy=ListNode()
        new=dummy
        while current is not None and current.next is not None:
            slow=current
            fast=current.next
            #swap
            new.next=fast
            slow.next=fast.next
            fast.next=slow
            new=slow
            current=slow.next
        else:
            new.next=current

        return dummy.next

