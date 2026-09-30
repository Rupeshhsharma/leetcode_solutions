link- https://leetcode.com/problems/binary-tree-preorder-traversal/description/
code:
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        a=[]
        def preorder(root):
            if root is None:
                return
            a.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return a
        
