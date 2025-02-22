class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not s[l].isalpha() and not s[l].isdigit():
                l += 1
            while l < r and not s[r].isalpha() and not s[r].isdigit():
                r -= 1
            if s[l].lower() != s[r].lower():
                return self.valid(s, l + 1, r) or self.valid(s, l, r - 1)
            l += 1
            r -= 1
        return True
    
    def valid(self, s, l, r):
        while l < r:
            while not s[l].isalpha() and not s[l].isdigit():
                l += 1
            while not s[r].isalpha() and not s[r].isdigit():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

# Time: O(n)
# Space: O(1)