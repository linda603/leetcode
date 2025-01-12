class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []
        res = []

        for i in range(1, min(4, len(s))):
            if not self.is_valid(s[:i]):
                continue
            curr = ["", "", "", ""]
            curr[0] = s[:i]
            for j in range(i + 1, min(i + 4, len(s))):
                if not self.is_valid(s[i: j]):
                    continue
                curr[1] = s[i: j]
                for k in range(j + 1, min(j + 4, len(s))):
                    if self.is_valid(s[j: k]) and self.is_valid(s[k:]):
                        curr[2] = s[j: k]
                        curr[3] = s[k:]
                        res.append(".".join(curr))
        return res
    
    def is_valid(self, string):
        num = int(string)
        return num <= 255 and len(string) == len(str(num))

# Time: O(3^4*4) = O(1)
# Space: O(1)