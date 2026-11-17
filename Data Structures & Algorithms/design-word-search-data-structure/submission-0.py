class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = Node()
            cur = cur.children[w]
        
        cur.is_word = True
        

    def search(self, word: str) -> bool:
        def dfs(cur, index):
            for i in range(index, len(word)):
                if word[i] == ".":
                    for child in cur.children.values():
                        if not dfs(child, i):
                            return False
                    return True
                else:
                    if word[i] not in cur.children:
                        cur.children[word[i]] = Node()
                    cur = cur.children[word[i]]
            return cur.is_word
        
        return dfs(self.root, 0)
        
