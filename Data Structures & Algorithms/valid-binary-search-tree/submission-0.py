# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        left_val = root.val > root.left.val if root.left else True
        right_val = root.val < root.right.val if root.right else True

        is_valid = left_val and right_val

        left = self.isValidBST(root.left) if root.left else True
        right = self.isValidBST(root.right) if root.right else True

        return is_valid and left and right
