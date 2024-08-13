class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        vowels = "aeiou"

        for i in range(k):
            if s[i] in vowels:
                res += 1
        
        count = res
        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i - k] in vowels:
                count -= 1
            res = max(res, count)
        return res

#Time: O(n)
#Space: O(1)