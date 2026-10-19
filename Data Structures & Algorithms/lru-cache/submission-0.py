class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left
    
    def _append(self, node):
        self.right.prev.next = node
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev = node
    
    def _remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        node.prev = node.next = None
        

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        
        self._remove(self.cache[key])
        self._append(self.cache[key])
        
        return self.cache[key].value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self._remove(self.cache[key])
            self._append(self.cache[key])
            return
        
        self.cache[key] = Node(key, value)
        self._append(self.cache[key])

        if len(self.cache) > self.capacity:
            node = self.cache[self.left.next.key]
            self._remove(node)
            del self.cache[node.key]
        
