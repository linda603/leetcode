class Solution:
    def myAtoi(self, s: str) -> int:
        # 1. Strip all leading spaces
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        if i == len(s):
            return 0

        INT_MAX = 2**31 - 1 # pow(2, 31) - 1
        INT_MIN = -2**31
        
        # 2. Check for the sign
        is_positive = True
        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            i += 1
            is_positive = False
        
        # 3. Parse digits
        res = 0
        while i < len(s) and s[i].isdigit():
            # handle overflow res
            if (res > INT_MAX // 10) or (res == INT_MAX // 10 and int(s[i]) > INT_MAX % 10):
                return INT_MAX if is_positive else INT_MIN

            res = res * 10 + int(s[i])
            i += 1
        return res if is_positive else -res

# Time: O(n)
# Space: O(1)