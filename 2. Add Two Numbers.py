link- https://leetcode.com/problems/add-two-numbers/description/
code:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        new=ListNode(0)
        head=new
        curr1=l1
        curr2=l2
        car=0
        
        while curr1 is not None or curr2 is not None or car!=0:
            sumi=car
            if curr1 is not None:
                sumi += curr1.val
                curr1 = curr1.next

            if curr2 is not None:
                sumi += curr2.val
                curr2 = curr2.next
                
            
            car=(sumi//10)
            sumi=sumi%10
            new.next=ListNode(sumi)
            new=new.next
            
        return head.next
