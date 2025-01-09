class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res = []
        l = 0
        r = len(s)

        for c in s:
            if c == "I":
                res.append(l)
                l += 1
            else:
                res.append(r)
                r -= 1
        return res + [l]

# Time: O(n)
# Space: O(n)