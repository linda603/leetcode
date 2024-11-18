class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n = len(words)
        order_idx = {c: i for i, c in enumerate(order)}

        for i in range(n - 1):
            word1 = words[i]
            word2 = words[i + 1]
            # compare word1 and word2 to check the first diff character
            for j in range(len(word1)):
                if j == len(word2):
                    return False # word2 is shortert than word1
                if word1[j] != word2[j]:
                    if order_idx[word1[j]] > order_idx[word2[j]]:
                        return False
                    break # order is valid
        return True

# Time: O(m + n^2)
# Space: O(m) due to hash map order_idx