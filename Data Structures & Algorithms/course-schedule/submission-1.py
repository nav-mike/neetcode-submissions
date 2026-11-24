class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = { i: [] for i in range(numCourses) }
        visited = set()

        for k, v in prerequisites:
            adj[k].append(v)
        
        def dfs(course):
            if len(adj[course]) == 0:
                return True
            if course in visited:
                return False
            
            visited.add(course)
            for c in adj[course]:
                if not dfs(c):
                    return False
            
            adj[course] = []
            visited.remove(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True