class Solution:
    def minimumLength(self, s: str) -> int:
        count = {}

        for c in s:
            count[c] = 1 + count.get(c, 0)
        
        res = 0
        for c, freq in count.items():
            if freq == 1 or freq == 2:
                res += freq
            elif freq % 2 == 1:
                res += 1
            elif freq % 2 == 0:
                res += 2
        return res

# Time: O(n + 26) = O(n)
# Space: O(26) = O(1)   