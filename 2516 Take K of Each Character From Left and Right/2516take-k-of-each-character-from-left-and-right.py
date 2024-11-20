class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0: return 0
        n = len(s)

        count = [0] * 3 # a, b, b
        for c in s:
            count[ord(c) - ord('a')] += 1
        
        if min(count) < k:
            return -1
        
        res = float("inf")
        l = 0
        for r in range(n):
            count[ord(s[r]) - ord('a')] -= 1
            while l < n and min(count) < k:
                count[ord(s[l]) - ord('a')] += 1
                l += 1
            res = min(res, n - (r - l + 1))
        
        return res if res != float("inf") else - 1

# Time: O(n + 2n) = O(1)
# Space: O(3) = O(1)