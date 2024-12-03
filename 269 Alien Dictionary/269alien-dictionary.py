class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {c: [] for word in words for c in word}
        
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            min_len = min(len(word1), len(word2))
            # invalid case "wrtui" before "wrt"
            if word1[:min_len] == word2[:min_len] and len(word1) > len(word2):
                return ""
            for j in range(min_len):
                if word1[j] != word2[j]:
                    adj[word1[j]].append(word2[j])
                    break
        
        visited = set()
        cycle = set()
        res = []

        def dfs(c):
            if adj[c] == []:
                if c not in visited:
                    res.append(c)
                    visited.add(c)
                return True
            if c in cycle:
                return False
            cycle.add(c)
            for nei in adj[c]:
                if not dfs(nei):
                    return False
            cycle.remove(c)
            adj[c] = []
            res.append(c)
            visited.add(c)
            return True

        for c in adj.keys():
            if not dfs(c):
                return ""
        
        return "".join(res[::-1])

# Time: O(n + V + E). n: len(words) to build adj list {}. dfs() takes O(E + V)
# Space: O(26*26 + 26 + 26) = O(1)
        
