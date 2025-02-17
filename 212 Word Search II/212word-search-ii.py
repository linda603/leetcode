class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = ""

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end_of_word = word

class Solution:
    def __init__(self):
        self.res = []

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        trie = Trie()
        for word in words:
            trie.add(word)
        
        for r in range(m):
            for c in range(n):
                if board[r][c] in trie.root.children:
                    self.dfs(board, trie, r, c, trie.root, set())
        return self.res
    
    def dfs(self, board, trie, r, c, node, visited):
        m, n = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        if (r < 0 or r == m or c < 0 or c == n or board[r][c] not in node.children or
            (r, c) in visited):
            return
        visited.add((r, c))
        node = node.children[board[r][c]]
        #print(r, c, board[r][c])
        if node.end_of_word:
            self.res.append(node.end_of_word)
            node.end_of_word = ""
        #print(self.res)
        for dr, dc in directions:
            nei_r = r + dr
            nei_c = c + dc
            self.dfs(board, trie, nei_r, nei_c, node, visited)
        visited.remove((r, c))
        return

# Time: O(kw + mn*4^w)
# Space: O(kw + w)
