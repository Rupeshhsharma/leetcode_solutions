link- https://leetcode.com/problems/binary-tree-right-side-view/description/
code:
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []
        queue=deque([root])
        ans=[]
        while queue:
            demo=[]
            for _ in range(len(queue)):
                node=queue.popleft()
                demo.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(demo[-1])
        return ans



        
