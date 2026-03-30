# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.result = None
        
        self.helper(root)
        return self.result

    def helper(self, node):
        # Base case or stop if we already found the result
        if not node or self.result is not None:
            return
        
        # Traverse Left
        self.helper(node.left)
        
        # Process Current Node
        self.k -= 1
        if self.k == 0:
            self.result = node.val
            return
        
        # Traverse Right
        self.helper(node.right)

'''
procedure inorder(node)
    if node is not null
        inorder(node.left)
        visit(node)
        inorder(node.right)
end procedure
'''
