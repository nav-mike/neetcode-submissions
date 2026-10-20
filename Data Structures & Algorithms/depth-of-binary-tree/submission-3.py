# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        q = deque([root])
        depth = 0

        while q:
            
            for i in range(len(q)):
                r = q.popleft()
                if r.left: q.append(r.left)
                if r.right: q.append(r.right)
            
            depth += 1
        
        return depth