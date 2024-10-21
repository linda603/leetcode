class Solution:
    def partitionString(self, s: str) -> int:
        res = 0
        window = set()

        for c in s:
            if c in window:
                res += 1
                window = set()
            window.add(c)
        return res + 1

# Time: O(n)
# Space: O(26) = O(1)