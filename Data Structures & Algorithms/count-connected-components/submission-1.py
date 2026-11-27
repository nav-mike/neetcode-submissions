class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n
        
        def find(node):
            current = node
            while current != parent[current]:
                parent[current] = parent[parent[current]]
                current = parent[current]
            
            return current
        
        def union(node1, node2):
            p1, p2 = find(node1), find(node2)

            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            
            return 1
        
        for n1, n2 in edges:
            n -= union(n1, n2)
        
        return n