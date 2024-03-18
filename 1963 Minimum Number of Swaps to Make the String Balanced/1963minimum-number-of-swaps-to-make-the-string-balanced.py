class Solution:
    def minSwaps(self, s: str) -> int:
        extraClose = 0
        maxClose = 0

        for char in s:
            if char == ']':
                extraClose += 1
            else:
                extraClose -= 1
            maxClose = max(extraClose, maxClose)
        return (maxClose + 1) // 2

#Time: O(n)
#Space: O(1)