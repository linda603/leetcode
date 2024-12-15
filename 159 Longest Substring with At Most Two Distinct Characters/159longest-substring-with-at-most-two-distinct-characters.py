class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        count = {}
        res = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            while len(count) > 2:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                l += 1
            res = max(res, r - l + 1)
        return res

# Time: O(n)
# Space: O(1)