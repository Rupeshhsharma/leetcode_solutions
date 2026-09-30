link - https://leetcode.com/problems/binary-tree-level-order-traversal/description/
Code:
# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        queue=deque([root])
        ans=[]
        while queue:
            demo=[]
            for _ in range(len(queue)):
                node = queue.popleft()
                demo.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(demo)
        return ans


            
        
