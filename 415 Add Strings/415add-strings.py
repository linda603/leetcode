class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        i = len(num1) - 1
        j = len(num2) - 1
        res = []

        while i >= 0 or j >= 0:
            val1 = int(num1[i]) if i >= 0 else 0
            val2 = int(num2[j]) if j >= 0 else 0
            val = val1 + val2 + carry

            res.append(str(val % 10))
            carry = val // 10
            i -= 1
            j -= 1

        if carry:
            res.append("1")
        return "".join(res[::-1])

# Time: O(max(n1, n2))
# Space: O(max(n1, n2))