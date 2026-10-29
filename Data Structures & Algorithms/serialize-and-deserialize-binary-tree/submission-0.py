# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []

        def dfs(node):
            if node is None:
                result.append("N")
                return

            result.append(str(node.val))
            
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(result)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None

        values = data.split(",")
        index = 0

        def dfs():
            nonlocal index

            value = values[index]
            index += 1
            
            if value == "N":
                return None
            
            node = TreeNode(val=int(value))
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()
