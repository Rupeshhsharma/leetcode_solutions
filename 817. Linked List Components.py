link-https://leetcode.com/problems/linked-list-components/description/
code:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        current=head
        nums=set(nums)
        sumi=0
        while current is not None:
            if current.val in nums:
                if current.next is None or current.next.val not in nums:
                    sumi+=1
            current=current.next
        return sumi

   

        
        
