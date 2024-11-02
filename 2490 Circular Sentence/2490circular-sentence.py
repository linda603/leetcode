class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[len(sentence) - 1]:
            return False
        sentence = sentence.split(" ")
        for i in range(len(sentence) - 1):
            curr_word = sentence[i]
            next_word = sentence[i + 1]
            if curr_word[len(curr_word) - 1] != next_word[0]:
                return False
        return True

# Time: O(n)
# Space: O(n)