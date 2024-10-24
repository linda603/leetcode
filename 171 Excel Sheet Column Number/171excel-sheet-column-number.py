class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        # char to digit 'A': 1 = char - 'A' + 1
        for c in columnTitle:
            digit = ord(c) - ord('A') + 1
            res = res * 26 + digit
        return res

# Time: O(n)
# Space: O(1)