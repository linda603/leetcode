class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = Counter(s)
        
        for c in t:
            if c not in count:
                return c
            count[c] -= 1
            if count[c] == 0:
                del count[c]
# Time: O(2n)
# Space: O(26) = O(1)