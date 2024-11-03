class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        if len(pattern) > len(s):
            return False
        
        def dfs(i, j, mapping):
            if i == len(pattern) and j == len(s):
                return True
            if i == len(pattern) or j == len(s):
                return False
            word = pattern[i]
            # word is already mapped
            if word in mapping:
                if s[j : j + len(mapping[word])] != mapping[word]:
                    return False
                return dfs(i + 1, j + len(mapping[word]), mapping)
                
            # need to map the curr pattern[i]
            for k in range(j + 1, len(s) + 1):
                pos_word = s[j: k]
                if pos_word in mapping.values():
                    continue
                mapping[pattern[i]] = pos_word
                if dfs(i + 1, j + len(pos_word), mapping):
                    return True
                del mapping[pattern[i]]
            return False
        
        return dfs(0, 0, {})

# Time: O(mn*n^2). m: len(pattern), n: len(s)
#       for loop O(n), generate substring s[i: k]: O(n) -> O(n^2)
# Space: O(m + n)