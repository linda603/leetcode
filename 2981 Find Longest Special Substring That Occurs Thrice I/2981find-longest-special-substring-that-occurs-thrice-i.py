class Solution:
    def maximumLength(self, s: str) -> int:
        count = {}
        res = -1

        for i in range(len(s)):
            substring = ""
            char = s[i]
            for j in range(i, len(s)):
                if s[j] != char:
                    break
                substring += s[j]
                count[substring] = 1 + count.get(substring, 0)
                if count[substring] >= 3 and len(substring) > res:
                    res = len(substring)
        return res

# Time: O(n^2)
# Space: O(n^2)