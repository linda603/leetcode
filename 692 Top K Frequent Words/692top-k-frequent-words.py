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
            val = ord(c) - ord('a')
            if val not in curr.children:
                curr.children[val] = trie_node()
            curr = curr.children[val]
        curr.end_of_word = word
    
    def get_word(self): # return list of words at this root
        res = []

        def dfs(node):
            if not node:
                return 
            if node.end_of_word:
                res.append(node.end_of_word)
            for val in range(26):
                if val in node.children:
                    dfs(node.children[val])
            return
    
        dfs(self.root)
        return res

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        buckets = [trie() for i in range(len(words) + 1)]

        for word, cnt in count.items():
            buckets[cnt].add(word)
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            if len(buckets[i].root.children) == 0:
                continue
            lists = buckets[i].get_word()
            for j in range(len(lists)):
                res.append(lists[j])
                k -= 1
                if k == 0:
                    return res

# Time: O(n + n + k) = O(n). We traverse to get k words.
# Space: O(n)