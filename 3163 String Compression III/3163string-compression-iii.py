class Solution:
    def compressedString(self, word: str) -> str:
        res = []

        i = 0
        while i < len(word):
            cnt = 1
            while i + 1 < len(word) and word[i] == word[i + 1] and cnt < 9:
                i += 1
                cnt += 1
            res.append(str(cnt))
            res.append(word[i])
            i += 1
        return "".join(res)

# Time: O(n)
# Space: O(n) due to res