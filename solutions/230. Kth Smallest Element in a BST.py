# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def dfs(node):
            if not node or len(res) == k:
                return

            dfs(node.left)
            if len(res) < k:
                res.append(node.val)
            dfs(node.right)

        dfs(root)
        return res[-1]
