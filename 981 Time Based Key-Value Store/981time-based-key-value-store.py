class TimeMap:

    def __init__(self):
        self.stores = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.stores:
            self.stores[key] = []
        self.stores[key].append([timestamp, value])
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.stores:
            return ""
        lists = self.stores[key]

        l = 0
        r = len(lists) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2
            if lists[mid][0] <= timestamp:
                res = lists[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res

# Time: O(1) for set(), O(logn) for get()
# Space: O(n)

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)