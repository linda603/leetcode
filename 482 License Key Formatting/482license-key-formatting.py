class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        res = []
        count = 0

        for i in range(len(s) - 1, -1, -1):
            c = s[i].upper()
            if c == "-":
                continue
            if count != 0 and count % k == 0:
                res.append("-")
                count = 0
            res.append(c)
            count += 1
        res.reverse()
        return "".join(res)
    
    def convert_to_upper(self, char):
        diff = ord('A') - ord('a')
        if ord('a') <= ord(char) <= ord('z'):
            return chr(ord(char) + diff)
        return char

# Time: O(n + n)
# Space: O(n)