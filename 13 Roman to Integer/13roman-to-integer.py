class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_to_num = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res = 0

        for i in range(len(s)):
            if i + 1 < len(s) and symbol_to_num[s[i + 1]] > symbol_to_num[s[i]]:
                res -= symbol_to_num[s[i]]
            else:
                res += symbol_to_num[s[i]]
        return res

# Time: O(n)
# Space: O(1)