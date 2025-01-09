class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0

        for word in words:
            if len(word) >= len(pref) and word[:len(pref)] == pref:
                res += 1
        return res

# Time: O(n*p). n: len(words), p: len(pref)
# Space: O(p)