class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = { i: [] for i in range(n) }
        visited = set()

        for l, r in edges:
            adj[l].append(r)
            adj[r].append(l)
        
        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            
            for child in adj[node]:
                if child == parent:
                    continue
                if not dfs(child, node):
                    return False
            
            return True
        

        return dfs(0, -1) and len(visited) == n