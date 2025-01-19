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
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        curr_trie = trie()
        for word in words:
            curr_trie.add(word)

        visited = set()
        res = []
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r, c, node):
            nonlocal res, visited
            if r < 0 or r == m or c < 0 or c == n or (r, c) in visited or board[r][c] not in node.children:
                return
            node = node.children[board[r][c]]
            if node.end_of_word:
                res.append(node.end_of_word)
                node.end_of_word = "" # to prevent adding this word repeatedly
            visited.add((r, c))
            for dr, dc in directions:
                nei_r = r + dr
                nei_c = c + dc
                dfs(nei_r, nei_c, node)
            visited.remove((r, c))
            return

        for r in range(m):
            for c in range(n):
                dfs(r, c, curr_trie.root)
        return res

# Time: O(kl + mn*4^l). O(kl) to build trie. O(mn4^l) dfs() of the word
# Space: O(kl + l) = O(kl)