link- https://leetcode.com/problems/balanced-binary-tree/description/
code:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def balance(root):
            if root is None:
                return 0
            left=balance(root.left)
            if left==-1:
                return -1
            right=balance(root.right)
            if right==-1:
                return -1
            if abs(left-right)>1:
                return -1
            return 1+max(left,right)
        return balance(root)!=-1
        
