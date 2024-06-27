class Solution:
    def reverseVowels(self, s: str) -> str:
        arr = list(s)
        l = 0
        r = len(s) - 1
        vowels = "aeiouAEIOU"

        while l < r:
            while l < r and arr[l] not in vowels:
                l += 1
            
            while l < r and arr[r] not in vowels:
                r -= 1
            
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        
        return "".join(arr)

#Time: O(2n)
#Space: O(n)