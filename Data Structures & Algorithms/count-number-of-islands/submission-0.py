class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(row, col):
            visited.add((row, col))
            q = collections.deque()
            q.append((row, col))

            while q:
                r, c = q.popleft()
                for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    row, col = r + dr, c + dc
                    if (row not in range(rows) or
                        col not in range(cols) or
                        (row, col) in visited or
                        grid[row][col] != "1"):
                        continue
                        
                    visited.add((row, col))
                    q.append((row, col))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1

        return islands