class Trie():
    def __init__(self):
        self.children = {}
        self.word = False
    
    
    def add_word(self, word):
        cur = self

        for w in word:
            if w not in cur.children:
                cur.children[w] = Trie()
            cur = cur.children[w]
        
        cur.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = set()
        root = Trie()
        visited = set()
        
        rows, cols = len(board), len(board[0])

        for word in words:
            root.add_word(word)

        def dfs(row, col, node, word):
            if (row not in range(rows) or
                col not in range(cols) or
                (row, col) in visited or
                board[row][col] not in node.children):
                return
            
            visited.add((row, col))
            word += board[row][col]
            node = node.children[board[row][col]]

            if node.word:
                node.word = False
                result.add(word)
            
            dfs(row+1, col, node, word)
            dfs(row-1, col, node, word)
            dfs(row, col+1, node, word)
            dfs(row, col-1, node, word)

            visited.remove((row, col))
        
        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root, "")

        return list(result)
        