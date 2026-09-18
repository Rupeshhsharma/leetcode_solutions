link-https://leetcode.com/problems/intersection-of-two-linked-lists/description/?envType=problem-list-v2&envId=linked-list
code:
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        x = headA
        y = headB

        while x != y:
            x = x.next if x else headB
            y = y.next if y else headA
        
        return x
