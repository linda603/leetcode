class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        count = [0] * 3
        l = 0

        for r in range(len(s)):
            count[ord(s[r]) - ord("a")] += 1
            while count[0] and count[1] and count[2]:
                res += len(s) - r
                count[ord(s[l]) - ord("a")] -= 1
                l += 1
        return res

# Time: O(n)
# Space: O(1)