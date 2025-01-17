class list_node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.head = list_node(-1, -1)
        self.tail = list_node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def delete(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    
    # insert node after the head (MRU)
    def insert(self, node):
        nxt = self.head.next
        self.head.next = nxt.prev = node
        node.prev = self.head
        node.next = nxt

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.delete(self.cache[key])
        # reuse the same node to insert the node
        self.insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
            self.insert(self.cache[key])
            self.cache[key].val = value
        else:
            if len(self.cache) == self.cap:
                lru = self.tail.prev
                self.delete(lru)
                del self.cache[lru.key]
            self.cache[key] = list_node(key, value)
            self.insert(self.cache[key])
        return

# Time: O(1)
# Space: O(capacity)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)