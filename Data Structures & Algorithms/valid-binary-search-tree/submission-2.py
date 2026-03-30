# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float('inf'), float('-inf'))
    
    def helper(self, root: Optional[TreeNode], left_max: int, right_min: int) -> bool:
        if not root:
            return True

        if root.val >= left_max or root.val <= right_min:
            return False
        
        old_left = left_max
        if root.val < left_max:
            left_max = root.val

        old_right = right_min
        if root.val > right_min:
            right_min = root.val
        
        return self.helper(root.left, left_max, old_right) and self.helper(root.right, old_left, right_min)
        

        
        

