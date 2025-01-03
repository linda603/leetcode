class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        start = 0

        def reverse(l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        for end in range(len(s)):
            if s[end] == " ":
                reverse(start, end - 1)
                start = end + 1
        # reverse the last word if any last word after " "
        reverse(start, end)

# Time: O(n + 2n) = O(n)
# Space: O(1)