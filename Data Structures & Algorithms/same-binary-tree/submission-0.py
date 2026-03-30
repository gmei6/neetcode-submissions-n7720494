# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # We check if the two trees have the same heights for each node?
        test = self.height(p, q)
        print(test)
        if test == -1:
            return False
        return True


    def height(self, root_p, root_q) -> int:
        if not root_p or not root_q:
            if root_p or root_q:
                return -1
            return 0

        if root_p.val != root_q.val:
            return -1
        
        left = self.height(root_p.left, root_q.left)
        right = self.height(root_p.right, root_q.right)

        if left + right < 0:
            return -1

        return 0

