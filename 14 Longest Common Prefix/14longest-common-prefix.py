class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            for word in strs:
                if i >= len(word) or word[i] != strs[0][i]:
                    return res
            res += word[i]
        return res

# Time: O(nl). n: len(strs), l: shortest len (word)
# Space: O(l). 