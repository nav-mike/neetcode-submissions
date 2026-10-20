# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result, _ = self.dfs(root)

        return result
    
    def dfs(self, root):
        if not root:
            return (True, 0)
        
        left_b, left_h = self.dfs(root.left)
        right_b, right_h = self.dfs(root.right)

        return (left_b and right_b and abs(left_h - right_h) <= 1, 1 + max(left_h, right_h))