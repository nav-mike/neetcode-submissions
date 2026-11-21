class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = collections.deque()
        depth = 0
        ds = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def add_cell(row, col):
            if (row not in range(rows) or
                col not in range(cols) or
                (row, col) in visited or
                grid[row][col] == -1):
                return
            
            visited.add((row, col))
            q.append((row, col))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    visited.add((row, col))
                    q.append((row, col))
        
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = depth

                for dr, dc in ds:
                    add_cell(row+dr, col+dc)
            depth += 1