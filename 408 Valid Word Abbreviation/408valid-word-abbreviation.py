class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        digits = "0123456789"

        while i < len(word) and j < len(abbr):
            if abbr[j] in digits:
                if abbr[j] == "0":
                    return False
                length = 0
                while j < len(abbr) and abbr[j] in digits:
                    length = length * 10 + int(abbr[j])
                    j += 1
                i = i + length
            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        return True if i == len(word) and j == len(abbr) else False

# Time: O(m + n)
# Space: O(1)