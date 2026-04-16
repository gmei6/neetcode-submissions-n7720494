# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.total = float('-inf')
        
        def dfs(root: Optional[TreeNode]) -> tuple[int, int]:
            if not root:
                return 0
            
            left_to_gain = max(0, dfs(root.left))
            right_to_gain = max(0, dfs(root.right))

            self.total = max(self.total, root.val + max(0, left_to_gain) + max(0, right_to_gain))

            return root.val + max(left_to_gain, right_to_gain)
        
        dfs(root)
        return self.total