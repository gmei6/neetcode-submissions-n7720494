# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        list_node = [[root]]
        list_val = [[root.val]]



        return self.bfs(list_node, list_val)
    
    def bfs(self, nodes: List[List[TreeNode]], output: List[List[int]]) -> List[List[int]]:
        node_list = []
        val_list = []


        for curr in nodes[-1]:
            if curr.left:
                node_list.append(curr.left)
                val_list.append(curr.left.val)
            if curr.right:
                node_list.append(curr.right)
                val_list.append(curr.right.val)
        if node_list and val_list:
            nodes.append(node_list)
            output.append(val_list)
            return self.bfs(nodes, output)
        return output