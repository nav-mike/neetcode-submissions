# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        q = deque([root])

        while q:
            tmp = None
            for _ in range(len(q)):
                node = q.popleft()
                if not node: continue
                q.append(node.left)
                q.append(node.right)
                tmp = node
            
            if tmp: result.append(tmp.val)

        return result