class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not s[l].isdigit() and not s[l].isalpha():
                l += 1
            while l < r and not s[r].isdigit() and not s[r].isalpha():
                r -= 1
            if s[l] != s[r]:
                return self.is_palindrome(s, l + 1, r) or self.is_palindrome(s, l, r - 1)
            l += 1
            r -= 1
        return True
    
    def is_palindrome(self, s, l, r):

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

# Time: O(n)
# Space: O(1)
