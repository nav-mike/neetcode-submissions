class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n
        components = n

        def find(node):
            result = node
            while result != parent[result]:
                parent[result] = parent[parent[result]]
                result = parent[result]
            
            return result
        
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)

            if parent1 == parent2:
                return 0
            
            if rank[parent2] > rank[parent1]:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]
            else:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]
            
            return 1

        for n1, n2 in edges:
            n -= union(n1, n2)
        
        return n