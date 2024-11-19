class trie_node:
    def __init__(self):
        self.children = {}
        self.end_of_word = ""

class trie:
    def __init__(self):
        self.root = trie_node()
    
    def add(self, word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = trie_node()
            curr = curr.children[c]
        curr.end_of_word = word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        curr_trie = trie()
        for word in dictionary:
            curr_trie.add(word)

        def dfs(node, i, word):
            if i >= len(word) or word[i] not in node.children:
                return word
            node = node.children[word[i]]
            if node.end_of_word:
                return node.end_of_word
            return dfs(node, i + 1, word)


        array = sentence.split(" ")
        res = []
        for word in array:
            testing = dfs(curr_trie.root, 0, word)
            res.append(testing)
        
        return " ".join(res)

# Time: O(nl + ml). n: len(dictionary), m: len(sentence), l: len of longest word.
# Space: O(nl + ml). nl for trie space, ml for array and res spaces.