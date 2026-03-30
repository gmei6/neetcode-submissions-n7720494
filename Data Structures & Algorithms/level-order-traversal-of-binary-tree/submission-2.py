# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
        queue = collections.deque()
        queue.append(root)

        while queue:
            length = len(queue)
            level = []
            
            for i in range(0, length):
                current = queue.popleft()

                if current:
                    level.append(current.val)
                    if current.left:
                        queue.append(current.left)

                    if current.right:
                        queue.append(current.right)

            if level:
                result.append(level)



        return result
    
    