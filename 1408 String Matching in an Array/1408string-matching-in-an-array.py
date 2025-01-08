class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()

        for word1 in words:
            for word2 in words:
                if word1 == word2 or len(word1) < len(word2):
                    continue
                for i in range(len(word1)):
                    if word1[i: i + len(word2)] == word2:
                        res.add(word2)
        return [word for word in res]

# Time: O(n^2*w)
# Space: O(n + w)