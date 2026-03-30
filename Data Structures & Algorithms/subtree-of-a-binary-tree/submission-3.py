from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # This seems like a continuation of the "same tree" problem. 
        # I suppose we first attempt to find the matching node, and from there, 
        # we determine if the trees are the same
        queue = deque()
        queue.append(root)
        
        while queue:
            curr = queue.popleft()
            if not curr:
                if not subRoot:
                    return True

            if curr and curr.val == subRoot.val:
                # Now we apply the search to determine if the two trees are equal
                if self.sameTree(curr, subRoot):
                    return True
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        print(curr.val)
        return False
    
    def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return (self.sameTree(p.left, q.left) and 
        self.sameTree(p.right, q.right))
        

