class NumberContainers:

    def __init__(self):
        self.idx_num = {} # idx: num
        self.num_idx = defaultdict(SortedList) # num: list of idx

    def change(self, index: int, number: int) -> None:
        if index in self.idx_num:
            val = self.idx_num[index]
            self.num_idx[val].remove(index)
            if not self.num_idx[val]:
                del self.num_idx[val]

        self.idx_num[index] = number
        self.num_idx[number].add(index)

    def find(self, number: int) -> int:
        if number not in self.num_idx:
            return -1
        return self.num_idx[number][0]
        
# Time: change() O(logn), find() O(logn)
# Space: O(n)

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)