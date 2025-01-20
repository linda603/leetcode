class list_node:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.map = [list_node() for i in range(1000)]

    def hash(self, key):
        return key % 1000

    def put(self, key: int, value: int) -> None:
        idx = self.hash(key)
        curr = self.map[idx]

        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        curr.next = list_node(key, value)

    def get(self, key: int) -> int:
        idx = self.hash(key)
        curr = self.map[idx]
        
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        idx = self.hash(key)
        curr = self.map[idx]

        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                break
            curr = curr.next
        return

# Time: O(1). Worst case O(1000), 1000 keys have the same hash idx
# Space: O(1000) = O(1)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)