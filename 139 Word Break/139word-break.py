class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for i in range(len(s) + 1)]
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if s[i: i + len(word)] == word and dp[i + len(word)]:
                    dp[i] = True
                    break
        return dp[0]

# Time: O(n*m*w). n: len(s), m: len(wordDict), w: len(word)
# Space: O(n + w)
                    