class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n
        if k == 0: return res

        l = 0
        curr_sum = 0
        for r in range(n + abs(k)):
            curr_sum += code[r % n]

            if r - l + 1 > abs(k):
                curr_sum -= code[l % n]
                l = (l + 1) % n
            
            if r - l + 1 == abs(k):
                if k > 0:
                    res[(l - 1) % n] = curr_sum
                else:
                    res[(r + 1) % n] = curr_sum
        return res

# Time: O(n + k)
# Space: O(n)