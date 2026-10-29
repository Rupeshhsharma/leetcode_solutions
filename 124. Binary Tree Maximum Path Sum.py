link- https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
code:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        maxi=float("-inf")
        def maxpath(root):
            nonlocal maxi
            if root is None:
                return 0
            left=max(0,maxpath(root.left))
            right=max(0,maxpath(root.right))
            maxi=max(maxi,left+right+root.val)
            return root.val + max(left,right)
        maxpath(root)
        return maxi

        
