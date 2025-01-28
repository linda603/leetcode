class Solution:
    def intToRoman(self, num: int) -> str:
        digit_to_symbol = [[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"], [50, "L"], [40, "XL"], [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]]
        res = ""

        for i in range(len(digit_to_symbol)):
            cnt = num // digit_to_symbol[i][0]
            res += cnt * digit_to_symbol[i][1]
            num = num % digit_to_symbol[i][0]
            if not num:
                break
        return res

# Time: O(1)
# Space: O(1)