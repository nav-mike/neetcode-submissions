# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = root.val

        def dfs(node):
            nonlocal max_path

            if node is None:
                return 0
            
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            max_path = max(max_path, left + right + node.val)

            return max(left, right) + node.val

        dfs(root)

        return max_path