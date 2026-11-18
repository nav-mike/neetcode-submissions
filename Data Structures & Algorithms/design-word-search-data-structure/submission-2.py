class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root

        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        
        cur.is_word = True
        

    def search(self, word: str) -> bool:
        def dfs(index, cur):
            for i in range(index, len(word)):
                w = word[i]

                if w == ".":
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if w not in cur.children:
                        return False
                    cur = cur.children[w]
            
            return cur.is_word
        
        return dfs(0, self.root)
        
