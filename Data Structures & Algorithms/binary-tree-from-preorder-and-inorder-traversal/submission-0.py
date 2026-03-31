# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Root is always 1st node in preorder
        # find the index of the root in the inorder
        if preorder:
            root_index = inorder.index(preorder[0])
            left = self.buildTree(preorder[1:root_index + 1], inorder[:root_index])
            right = self.buildTree(preorder[root_index + 1:], inorder[root_index+1:])

            root = TreeNode(preorder[0], left, right)
            return root
        return None