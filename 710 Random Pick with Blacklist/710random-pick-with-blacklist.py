class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        # [0, 1, 2, 3, 4, 5, 6]
        #             |<------>
        #                 tmp, remove 5 = [4, 6]
        # whitelist = {2: 4, 3: 6}
        self.n = n
        self.len_half_left = n - len(blacklist) # half left length
        self.whitelist = {} # map all val in the backlist in the left half to the value in tmp

        tmp = set(i for i in range(self.len_half_left, n))
        for num in blacklist:
            if num in tmp:
                tmp.remove(num)
        arr = [num for num in tmp]
        i = 0

        for num in blacklist:
            if num < self.len_half_left:
                self.whitelist[num] = arr[i]
                i += 1

    def pick(self) -> int:
        pick_val = int(random.random() * self.len_half_left)
        if pick_val in self.whitelist:
            return self.whitelist[pick_val]
        return pick_val

# Time: O((n - m) + m) = O(n). m: len(blacklist)
# Space: O(m + (n - m)) = O(n) due to tmp, arr, O(n - m): self.whitelist

# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()