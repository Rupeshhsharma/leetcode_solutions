link- https://leetcode.com/problems/maximum-width-of-binary-tree/description/
code:
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        if not root:
                return 0
        queue=deque([(root,0)])
        ans=0
        while queue:
            start=queue[0][1]
            size=len(queue)
            for _ in range(size):
                node,idx =queue.popleft()
                idx-=start
                end=idx
                if node.left:
                    queue.append((node.left,2*idx))  #it counts the index for every left it remain 0 but for every right it get increased
                if node.right:
                    queue.append((node.right,2*idx+1))
            ans=max(ans,end+1)
        return ans
        

        
