class Solution:
    def canChange(self, start: str, target: str) -> bool:
        i = j = 0
        start += "#"
        target += "#"

        while i < len(start) and j < len(target):
            while i < len(start) and start[i] == "_":
                i += 1
            while j < len(target) and target[j] == "_":
                j += 1
            if start[i] != target[j] or (start[i] == "L" and i < j) or (start[i] == "R" and i > j):
                return False
            i += 1
            j += 1
        return True

# Time: O(m + n)
# Space: O(1)