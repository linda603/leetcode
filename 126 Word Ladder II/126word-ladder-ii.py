class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList: return []
        wordList.append(beginWord)
        res = []
        adj = {}

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                if pattern not in adj:
                    adj[pattern] = []
                adj[pattern].append(word)
        
        queue = collections.deque([beginWord])
        visited = {beginWord: []}

        found = False
        while queue and not found:
            size = len(queue)
            visited_level = {} # keep track of words visited in this level

            for i in range(size):
                word = queue.popleft()
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for nei in adj[pattern]:
                        if nei == endWord:
                            found = True
                        if nei not in visited:
                            if nei not in visited_level:
                                visited_level[nei] = [word]
                                queue.append(nei)
                            else:
                                visited_level[nei].append(word)
            visited.update(visited_level)
        
        return self.get_ladders(beginWord, endWord, visited)
    
    def get_ladders(self, beginWord, endWord, visited):

        def dfs(word):
            if word == beginWord:
                return [[beginWord]]
            if word not in visited:
                return []
            res = []
            parents = visited[word]
            for parent in parents:
                res += dfs(parent)
            for r in res:
                r.append(word)
            return res

        return dfs(endWord)

# Time: O(n*w*w + n*w*w + n*w) n: len(wordList). w: len(longestWord)
# Space: O(n*w)