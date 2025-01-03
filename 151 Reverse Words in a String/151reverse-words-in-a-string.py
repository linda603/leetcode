class Solution:
    def reverseWords(self, s: str) -> str:
        s += " "
        res = []
        curr = ""

        for c in s:
            if c == " ":
                if curr:
                    res.append(curr)
                    curr = ""
            else:
                curr += c
        res.reverse()
        return " ".join(res)

# Time: O(n + n)
# Space: O(n)
