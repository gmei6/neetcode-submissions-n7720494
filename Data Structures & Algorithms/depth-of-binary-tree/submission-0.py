from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxDepth = 0

        curr = root
        queue = deque()

        if curr == None:
            return 0
        queue.append((curr, 1))

        while queue:
            currNode, depth = queue.pop()

            maxDepth = max(depth, maxDepth)

            if currNode.left:
                queue.append((currNode.left, depth + 1))
            if currNode.right:
                queue.append((currNode.right, depth + 1))

        return maxDepth
            

