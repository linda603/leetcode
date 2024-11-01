class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []

        for i in range(len(s)):
            if i - 2 >= 0 and s[i] == s[i - 1] and s[i] == s[i - 2]:
                continue
            res.append(s[i])
        return "".join(res)

# Time: O(n)
# Space: O(n)