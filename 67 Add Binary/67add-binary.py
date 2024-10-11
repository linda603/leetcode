class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        res = []
        carry = 0
        i = 0

        for i in range(max(len(a), len(b))):
            val1 = int(a[i]) if i < len(a) else 0
            val2 = int(b[i]) if i < len(b) else 0
            val = val1 + val2 + carry
            carry = val // 2
            res.append(str(val % 2))

        if carry: res.append("1")
        res = res[::-1]
        return "".join(res)

#Time: O(n + m + n + n). Example: n: larger array
#Space: O(n)