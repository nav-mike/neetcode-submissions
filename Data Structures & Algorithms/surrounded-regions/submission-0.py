class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        # visited = set()

        def dfs(row, col):
            if (row not in range(rows) or
                col not in range(cols) or
                # (row, col) in visited or
                board[row][col] != 'O'):
                return
            
            # visited.add((row, col))
            board[row][col] = 'T'
        
        for col in range(cols):
            dfs(0, col)
            dfs(rows-1, col)

        for row in range(rows):
            dfs(row, 0)
            dfs(row, cols-1)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'T':
                    board[row][col] = 'O'