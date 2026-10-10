link- https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/?envType=problem-list-v2&envId=linked-list
code:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        current=head
    
        if current:
            new=current.next
        
        while current is not None and current.next is not None:
            while new is not None and current.val ==new.val:
                new=new.next
                current.next=new
            current=current.next
            if current is not None:
                new=current.next
        return head
