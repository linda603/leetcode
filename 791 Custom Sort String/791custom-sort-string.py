class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        res = ""

        for c in order:
            if c in count:
                res += c * count[c]
                del count[c]
        
        for c in count:
            res += c * count[c]
        return res

# Time: O(m + n)
# Space: O(26) = O(1)