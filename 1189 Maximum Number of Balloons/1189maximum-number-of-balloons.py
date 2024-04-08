class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countB = {}
        countText = {}
        result = len(text)
        
        for char in text:
            if char not in countText:
                countText[char] = 0
            countText[char] += 1
        for char in "balloon":
            if char not in countText:
                return 0
            if char not in countB:
                countB[char] = 0
            countB[char] += 1

        for char in countB:
            result = min(result, countText[char] // countB[char])

        return result

#Time: O(n)
#Space: O(n)

