class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges) + 1)

        def find(node):
            current = node
            while current != parent[current]:
                parent[current] = parent[parent[current]]
                current = parent[current]
            
            return current
        
        def union(node1, node2):
            p1, p2 = find(node1), find(node2)

            if p1 == p2:
                return False
            
            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
        
        return []