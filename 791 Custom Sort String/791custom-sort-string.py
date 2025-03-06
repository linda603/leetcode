class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = {}
        for c in s:
            if c not in count:
                count[c] = 0
            count[c] += 1
        
        res = ""
        for c in order:
            if c in count:
                res += c * count[c]
                del count[c]
        
        for c, cnt in count.items():
            res += c * count[c]
        return res

# Time: O(n + m). n: len(s), m: len(order)
# Space: O(26 + n)