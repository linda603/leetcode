class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        longestPal = [0, 0]

        def getPal(string, l, r):
            while l >= 0 and r < len(string):
                if string[l] != string[r]:
                    break
                l -= 1
                r += 1
            return [l + 1, r - 1]

        for i in range(1, len(s) - 1):
            oddString = getPal(s, i - 1, i + 1)
            evenString = getPal(s, i - 1, i)
            currPal = max(oddString, evenString, key=lambda x: x[1] - x[0])
            longestPal = max(currPal, longestPal, key=lambda x:x[1] - x[0])
        return longestPal[1] - longestPal[0] + 1
        """
        n = len(s)

        def reverseString(s):
            return s[::-1]

        reversedS = "".join(reversed(s))

        dp = [[0 for i in range(n + 1)] for i in range (n + 1)]
        for i in range(n - 1, -1 , -1):
            for j in range(n - 1, -1 , -1):
                if s[i] == reversedS[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[0][0]

#Time: O(n^2) because we iterate through every elements in the 2D dp
#Space: O(n^2) due to 2D dp