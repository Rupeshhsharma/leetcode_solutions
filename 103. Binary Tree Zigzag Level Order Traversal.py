link- https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
code:
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        queue=deque([root])
        flag=0
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
            if flag==0:
                ans.append(demo)
                flag=1
            else:
                ans.append(demo[::-1])
                flag=0
        return ans

            


        
