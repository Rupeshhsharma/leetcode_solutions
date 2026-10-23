link- https://leetcode.com/problems/reverse-linked-list-ii/description/
code:

class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        # Move prev to the node before position left
        for _ in range(left - 1):
            prev = prev.next

        # Start reversing
        curr = prev.next

        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next
