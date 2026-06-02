from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # Maybe queue up nodes in a way such that we have
        #[root, root.left, root.right, r.l.r, r.r.r, ]
        if not root:
            return 'x'
        queue = deque()
        queue.append(root)
        string = ""
        while queue:

            curr = queue.popleft()

            if curr is not None:
                queue.append(curr.left)
                queue.append(curr.right)
                string += str(curr.val) + ','
            else:
                string += 'x,'
        return string
            
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # the string format should be "3,5,2,x,34,5,8"
        # where x is a null, ie no node
        # the graph should be like:
        #            3
        #           /   \
        #          5       2
        #           \     / \
        #           34    5  8
        
        if data == 'x':
            return None

        values = data.split(',')
        root = TreeNode(int(values[0]))
        queue = deque([root])
        i = 1

        while queue and i < len(values):
            curr = queue.popleft()

            if values[i] != "x":
                curr.left = TreeNode(int(values[i]))
                queue.append(curr.left)
            i += 1

            if i < len(values) and values[i] != "x":
                curr.right = TreeNode(int(values[i]))
                queue.append(curr.right)
            i += 1
        return root


