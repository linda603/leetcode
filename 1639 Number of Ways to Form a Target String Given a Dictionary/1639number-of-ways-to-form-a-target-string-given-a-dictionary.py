class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        mod = 10 ** 9 + 7
        n = len(target)
        m = len(words[0])
        count = [[0] * m for _ in range(26)] # chat at index count

        for word in words:
            for i, c in enumerate(word):
                count[ord(c) - ord("a")][i] += 1

        cache = {}
        # i is index at target, k is index at word
        def dfs(i, k):
            if i == n: # formed a valid target
                return 1
            if k == m:
                return 0
            if (i, k) in cache:
                return cache[(i, k)]
            c = target[i]
            cache[(i, k)] = dfs(i, k + 1) # skip kth index
            # take kth index if found
            if count[ord(c) - ord("a")][k]:
                cache[(i, k)] += dfs(i + 1, k + 1) * count[ord(c) - ord("a")][k]
                cache[(i, k)] %= mod
            return cache[(i, k)]
        
        return dfs(0, 0)

# Time: O(mn). m: len(words[0]), n: len(target)
# Space: O(m + mn + mn). count takes O(26*m). dfs() takes O(mn) depth + O(mn) for caching
            

