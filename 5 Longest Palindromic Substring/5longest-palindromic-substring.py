class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        max_len = 0
        
        for i in range(len(s)):
            odd = self.get_longest_pal(s, i, i)
            even = self.get_longest_pal(s, i, i + 1)
            if len(odd) > max_len:
                max_len = len(odd)
                res = odd
            if len(even) > max_len:
                max_len = len(even)
                res = even
        return res
    
    def get_longest_pal(self, string, l, r):

        while l >= 0 and r < len(string):
            if string[l] != string[r]:
                break
            l -= 1
            r += 1
        return string[l + 1: r]

# Time: O(n^2)
# Space: O(n + n)