class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = ""

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end_of_word = word
    
class Solution:
    def __init__(self):
        self.cache = {}

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        return self.dfs(s, dictionary, 0)

    def dfs(self, s, dictionary, i):
        if i >= len(s):
            return 0
        if i in self.cache:
            return self.cache[i]
        self.cache[i] = len(s) - i
        j = i
        while j < len(s):
            for word in dictionary:
                if j + len(word) <= len(s) and s[j: j + len(word)] == word:
                    self.cache[i] = min(self.cache[i], j - i + self.dfs(s, dictionary, j + len(word)))
            j += 1
        return self.cache[i]