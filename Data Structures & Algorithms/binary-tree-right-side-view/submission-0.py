# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = collections.deque()
        rightview = []
        queue.append(root)

        while queue:
            length = len(queue) - 1
            curr = queue.popleft()

            

            if curr:
                rightview.append(curr.val)
                queue.append(curr.right)
                queue.append(curr.left)

                for _ in range(0, length):
                    temp = queue.popleft()
                    if temp:
                        queue.append(temp.right)
                        queue.append(temp.left)

            

        return rightview