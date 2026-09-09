link-https://leetcode.com/problems/palindrome-linked-list/submissions/2136724536/
code:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current=head
        a=[]
        while current is not None:
            a.append(current.val)
            current=current.next
        if a == a[::-1]:
            return True
        else:
            return False

        
