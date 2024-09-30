class SnapshotArray:

    def __init__(self, length: int):
        self.record = [[[0, 0]] for i in range(length)]
        self.snap_id = 0

# Input: ["SnapshotArray", "set", "snap", "set", "get"]
#        [[3],              [0, 5], [],   [0, 6], [0, 0]]
#   l                   r
# [[[0, 0], [0, 5], [1, 6]],
#  [[0, 0]],
#  [[0, 0]]]

    def set(self, index: int, val: int) -> None:
        self.record[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        res = 0
        data = self.record[index]
        l = 0
        r = len(data) - 1
        while l <= r:
            mid = (l + r) // 2
            if data[mid][0] <= snap_id:
                res = data[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res

#Time: set O(1), get O(log(data)).
#Space: O(n). n: length

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)