class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = Counter(s)
        odd_cnt = 0

        for c, cnt in count.items():
            if cnt % 2:
                odd_cnt += 1
        return odd_cnt <= 1

# Time: O(n + n)
# Space: O(26) = O(1)