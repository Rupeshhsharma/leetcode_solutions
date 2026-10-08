link- https://leetcode.com/problems/merge-two-sorted-lists/description/?envType=problem-list-v2&envId=linked-list
code:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        newlist=ListNode()
        dummy=newlist
        while list1 is not None and list2 is not None:
            if list1.val==list2.val:
                dummy.next=list2
                list2=list2.next
            elif list1.val<list2.val:
                dummy.next=list1
                list1=list1.next
            elif list1.val>list2.val:
                dummy.next=list2
                list2=list2.next
            dummy=dummy.next
        if list1 is not None:
            dummy.next=list1
        else:
            dummy.next=list2
        return newlist.next




            
