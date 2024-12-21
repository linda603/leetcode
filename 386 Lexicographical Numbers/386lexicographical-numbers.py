class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        num = 1

        while len(res) < n:
            res.append(num)
            if num * 10 <= n:
                num = num * 10
            else:
                while num >= n or num % 10 == 9:
                    num = num // 10
                num += 1
        return res

# Time: O(n)
# Space: O(1)