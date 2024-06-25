class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        
        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:] #Copy of palindrome takes O(n) space
            
        return palindrome[:-1] + 'b'

#Time: O(n)
#Space: O(n)