# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    flag = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.height(root)
        return self.flag 
        
    
    def height(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        right = self.height(node.right)
        left = self.height(node.left)

        global flag

        if abs(right - left) > 1:
            self.flag = False
        return 1 + max(left, right)