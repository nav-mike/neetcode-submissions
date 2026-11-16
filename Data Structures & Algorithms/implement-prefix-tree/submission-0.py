class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False

class PrefixTree:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = Node()
            cur = cur.children[w]
        cur.is_word = True


    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            if w not in cur.children:
                return False
            cur = cur.children[w]
        return cur.is_word
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for p in prefix:
            if p not in cur.children:
                return False
            cur = cur.children[p]
        return True
        
        