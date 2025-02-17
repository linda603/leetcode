class Solution:

    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            odd_count = self.get_pal(s, i, i)
            even_count = self.get_pal(s, i, i + 1) if i + 1 < len(s) else 0
            res += odd_count + even_count
        return res
    
    def get_pal(self, s, l, r):
        count = 0

        while l >= 0 and r < len(s):
            if s[l] != s[r]:
                break
            l -= 1
            r += 1
            count += 1
        return count

# Time: O(n^2)
# Space: O(1)