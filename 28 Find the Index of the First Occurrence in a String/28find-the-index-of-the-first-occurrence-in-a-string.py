class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1

        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return i
        return -1

# Time: O(mn). n: len(haystack), m: len(needle)
# Space: O(1)