class RandomizedSet:

    def __init__(self):
        self.records = {}
        self.lists = []

    def insert(self, val: int) -> bool:
        if val in self.records:
            return False
        self.records[val] = len(self.lists)
        self.lists.append(val)

    def remove(self, val: int) -> bool:
        if val not in self.records:
            return False
        idx = self.records[val]
        # replace val of idx in lists to the last val of self.lists[-1]
        self.lists[idx] = self.lists[-1]
        self.records[self.lists[-1]] = idx
        # del val
        self.lists.pop()
        del self.records[val]
        return True

    def getRandom(self) -> int:
        idx = int(random.random() * len(self.lists))
        return self.lists[idx]

# Time: O(1) for insert(), remove(), getRandom()
# Space: O(n)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()