class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = [-1, -1]
        max_len = 0

        for i in range(len(s)):
            odd_len = self.get_longest_pal(s, i, i)
            even_len = self.get_longest_pal(s, i, i + 1)
            if odd_len > max_len:
                max_len = odd_len
                dist = max_len // 2
                res = [i - dist, i + dist]
            if even_len > max_len:
                max_len = even_len
                dist = max_len // 2 - 1
                res = [i - dist, i + dist + 1]
        l, r = res
        return s[l: r + 1]
    
    def get_longest_pal(self, s, l, r):
        
        while l >= 0 and r < len(s):
            if s[l] != s[r]:
                break
            l -= 1
            r += 1
        return r - l - 1

# Time: O(n^2)
# Space: O(1)