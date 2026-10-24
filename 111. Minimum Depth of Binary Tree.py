link- https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
code:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        
        def mini(root):
            if root is None:
                return 0
            if root.left is None:
                return 1+mini(root.right)
            if root.right is None:
                return 1+ mini(root.left)
            left=mini(root.left)
            right=mini(root.right)
            return 1+min(left,right)
        
        
        return mini(root)
        
            
        
