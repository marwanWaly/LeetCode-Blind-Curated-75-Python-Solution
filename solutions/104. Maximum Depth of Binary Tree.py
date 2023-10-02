# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # # recursion
        # if not root:
        #     return 0
        
        # return 1 + max(self.maxDepth(node.left), self.maxDepth(node.right))

        # Iterative
        stack = [(1, root)]
        max_depth = 0
        while stack:
            node_depth, node = stack.pop()
            if node:
                max_depth = max(max_depth, node_depth)
                stack.append((node_depth + 1, node.left))
                stack.append((node_depth + 1, node.right))
        return max_depth
