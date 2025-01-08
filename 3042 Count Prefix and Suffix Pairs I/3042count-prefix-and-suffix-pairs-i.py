class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0

        def is_prefix_and_suffix(word1, word2):
            return len(word2) >= len(word1) and word1 == word2[:len(word1)] and word1 == word2[len(word2) - len(word1):]
        
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if is_prefix_and_suffix(words[i], words[j]):
                    res += 1
        return res

# Time: O(n^2*w)
# Space: O(w)