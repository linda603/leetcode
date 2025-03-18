class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        max_length = 0

        for i in range(len(s)):
            odd = self.get_longest_pal(s, i, i)
            even = self.get_longest_pal(s, i, i + 1) if i + 1 < len(s) else ""
            if len(odd) > max_length:
                max_length = len(odd)
                res = odd
            if len(even) > max_length:
                max_length = len(even)
                res = even
        return res

    def get_longest_pal(self, s, left, right):
        
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
            left -= 1
            right += 1
        return s[left + 1 : right]

# Time: O(n^2)
# Space: O(n)