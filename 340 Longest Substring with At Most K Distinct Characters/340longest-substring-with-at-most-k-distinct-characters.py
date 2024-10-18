class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        window = {}
        res = 0

        l = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            while len(window) > k:
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1
            res = max(res, r - l + 1)
        return res

# Time: O(n)
# Space: O(26) = O(1)