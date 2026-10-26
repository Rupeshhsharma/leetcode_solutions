link- https://leetcode.com/problems/diameter-of-binary-tree/description/
code:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi=0
        def dia(root):
            nonlocal maxi
            if root is None:
                return 0
            left=dia(root.left)
            right=dia(root.right)
            maxi=max(maxi,left+right)
            return 1+max(left,right)
        dia(root)
        return maxi
            
            
        
