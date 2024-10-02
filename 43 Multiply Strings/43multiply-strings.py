class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        res = [0] * (len(num1) + len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = int(num1[i]) * int(num2[j])
                res[i + j] += digit
                res[i + j + 1] += res[i + j] // 10
                res[i + j] = res[i + j] % 10
        res = res[::-1]

        # num1 = 10, num2 = 10
        # res = [0, 1, 0, 0] -> there is 1 leading 0
        start = 0
        while start < len(res) and res[start] == 0:
            start += 1
        res = res[start:]

        for i, val in enumerate(res):
            res[i] = str(val)

        return "".join(res)

#Time: O(mn + 3(m+n)) = O(mn)
#Space: O(m+n)