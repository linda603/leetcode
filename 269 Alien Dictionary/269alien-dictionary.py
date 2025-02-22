class Solution:
    def __init__(self):
        self.res = []
        self.visited = set()
        self.cycle = set()
        self.adj = {}

    def alienOrder(self, words: List[str]) -> str:
        if not self.get_adj(words):
            return ""

        for c in self.adj.keys():
            if not self.dfs(c):
                return ""
        return "".join(self.res[::-1])
    
    def get_adj(self, words):
        self.adj = {c: [] for word in words for c in word}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            min_len = min(len(word1), len(word2))
            # invalid case
            if len(word1) > len(word2) and word1[:min_len] == word2:
                return False
            for j in range(min_len):
                if word1[j] != word2[j]:
                    self.adj[word1[j]].append(word2[j])
                    break
        return True

    def dfs(self, char):
        if self.adj[char] == []:
            if char not in self.visited:
                self.res.append(char)
                self.visited.add(char)
            return True
        if char in self.cycle:
            return False
        self.cycle.add(char)
        for nei in self.adj[char]:
            if not self.dfs(nei):
                return False
        self.cycle.remove(char)
        self.res.append(char)
        self.visited.add(char)
        self.adj[char] = []
        return True

# Time: O(n + E + V). n: total length of words. O(n) to build adj list
# Space: O(E + V + V + V)