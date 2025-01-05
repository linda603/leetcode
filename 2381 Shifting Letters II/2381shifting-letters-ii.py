class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        diff = [0] * (len(s) + 1)

        for start, end, direction in shifts:
            if direction:
                diff[start] += 1
                diff[end + 1] -= 1
            else:
                diff[start] -= 1
                diff[end + 1] += 1

        return self.convert(s, diff)
    
    def convert(self, s, diff):
        res = []
        count = 0

        for i in range(len(s)):
            count += diff[i]
            increment = (ord(s[i]) - ord("a") + count) % 26
            # update neg to pos
            increment = (increment + 26) % 26
            res.append(chr(ord("a") + increment))
        return "".join(res)

# Time: O(m + n) = O(m + n). m: len(shifts), n: len(s)
# Space: O(n)