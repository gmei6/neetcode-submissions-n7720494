# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> None:
        self.max_diameter = 0

        def maxDepth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_height = maxDepth(node.left)
            right_height = maxDepth(node.right)
            
            self.max_diameter = max(left_height + right_height, self.max_diameter)

            return 1 + max(left_height, right_height)
        
        maxDepth(root)


        

        


        return self.max_diameter