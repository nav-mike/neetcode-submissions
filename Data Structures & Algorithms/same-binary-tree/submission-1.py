# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False

        val_eq = p.val == q.val
        if not val_eq:
            return False
        
        if p.left and q.left:
            val_eq = val_eq and self.isSameTree(p.left, q.left)
        else:
            val_eq = val_eq and p.left is None and q.left is None
        
        if p.right and q.right:
            val_eq = val_eq and self.isSameTree(p.right, q.right)
        else:
             val_eq = val_eq and p.right is None and q.right is None
        
        return val_eq