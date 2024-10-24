class trie_node:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = trie_node()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = trie_node()
            curr = curr.children[c]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        
        def dfs(i, curr):
            if i >= len(word):
                return curr.end_of_word
            if word[i] == ".":
                for child in curr.children.values():
                    if dfs(i + 1, child):
                        return True
                return False
            if word[i] not in curr.children:
                return False
            return dfs(i + 1, curr.children[word[i]])

        return dfs(0, self.root)

# Time: addWord() O(n), search() O(26^(l)). l: len(word)
# Space: addWord() O(n), search() O(l)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)