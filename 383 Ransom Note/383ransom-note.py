class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}

        for c in magazine:
            count[c] = 1 + count.get(c, 0)
        
        for c in ransomNote:
            if c not in count:
                return False
            count[c] -=1
            if count[c] == 0:
                del count[c]
        return True

# Time: O(m + n)
# Space: O(26) = O(1)