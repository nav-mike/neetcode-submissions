# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        inorder_hash = { val: index for index, val in enumerate(inorder) }
        preorder_index = 0

        def helper(left, right):
            nonlocal preorder_index

            if left > right:
                return None
            
            val = preorder[preorder_index]
            preorder_index += 1
            root_index = inorder_hash[val]

            root = TreeNode(val=val)
            root.left = helper(left, root_index-1)
            root.right = helper(root_index+1, right)

            return root
        
        return helper(0, len(preorder) - 1)