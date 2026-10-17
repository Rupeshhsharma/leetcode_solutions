link - https://leetcode.com/problems/same-tree/description/?envType=problem-list-v2&envId=breadth-first-search
code:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        def rec(p,q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            
            if p.val ==q.val:
                return rec(p.left,q.left) and rec(p.right,q.right)
            else:
                return False
            
        return rec(p,q)
