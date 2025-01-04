class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        right = {}
        left = set()
        res = set()

        for i in range(1, len(s)):
            right[s[i]] = 1 + right.get(s[i], 0)

        for mid in range(1, len(s) - 1):
            left.add(s[mid - 1])
            right[s[mid]] -= 1
            if right[s[mid]] == 0:
                del right[s[mid]]
            
            for c in left:
                if c in right:
                    res.add((c, s[mid]))
        return len(res)

# Time: O(n + n*26) = O(n)
# Space: O(26 + 26 + len(res) = 26^2) = O(1)
            