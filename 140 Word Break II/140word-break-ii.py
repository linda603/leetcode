class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        cache = {}
        
        def dfs(i):
            if i >= len(s):
                return [""]
            if i in cache:
                return cache[i]
            cache[i] = []
            for j in range(i, len(s)):
                word = s[i: j + 1]
                if word in wordDict:
                    lists = dfs(j + 1)
                    if lists:
                        for string in lists:
                            sentence = word
                            if string:
                                sentence += " " + string
                            cache[i].append(sentence)
            return cache[i]
        return dfs(0)

# Time: O(2^n)
# Space: O(n*w)