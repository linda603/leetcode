class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        # can seperate all single char as 1 palindrome
        if k == len(s):
            return True
        count = {}

        for c in s:
            count[c] = 1 + count.get(c, 0)

        odd = 0

        for c, cnt in count.items():
            if cnt % 2:
                odd += 1
        return odd <= k
        
# Time: O(2n)
# Space: O(26) = O(1)