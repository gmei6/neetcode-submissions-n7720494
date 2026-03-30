# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, float('-inf'))
    
    def dfs(self, curr: TreeNode, highest: int) -> int:
        temp = 0
        if not curr:
            return 0
        if curr.val >= highest:
            temp = 1
            highest = curr.val
        return temp + self.dfs(curr.left, highest) + self.dfs(curr.right, highest)