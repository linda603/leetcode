class list_node:
    def __init__(self, count=0):
        self.keys_set = set()
        self.count = count
        self.prev = None
        self.next = None

class AllOne:

    def __init__(self):
        # initialize double linked list with dummy node left and right in increasing order
        self.record = {}
        self.left = list_node()
        self.right = list_node()
        self.left.next = self.right
        self.right.prev = self.left
    
    def delete(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    # insert curr node after prev node
    def insert(self, prev, curr):
        nxt = prev.next
        prev.next = nxt.prev = curr
        curr.prev = prev
        curr.next = nxt

    def inc(self, key: str) -> None:
        # if key is new, add it to the left
        if key not in self.record:
            curr = self.left
        else:
            curr = self.record[key]
            curr.keys_set.remove(key)
        
        # if the next node count != curr count + 1, create the new node
        if curr.next.count != curr.count + 1:
            new_node = list_node(curr.count + 1)
            self.insert(curr, new_node)
        else:
            new_node = curr.next
        new_node.keys_set.add(key)
        self.record[key] = new_node
    
        # remove the curr node if it's empty
        if not curr.keys_set and curr.count != 0:
            self.delete(curr)  
        return

    def dec(self, key: str) -> None:
        if key not in self.record:
            return
        curr = self.record[key]
        curr.keys_set.remove(key)

        if curr.count == 1:
            del self.record[key]
        else:
            if curr.prev.count != curr.count - 1:
                new_node = list_node(curr.count - 1)
                self.insert(curr.prev, new_node)
            else:
                new_node = curr.prev
            new_node.keys_set.add(key)
            self.record[key] = new_node


        # remove the curr node if it's empty
        if not curr.keys_set and curr.count != 0:
            self.delete(curr)

    def getMaxKey(self) -> str:
        if self.right.prev.count == 0:
            return ""
        # return the first key: next(iter(self.right.prev.keys_set))
        for key in self.right.prev.keys_set:
            return key

    def getMinKey(self) -> str:
        if self.left.next.count == 0:
            return ""
        for key in self.left.next.keys_set:
            return key

# Time: O(1)
# Space: O(n). n: len(self.record)


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()