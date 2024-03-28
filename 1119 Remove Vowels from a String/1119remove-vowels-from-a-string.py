class Solution:
    def removeVowels(self, s: str) -> str:
        result = []
        
        def isVowel(char):
            vowel = "aeiou"
            if char in vowel:
                return True
            else:
                return False

        for char in s:
            if not isVowel(char):
                result.append(char)
        return "".join(result)

#Time: O(n)
#Space: O(1)