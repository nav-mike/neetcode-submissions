class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = { i: [] for i in range(numCourses) }
        for k, v in prerequisites:
            adj[k].append(v)
        
        result = []
        visited, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            visited.add(course)
            cycle.add(course)

            for c in adj[course]:
                if not dfs(c):
                    return False
            
            result.append(course)
            cycle.remove(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return result