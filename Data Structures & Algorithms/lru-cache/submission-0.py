from collections import defaultdict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        
        # Map key to node
        self.cache = {}
        
        # left = least recently used
        # right = most recently used
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    # remove node from list
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev


    # insert node at right
    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.next, node.prev = next, prev
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
    
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None
